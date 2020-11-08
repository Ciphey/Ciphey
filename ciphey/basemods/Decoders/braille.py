import re

from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Config, Decoder, ParamSpec, T, Translation, U, registry

@registry.register
class Braille(Decoder[str]):
    def decode(self, text: T) -> Optional[U]:
        braille_matches = 0
        for symbol in self.BRAILLE_DICT_INV.values():
            if symbol in text:
                braille_matches += 1
            else:
                continue
        if braille_matches == 0:
            return None

        for pattern, value in self.BRAILLE_DICT.items():
            text = re.sub(pattern, value, text)

        wordArr = []
        for word in text.split(' '):
            # if two commas are infront of word, uppercase word and remove comma
            if (word[:2].find(',,') != -1):
                wordArr.append(word.replace(',,', '').upper())
            else:
                wordArr.append(word)

        result = []
        for word in wordArr:
            # if one comma is infront of word, capitalize word and remove comma
            if (word[0].find(',') != -1):
                result.append(word.replace(',', '').capitalize())
            else:
                result.append(word)

        return ' '.join(result)

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)
        self.BRAILLE_DICT = config.get_resource(self._params()["dict"], Translation)
        self.BRAILLE_DICT_INV = {v: k for k, v in self.BRAILLE_DICT.items()}

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The braille dictionary to use",
                req=False,
                default="cipheydists::translate::braille",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "braille"
