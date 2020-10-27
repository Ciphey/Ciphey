import zlib
from typing import Dict, Optional

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Gzip(Decoder[bytes]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Gzip decoding
        """
        try:
            return zlib.decompress(ctext, 16 + zlib.MAX_WBITS).decode("utf-8")
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
        return "gzip"
