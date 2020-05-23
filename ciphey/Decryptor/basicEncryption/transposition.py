"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
https://github.com/brandonskerritt/ciphey

Code taken from http://invpy.com/transpositionHacker.py
Permission granted from author.
"""

import math
from loguru import logger


class Transposition:
    def __init__(self, lc):
        self.lc = lc

    def getName(self):
        return "Transposition"

    def decrypt(self, text):
        # Brute-force by looping through every possible key.
        text = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

        decryptedText = self.hackTransposition(text)
        return decryptedText

    def hackTransposition(self, message):
        logger.debug("Entering transposition")
        # brute-force by looping through every possible key
        for key in range(1, len(message)):
            logger.debug(f"Transposition trying key {key}")
            decryptedText = self.decryptMessage(key, message)
            # if decrypted english is found, return them
            result = self.lc.checkLanguage(decryptedText)
            if key == 6:
                logger.debug(f"KEY 6 HAS BEEN REACHED")
            if result:
                logger.debug("transposition returns true")
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Transposition",
                    "Extra Information": f"The key is {key}",
                }

        # it is not found
        return { "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": "Transposition",
            "Extra Information": None,
        }

    def decryptMessage(self, key, message):
        logger.debug("Decrypting message in transposition the mesage is {message}")
        # The transposition decrypt function will simulate the "columns" and
        # "rows" of the grid that the plaintext is written on by using a list
        # of strings. First, we need to calculate a few values.

        # The number of "columns" in our transposition grid:
        numOfColumns = math.ceil(len(message) / key)
        # The number of "rows" in our grid will need:
        numOfRows = key
        # The number of "shaded boxes" in the last "column" of the grid:
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

        # Each string in plaintext represents a column in the grid.
        plaintext = [""] * numOfColumns

        # The col and row variables point to where in the grid the next
        # character in the encrypted message will go.
        col = 0
        row = 0

        for symbol in message:
            plaintext[col] += symbol
            col += 1  # point to next column

            # If there are no more columns OR we're at a shaded box, go back to
            # the first column and the next row.
            if (col == numOfColumns) or (
                col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes
            ):
                col = 0
                row += 1

        logger.debug(f"The transposition decrypted message is {''.join(plaintext)}")
        return "".join(plaintext)
