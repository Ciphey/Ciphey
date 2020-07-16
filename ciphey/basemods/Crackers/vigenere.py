"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝
╚██████╗██║██║     ██║  ██║███████╗   ██║
© Brandon Skerritt
Github: brandonskerritt
"""
from distutils import util
from typing import Optional, Dict, Union, Set, List

import re

from loguru import logger
import ciphey
import cipheycore

from ciphey.iface import ParamSpec, Cracker, CrackResult, T, CrackInfo, registry


@registry.register
class Vigenere(ciphey.iface.Cracker[str]):
    def getInfo(self, ctext: T) -> CrackInfo:
        if self.keysize is not None:
            analysis = self.cache.get_or_update(
                ctext,
                f"vigenere::{self.keysize}",
                lambda: cipheycore.analyse_string(ctext, self.keysize, self.group),
            )

            return CrackInfo(
                success_likelihood=cipheycore.vigenere_detect(analysis, self.expected),
                # TODO: actually calculate runtimes
                success_runtime=1e-4,
                failure_runtime=1e-4,
            )
        else:
            return CrackInfo(
                success_likelihood=0.5,  # TODO: actually work this out
                # TODO: actually calculate runtimes
                success_runtime=1e-4,
                failure_runtime=1e-4,
            )

    @staticmethod
    def getTarget() -> str:
        return "vigenere"

    def crackOne(
        self, ctext: str, analysis: cipheycore.windowed_analysis_res
    ) -> List[CrackResult]:
        possible_keys = cipheycore.vigenere_crack(
            analysis, self.expected, self.group, self.p_value
        )
        logger.trace(f"Vigenere crack got keys: {[[i for i in candidate.key] for candidate in possible_keys]}")
        return [
            CrackResult(
                value=cipheycore.vigenere_decrypt(ctext, candidate.key, self.group),
                key_info="".join([self.group[i] for i in candidate.key]),
            )
            for candidate in possible_keys[:min(len(possible_keys), 10)]
        ]

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logger.debug("Trying vigenere cipher")
        # Convert it to lower case
        if self.lower:
            message = ctext.lower()
        else:
            message = ctext

        # Analysis must be done here, where we know the case for the cache
        if self.keysize is not None:
            return self.crackOne(
                message,
                self.cache.get_or_update(
                    ctext,
                    f"vigenere::{self.keysize}",
                    lambda: cipheycore.analyse_string(ctext, self.keysize, self.group),
                ),
            )
        else:
            arrs = []
            possible_len = self.kasiskiExamination(message)
            possible_len.sort()
            logger.trace(f"Got possible lengths {possible_len}")
            # TODO: work out length
            for i in possible_len:
                arrs.extend(
                    self.crackOne(
                        message,
                        self.cache.get_or_update(
                            ctext,
                            f"vigenere::{i}",
                            lambda: cipheycore.analyse_string(ctext, i, self.group),
                        ),
                    )
                )

            logger.debug(f"Vigenere returned {len(arrs)} candidates")
            return arrs

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "group": ciphey.iface.ParamSpec(
                desc="An ordered sequence of chars that make up the caesar cipher alphabet",
                req=False,
                default="abcdefghijklmnopqrstuvwxyz",
            ),
            "lower": ciphey.iface.ParamSpec(
                desc="Whether or not the ciphertext should be converted to lowercase first",
                req=False,
                default=True,
            ),
            "keysize": ciphey.iface.ParamSpec(
                desc="A key size that should be used. If not given, will attempt to work it out",
                req=False,
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for windowed frequency analysis",
                req=False,
                default=0.99,
            ),
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.lower: Union[str, bool] = self._params()["lower"]
        if type(self.lower) != bool:
            self.lower = util.strtobool(self.lower)
        self.group = list(self._params()["group"])
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.keysize = self._params().get("keysize")
        if self.keysize is not None:
            self.keysize = int(self.keysize)
        self.p_value = self._params()["p_value"]
        self.MAX_KEY_LENGTH = 16

    def kasiskiExamination(self, ciphertext) -> List[int]:
        # Find out the sequences of 3 to 5 letters that occur multiple times
        # in the ciphertext. repeatedSeqSpacings has a value like:
        # {'EXG': [192], 'NAF': [339, 972, 633], ... }
        repeatedSeqSpacings = self.findRepeatSequencesSpacings(ciphertext)

        max = len(ciphertext) // 3

        # (See getMostCommonFactors() for a description of seqFactors.)
        seqFactors = {}
        for seq in repeatedSeqSpacings:
            seqFactors[seq] = []
            for spacing in repeatedSeqSpacings[seq]:
                seqFactors[seq].extend(self.getUsefulFactors(spacing, max))

        # (See getMostCommonFactors() for a description of factorsByCount.)
        factorsByCount = self.getMostCommonFactors(seqFactors)

        # Now we extract the factor counts from factorsByCount and
        # put them in allLikelyKeyLengths so that they are easier to
        # use later:
        allLikelyKeyLengths = []
        for twoIntTuple in factorsByCount:
            allLikelyKeyLengths.append(twoIntTuple[0])

        return allLikelyKeyLengths

    def findRepeatSequencesSpacings(self, message):
        # Goes through the message and finds any 3 to 5 letter sequences
        # that are repeated. Returns a dict with the keys of the sequence and
        # values of a list of spacings (num of letters between the repeats).
        # Use a regular expression to remove non-letters from the message:

        # Compile a list of seqLen-letter sequences found in the message:
        seqSpacings = {}  # Keys are sequences, values are lists of int spacings.
        for seqLen in range(3, 6):
            for seqStart in range(len(message) - seqLen):
                # Determine what the sequence is, and store it in seq:
                seq = message[seqStart : seqStart + seqLen]

                # Look for this sequence in the rest of the message:
                for i in range(seqStart + seqLen, len(message) - seqLen):
                    if message[i : i + seqLen] == seq:
                        # Found a repeated sequence.
                        if seq not in seqSpacings:
                            seqSpacings[seq] = []  # Initialize a blank list.

                        # Append the spacing distance between the repeated
                        # sequence and the original sequence:
                        seqSpacings[seq].append(i - seqStart)
        return seqSpacings

    def getUsefulFactors(self, num, max: int):
        # Returns a list of useful factors of num. By "useful" we mean factors
        # less than MAX_KEY_LENGTH + 1 and not 1. For example,
        # getUsefulFactors(144) returns [2, 3, 4, 6, 8, 9, 12, 16]

        if num < 2:
            return []  # Numbers less than 2 have no useful factors.

        factors = set()  # The list of factors found.

        # When finding factors, you only need to check the integers up to
        # MAX_KEY_LENGTH.
        #
        # Mathematician note: whilst this is *definitely* suboptimal,
        # for small numbers it's probably as good as other methods
        for i in range(
            2, min(max, num)
        ):  # Don't test 1: it's not useful.
            if num % i == 0:
                factors.add(i)
                otherFactor = num // i
                if otherFactor < self.MAX_KEY_LENGTH + 1 and otherFactor != 1:
                    factors.add(otherFactor)
        return list(factors)

    #
    def getMostCommonFactors(self, seqFactors):
        # First, get a count of how many times a factor occurs in seqFactors:
        factorCounts = {}  # Key is a factor, value is how often it occurs.

        # seqFactors keys are sequences, values are lists of factors of the
        # spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
        # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
        for seq in seqFactors:
            factorList = seqFactors[seq]
            for factor in factorList:
                if factor not in factorCounts:
                    factorCounts[factor] = 0
                factorCounts[factor] += 1

        # Second, put the factor and its count into a tuple, and make a list
        # of these tuples so we can sort them:
        factorsByCount = []
        for factor in factorCounts:
            # Exclude factors larger than MAX_KEY_LENGTH:
            if factor <= self.MAX_KEY_LENGTH:
                # factorsByCount is a list of tuples: (factor, factorCount)
                # factorsByCount has a value like: [(3, 497), (2, 487), ...]
                factorsByCount.append((factor, factorCounts[factor]))

        # Sort the list by the factor count:
        factorsByCount.sort(key=lambda x: x[1], reverse=True)

        return factorsByCount
