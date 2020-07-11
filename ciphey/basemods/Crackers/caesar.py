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

from loguru import logger
import ciphey
import cipheycore

from ciphey.iface import ParamSpec, CrackResult, T, CrackInfo, registry

@registry.register
class Caesar(ciphey.iface.Cracker[str]):
    def getInfo(self, ctext: T) -> CrackInfo:
        analysis = self.cache.get_or_update(
            ctext,
            "cipheycore::simple_analysis",
            lambda: cipheycore.analyse_string(ctext),
        )

        return CrackInfo(
            success_likelihood=cipheycore.caesar_detect(analysis, self.expected),
            # TODO: actually calculate runtimes
            success_runtime=1e-4,
            failure_runtime=1e-4,
        )

    @staticmethod
    def getTarget() -> str:
        return "caesar"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logger.debug("Trying caesar cipher")
        # Convert it to lower case
        #
        # TODO: handle different alphabets
        if self.lower:
            message = ctext.lower()
        else:
            message = ctext

        logger.trace("Beginning cipheycore simple analysis")

        # Hand it off to the core
        analysis = self.cache.get_or_update(
            ctext,
            "cipheycore::simple_analysis",
            lambda: cipheycore.analyse_string(message),
        )
        logger.trace("Beginning cipheycore::caesar")
        possible_keys = cipheycore.caesar_crack(
            analysis, self.expected, self.group, True, self.p_value
        )
        n_candidates = len(possible_keys)
        logger.debug(f"Caesar returned {n_candidates} candidates")

        candidates = []

        for candidate in possible_keys:
            translated = cipheycore.caesar_decrypt(message, candidate.key, self.group)
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
                desc="An ordered sequence of chars that make up the caesar cipher alphabet",
                req=False,
                default="abcdefghijklmnopqrstuvwxyz",
            ),
            "lower": ciphey.iface.ParamSpec(
                desc="Whether or not the ciphertext should be converted to lowercase first",
                req=False,
                default=True,
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for standard frequency analysis",
                req=False,
                default=0.1,
            )
            # TODO: add "filter" param
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
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.p_value = self._params()["p_value"]
