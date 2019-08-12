class Transposition:
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        # Brute-force by looping through every possible key.
        for key in range(1, len(message)):
            decryptedText = self.decryptMessage(key, message)
            if self.lc.
        
            # Python programs can be stopped at any time by pressing Ctrl-C (on
            # Windows) or Ctrl-D (on Mac and Linux)
            print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
        
            # Brute-force by looping through every possible key.
            for key in range(1, len(message)):
                print('Trying key #%s...' % (key))
        
                decryptedText = transpositionDecrypt.decryptMessage(key, message)
        
                if detectEnglish.isEnglish(decryptedText):
                    # Ask user if this is the correct decryption.
                    print()
                    print('Possible encryption hack:')
                    print('Key %s: %s' % (key, decryptedText[:100]))
                    print()
                    print('Enter D if done, anything else to continue hacking:')
                    response = input('> ')
        
                    if response.strip().upper().startswith('D'):
                        return decryptedText
        
            return None
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