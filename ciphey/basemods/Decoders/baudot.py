import re
from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry

@registry.register_multi((str, str), (bytes, bytes))
class Baudot(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """Write the code that decodes here
        ctext -> the input to the function
        returns string
    """
        baudot_map = {
            '00100': ' ',
            '00011': 'A',
            '11001': 'B',
            '01110': 'C',
            '01001': 'D',
            '00001': 'E',
            '01101': 'F',
            '11010': 'G',
            '10100': 'H',
            '00110': 'I',
            '01011': 'J',
            '01111': 'K',
            '10010': 'L',
            '11100': 'M',
            '01100': 'N',
            '11000': 'O',
            '10110': 'P',
            '10111': 'Q',
            '01010': 'R',
            '00101': 'S',
            '10000': 'T',
            '00111': 'U',
            '11110': 'V',
            '10011': 'W',
            '11101': 'X',
            '10101': 'Y',
            '10001': 'Z',
            '11011': '',
            '11111': '',
        }
        baudot_digit_map = {
            '00100': ' ',
            '00011': '-',
            '11001': '?',
            '01110': ':',
            '01001': '$',
            '00001': '3',
            '01101': '!',
            '11010': '&',
            '10100': '#',
            '00110': '8',
            '01011': '\'',
            '00101': 'BELL',
            '01111': '(',
            '10010': ')',
            '11100': '.',
            '01100': ',',
            '11000': '9',
            '10110': '0',
            '10111': '1',
            '01010': '4',
            '10000': '5',
            '00111': '7',
            '11110': ';',
            '10011': '2',
            '11101': '/',
            '10101': '6',
            '10001': '\"',
            '11011': '',
            '11111': '',
        }

        ret = ""
        j = 0

        if type(ctext) == str:
            if re.search("^[01]{5}$", ctext.split()[0]):
                for i in ctext.split():
                    if i == "11011":
                        j = 1
                    if i == "11111":
                        j = 0
                    if j == 1:
                        ret += baudot_digit_map[i]
                    if j == 0:
                        ret += baudot_map[i]
                return ret
        else:
            return None

    @staticmethod
    def priority() -> float:
        """How often is this seen in a CTF out of 1
        Returns float
        """
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """The parameters this returns"""
        return None

    @staticmethod
    def getTarget() -> str:
        """The name of the decoding ussed
        returns string
        """
        return "baudot"