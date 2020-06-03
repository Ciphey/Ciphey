from loguru import logger


class Ascii:
    """
    turns ASCII numbers into strings
    """

    def __init__(self, lc):
        self.lc = lc

    def decrypt(self, text):
        logger.debug("Running ASCII decrypt")
        try:
            result = self.deascii(text)
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
            logger.debug(f"English found in ASCII, returning {result}")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": result,
                "Cipher": "Ascii to Ascii number encoded",
                "Extra Information": None,
            }

    def deascii(self, text):
        # splits into individual ascii nums
        text = text.split(" ")
        sentence = []
        # for every char in the text (63, for example)
        for char in text:
            # turn it from ascii num to char and append to list
            sentence.append(chr(char))
        # return the list as a string
        return "".join(sentence)
