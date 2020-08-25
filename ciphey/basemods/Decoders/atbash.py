# community
# by https://github.com/lukasgabriel

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry
from ciphey.common import fix_case


@registry.register
class Atbash(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Takes an encoded string and attempts to decode it according to the Atbash cipher.

            The Atbash cipher is a very simple substitution cipher without a key.
            It operates by replacing every letter in the input by its 'counterpoint'
            in the alphabet. Example: A -> Z, B -> Y, ... , M -> N and vice versa.
        """

        result = ""
        letters = list("abcdefghijklmnopqrstuvwxyz")
        atbash_dict = {letters[i]: letters[::-1][i] for i in range(26)}

        for letter in ctext.lower():
            if letter in atbash_dict.keys():
                # Match every letter of the input to its atbash counterpoint
                result += atbash_dict[letter]
            else:
                # If the current character is not in the defined alphabet,
                # just accept it as-is (useful for numbers, punctuation,...)
                result += letter
        return fix_case(result, ctext)

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.1

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "atbash"
