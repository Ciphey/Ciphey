from typing import Optional, Dict, Any

from loguru import logger

import ciphey
from ciphey.iface import registry


@registry.register
class Octal(ciphey.iface.Decoder[str, bytes]):
    def decode(self, text: str) -> Optional[bytes]:
        """
        It takes an octal string and return a string
            :octal_str: octal str like "110 145 154"
        """
        str_converted = []
        octal_seq = text.split(" ")
        if len(octal_seq) == 1:
            # Concatted octal must be formed of octal triplets
            if len(text) % 3 != 0:
                return None
            octal_seq = [text[i : i + 3] for i in range(0, len(text), 3)]
            logger.trace(f"Trying chunked octal {octal_seq}")
        try:
            for octal_char in octal_seq:
                if len(octal_char) > 3:
                    logger.trace(f"Octal subseq too long")
                    return None
                n = int(octal_char, 8)
                if (
                    n < 0
                ):  # n cannot be greater than 255, as we checked that with the earlier length check
                    logger.trace(f"Non octal char {octal_char}")
                    return None
                str_converted.append(n)

            return bytes(str_converted)
        # Catch bad octal chars
        except ValueError:
            return None

    @staticmethod
    def priority() -> float:
        return 0.025

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "octal"

