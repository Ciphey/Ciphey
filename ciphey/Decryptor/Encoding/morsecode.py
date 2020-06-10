from loguru import logger
import cipheydists


class MorseCode:
    def __init__(self, lc):
        self.lc = lc
        self.ALLOWED = {".", "-", " ", "/", "\n"}
        self.MORSE_CODE_DICT = dict(cipheydists.get_charset("morse"))
        self.MORSE_CODE_DICT_INV = {v: k for k, v in self.MORSE_CODE_DICT.items()}

    def decrypt(self, text):
        logger.debug("Attempting morse code")
        if not self.checkIfMorse(text):
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Morse Code",
                "Extra Information": None,
            }
        try:
            result = self.unmorse_it(text)
        except TypeError as e:
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Morse Code",
                "Extra Information": None,
            }
        logger.debug(f"Morse code successful, returning {result}")
        return {
            "lc": self.lc,
            "IsPlaintext?": True,
            "Plaintext": result,
            "Cipher": "Morse Code",
            "Extra Information": None,
        }

    def checkIfMorse(self, text):
        count = 0
        for i in text:
            if i in self.ALLOWED:
                count += 1
        return count / len(text) > 0.625

    def unmorse_it(self, text):
        returnMsg = ""
        for word in text.split("/"):
            for char in word.strip().split():
                # translates every letter
                try:
                    m = self.MORSE_CODE_DICT_INV[char]
                except KeyError:
                    m = ""
                returnMsg = returnMsg + m
                # after every word add a space
            # after every word add a space
            returnMsg = returnMsg + " "
        return returnMsg.strip().upper()
