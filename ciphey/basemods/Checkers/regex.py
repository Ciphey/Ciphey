import re
from typing import Dict, Optional

import logging
from rich.logging import RichHandler

from ciphey.iface import Checker, Config, ParamSpec, T, registry


@registry.register
class Regex(Checker[str]):
    def getExpectedRuntime(self, text: T) -> float:
        return 1e-5  # TODO: actually calculate this

    def __init__(self, config: Config):
        super().__init__(config)
        self.regexes = list(map(re.compile, self._params()["regex"]))
        logging.debug(f"There are {len(self.regexes)} regexes")

    def check(self, text: str) -> Optional[str]:
        for regex in self.regexes:
            logging.debug(f"Trying regex {regex} on {text}")
            res = regex.search(text)
            logging.debug(f"Results: {res}")
            if res:
                return f"Passed with regex {regex}. Want to contribute to Ciphey? Submit your regex here to allow Ciphey to automatically get this next time https://github.com/bee-san/pyWhat/wiki/Adding-your-own-Regex\n"

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "regex": ParamSpec(
                req=True,
                desc="The regex that must be matched (in a substring)",
                list=True,
            )
        }


@registry.register
class RegexList(Checker[str]):
    def getExpectedRuntime(self, text: T) -> float:
        return 1e-5  # TODO: actually calculate this

    def __init__(self, config: Config):
        super().__init__(config)
        self.regexes = []
        for i in self._params()["resource"]:
            self.regexes += [re.compile(regex) for regex in config.get_resource(i)]
        logging.debug(f"There are {len(self.regexes)} regexes")

    def check(self, text: str) -> Optional[str]:
        for regex in self.regexes:
            logging.debug(f"Trying regex {regex} on {text}")
            res = regex.search(text)
            logging.debug(f"Results: {res}")
            if res:
                return f"passed with regex {regex}"

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "resource": ParamSpec(
                req=True,
                desc="A list of regexes that could be matched",
                list=True,
            )
        }
