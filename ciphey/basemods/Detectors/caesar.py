from typing import Dict, Optional, Set

import ciphey
import cipheycore
from ciphey.iface import ParamSpec, Config, registry


class CaesarCoreDetect(ciphey.iface.Detector[str]):
    @staticmethod
    def getTargets() -> Set[str]:
        return ["caesar"]

    def scoreLikelihood(self, ctext: str) -> Dict[str, float]:
        # Match the distribution, and then run a chi-squared analysis
        analysis = self.cache.get_or_update(ctext, "cipheycore::simple_analysis",
                                            lambda: cipheycore.analyse_string(ctext))
        return cipheycore.caesar_detect(analysis, self.expected)

    def __init__(self, config: Config):
        super().__init__(config)
        self.cache = config.cache
        caesar = config.params.get("caesar")
        if caesar is not None:
            res = caesar.get("expected")
            if res is not None:
                self.expected = res
                return
        other_params: Dict[str, ParamSpec] = registry.get_named("caesar").getParams()
        self.expected = other_params["expected"].default

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getName() -> str:
        return "caesar_coredetect"

    @staticmethod
    def scoreUtility() -> float:
        # It's very quick, and should catch almost all caesar ciphers
        return 1.9