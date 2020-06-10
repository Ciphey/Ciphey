try:
    from Decryptor.Hash import hashBuster
except ModuleNotFoundError:
    from ciphey.Decryptor.Hash import hashBuster

from loguru import logger


class HashParent:
    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        logger.debug(f"Calling hash crackers")
        result = hashBuster.crack(text, self.lc)
        logger.debug(f"Returning {result}")
        return result

    def setProbTable(self, val):
        pass
