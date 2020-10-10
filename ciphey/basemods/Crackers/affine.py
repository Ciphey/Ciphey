# Community
# by https://github.com/Ozzyz

from typing import Dict, List, Optional

import ciphey
import cipheycore
from ciphey.common import fix_case
from ciphey.iface import Config, Cracker, CrackInfo, CrackResult, ParamSpec, registry
from ciphey.mathsHelper import mathsHelper
from loguru import logger


@registry.register
class Affine(Cracker[str]):
    """
    Each character in the Affine Cipher is encoded with the rule E(x) = (ax + b) mod m
    m is the size of the alphabet, while a and b are the keys in the cipher. a must be coprime to b.
    The Caesar cipher is a specific case of the Affine Cipher, with a=1 and b being the shift of the cipher.
    Decryption is performed by D(x) = a_inv (x - b) mod m where a_inv is the modular multiplicative inverse of a mod m.

    In this version of the Affine Cipher, we do not allow alphabets with several instances of the same letter in different cases.
    For instance, the alphabet 'ABCdef123' is allowed, but 'AaBbCc' is not.
    """

    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1,
            success_runtime=1e-5,
            failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "affine"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
        Brute forces all the possible combinations of a and b to attempt to crack the cipher.
        """
        logger.trace("Attempting affine")
        candidates = []

        # a and b are coprime if gcd(a,b) is 1.
        possible_a = [
            a
            for a in range(1, self.ALPHABET_LENGTH)
            if mathsHelper.gcd(a, self.ALPHABET_LENGTH) == 1
        ]
        logger.debug(
            f"Trying Affine Cracker with {len(possible_a)} a-values and {self.ALPHABET_LENGTH} b-values"
        )

        for a in possible_a:
            a_inv = mathsHelper.mod_inv(a, self.ALPHABET_LENGTH)
            # If there is no inverse, we cannot decrypt the text
            if a_inv is None:
                continue
            for b in range(self.ALPHABET_LENGTH):
                # Pass in lowered text. This means that we expect alphabets to not contain both 'a' and 'A'.
                translated = self.decrypt(ctext.lower(), a_inv, b, self.ALPHABET_LENGTH)

                candidate_probability = self.plaintext_probability(translated)
                if candidate_probability > self.PLAINTEXT_PROB_THRESHOLD:
                    candidates.append(
                        CrackResult(
                            value=fix_case(translated, ctext), key_info=f"a={a}, b={b}"
                        )
                    )
        logger.debug(f"Affine Cipher returned {len(candidates)} candidates")
        return candidates

    def plaintext_probability(self, translated: str) -> float:
        """
        Analyses the translated text and applies the chi squared test to see if it is a probable plaintext candidate
        Returns the probability of the chi-squared test.
        """
        analysis = cipheycore.analyse_string(translated)
        return cipheycore.chisq_test(analysis, self.expected)

    def decrypt(self, text: str, a_inv: int, b: int, m: int) -> str:
        """
        Each letter is decrypted at D(x) = a_inv (x - b) mod m where x is the char
        We treat the char value as its index in the alphabet, so if
        the alphabet is 'abcd....' and the char is 'b', it has the value 1.
        """
        return "".join([self.decryptChar(char, a_inv, b, m) for char in text])

    def decryptChar(self, char: str, a_inv: int, b: int, m: int) -> str:

        # We lower the alphabet since both ctext and alphabet need to be in the same case in order
        # to perform the shifts. The translated text will have fixed case after the translation anyways.
        # This is only necessary if the specified alphabet is uppercase.
        alphabet = [x.lower() for x in self.group]

        # Preserve characters that are not in alphabet
        if char not in alphabet:
            return char
        char_idx = alphabet.index(char)
        decrypted_char_idx = (a_inv * (char_idx - b)) % m
        return alphabet[decrypted_char_idx]

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "group": ciphey.iface.ParamSpec(
                desc="An ordered sequence of chars that make up the alphabet",
                req=False,
                default="abcdefghijklmnopqrstuvwxyz",
            ),
        }

    def __init__(self, config: Config):
        super().__init__(config)
        self.group = list(self._params()["group"])
        self.expected = config.get_resource(self._params()["expected"])
        self.ALPHABET_LENGTH = len(self.group)
        self.cache = config.cache
        self.PLAINTEXT_PROB_THRESHOLD = 0.01
