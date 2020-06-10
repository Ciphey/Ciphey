import base64
import binascii
from typing import Callable

from loguru import logger


class Bases:
    """
    turns base64 strings into normal strings
    """

    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text: str):
        logger.debug("Attempting base decoding")

        bases = [
            self.base32(text),
            self.base16(text),
            self.base64(text),
            self.base85(text),
            self.ascii85(text)
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

    def _dispatch(self, decoder: Callable[[str], bytes], text: str, cipher: str):
        logger.trace("Attempting base64")
        result = None
        try:
            result = decoder(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            logger.trace("Bad unicode")
            result = None
        except binascii.Error as e:
            logger.trace("binascii error")
            result = None
        except ValueError:
            logger.trace("Failed to decode base")
            result = None
        except:
            logger.trace("Failed to decode base")
            result = None

        if result is not None and self.lc.checkLanguage(result):
            logger.debug(f"Bases successful, returning {result}")
            return self.goodRet(result, cipher=cipher)
        else:
            return self.badRet()

    def base64(self, text: str):
        """Base64 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base64
        """
        logger.trace("Attempting base64")
        return self._dispatch(base64.b64decode, text, "base64")

    def base32(self, text: str):
        """Base32 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base32
        """
        logger.trace("Attempting base32")
        return self._dispatch(base64.b32decode, text, "base32")

    def base16(self, text: str):
        """Base16 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base16
        """
        logger.trace("Attempting base16")
        return self._dispatch(base64.b16decode, text, "base16")

    def base85(self, text: str):
        """Base85 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base85
        """
        logger.trace("Attempting base85")
        return self._dispatch(base64.b85decode, text, "base85")

    def ascii85(self, text: str):
        """Base85 decode

            args:
                text -> text to decode
            returns:
                the text decoded as base85
        """
        logger.trace("Attempting ascii85")
        result = None
        return self._dispatch(base64.a85decode, text, "base85")

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
