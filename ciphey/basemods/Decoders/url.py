from typing import Dict, Optional
from urllib.parse import unquote_plus

from loguru import logger

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Url(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs URL decoding
        """
        logger.trace("Attempting URL")
        result = ""
        try:
            result = unquote_plus(ctext, errors="strict")
            if result != ctext:
                logger.debug(f"URL successful, returning '{result}'")
                return result
            else:
                return None
        except Exception:
            logger.trace("Failed to decode URL")
            return None

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
        return "url"
