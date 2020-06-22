import itertools, re
import cipheycore
import cipheydists

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
from typing import Optional, Dict, Union, Set

from loguru import logger
import ciphey
import cipheycore
import cipheydists

from ciphey.iface import ParamSpec, CrackResults


class Vigenere(ciphey.iface.Cracker[str], ciphey.iface.Detector[str]):
    @staticmethod
    def getTargets() -> Set[str]:
        return {"vigenere"}

    def scoreLikelihood(self, ctext: str) -> Dict[str, float]:
        # Match the distribution, and then run a chi-squared analysis
        analysis = self.cache.get_or_update(ctext, "cipheycore::simple_analysis",
                                            lambda: cipheycore.analyse_string(ctext))
        return {"caesar": cipheycore.caesar_detect(analysis, self.expected)}

    def attemptCrack(self, message: str, target: str) -> Optional[CrackResults]:
        assert(target == "vigenere")

        logger.debug("Trying caesar cipher")
        # Convert it to lower case
        #
        # TODO: handle different alphabets
        message = message.lower()

        # Hand it off to the core
        analysis = self.cache.get_or_update(message, "cipheycore::simple_analysis",
                                            lambda: cipheycore.analyse_string(message))
        possible_keys = cipheycore.caesar_crack(analysis, self.expected, self.group)
        n_candidates = len(possible_keys)
        logger.debug(f"Caesar cipher core heuristic returned {n_candidates} candidates")

        for candidate in possible_keys:
            translated = cipheycore.caesar_decrypt(message, candidate.key, self.group)
            result = self.lc.check(translated)
            if result:
                logger.debug(f"Caesar cipher returns true {result}")
                return CrackResults(plaintext=translated, keyInfo=f"{candidate.key}")

        # if none of them match English, return false!
        logger.debug(f"Caesar cipher crack failed")
        return None

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                configPath=["default_dist"]),
            "group": ciphey.iface.ParamSpec(
                desc="An ordered sequence of chars that make up the caesar cipher alphabet",
                req=False,
                default="abcdefghijklmnopqrstuvwxyz"),
            "lower": ciphey.iface.ParamSpec(
                desc="Whether or not the ciphertext should be converted to lowercase first",
                req=False,
                default=True),
            "keysize": ciphey.iface.ParamSpec(
                desc="A key size that should be used",
                req=False,
                default=True),
        }

    @staticmethod
    def scoreUtility() -> float:
        return 1.5

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.lower: Union[str, bool] = self._params()["lower"]
        if type(self.lower) != bool:
            self.lower = util.strtobool(self.lower)
        self.group = list(self._params()["group"])
        self.lc = config.objs["checker"]
        loader, name = ciphey.iface.split_resource_name(self._params()["expected"])
        self.expected = config(ciphey.iface.registry.get_named(name, ciphey.iface))
        self.cache = config.cache
        self.keysize = self._params()["keysiz"]

    @staticmethod
    def getName():
        return "caesar"


ciphey.iface.registry.register(Vigenere, ciphey.iface.Cracker[str], ciphey.iface.Detector[str])



class Vigenere:
    def __init__(self, lc):
        self.LETTERS = "abcdefghijklmnopqrstuvwxyz"
        self.SILENT_MODE = True  # If set to True, program doesn't print anything.
        self.NUM_MOST_FREQ_LETTERS = 4  # Attempt this many letters per subkey.
        self.MAX_KEY_LENGTH = 16  # Will not attempt keys longer than this.
        self.NONLETTERS_PATTERN = re.compile("[^A-Z]")

        self.lc = lc

    def decrypt(self, text):
        result = self.hackVigenere(text)
        if result is None:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Viginere",
                "Extra Information": None,
            }

        return result

    def findRepeatSequencesSpacings(self, message):
        # Goes through the message and finds any 3 to 5 letter sequences
        # that are repeated. Returns a dict with the keys of the sequence and
        # values of a list of spacings (num of letters between the repeats).
        # Use a regular expression to remove non-letters from the message:
        message = self.NONLETTERS_PATTERN.sub("", message.upper())

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

    def getUsefulFactors(self, num):
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
        for i in range(2, min(self.MAX_KEY_LENGTH + 1, num)):  # Don't test 1: it's not useful.
            if num % i == 0:
                factors.add(i)
                otherFactor = num // i
                if otherFactor < self.MAX_KEY_LENGTH + 1 and otherFactor != 1:
                    factors.add(otherFactor)
        return list(factors)

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

    def kasiskiExamination(self, ciphertext):
        # Find out the sequences of 3 to 5 letters that occur multiple times
        # in the ciphertext. repeatedSeqSpacings has a value like:
        # {'EXG': [192], 'NAF': [339, 972, 633], ... }
        repeatedSeqSpacings = self.findRepeatSequencesSpacings(ciphertext)

        # (See getMostCommonFactors() for a description of seqFactors.)
        seqFactors = {}
        for seq in repeatedSeqSpacings:
            seqFactors[seq] = []
            for spacing in repeatedSeqSpacings[seq]:
                seqFactors[seq].extend(self.getUsefulFactors(spacing))

        # (See getMostCommonFactors() for a description of factorsByCount.)
        factorsByCount = self.getMostCommonFactors(seqFactors)

        # Now we extract the factor counts from factorsByCount and
        # put them in allLikelyKeyLengths so that they are easier to
        # use later:
        allLikelyKeyLengths = []
        for twoIntTuple in factorsByCount:
            allLikelyKeyLengths.append(twoIntTuple[0])

        return allLikelyKeyLengths

    def attemptHackWithKeyLength(self, ciphertext, mostLikelyKeyLength):
        # Determine the most likely letters for each letter in the key:
        ciphertext = ciphertext.lower()

        # Do core work
        group = cipheydists.get_charset("english")["lcase"]
        expected = cipheydists.get_dist("lcase")
        possible_keys = cipheycore.vigenere_crack(
            ciphertext, expected, group, mostLikelyKeyLength
        )
        n_keys = len(possible_keys)

        # Try all the feasible keys
        for candidate in possible_keys:
            nice_key = list(candidate.key)
            # Create a possible key from the letters in allFreqScores:
            if not self.SILENT_MODE:
                print("Attempting with key: %s" % nice_key)

            decryptedText = cipheycore.vigenere_decrypt(
                ciphertext, candidate.key, group
            )

            if self.lc.check(decryptedText):
                # Set the hacked ciphertext to the original casing:
                origCase = []
                for i in range(len(ciphertext)):
                    if ciphertext[i].isupper():
                        origCase.append(decryptedText[i].upper())
                    else:
                        origCase.append(decryptedText[i].lower())
                decryptedText = "".join(origCase)

                # Check with user to see if the key has been found:
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Viginere",
                    "Extra Information": f"The key used is {nice_key}",
                }

        # No English-looking decryption found, so return None:
        return None

    def hackVigenere(self, ciphertext):
        # First, we need to do Kasiski Examination to figure out what the
        # length of the ciphertext's encryption key is:
        allLikelyKeyLengths = self.kasiskiExamination(ciphertext)
        if not self.SILENT_MODE:
            keyLengthStr = ""
            for keyLength in allLikelyKeyLengths:
                keyLengthStr += "%s " % (keyLength)
            print(
                "Kasiski Examination results say the most likely key lengths are: "
                + keyLengthStr
                + "\n"
            )
        hackedMessage = None
        for keyLength in allLikelyKeyLengths:
            if not self.SILENT_MODE:
                print(
                    "Attempting hack with key length %s (%s possible keys)..."
                    % (keyLength, self.NUM_MOST_FREQ_LETTERS ** keyLength)
                )
            hackedMessage = self.attemptHackWithKeyLength(ciphertext, keyLength)
            if hackedMessage != None:
                break

        # If none of the key lengths we found using Kasiski Examination
        # worked, start brute-forcing through key lengths:
        if hackedMessage == None:
            if not self.SILENT_MODE:
                print(
                    "Unable to hack message with likely key length(s). Brute forcing key length..."
                )
            for keyLength in range(1, self.MAX_KEY_LENGTH + 1):
                # Don't re-check key lengths already tried from Kasiski:
                if keyLength not in allLikelyKeyLengths:
                    if not self.SILENT_MODE:
                        print(
                            "Attempting hack with key length %s (%s possible keys)..."
                            % (keyLength, self.NUM_MOST_FREQ_LETTERS ** keyLength)
                        )
                    hackedMessage = self.attemptHackWithKeyLength(ciphertext, keyLength)
                    if hackedMessage != None:
                        break
        return hackedMessage

    def getName(self):
        return "Viginere"

