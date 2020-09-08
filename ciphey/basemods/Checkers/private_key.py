from typing import Optional, Dict

from ciphey.iface import PrivateKey, registry, Checker, Config, ParamSpec


@registry.register
class PrivateKeyChecker(Checker[PrivateKey]):
    def getExpectedRuntime(self, text: PrivateKey) -> float:
        return 0

    def __init__(self, config: Config):
        super().__init__(config)

    def check(self, text: PrivateKey) -> Optional[str]:
        return ""

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
