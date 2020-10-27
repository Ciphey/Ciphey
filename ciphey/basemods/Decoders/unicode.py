from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Utf8(Decoder[bytes]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs UTF-8 decoding
        """
        logger.trace("Attempting UTF-8 decoder")
        result = ""
        try:
            result = ctext.decode("utf-8")
            if result != ctext:
                logger.debug(f"UTF-8 successful, returning '{result}'")
                return result
            else:
                return None
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
