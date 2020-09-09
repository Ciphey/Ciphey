from typing import Optional, Dict, List

from loguru import logger

from . import brandon
from ciphey.iface import registry, Checker, ParamSpec, T, Config

import json


@registry.register
class Enttropy(Checker[str]):

    """
        Uses entropy to determine plaintext
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace(f"Trying entropy checker")
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
