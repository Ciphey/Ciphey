from typing import Optional, Dict

import ciphey
import re
from ciphey.iface import ParamSpec, T, Config

from loguru import logger


class Regex(ciphey.iface.Checker[str]):
    def __init__(self, config: Config):
        super().__init__(config)
        self.regexes = map(re.compile, self._params()["regex"])

    def check(self, text: str) -> bool:
        for regex in self.regexes:
            logger.trace(f"Trying regex {regex} on {text}")
            res = regex.search(text)
            logger.trace(f"Results: {res}")
            if res:
                return True
        return False

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "regex": ParamSpec(req=True, desc="The regex that must be matched (in a substring)", list=True)
        }

    @staticmethod
    def getName() -> str: return "regex"


ciphey.iface.registry.register(Regex, ciphey.iface.Checker[str])
