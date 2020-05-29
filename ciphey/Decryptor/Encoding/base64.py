import base64
import binascii
from loguru import logger

class Base64:
    """
    turns base64 strings into normal strings
    """

    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        logger.debug("Attempting base decoding")
        result = "None"
        ciph = "None"

        # try to decode, if it fails do nothing until the end
        logger.debug("Base64 decode attempt")
        try:
            result = base64.b64decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
        except ValueError:
            None
        
        if self.lc.checkLanguage(result):
            logger.debug(f"Base64 successful, returning {result}")
            return self.goodRet(result, cipher="Base64")

        # Base32
        logger.debug("attempting base32")
        try:
            result = base64.b32decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
        except ValueError:
            None

        if self.lc.checkLanguage(result):
            logger.debug(f"base32 successful, {result}")      
            return self.goodRet(result, cipher="Base32")

        # Base16
        logger.debug("Attempting base16")
        try:
            result = base64.b16decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
        except ValueError:
            None

        if self.lc.checkLanguage(result):
            logger.debug(f"Base16 successful, {result}")
            return self.goodRet(result, cipher="Base16")

        # Base85
        logger.debug("Attempting base85")
        try:
            result = base64.b85decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
        except ValueError:
            None

        if self.lc.checkLanguage(result):
            logger.debug(f"Base85 successful, {result}")
            return self.goodRet(result, cipher="Base85")

        # if nothing works, it has failed.
        return self.badRet()

    def goodRet(self, result, cipher):
        logger.debug(f"Result for base is true, where result is {result}")
        return {
            "lc": self.lc,
            "IsPlaintext?": True,
            "Plaintext": result,
            "Cipher": cipher,
            "Extra Information": None,
        }

    def badRet(self):
        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": None,
            "Extra Information": None,
        }
