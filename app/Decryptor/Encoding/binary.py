import binascii


class Binary:
    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
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
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": result,
                "Cipher": "Ascii to Binary encoded",
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
        """
        my own binary decoder lol ;p
        """
        text = text.replace(" ", "")
        # to a bytes string
        text = text.encode("utf-8")

        # into base 2
        n = int(text, 2)

        # into ascii
        text = n.to_bytes((n.bit_length() + 7) // 8, "big").decode()

        return text
