from typing import Optional, Dict, Any

from loguru import logger

import ciphey
from ciphey.iface import registry

import binascii


@registry.register
class Binary(ciphey.iface.Decoder[str, bytes]):
    @staticmethod
    def getTarget() -> str:
        return "binary"

    def decode(self, text: str) -> Optional[bytes]:
        try:
            text = text.replace(" ", "")
            # to a bytes string
            text = text.encode("utf-8")

            # into base 2
            n = int(text, 2)

            # into ascii
            text = n.to_bytes((n.bit_length() + 7) // 8, "big").decode()
            return text
        # Catch bad octal chars
        except ValueError:
            return None

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def priority() -> float:
        return 0.3

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
