from typing import Optional, Dict, Any, Set

from loguru import logger

import ciphey
from ciphey.iface import registry


@registry.register
class Hexadecimal(ciphey.iface.Decoder[str]):
    @staticmethod
    def getTarget() -> str:
        return "hexadecimal"

    @staticmethod
    def getTags() -> Set[str]:
        return {"hexadecimal", "base"}

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
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def priority() -> float:
        return 0.015

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
