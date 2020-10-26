from typing import Dict, Optional

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Reverse(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        return ctext[::-1]

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "reverse"
