class Transposition:
    """
    Transposition hacker. Try to multi 
    """
    def __init__(self, lc):
        self.lc = lc

    def main(self):
        # this main exists so i can test it
        myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri

        ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaetee
        
        oinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fs
        
        edbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  a
        
        ihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.
        
        rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh
        
        meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a
        
        ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofg
        
        BRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm
        
        -eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

        hackedMessage = self.hackTransposition(myMessage)

    def hackTransposition(message):
        # we could probably multi thread this
        for key in range(1, len(message)):
            decryptedText = transpositionDecrypt.decryptMessage(key, message)
            # if decrypted text is english, return true
            if self.lc.checkLanguage(decryptedText):
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Transposition",
                    "Extra Information": f"The key is {key}",
                }
        # after all keys, return false
        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": "Transposition",
            "Extra Information": None,
        }

    def decrypt(self, text):
        # Brute-force by looping through every possible key.
        decryptedText = self.hackTransposition(text)

    def getName(self):
        return "Transposition"

    def decryptMessage(key, message):
        numOfColumns = int(math.ceil(len(message) / float(key)))
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
        plaintext = [""] * numOfColumns
        column = 0
        row = 0
        for symbol in message:
            plaintext[column] += symbol
            column += 1  # Point to the next column.

            if (column == numOfColumns) or (
                column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes
            ):
                column = 0
                row += 1
        return "".join(plaintext)


if __name__ == "__main__":
    t = Transposition("a")
    t.main()
