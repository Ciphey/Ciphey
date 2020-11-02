from typing import Dict, Optional

import base62

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Base62(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base62 decoding
        """
        try:
            return base62.decodebytes(ctext).decode("utf-8")
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
        return "base62"
