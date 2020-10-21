from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Checker, Config, ParamSpec, T, registry


@registry.register
class Entropy(Checker[str]):

    """
    Uses entropy to determine plaintext
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace("Trying entropy checker")
        pass

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        # Uses benchmark from Discord
        return 2e-7 * len(text)

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
