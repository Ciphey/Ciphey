from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, T, registry
import logging
from rich.logging import RichHandler
from pywhat import identifier
from rich.console import Console

console = Console()


@registry.register
class What(Checker[str]):

    """
    Uses PyWhat to determine plaintext with regexes
    https://github.com/bee-san/pyWhat
    """

    def check(self, ctext: T) -> Optional[str]:
        logging.debug("Trying PyWhat checker")
        returned_regexes = self.id.identify(ctext, api=True)
        if len(returned_regexes["Regexes"]) > 0:
            # If greppable mode is on, don't print this
            if self.config.verbosity > 0:
                console.print(
                    f'\nI think the plaintext is a [yellow]{returned_regexes["Regexes"][0]["Regex Pattern"]["Name"]}[/yellow].'
                )
            return f'The plaintext is a [yellow]{returned_regexes["Regexes"][0]["Regex Pattern"]["Name"]}[/yellow].'
        return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 2e-7 * len(text)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    def __init__(self, config: Config):
        super().__init__(config)
        self.config = config
        self.id = identifier.Identifier()
