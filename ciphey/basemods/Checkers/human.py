from typing import Dict, Optional
import os
from rich.console import Console

console = Console()

from ciphey.iface import Checker, Config, ParamSpec, registry


@registry.register
class HumanChecker(Checker[str]):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def check(self, text: str) -> Optional[str]:
        with self._config().pause_spinner_handle():
            response = console.input(f"Result [blue bold]{text.__repr__()}[/blue bold] ([green]y[/green]/[red]N[/red]): ")
        if response == "y":
            self.clear_terminal()
            return ""
        elif response in ("n", ""):
            return None
        else:
            return self.check(text)

    def getExpectedRuntime(self, text: str) -> float:
        return 1  # About a second

    def __init__(self, config: Config):
        super().__init__(config)

    def clear_terminal(self):
        # https://stackoverflow.com/a/2084628
        os.system('cls' if os.name == 'nt' else 'clear')
