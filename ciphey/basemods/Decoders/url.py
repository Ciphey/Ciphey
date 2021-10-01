from typing import Dict, Optional
from urllib.parse import unquote_plus

import logging
from rich.logging import RichHandler

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Url(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs URL decoding
        """
        logging.debug("Attempting URL")
        result = ""
        try:
            result = unquote_plus(ctext, errors="strict")
            if result == ctext:
                return None
            logging.info(f"URL successful, returning '{result}'")
            return result
        except Exception:
            logging.debug("Failed to decode URL")
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
