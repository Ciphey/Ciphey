import app.mathsHelper


class Reverse:
    def __init__(self, lc):
        self.lc = lc
        self.mh = app.mathsHelper.mathsHelper()

    def decrypt(self, message):
        message = self.mh.stripPuncuation(message)

        message = message[::-1]
        result = self.lc.checkLanguage(message)
        if result:
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": message,
                "Cipher": "Reverse",
                "Extra Information": None,
            }
        else:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Reverse",
                "Extra Information": None,
            }

    def getName(self):
        return "Reverse"
