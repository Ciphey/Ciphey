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


class Caesar(ciphey.iface.Cracker[str], ciphey.iface.Detector[str]):
    @staticmethod
    def getTargets() -> Set[str]:
        return {"caesar"}

    def scoreLikelihood(self, ctext: str) -> Dict[str, float]:
        # Match the distribution, and then run a chi-squared analysis
        analysis = self.cache.get_or_update(ctext, "cipheycore::simple_analysis",
                                            lambda: cipheycore.analyse_string(ctext))
        return {"caesar": cipheycore.caesar_detect(analysis, self.expected)}

    def attemptCrack(self, message: str, target: str) -> Optional[CrackResults]:
        assert(target == "caesar")

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
        self.lc = config.objs["checker"]
        loader, name = ciphey.iface.split_resource_name(self._params()["expected"])
        self.expected = config(ciphey.iface.registry.get_named(name, ciphey.iface))
        self.cache = config.cache

    @staticmethod
    def getName():
        return "caesar"


ciphey.iface.registry.register(Caesar, ciphey.iface.Cracker[str], ciphey.iface.Detector[str])
