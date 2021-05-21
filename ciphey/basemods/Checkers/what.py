from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, T, registry
from loguru import logger
from pywhat import identifier
from rich.console import Console

console = Console()

@registry.register
class What(Checker[str]):

    """
    G-test of fitness, similar to Chi squared.
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace("Trying PyWhat checker")
        returned_regexes = self.id.identify(text, api=True)
        if len(returned_regexes["Regexes"]) > 0:
            console.print(f'\nI think the plaintext is a [yellow]{returned_regexes["Regexes"][0]["Regex Pattern"]["Name"]}[/yellow]')
            print(returned_regexes)
            exit(0)
            return returned_regexes["Regexes"][0]["Regex Pattern"]["Name"]
        return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 4e-7 * len(text)

    def __init__(self, config: Config):
        super().__init__(config)
        self.id = identifier.Identifier()

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
