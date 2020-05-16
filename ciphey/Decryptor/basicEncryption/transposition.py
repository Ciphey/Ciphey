"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
https://github.com/brandonskerritt/ciphey
"""
import math
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

    def hackTransposition(self, message):
        Message = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
        # we could probably multi thread this
        for key in range(1, len(message)):
            decryptedText = self.decryptMessage(key, message)
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            # if decrypted text is english, return true
            if self.lc.checkLanguage(decryptedText):
                print("found decrypted text")
                """return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Transposition",
                    "Extra Information": f"The key is {key}",
                }"""
        # after all keys, return false
        print("no decrypted text")
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
        return decryptedText

    def getName(self):
        return "Transposition"

    def decryptMessage(self, key, message):
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
        plaintext = [''] * numOfColumns

        # The col and row variables point to where in the grid the next
        # character in the encrypted message will go.
        col = 0
        row = 0

        for symbol in message:
            plaintext[col] += symbol
            col += 1 # point to next column

            # If there are no more columns OR we're at a shaded box, go back to
            # the first column and the next row.
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1

        return ''.join(plaintext)



if __name__ == "__main__":
    t = Transposition("a")
    t.main()
