from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Config, Decoder, ParamSpec, T, Translation, U, registry


@registry.register
class Morse_code(Decoder[str]):
    # A priority list for char/word boundaries
    BOUNDARIES = {" ": 1, "/": 2, "\n": 3}
    PURGE = {ord(c): None for c in BOUNDARIES.keys()}
    MAX_PRIORITY = 3
    ALLOWED = {".", "-", " ", "/", "\n"}
    MORSE_CODE_DICT: Dict[str, str]
    MORSE_CODE_DICT_INV: Dict[str, str]

    def decode(self, ctext: T) -> Optional[U]:
        logger.trace("Attempting Morse code decoder")

        char_boundary = word_boundary = None

        char_boundary = word_boundary = None
        char_priority = word_priority = 0
        # Custom loop allows early break
        for i in ctext:
            i_priority = self.BOUNDARIES.get(i)
            if i_priority is None:
                if i in self.ALLOWED:
                    continue
                logger.trace(f"Non-morse char '{i}' found")
                return None

            if i_priority <= char_priority or i == char_boundary or i == word_boundary:
                continue
            # Default to having a char boundary over a word boundary
            if (
                i_priority > word_priority
                and word_boundary is None
                and char_boundary is not None
            ):
                word_priority = i_priority
                word_boundary = i
                continue
            char_priority = i_priority
            char_boundary = i

        logger.trace(
            f"Char boundary is unicode {ord(char_boundary)}, and word boundary is unicode {ord(word_boundary) if word_boundary is not None else None}"
        )

        result = ""

        for word in ctext.split(word_boundary) if word_boundary else [ctext]:
            logger.trace(f"Attempting to decode word {word}")
            for char in word.split(char_boundary):
                char = char.translate(self.PURGE)
                if len(char) == 0:
                    continue
                try:
                    m = self.MORSE_CODE_DICT_INV[char]
                except KeyError:
                    logger.trace(f"Invalid codeword '{char}' found")
                    return None
                result = result + m
            # after every word add a space
            result = result + " "
        if len(result) == 0:
            logger.trace("Morse code failed to match")
            return None
        # Remove trailing space
        result = result[:-1]
        logger.debug(f"Morse code successful, returning {result}")
        return result.strip().upper()

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)
        self.MORSE_CODE_DICT = config.get_resource(self._params()["dict"], Translation)
        self.MORSE_CODE_DICT_INV = {v: k for k, v in self.MORSE_CODE_DICT.items()}

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The morse code dictionary to use",
                req=False,
                default="cipheydists::translate::morse",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "morse_code"
