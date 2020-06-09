from .bases import Bases
from .binary import Binary
from .hexadecimal import Hexadecimal
from .ascii import Ascii
from .morsecode import MorseCode

from loguru import logger


class EncodingParent:
    def __init__(self, lc):
        self.lc = lc
        self.base64 = Bases(self.lc)
        self.binary = Binary(self.lc)
        self.hex = Hexadecimal(self.lc)
        self.ascii = Ascii(self.lc)
        self.morse = MorseCode(self.lc)

    def setProbTable(self, table):
        pass

    def decrypt(self, text):
        self.text = text
        torun = [self.base64, self.binary, self.hex, self.ascii, self.morse]
        logger.debug(f"Encoding parent is running {torun}")
        """
        ok so I have an array of functions
        and I want to apply each function to some text
        (text, function)
        but the way it works is you apply text to every item in the array (function)

        """
        # from multiprocessing.dummy import Pool as ThreadPool

        # pool = ThreadPool(4)
        # answers = pool.map(self.callDecrypt, torun)  # It's not worth the thread overhead
        answers = map(self.callDecrypt, torun)

        for answer in answers:
            logger.debug(f"All answers are {answers}")
            # adds the LC objects together
            # self.lc = self.lc + answer["lc"]
            if answer is not None and answer["IsPlaintext?"]:
                logger.debug(f"Plaintext found {answer}")
                return answer
        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": None,
            "Extra Information": None,
        }

    def callDecrypt(self, obj):
        # i only exist to call decrypt
        return obj.decrypt(self.text)
