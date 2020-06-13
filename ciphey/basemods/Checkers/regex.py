from typing import Optional, Dict

import ciphey
import re
from ciphey.iface import ParamSpec, T, Config


class Regex(ciphey.iface.Checker[str]):
    def __init__(self, config: Config):
        super().__init__(config)
        self.regex = re.compile(config.params[self.getName()]["regex"])

    def check(self, text: str) -> bool:
        return bool(re.match(self.regex, text))

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "regex": ParamSpec(req=True, desc="The regex that must be matched (in a substring)")
        }

    @staticmethod
    def getName() -> str: return "regex"


ciphey.iface.registry.register(Regex, ciphey.iface.Checker[str])
