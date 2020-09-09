from typing import Optional, Dict, List

from loguru import logger

from . import brandon
from ciphey.iface import registry, Checker, ParamSpec, T, Config

import json


@registry.register
class GTestChecker(Checker[str]):

    """
    G-test of fitness, similar to Chi squared.
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace(f"Trying entropy checker")
        pass

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 4e-7 * len(text)

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
