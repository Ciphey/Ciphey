import sys

sys.path.append("..")
try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import ciphey.mathsHelper as mh
from loguru import logger


class Reverse:
    def __init__(self, lc):
        self.lc = lc
        self.mh = mh.mathsHelper()

    def decrypt(self, message):
        logger.debug("In reverse")
        message = self.mh.strip_puncuation(message)

        message = message[::-1]
        result = self.lc.checkLanguage(message)
        if result:
            logger.debug("Reverse returns True")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": message,
                "Cipher": "Reverse",
                "Extra Information": None,
            }
        else:
            logger.debug(f"Reverse returns False")
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Reverse",
                "Extra Information": None,
            }

    def getName(self):
        return "Reverse"
