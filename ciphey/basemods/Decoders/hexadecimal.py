from typing import Dict, Optional

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Hexadecimal(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Hexadecimal decoding
        """
        ctext_decoded = ""
        try:
            ctext_decoded = bytearray.fromhex(ctext).decode("utf-8")
            return ctext_decoded
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        return 0.015

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "hexadecimal"
