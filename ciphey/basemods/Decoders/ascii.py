from typing import Optional, Dict, Any

from loguru import logger

import ciphey
from ciphey.iface import registry


@registry.register
class Ascii(ciphey.iface.Decoder[bytes, str]):
    @staticmethod
    def getTarget() -> str:
        return "utf8"

    def decode(self, text: bytes) -> Optional[str]:
        logger.trace("Attempting Ascii decode")
        # splits into individual ascii nums
        text = text.split(" ")
        sentence = []
        # for every char in the text (63, for example)
        for char in text:
            # turn it from ascii num to char and append to list
            sentence.append(chr(char))
        # return the list as a string
        logger.trace("Ascii is returning {ret}")
        return "".join(sentence)

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def getName() -> str:
        return "Ascii"

    @staticmethod
    def priority() -> float:
        return 0.1

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
