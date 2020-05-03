import base64
import binascii


class Base64:
    """
    turns base64 strings into normal strings
    """

    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        print("Trying bases")
        result = "None"
        ciph = "None"

        # try to decode, if it fails do nothing until the end
        try:
            result = base64.b64decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
            print(result)
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
        
        if self.lc.checkLanguage(result):
            return self.goodRet(result, cipher="Base64")
            
        
        # Base32\
        try:
            result = base64.b32decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None

        if self.lc.checkLanguage(result):
            return self.goodRet(result, cipher="Base32")

        # Base16
        try:
            result = base64.b16decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
            
        if self.lc.checkLanguage(result):
            return self.goodRet(result, cipher="Base16")
        
        # Base85
        try:
            result = base64.b85decode(text)
            # yeet turning b strings into normal stringy bois
            result = result.decode("utf-8")
        except UnicodeDecodeError as e:
            None
        except binascii.Error as e:
            None
            
        if self.lc.checkLanguage(result):
            return self.goodRet(result, cipher="Base85")

        # if nothing works, it has failed.        
        return self.badRet

    def goodRet(self, result, cipher):
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