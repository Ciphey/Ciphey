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
        returned_regexes = self.id.identify(ctext)
        if returned_regexes["Regexes"]:
            matched_regex = returned_regexes["Regexes"]['text'][0]["Regex Pattern"]

            ret = f'The plaintext is a [yellow]{matched_regex["Name"]}[/yellow]'
            human = (
                f'\nI think the plaintext is a [yellow]{matched_regex["Name"]}[/yellow]'
            )

            if "Description" in matched_regex and matched_regex["Description"]:
                s = matched_regex["Description"]
                # lowercases first letter so it doesn't look weird
                s = f", which is {s[0].lower() + s[1:]}\n"
                ret += s
                human += s

            # if URL is attached, include that too.
            if "URL" in matched_regex and matched_regex["URL"]:
                link = matched_regex["URL"] + ctext.replace(" ", "")
                ret += f"\nClick here to view in browser [#CAE4F1][link={link}]{link}[/link][/#CAE4F1]\n"

            # If greppable mode is on, don't print this
            if self.config.verbosity >= 0:
                # Print with full stop
                console.print(human)
            return ret
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
