from typing import Optional, Dict, Any

import ciphey
from ciphey.iface import registry


@registry.register
class Hex(ciphey.iface.Decoder[str, bytes]):
    def decode(self, text: str) -> Optional[bytes]:
        """
        It takes an octal string and return a string
            :octal_str: octal str like "110 145 154"
        """
        try:
            str_converted = bytearray.fromhex(text).decode()
            return str_converted
        # Catch bad octal chars
        except ValueError:
            return None

    @staticmethod
    def priority() -> float:
        return 0.015

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "hex"
