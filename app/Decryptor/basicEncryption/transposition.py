import math

class Transposition:
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        # Brute-force by looping through every possible key.
        for key in range(1, len(text)):
            decryptedText = self.decryptMessage(key, text)
            if self.lc.checkLanguage(decryptedText):
                return {"lc": self.lc, "IsPlaintext?": True, "Plaintext": decryptedText, "Cipher": "Transposition", "Extra Information": f"The key used is {key}"}
        
            return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": "Transposition", "Extra Information": None}
    def decryptMessage(self, key, message):
        # The transposition decrypt function will simulate the "columns" and
        # "rows" of the grid that the plaintext is written on by using a list
        # of strings. First, we need to calculate a few values.
    
        # The number of "columns" in our transposition grid:
        numOfColumns = int(math.ceil(len(message) / float(key)))
        # The number of "rows" in our grid will need:
        numOfRows = key
        # The number of "shaded boxes" in the last "column" of the grid:
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    
        # Each string in plaintext represents a column in the grid.
        plaintext = [''] * numOfColumns
    
        # The column and row variables point to where in the grid the next
        # character in the encrypted message will go.
        column = 0
        row = 0
    
        for symbol in message:
            plaintext[column] += symbol
            column += 1 # Point to next column.
    
            # If there are no more columns OR we're at a shaded box, go back to
            # the first column and the next row:
            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1
    
        return ''.join(plaintext)