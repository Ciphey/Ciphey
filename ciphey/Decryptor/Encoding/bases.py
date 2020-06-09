import base64
import binascii
from loguru import logger


class Bases:
    """
    turns base64 strings into normal strings
    """

    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        logger.debug("Attempting base decoding")

        bases = [
            self.base32(text),
            self.base16(text),
            self.base64(text),
        ]
        for answer in bases:
            try:
                if answer["IsPlaintext?"]:
                    # good answer
                    logger.debug(f"Returning true for {answer}")
                    return answer
            except TypeError:
                continue
        # Base85
        # if nothing works, it has failed.
        return self.badRet()

    def base64(self, text):
        """Bases decode

            args:
                text -> text to decode
            returns:
                the text decoded as base64
        """
        logger.trace("Attempting base64")
        result = None
        try:
            result = base64.b64decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            return None
        except binascii.Error as e:
            return None
        except ValueError:
            return None

        if result is not None and self.lc.checkLanguage(result):
            logger.debug(f"Bases successful, returning {result}")
            return self.goodRet(result, cipher="Bases")

    def base32(self, text):
        """Base32 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base32
        """
        logger.trace("Attempting base32")
        result = None
        try:
            result = base64.b32decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            return None
        except binascii.Error as e:
            return None
        except ValueError:
            return None

        if result is not None and self.lc.checkLanguage(result):
            logger.debug(f"base32 successful, {result}")
            return self.goodRet(result, cipher="Base32")

    def base16(self, text):
        """Base16 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base16
        """
        logger.trace("Attempting base32")
        result = None
        try:
            result = base64.b16decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            return None
        except binascii.Error as e:
            return None
        except ValueError:
            return None
        if result is not None and self.lc.checkLanguage(result):
            logger.debug(f"Base16 successful, {result}")
            return self.goodRet(result, cipher="Base16")

    def base85(self, text):
        """Base85 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base85
        """
        logger.trace("Attempting base85")
        result = None
        try:
            result = base64.b85decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            return None
        except binascii.Error as e:
            return None
        except ValueError:
            return None

        if result is not None and self.lc.checkLanguage(result):
            logger.debug(f"Base85 successful, {result}")
            return self.goodRet(result, cipher="Base85")

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
