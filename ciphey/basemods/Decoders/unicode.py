from typing import Dict, Optional

import logging
from rich.logging import RichHandler

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Utf8(Decoder[bytes]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs UTF-8 decoding
        """
        logging.debug("Attempting UTF-8 decoder")
        result = ""
        try:
            result = ctext.decode("utf-8")
            if result == ctext:
                return None
            logging.info(f"UTF-8 successful, returning '{result}'")
            return result
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        return 0.9

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "utf8"
