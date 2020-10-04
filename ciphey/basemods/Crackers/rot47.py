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
class Rot47(ciphey.iface.Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        analysis = self.cache.get_or_update(
            ctext,
            "cipheycore::simple_analysis",
            lambda: cipheycore.analyse_string(ctext),
        )

        return CrackInfo(
            success_likelihood=cipheycore.caesar_detect(analysis, self.expected),
            # TODO: actually calculate runtimes
            success_runtime=1e-5,
            failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "rot47"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logger.debug(f"Trying ROT47 cipher on {ctext}")

        logger.trace("Beginning cipheycore simple analysis")

        # Hand it off to the core
        analysis = self.cache.get_or_update(
            ctext,
            "cipheycore::simple_analysis",
            lambda: cipheycore.analyse_string(ctext),
        )
        logger.trace("Beginning cipheycore::caesar")
        possible_keys = cipheycore.caesar_crack(
            analysis, self.expected, self.group, self.p_value
        )

        n_candidates = len(possible_keys)
        logger.debug(f"ROT47 returned {n_candidates} candidates")

        if n_candidates == 0:
            logger.trace(f"Filtering for better results")
            analysis = cipheycore.analyse_string(ctext, self.group)
            possible_keys = cipheycore.caesar_crack(
                analysis, self.expected, self.group, self.p_value
            )

        candidates = []

        for candidate in possible_keys:
            logger.trace(f"Candidate {candidate.key} has prob {candidate.p_value}")
            translated = cipheycore.caesar_decrypt(ctext, candidate.key, self.group)
            candidates.append(CrackResult(value=translated, key_info=candidate.key))

        return candidates

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "group": ciphey.iface.ParamSpec(
                desc="An ordered sequence of chars that make up the ROT47 cipher alphabet",
                req=False,
                default="""!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for standard frequency analysis",
                req=False,
                default=0.01,
            )
            # TODO: add "filter" param
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.group = list(self._params()["group"])
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.p_value = float(self._params()["p_value"])