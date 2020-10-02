from typing import Optional, Dict, Any, FrozenSet

from loguru import logger

import ciphey
from ciphey.iface import registry, Level


@registry.register
class Utf8(ciphey.iface.Decoder[bytes]):
    def decode(self, text: bytes) -> Optional[str]:
        logger.trace("Attempting utf-8 decode")
        try:
            res = text.decode("utf8")
            logger.debug(f"utf-8 decode gave '{res}'")
            return res if len(res) != 0 else None
        except UnicodeDecodeError:
            logger.trace("utf-8 decode failed")
            return None

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)

    @staticmethod
    def getLevel() -> Level:
        return Level.VeryCommon

    @staticmethod
    def getTags() -> FrozenSet[str]:
        return frozenset({"utf-8", "unicode", "text"})
