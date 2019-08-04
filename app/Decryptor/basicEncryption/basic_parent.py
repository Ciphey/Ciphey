from Decryptor.basicEncryption.caesar import Caesar

class BasicParent:
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        self.caesar = Caesar(self.lc, text)
        result = self.caesar.bruteforce()

