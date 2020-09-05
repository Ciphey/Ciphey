"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝
╚██████╗██║██║     ██║  ██║███████╗   ██║
© Brandon Skerritt
Github: brandonskerritt
"""
import sys
from distutils import util
from typing import Optional, Dict, Union, Set, List, Tuple

from loguru import logger
import ciphey
import cipheycore

from ciphey.iface import ParamSpec, CrackResult, T, CrackInfo, registry

@registry.register
class XorSingle(ciphey.iface.Cracker[bytes]):
    def getInfo(self, ctext: str) -> CrackInfo:
        analysis = self.cache.get_or_update(
            ctext,
            "cipheycore::simple_analysis",
            lambda: cipheycore.analyse_bytes(ctext),
        )

        return CrackInfo(
            success_likelihood=cipheycore.xor_single_detect(analysis, self.expected),
            # TODO: actually calculate runtimes
            success_runtime=1e-5,
            failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "xor_single"

    def attemptCrack(self, ctext: bytes) -> List[CrackResult]:
        logger.debug("Trying xor single cipher")
        # TODO: handle different alphabets

        logger.trace("Beginning cipheycore simple analysis")
        logger.trace(f"{ctext}")

        # Hand it off to the core
        analysis = self.cache.get_or_update(
            ctext,
            "cipheycore::simple_analysis",
            lambda: cipheycore.analyse_bytes(ctext),
        )
        logger.trace("Beginning cipheycore::xor_single")
        possible_keys = cipheycore.xor_single_crack(
            analysis, self.expected, self.p_value
        )

        n_candidates = len(possible_keys)
        logger.debug(f"XOR single returned {n_candidates} candidates")

        candidates = []

        for candidate in possible_keys:
            translated = cipheycore.xor_single_decrypt(ctext, candidate.key)
            logger.trace(f"Candidate {candidate.key} has prob {candidate.p_value}")
            candidates.append(CrackResult(value=translated, key_info=candidate.key))

        logger.trace(f"{candidates}")

        return candidates

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for standard frequency analysis",
                req=False,
                default=0.01,
            )
            # TODO: add "filter" param
        }

    @staticmethod
    def scoreUtility() -> float:
        return 1.5

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.p_value = self._params()["p_value"]
