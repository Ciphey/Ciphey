import math

class Transposition:
    def __init__(self, lc):
        self.lc = lc
    def main(self):
        myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh
                na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
                euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain
                one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp
                ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh
                gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
                aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    
        hackedMessage = self.hackTransposition(myMessage)
    
        if hackedMessage == None:
            print('Failed to hack encryption...')
        else:
            print('Copying hacked message to clipboard...')
            print(hackedMessage)
    def decrypt(self, text):
        # Brute-force by looping through every possible key.
        print(len(text))
        for key in range(1, len(text)):
            decryptedText = self.decryptMessage(key, text)
            print(decryptedText)
            if self.lc.checkLanguage(decryptedText):
                print("this is english according to lc")
                return {"lc": self.lc, "IsPlaintext?": True, "Plaintext": decryptedText, "Cipher": "Transposition", "Extra Information": f"The key used is {key}"}
        print("finished transposition")
        
        return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": "Transposition", "Extra Information": None}
    def getName(self):
        return "Transposition"
    def hackTransposition(self, message):
        print('Attempting to hack message...')
        print('Press CTRL-C on Windows or CTRL-D on macOS or Linux to cancel....')
    
        # Loop over every key
        for key in range(1, len(message)):
            print('Attempting key #%s' % (key))
            if key >= 10:
                return None
    
            decryptedText = self.decryptMessage(key, message)
            print('Key %s: %s' % (key, decryptedText[:100]))
            #if self.lc.checkLanguage(message):
                # Ask if this is correct decryption!!!
 
        # If hack failed
        return None
    def decryptMessage(self, key, message):
        # Simulate columns and rows of the grid the plaintext was written on
        numColumns = int(math.ceil(len(message) / float(key)))
        numRows = key
        numShadedBoxes = (numColumns * numRows) - len(message)
    
        # Each string in plaintext reprsents a column in the grid
        plaintext = [''] * numColumns
    
        # The column and row variables point to the grid location of the next char 
        # in the encrypted message
        column = 0
        row = 0
    
        for character in message:
            plaintext[column] += character
            column += 1
    
            # If no more columns or empty bos, move to first column of next row
            if(column == numColumns) or (column == numColumns - 1 and row >= numRows - numShadedBoxes):
                column = 0
                row += 1
    
        return''.join(plaintext)

if __name__ == '__main__':
    t = Transposition("a")
    t.main()