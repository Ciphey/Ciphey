from loguru import logger


class Hexadecimal:
    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        logger.debug("Attempting hexadecimal decryption")
        try:
            result = bytearray.fromhex(text).decode()
        except ValueError as e:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": None,
                "Extra Information": None,
            }

        if self.lc.checkLanguage(result):
            logger.debug(f"Hexadecimal successful, returning {result}")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": result,
                "Cipher": "Ascii to Hexadecimal encoded",
                "Extra Information": None,
            }
