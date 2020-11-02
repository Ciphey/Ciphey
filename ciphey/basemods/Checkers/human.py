from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, registry


@registry.register
class HumanChecker(Checker[str]):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def check(self, text: str) -> Optional[str]:
        with self._config().pause_spinner_handle():
            response = input(f"Result {text.__repr__()} (y/N): ").lower()
        if response == "y":
            return ""
        elif response in ("n", ""):
            return None
        else:
            return self.check(text)

    def getExpectedRuntime(self, text: str) -> float:
        return 1  # About a second

    def __init__(self, config: Config):
        super().__init__(config)
