from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, registry


@registry.register
class HumanChecker(Checker[str]):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def check(self, text: str, res: str = None) -> Optional[str]:
        """
        text = the potential plaintext
        res = the result of the checker that triggered this.
            this may be helpful if a regex checker triggered the human checker
            so if the plaintext is a bitcoin address like 3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5
            the human may not understand that this is bitcoin and may ignore it
            so we tell them what triggered this (this is a bitcoin address) to help them decide.
        """

        with self._config().pause_spinner_handle():
            if res:
                print(f"Triggered by {res}")
            response = input(f"\nResult {text.__repr__()} (y/N): ").lower()
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
