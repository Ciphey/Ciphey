"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
https://github.com/brandonskerritt/ciphey
"""

import transpositionDecrypt
import math
class Transposition:
    def __init__(self, lc):
        self.lc = lc
    def getName(self):
        return "Transposition"
        
    def decrypt(self, text):
        # Brute-force by looping through every possible key.
        decryptedText = self.hackTransposition(text)
        print(decryptedText)
        return decryptedText
    def hackTransposition(self, message):
        print('Hacking...')

        # Python programs can be stopped at any time by pressing Ctrl-C (on
        # Windows) or Ctrl-D (on Mac and Linux)
        print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

        # brute-force by looping through every possible key
        for key in range(1, len(message)):
            print('Trying key #%s...' % (key))
            decryptedText = decryptMessage(key, message)
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return {
                    "lc": "lc",
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Transposition",
                    "Extra Information": f"The key is {key}",
                }

        return None
    def hackTransposition(self, message):
        print('Hacking...')

        # Python programs can be stopped at any time by pressing Ctrl-C (on
        # Windows) or Ctrl-D (on Mac and Linux)
        print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

        # brute-force by looping through every possible key
        for key in range(1, len(message)):
            print('Trying key #%s...' % (key))
            decryptedText = self.decryptMessage(key, message)
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

        return None

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

def main():
    # You might want to copy & paste this text from the source code at
    # http://invpy.com/transpositionHacker.py
    myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
    x = Transposition("hello")
    hackedMessage = x.decrypt(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)

if __name__ == '__main__':
    main()