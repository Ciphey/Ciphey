class MorseCode:
    def __init__(self, lc):
        self.lc = lc
        self.ALLOWED = [".", "-", " ", "/", "\n"]
        self.MORSE_CODE_DICT = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "?": "..--..",
            ".": ".-.-.-",
            " ": "/",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "\n",
        }

        self.MORSE_CODE_DICT_INV = {v: k for k, v in self.MORSE_CODE_DICT.items()}

    def decrypt(self, text):
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

        return {
            "lc": self.lc,
            "IsPlaintext?": True,
            "Plaintext": result,
            "Cipher": "Morse Code",
            "Extra Information": None,
        }

    def checkIfMorse(self, text):
        return set(self.ALLOWED).issuperset(text)

    def unmorse_it(self, text):
        returnMsg = ""
        for word in text.split("/"):
            for char in word.strip().split():
                # translates every letter
                returnMsg += self.MORSE_CODE_DICT_INV[char]
            # after every word add a space
            returnMsg += " "
        return returnMsg.strip().capitalize()
