import binascii

from loguru import logger


class Octal:
    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        logger.debug("Attempting to decrypt octal")
        try:
            result = self.decode(text)
        except ValueError as e:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": None,
                "Extra Information": None,
            }
        except TypeError as e:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": None,
                "Extra Information": None,
            }

        if self.lc.checkLanguage(result):
            logger.debug(f"Answer found for octal")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": result,
                "Cipher": "Ascii to Octal encoded",
                "Extra Information": None,
            }
        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": None,
            "Extra Information": None,
        }

    def decode(self, text):
    '''
    It takes an octal string and return a string
        :octal_str: octal str like "110 145 154"
    '''
    str_converted = ""
    for octal_char in octal_str.split(" "):
        str_converted += chr(int(octal_char, 8))
    return str_converted
