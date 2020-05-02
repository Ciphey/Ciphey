from mathsHelper import mathsHelper


class Affine:
    def __init__(self, lc):
        self.lc = lc
        self.mh = mathsHelper()
        self.SYMBOLS = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
        )

    def decrypt(self, text):
        # Brute-force by looping through every possible key
        for key in range(len(self.SYMBOLS) ** 2):
            keyA = self.getKeyParts(key)[0]
            if self.mh.gcd(keyA, len(self.SYMBOLS)) != 1:
                continue
            decryptedText = self.decryptMessage(key, message)

            if self.lc.checkLanguage(decryptedText):
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": decryptedText,
                    "Cipher": "Affine",
                    "Extra Information": f"The key used is {key}",
                }

        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": "Affine",
            "Extra Information": None,
        }

    def getName(self):
        return "Affine"

    def getKeyParts(self, key):
        keyA = key // len(SYMBOLS)
        keyB = key % len(SYMBOLS)
        return (keyA, keyB)

    def checkKeys(self, keyA, keyB, mode):
        if keyA == 1 and mode == "encrypt":
            sys.exit("Cipher is weak if key A is 1. Choose a different key.")
        if keyB == 0 and mode == "encrypt":
            sys.exit("Cipher is weak if key B is 0. Choose a different key.")
        if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
            sys.exit(
                "Key A must be greater than 0 and Key B must be between 0 and %s."
                % (len(SYMBOLS) - 1)
            )
        if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
            sys.exit(
                "Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key."
                % (keyA, len(SYMBOLS))
            )

    def decryptMessage(self, key, message):
        keyA, keyB = getKeyParts(key)
        self.checkKeys(keyA, keyB, "decrypt")
        plaintext = ""
        modInverseOfKeyA = self.mh.findModInverse(keyA, len(SYMBOLS))

        for symbol in message:
            if symbol in self.SYMBOLS:
                # Decrypt the symbol:
                symbolIndex = self.SYMBOLS.find(symbol)
                plaintext += self.SYMBOLS[
                    (symbolIndex - keyB) * modInverseOfKeyA % len(self.SYMBOLS)
                ]
            else:
                plaintext += symbol  # Append the symbol without decrypting.
        return plaintext
