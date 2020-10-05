from typing import Optional, Dict

from ciphey.iface import ParamSpec, Config, Decoder, registry

from loguru import logger

from codecs import decode
from binascii import a2b_uu

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
            # uuencoded messages may begin with prefix "begin" and end with suffix "end".
            # codecs module in python is used in that case 
            ctext_strip = ctext.strip()
            if ctext_strip.startswith("begin") and ctext_strip.endswith("end"):
                res = decode(bytes(ctext, "utf-8"), "uu").decode()
            else:
                # If there is no "begin" prefix & "end" suffix use binascii module.
                # It is possible that encoded string has multiple lines, so convert each line and append
                ctext_split=list(filter(None, ctext.splitlines()))
                res = ""
                for i in range(0, len(ctext_split)):
                    res += a2b_uu(ctext_split[i]).decode("utf-8")
            logger.debug(f"uuencode decode gave '{res}'")
            return res
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
