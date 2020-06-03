from loguru import logger


class PigLatin:
    def __init__(self, lc):
        self.lc = lc

    def getName(self):
        return "Pig Latin"

    def decrypt(self, message):
        # If the message is less than or equal to 3 charecters, it's impossible to perform
        # a pig latin cipher on it unless the word was one letter long
        logger.debug("Trying pig latin")
        if len(message) <= 3:
            logger.debug(f"Pig Latin is less than 3 so returning false")
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Pig Latin",
                "Extra Information": None,
            }

        else:
            messagePIGWAY = message

            messagePIGAY = message[0 : len(message) - 2]
            # takes the last 2 letters of message
            message2AY = messagePIGAY[-1]
            # takes last letter of word and puts it into a variable
            messagePIGAY = messagePIGAY[0 : len(messagePIGAY) - 1]
            # removes the last letter of the word
            message3AY = message2AY + messagePIGAY
            # creates a varaible which has the previous last letter as the first and
            # the rest of the word as the rest of it. This is one way to do Pig Latin.

            messagePIGWAY1 = messagePIGWAY[0 : len(messagePIGWAY) - 3]
            # takes the last 3 letters of message
            message2WAY = messagePIGWAY1
            # copies varaibles
            message2WAY = message2WAY[-1]
            # takes last letter of word and puts it into a variable
            messagePIGWAY1 = messagePIGWAY1[0 : len(messagePIGWAY1) - 1]
            # removes the last letter of the word
            messagepigWAY = message2WAY + messagePIGWAY1
            # creates a varaible which has the previous last letter as the first and
            # the rest of the word as the rest of it. This is one way to do Pig Latin.

        # TODO find a way to return 2 variables
        # this returns 2 variables in a tuple
        if self.lc.checkLanguage(message3AY):
            logger.debug("Pig latin 3AY returns True")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": message3AY,
                "Cipher": "Pig Latin",
                "Extra Information": None,
            }
        elif self.lc.checkLanguage(messagepigWAY):
            logger.debug("Pig latin WAY returns True")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": messagepigWAY,
                "Cipher": "Pig Latin",
                "Extra Information": None,
            }
        else:
            logger.debug(f"Pig Latin returns false")
            return {
                "lc": self.lc,
                "IsPlaintext?": False,
                "Plaintext": None,
                "Cipher": "Pig Latin",
                "Extra Information": None,
            }
