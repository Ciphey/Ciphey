from typing import Optional, Dict, Any, List, Set

from loguru import logger

import ciphey
from ciphey.iface import registry, Level

import re


@registry.register
class Binary(ciphey.iface.Decoder[str]):
    def decode(self, text: str) -> Optional[bytes]:
        try:
            text = re.sub(r"[^\S \n]", " ", text, flags=re.UNICODE)
            text = text.replace("\n", " ")

            existing_split = self.try_split(text.split(" "))
            if existing_split is not None:
                return existing_split

            # Now we try our own grouping

            # Remove final bit of whitespace
            text = text.replace(" ", "")
            # Split into bytes, and test
            return self.try_split([text[i : i + 8] for i in range(0, len(text), 8)])
        # Catch bad octal chars
        except ValueError:
            return None

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def getLevel() -> Level:
        return Level.Common

    @staticmethod
    def getTags() -> Set[str]:
        return {"binary", "base2", "base"}

    @staticmethod
    def try_split(split_text: List[str]):
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

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
