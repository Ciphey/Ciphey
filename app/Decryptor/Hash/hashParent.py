from Decryptor.Hash import hashBuster
class HashParent:
    def decrypt(self, text):
        return hashBuster.crack(text)
    def setProbTable(self, val):
        pass
