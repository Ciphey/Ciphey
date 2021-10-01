from typing import Dict, Optional

from ciphey.common import fix_case
from ciphey.iface import Config, Decoder, ParamSpec, T, U, WordList, registry


@registry.register
class Atbash(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Takes an encoded string and attempts to decode it according to the Atbash cipher.

        The Atbash cipher is a very simple substitution cipher without a key.
        It operates by replacing every letter in the input by its 'counterpoint'
        in the alphabet. Example: A -> Z, B -> Y, ... , M -> N and vice versa.
        """

        atbash_dict = {self.ALPHABET[i]: self.ALPHABET[::-1][i] for i in range(26)}

        result = "".join(atbash_dict.get(letter, letter) for letter in ctext.lower())
        return fix_case(result, ctext)

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.1

    def __init__(self, config: Config):
        super().__init__(config)
        self.ALPHABET = config.get_resource(self._params()["dict"], WordList)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The alphabet used for the atbash operation.",
                req=False,
                default="cipheydists::list::englishAlphabet",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "atbash"
