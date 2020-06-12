from typing import Optional, Dict, Any

from loguru import logger
import cipheydists
import ciphey
from ciphey.iface import T, U


class MorseCode(ciphey.iface.Decoder[str, str]):
    def decode(self, text: T) -> Optional[U]:
        logger.trace("Attempting morse code")

        try:
            result = ""
            for word in text.split("/"):
                for char in word.strip().split():
                    if char not in self.ALLOWED:
                        return None
                    # translates every letter
                    try:
                        m = self.MORSE_CODE_DICT_INV[char]
                    except KeyError:
                        m = ""
                    result = result + m
                    # after every word add a space
                # after every word add a space
                result = result + " "
            logger.debug(f"Morse code successful, returning {result}")
            return result.strip().upper()
        except TypeError as e:
            return None

    @staticmethod
    def getArgs() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def getName() -> str: return "morse"

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.lc = config["objs"]["checker"]
        self.ALLOWED = {".", "-", " ", "/", "\n"}
        self.MORSE_CODE_DICT = dict(cipheydists.get_charset("morse"))
        self.MORSE_CODE_DICT_INV = {v: k for k, v in self.MORSE_CODE_DICT.items()}


ciphey.iface.registry.register(MorseCode, ciphey.iface.Decoder[str, str])
