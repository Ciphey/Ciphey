# by https://github.com/lukasgabriel
# translated to Python and adapted for Ciphey from the JS original at https://github.com/pshihn/base69


import re
from math import ceil

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, WordList


@registry.register
class Base69(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base69 decoding
        """
        # Remove whitespace
        try:
            ctext = re.sub(r"\s+", "", ctext, flags=re.UNICODE)
            extra_bytes = 0
            clen = len(ctext)

            if ctext[:-1] == "=":
                extra_bytes = int(ctext[clen - 2])

            CHUNK_COUNT = ceil(clen / 16)
            result = [0 for _ in range(CHUNK_COUNT * 7 - extra_bytes)]

            for i in range(CHUNK_COUNT):
                chunk_string = ctext[i * 16 : (i + 1) * 16]
                if extra_bytes and (i == CHUNK_COUNT - 1):
                    insert = self.decode_chunk(chunk_string)
                    for n, elem in enumerate(insert[0 : 7 - extra_bytes]):
                        result[n + i * 7] = elem
                else:
                    insert = self.decode_chunk(chunk_string)
                    for n, elem in enumerate(insert):
                        result[n + i * 7] = elem % 256
            return bytearray(result).decode().strip("\x00")
        except:
            return None

    def decode_chunk(self, s: str):
        padded_bytes = s.endswith("=")

        decoded = [0 for _ in range(8)]
        for i in range(8):
            decoded[i] = (
                0
                if i == 7 and padded_bytes
                else self.chars_to_byte(s[i * 2 : i * 2 + 2])
            )

        result = [0 for _ in range(7)]
        for i in range(7):
            t1 = decoded[i] << (i + 1)
            t2 = decoded[i + 1] >> (7 - i - 1)
            result[i] = t1 | t2
        return result

    def chars_to_byte(self, s: str):
        return (69 * self.CHARS.index(s[1])) + (self.CHARS.index(s[0]))

    @staticmethod
    def priority() -> float:
        # If this becomes lower or equal to the reverse, it breaks.
        # So I'll set it to 0.2 for now since it is very fast anyways.
        return 0.2

    def __init__(self, config: Config):
        super().__init__(config)
        self.CHARS = config.get_resource(self._params()["dict"], WordList)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The charset used for the decoder.",
                req=False,
                default="cipheydists::list::base69",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "base69"
