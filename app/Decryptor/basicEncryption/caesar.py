"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt
"""


class Caesar:
    def __init__(self, lc):
        self.lc = lc

    def getName(self):
        return "Caesar"

    def decrypt(self, message):
        """ Simple python program to bruteforce a caesar cipher"""

        # Example string
        message = message.lower()
        # Everything we can encrypt
        SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

        for counter, key in enumerate(range(len(SYMBOLS))):
            # try again with each key attempt
            translated = ""

            for character in message:
                if character in SYMBOLS:
                    symbolIndex = SYMBOLS.find(character)
                    translatedIndex = symbolIndex - key

                    # In the event of wraparound
                    if translatedIndex < 0:
                        translatedIndex += len(SYMBOLS)

                    translated += SYMBOLS[translatedIndex]

                else:
                    # Append the symbol without encrypting or decrypting
                    translated += character

            # Output each attempt
            result = self.lc.checkLanguage(translated)
            if result:
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": translated,
                    "Cipher": "Caesar",
                    "Extra Information": f"The rotation used is {counter}",
                }
        # if none of them match English, return false!
        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": "Caesar",
            "Extra Information": None,
        }
