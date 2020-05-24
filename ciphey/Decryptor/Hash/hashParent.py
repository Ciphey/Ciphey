try:
    from Decryptor.Hash import hashBuster
except ModuleNotFoundError:
    from ciphey.Decryptor.Hash import hashBuster

from loguru import logger

class HashParent:
    def decrypt(self, text):
        logger.debug(f"Calling hash crackers")
        result = hashBuster.crack(text)
        return result

    def setProbTable(self, val):
        pass
