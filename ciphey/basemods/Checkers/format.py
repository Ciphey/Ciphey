from typing import Optional, Dict, List

from loguru import logger

from . import brandon
from ciphey.iface import registry, Checker, ParamSpec, T, Config

import json


@registry.register
class JsonChecker(Checker[str]):

    """
        This object is effectively a prebuilt quroum (with requirement 1) of common patterns
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace(f"Trying json checker")

        # https://github.com/Ciphey/Ciphey/issues/389
        if text.isdigit():
            return None

        try:
            json.loads(text)
            return ""
        except ValueError:
            return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 1e-7 * len(text)  # From benchmarks I found online

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
