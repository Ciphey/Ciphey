import random
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import random
import base64
import binascii
import cipheydists
import string
import cipheycore
import cipheydists
import base58
import base62
import re

import lukas


class encipher:

    """Generates encrypted text. Used for the NN and test_generator"""

    def __init__(self):  # pragma: no cover
        """Inits the encipher object """
        self.text = self.read_text()
        self.MAX_SENTENCE_LENGTH = 5
        self.crypto = encipher_crypto()

    def read_text(self):  # pragma: no cover
        f = open("hansard.txt", encoding="ISO-8859-1")
        x = f.read()
        splits = nltk.tokenize.sent_tokenize(x)
        return splits

    def getRandomSentence(self, size):  # pragma: no cover
        return TreebankWordDetokenizer().detokenize(
            random.sample(self.text, random.randint(1, size))
        )

    def getRandomEncryptedSentence(self, size):  # pragma: no cover
        sents = self.getRandomSentence(size)

        sentsEncrypted = self.crypto.randomEncrypt(sents)
        return {"PlainText Sentences": sents, "Encrypted Texts": sentsEncrypted}


class encipher_crypto:  # pragma: no cover

    """Holds the encryption functions
    can randomly select an encryption function  use on text
    returns:
        {"text": t, "plaintext": c, "cipher": p, "suceeds": False}

    where suceeds is whether or not the text is really encrypted or falsely decrypted

    Uses Cyclic3's module  generate psuedo random text"""

    def __init__(self):  # pragma: no cover
        self.methods = [
            self.Base64,
            self.Ascii,
            self.Base16,
            self.Base32,
            self.Binary,
            self.Hex,
            self.MorseCode,
            self.Reverse,
            self.Vigenere,
            self.base58_bitcoin,
            self.base58_ripple,
            self.b62,
        ]
        self.morse_dict = dict(cipheydists.get_translate("morse"))
        self.letters = string.ascii_lowercase
        self.group = cipheydists.get_charset("english")["lcase"]

    # pragma: no cover
    def random_key(self, text) -> str:  # pragma: no cover
        if len(text) < 8:
            length = 3
        else:
            length = 8
        return self.random_string(length)

    def random_string(self, length) -> str:  # pragma: no cover
        return "".join(random.sample(self.letters, length))

    def randomEncrypt(self, text: str) -> str:  # pragma: no cover
        """Randomly encrypts string with an encryption"""
        func__use = random.choice(self.methods)
        encryptedText = func__use(text)
        name = func__use.__name__

        return {"PlainText": text, "EncryptedText": encryptedText, "CipherUsed": name}

    def Base64(self, text: str) -> str:  # pragma: no cover
        """Turns text in base64 using Python libray

            args:
                text -> text  convert

            returns:
                text -> as base 64"""
        return base64.b64encode(bytes(text, "utf-8")).decode("utf-8")

    def Caesar(self, s, k):  # pragma: no cover
        """Iterates through each letter and constructs the cipher text"""
        new_message = ""
        facr = k % 26
        for c in s:
            new_message += self.apply_rotation(c, facr)
        return new_message

    def apply_rotation(self, c, facr):  # pragma: no cover
        """Applies a shift of facr  the letter denoted by c"""
        if c.isalpha():
            lower = ord("A") if c.isupper() else ord("a")
            c = chr(lower + ((ord(c) - lower + facr) % 26))
        return c

    def Base32(self, text: str) -> str:  # pragma: no cover
        """Turns text in base64 using Python libray

            args:
                text -> text  convert

            returns:
                text -> as base 64"""
        return base64.b32encode(bytes(text, "utf-8")).decode("utf-8")

    def Base16(self, text: str) -> str:  # pragma: no cover
        """Turns text in base64 using Python libray

            args:
                text -> text  convert

            returns:
                text -> as base 64"""
        return base64.b16encode(bytes(text, "utf-8")).decode("utf-8")

    def Binary(self, text: str) -> str:  # pragma: no cover
        return " ".join(format(ord(x), "b") for x in text)

    # pragma: no cover
    def Ascii(self, text: str) -> str:  # pragma: no cover
        res = [ord(c) for c in text]
        return " ".join([str(x) for x in res])

    def Hex(self, text: str) -> str:  # pragma: no cover
        return binascii.hexlify(text.encode()).decode("utf-8")

    def MorseCode(self, text: str) -> str:  # pragma: :wno cover
        morse = []
        for i in text:
            m = self.morse_dict.get(i.upper())
            if m == None:
                m = ""
            morse.append(m)

        output = morse
        # output = " ".join(MORSE_CODE_DICT.get(i.upper()) for i in text)

        return " ".join(output)

    def Reverse(self, text: str) -> str:
        return text[::-1]

    def Vigenere(self, plaintext):
        key = self.vig_key(plaintext, self.random_key(plaintext))
        cipheycore.vigenere_encrypt(plaintext, key, self.group)

    def vig_key(self, msg, key):
        tab = dict()
        for counter, i in enumerate(self.group):
            tab[self.group[counter]] = counter

        real_key = []
        for i in key:
            real_key.append(tab[i])
        return real_key
        # vigenere_encrypt(msg, real_key, group)

    def base58_bitcoin(self, text: str):
        return base58.b58encode(bytes(text, "utf-8")).decode("utf-8")

    def base58_ripple(self, text: str):
        return base58.b58encode(
            bytes(text, "utf-8"), alphabet=base58.RIPPLE_ALPHABET
        ).decode("utf-8")

    def b62(self, text: str):
        return base62.decode(str(re.sub(r"[^A-Za-z1-9]+", "", text)))


