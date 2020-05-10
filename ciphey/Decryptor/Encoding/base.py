"""
This class decodes encrypted text using any base up to 1024.
"""

class allBases:
    def __init__(self, lc, encryptedText):
        self.lc = lc
        self.encryptedText encryptedText
        
    def numberToBase(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]
    
