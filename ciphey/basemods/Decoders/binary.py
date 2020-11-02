import re
from typing import Dict, List, Optional

from loguru import logger

from ciphey.iface import Config, Decoder, ParamSpec, T, U, registry


@registry.register
class Binary(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        try:
            ctext = re.sub(r"[^\S \n]", " ", ctext, flags=re.UNICODE)
            ctext = ctext.replace("\n", " ")

            existing_split = self.try_split(ctext.split(" "))
            if existing_split is not None:
                return existing_split

            # Now we try our own grouping

            # Remove final bit of whitespace
            ctext = ctext.replace(" ", "")
            # Split into bytes, and test
            return self.try_split([ctext[i : i + 8] for i in range(0, len(ctext), 8)])
        # Catch bad octal chars
        except ValueError:
            return None

    def try_split(self, split_text: List[str]):
        ret = []

        for i in split_text:
            if len(i) == 0:
                continue
            val = int(i, 2)
            if val > 255 or val < 0:
                return None
            ret.append(val)

        if len(ret) != 0:
            ret = bytes(ret)
            logger.debug(f"binary successful, returning {ret.__repr__()}")
            return ret

    @staticmethod
    def priority() -> float:
        return 0.3

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "binary"
