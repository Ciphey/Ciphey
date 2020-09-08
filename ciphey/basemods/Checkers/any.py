from typing import Optional, Dict

from ciphey.iface import registry, PolymorphicChecker, Config, ParamSpec


@registry.register
class Any(PolymorphicChecker):
    """Should only be used for debugging, frankly"""

    def getExpectedRuntime(self, text) -> float:
        return 0  # TODO: actually calculate this

    def __init__(self, config: Config):
        super().__init__(config)

    def check(self, text: str) -> Optional[str]:
        return ""

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
