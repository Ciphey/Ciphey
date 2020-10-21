import json
from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Checker, Config, ParamSpec, T, registry


@registry.register
class JsonChecker(Checker[str]):

    """
    This object is effectively a prebuilt quorum (with requirement 1) of common patterns
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace("Trying json checker")

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
