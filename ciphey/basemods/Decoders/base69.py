# community
# by https://github.com/lukasgabriel
# translated to Python and adapted for Ciphey from the JS original at https://github.com/pshihn/base69

from math import floor, ceil

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry


@registry.register
class Base69(Decoder[str, str]):

    def byte_to_chars(self, n: int):
        return f'{self.CHARS[n % 69]}{self.CHARS[floor(n / 69)]}'

    def chars_to_byte(self, s: str):
        return (69 * self.CHARS.index(s[1])) + (self.CHARS.index(s[0]))

    def decode_chunk(self, s: str):
        padded_bytes = s.endswith('=')
        decoded = []
        for i in range(8):
            decoded[i] = 0 if i == 7 and padded_bytes else chars_to_byte(s[ i * 2 : i * 2 + 2 ])
        result = []
        for i in range(8):
            t1 = decoded[i] << (i + 1)
            t2 = decoded[i + 1] >> (7 - i - 1)
            result[i] = t1 | t2
        return result

    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base69 decoding
        """
        extra_bytes = 0
        clen = len(ctext)
        if ctext[clen - 1] == '=':
            extra_bytes = ctext[clen - 2]
        CHUNK_COUNT = ceil(clen / 16)
        result = []
        for i in range(CHUNK_COUNT):
            chunk_string = ctext[i * 16 : (i + 1) * 16]
            if extra_bytes and (i == CHUNK_COUNT - 1):
                result[self.decode_chunk(chunk_string)[0: 7 - extra_bytes]] = i * 7
            else:
                result[self.decode_chunk(chunk_string)] =  i * 7
        return result


    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self, config: Config):
        self.CHARS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-*<>|') # To be moved to CipheyDists
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "base69"
