from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

import base65536


@registry.register
class Base65536(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base65536 decoding
        """
        try:
            return base65536.decode(ctext).decode("utf-8")
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "base65536"
