from typing import Dict, Optional

from loguru import logger
from pywhat import identifier

from ciphey.iface import Checker, Config, ParamSpec, T, registry


@registry.register
class GTestChecker(Checker[str]):

    """
    G-test of fitness, similar to Chi squared.
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace("Trying PyWhat checker")
        returned_regexes = self.id.identify(text)
        if returned_regexes["Regexes"] > 0:
            return returned_regexes["Regexes"][0]["Regex Pattern"]["Name"]
        return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 4e-7 * len(text)

    def __init__(self, config: Config):
        super().__init__(config)
        self.id = identifier.Identifier()

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
