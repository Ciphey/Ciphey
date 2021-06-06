import re
from typing import Dict, Optional

import logging
from rich.logging import RichHandler

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Decimal(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Decimal decoding
        """
        logging.debug("Attempting decimal")
        ctext_converted = []
        ctext_split = re.split(r"[ ,;:\-\n]", ctext)
        delimiters = set(sorted(re.sub(r"[^ ,;:\-\n]", "", ctext)))
        ctext_num = re.sub(r"[,;:\-\s]", "", ctext)
        ctext_decoded = ""
        if ctext_num.isnumeric() is False:
            logging.debug("Failed to decode decimal due to non numeric character(s)")
            return None
        try:
            for i in ctext_split:
                val = int(i)
                if val > 255 or val < 0:
                    logging.debug(
                        f"Failed to decode decimal due to invalid number '{val}'"
                    )
                    return None
                ctext_converted.append(chr(val))
            ctext_decoded = "".join(ctext_converted)
            logging.info(
                f"Decimal successful, returning '{ctext_decoded}' with delimiter(s) {delimiters}"
            )
            return ctext_decoded
        except Exception:
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
        return "decimal"
