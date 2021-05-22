from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, registry
from rich.console import Console

console = Console()


@registry.register
class HumanChecker(Checker[str]):

    """
    Uses the person's decision to determine plaintext
    """

    def check(self, ctext: str) -> Optional[str]:
        with self._config().pause_spinner_handle():
            response = console.input(
                f"Possible plaintext: [blue bold]{ctext.__repr__()}[/blue bold] ([green]y[/green]/[red]N[/red]): "
            )
        if response == "y":
            return ""
        elif response in ("n", ""):
            return None
        else:
            return self.check(ctext)

    def getExpectedRuntime(self, text: str) -> float:
        return 1  # About a second

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    def __init__(self, config: Config):
        super().__init__(config)
