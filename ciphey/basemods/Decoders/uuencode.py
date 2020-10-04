from typing import Optional, Dict

from ciphey.iface import ParamSpec, Config, Decoder, registry

from loguru import logger

from codecs import decode

@registry.register
class Uuencode(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        """
        UUEncode (for Unix to Unix Encoding) is a symmetric encryption 
        based on conversion of binary data (split into 6-bit blocks) into ASCII characters.

        This function decodes the input string 'ctext' if it has been decoded using `uuencoder`. 
        Will return 'None' otherwise
        """
        logger.trace("Attempting uuencode decode")
        try:
            # uuencoded messages begin with "begin (mode) (name)". 
            # So we can skip the decoding if that is not the case
            if ctext.startswith('begin'):
                res = decode(bytes(ctext, 'utf-8'), 'uu').decode()
                logger.debug(f"uuencode decode gave '{res}'")
                return res
            else:
                logger.debug("Not a valid uuencoded text")
                return None
        except ValueError:
            logger.trace("uuuencode decode failed")
            return None

    @staticmethod
    def priority() -> float:
        # low probability as it is a not a commonly used encoding.
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """No parameters needed"""
        pass

    @staticmethod
    def getTarget() -> str:
        return "uuencode"
