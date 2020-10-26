from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Checker, Config, ParamSpec, T, registry


@registry.register
class GTestChecker(Checker[str]):

    """
    G-test of fitness, similar to Chi squared.
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace("Trying entropy checker")
        pass

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 4e-7 * len(text)

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
