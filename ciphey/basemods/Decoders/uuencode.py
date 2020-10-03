from typing import Optional, Dict

from ciphey.iface import ParamSpec, Config, Decoder, registry

from loguru import logger

from codecs import decode

@registry.register
class Uuencode(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        logger.trace("Attempting uuencode decode")
        try:
            res = decode(bytes(ctext, 'utf-8'), 'uu').decode()
            logger.debug(f"uuencode decode gave '{res}'")
            return res
        except ValueError:
            logger.trace("uuuencode decode failed")
            return None

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """The parameters this returns"""
        pass

    @staticmethod
    def getTarget() -> str:
        return "uuencode"
