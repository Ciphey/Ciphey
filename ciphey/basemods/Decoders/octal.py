from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Octal(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Octal decoding
        """
        str_converted = []
        octal_seq = ctext.split(" ")
        if len(octal_seq) == 1:
            # Concatted octal must be formed of octal triplets
            if len(ctext) % 3 != 0:
                return None
            octal_seq = [ctext[i : i + 3] for i in range(0, len(ctext), 3)]
            logger.trace(f"Trying chunked octal {octal_seq}")
        try:
            for octal_char in octal_seq:
                if len(octal_char) > 3:
                    logger.trace("Octal subseq too long")
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

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "octal"
