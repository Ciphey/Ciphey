from typing import Optional, Dict

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

from loguru import logger

from codecs import decode

from binascii import a2b_uu


@registry.register
class Uuencode(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        UUEncode (Unix to Unix Encoding) is a symmetric encryption
        based on conversion of binary data (split into 6-bit blocks) into ASCII characters.

        This function decodes the input string 'ctext' if it has been encoded using 'uuencoder'
        It will return None otherwise
        """
        logger.trace("Attempting UUencode")
        result = ""
        try:
            # UUencoded messages may begin with prefix "begin" and end with suffix "end"
            # In that case, we use the codecs module in Python
            ctext_strip = ctext.strip()
            if ctext_strip.startswith("begin") and ctext_strip.endswith("end"):
                result = decode(bytes(ctext, "utf-8"), "uu").decode()
            else:
                # If there isn't a "being" prefix and "end" suffix, we use the binascii module instead
                # It is possible that the ctext has multiple lines, so convert each line and append
                ctext_split = list(filter(None, ctext.splitlines()))
                for i in range(0, len(ctext_split)):
                    result += a2b_uu(ctext_split[i]).decode("utf-8")
            logger.debug(f"UUencode successful, returning '{result}'")
            return result
        except Exception:
            logger.trace("Failed to decode UUencode")
            return None

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "uuencode"
