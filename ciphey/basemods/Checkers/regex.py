from typing import Optional, Dict

import ciphey
import re
from ciphey.iface import ParamSpec, T, Config, registry

from loguru import logger


@registry.register
class Regex(ciphey.iface.Checker[str]):
    def getExpectedRuntime(self, text: T) -> float:
        return 1e-5  # TODO: actually calculate this

    def __init__(self, config: Config):
        super().__init__(config)
        self.regexes = list(map(re.compile, self._params()["regex"]))
        logger.trace(f"There are {len(self.regexes)} regexes")

    def check(self, text: str) -> Optional[str]:
        for regex in self.regexes:
            logger.trace(f"Trying regex {regex} on {text}")
            res = regex.search(text)
            logger.trace(f"Results: {res}")
            if res:
                return f"passed with regex {regex}"

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "regex": ParamSpec(
                req=True,
                desc="The regex that must be matched (in a substring)",
                list=True,
            )
        }

    @staticmethod
    def getName() -> str:
        return "regex"
