# Community
# by https://github.com/AlexandruValeanu
from typing import Optional, Dict, List

import cipheycore
import logging

from ciphey.common import fix_case
from ciphey.iface import registry, Cracker, ParamSpec, CrackResult, CrackInfo
from ciphey.iface._fwd import config as Config


@registry.register
class RailFence(Cracker[str]):
    """
    In the rail fence cipher, the plaintext is written downwards diagonally on successive "rails" of an imaginary
    fence, then moving up when the bottom rail is reached, down again when the top rail is reached, and so on until
    the whole plaintext is written out. The ciphertext is then read off in rows.

    The key of the cipher is the number of rails in the fence.
    """
    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1,
            success_runtime=1e-5,
            failure_runtime=1e-5,
        )

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
            Brute force all keys between 2 and len(text)-1.
        """
        logging.debug("Attempting RailFence")
        candidates = []

        for key in range(2, len(ctext)):
            text = ctext.lower()
            logging.debug(f"Building rail_fence from '{text}'")
            rail_fence = self.build_rail_fence(text, key)
            logging.debug(f"Decrypting rail_fence")
            translated = self.decrypt(rail_fence, len(text), key)

            candidate_probability = self.plaintext_probability(translated)
            if candidate_probability > self.plaintext_prob_threshold:
                candidates.append(
                    CrackResult(
                        value=fix_case(translated, ctext), key_info=f"K={key}"
                    )
                )

        logging.info(f"RailFence Cipher returned {len(candidates)} candidates")
        return candidates

    @staticmethod
    def build_rail_fence(text: str, key: int) -> [str]:
        """
            Build rail_fence by iterating over the text diagonally.
        """
        size_fences = [0 for _ in range(key)]
        rail, step = 0, 1
        for _ in range(len(text)):
            size_fences[rail] += 1
            rail += step
            if rail == 0 or rail == key - 1:
                step = -step

        rail_fence = [[] for _ in range(key)]
        idx = 0
        for i in range(key):
            for j in range(size_fences[i]):
                rail_fence[i].append(text[idx])
                idx += 1

        return rail_fence

    @staticmethod
    def decrypt(rail_fence: [str], text_length, key) -> str:
        """
        Decrypt the rail_fence by traversing it diagonally.
        """
        rail, step = 0, 1
        result = ''
        for _ in range(text_length):
            result += rail_fence[rail][0]
            rail_fence[rail].remove(rail_fence[rail][0])
            rail += step
            if rail == 0 or rail == key - 1:
                step = -step

        return result

    def plaintext_probability(self, translated: str) -> float:
        """
        Analyses the translated text and applies the chi squared test to see if it is a probable plaintext candidate
        Returns the probability of the chi-squared test.
        """
        analysis = cipheycore.analyse_string(translated)
        return cipheycore.chisq_test(analysis, self.expected)

    def __init__(self, config: Config):
        super().__init__(config)
        self.expected = config.get_resource(self._params()["expected"])
        self.plaintext_prob_threshold = 0.01

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "railfence"
