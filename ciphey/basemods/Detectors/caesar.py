from typing import Optional, Dict, List

import ciphey
import cipheycore
from ciphey.iface import ParamSpec, Config, T


class CaesarCoreDetect(ciphey.iface.Detector[str]):
    def what(self) -> List[str]:
        return ["caesar"]

    def scoreLikelihood(self, ctext: T) -> Dict[str, float]:
        # Match the distribution, and then run a chi-squared analysis
        pass

    def __init__(self, config: Config):
        super().__init__(config)

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