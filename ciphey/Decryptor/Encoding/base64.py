import base64
import binascii


class Base64:
    """
    turns base64 strings into normal strings
    """

    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):

        try:
            result = base64.b64decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": None,
                "Extra Information": None,
            }
        except binascii.Error as e:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": None,
                "Extra Information": None,
            }
        if self.lc.checkLanguage(result):
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": result,
                "Cipher": "Base64 encoded",
                "Extra Information": None,
            }
        else:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": None,
                "Extra Information": None,
            }
