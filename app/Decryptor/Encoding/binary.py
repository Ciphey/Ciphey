import binascii

class Binary:
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        try:
            ret = text_to_bits(text)
        except ValueError as e:
            return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": None, "Extra Information": None}
        if self.lc.checkLanguage(result):
            return {"lc": self.lc, "IsPlaintext?": True, "Plaintext": result, "Cipher": "Ascii to Binary encoded", "Extra Information": None}

    def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    
    def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return int2bytes(n).decode(encoding, errors)
    
    def int2bytes(i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    