# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added


#%%
from string import punctuation
from scipy.stats import chisquare
import base64

with open("harrypotter.txt", "r") as f:
    text = f.read()


#%%


#%%
# replaces new lines with full stops
text = text.replace("\n", ".").lower()


#%%
# splits it up into sentences
sentences = text.split(".")


#%%
# gets rid of empty stirngs and get rid of the "i" for chapter numbers
sentences = list(filter(None, sentences))
for counter, sent in enumerate(sentences):
    if sent == "i":
        del sentences[counter]


#%%
print(sentences[:10])

#%% [markdown]
# So I want the table to look like:
# text | length | how many letters are used (uniqueness) | maybe the chi squared score ? (normalised distribution not english) | frequency distribution | what it is | the plaintext
#
# I want it to include these things:
# base64
# sha1
# md5
# sha256
# caeser cipher
# plaintext
#
# So the next step would be to create encryption functions
# then for every sentence in it
# encrypt it
# create a csv line
# plaintext | encrypted text | length | how many letters are used | frequency distribution | chi squared score | what it is (base 64, sha 256, etc)
#

#%%
def apply_rotation(c, factor):
    """Applies a shift of factor to the letter denoted by c"""
    if c.isalpha():
        lower = ord("A") if c.isupper() else ord("a")
        c = chr(lower + ((ord(c) - lower + factor) % 26))
    return c


def caesar_cipher(s, k):
    """Iterates through each letter and constructs the cipher text"""
    new_message = ""
    factor = k % 26
    for c in s:
        new_message += apply_rotation(c, factor)
    return new_message


#%%
caesar_cipher("hello", 3)


#%%
import hashlib


#%%
hash_object = hashlib.sha1(b"HelWorld")


#%%
hash_object


#%%
hash_object.hexdigest()


#%%
def sha1hash(s):
    temp = str.encode(s)
    temp = hashlib.sha1(temp)
    return temp.hexdigest()


#%%
def md5hash(s):
    temp = str.encode(s)
    temp = hashlib.md5(temp)
    return temp.hexdigest()


#%%
def sha256hash(s):
    temp = str.encode(s)
    temp = hashlib.sha256(temp)
    return temp.hexdigest()


#%%


#%%
def sha512hash(s):
    temp = str.encode(s)
    temp = hashlib.sha512(temp)
    return temp.hexdigest()


#%%
types = [
    "sha1",
    "md5",
    "sha256",
    "sha512",
    "caeser",
    "caeser",
    "plaintext",
    "reverse",
    "morse",
    "base64",
    "binary",
    "hexadecimal",
    "ascii",
]


#%%
def howManyLettersUsed(text):
    text = list(set(list(text)))
    return len(text)


#%%
def isAscii(letter):
    """Determines whether a letter (or word) is ASCII"""
    # checks if a charecter is ascii
    # https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
    return bool(lambda s: len(s) == len(s.encode()))


#%%
def reverse(s):
    return s[::-1]


#%%
def b64(s):
    s = s.encode()
    s = base64.b64encode(s)
    return s.decode()


#%%
def binary(s):
    return " ".join(format(x, "b") for x in bytearray(s))


#%%
def hexade(s):
    return "".join(hex(ord(c))[2:] for c in s)


#%%
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "?": "..--..",
    ".": ".-.-.-",
    " ": "/",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def morse(s):
    return " ".join(MORSE_CODE_DICT.get(i.upper()) for i in s)


#%%
def asci(s):
    a = []
    for ch in s:
        a.append(str(ord(ch)))
    return " ".join(a)


#%%
def getLetterFreq(text):
    # This part creates a letter frequency of the text
    letterFreq = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for letter in text.lower():
        if letter in letterFreq:
            letterFreq[letter] += 1
        else:
            # if letter is not puncuation, but it is still ascii
            # it's probably a different language so add it to the dict
            if letter not in punctuation and isAscii(letter):
                letterFreq[letter] = 1
    return list(letterFreq.values())


#%%


#%%
import csv

f = open("encryptionData.csv", "w")
counter = 0
encryption_writer = csv.writer(
    f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
)


#%%
def makeCsvLine(plaintext, text, cipher):
    plaintext = plaintext
    ciphertext = text
    length = len(text)
    howManyLetters = howManyLettersUsed(text)
    letterfreq = getLetterFreq(text)
    chi = chisquare(letterfreq)[1]

    used = cipher
    if used == "sha1":
        used = 0
    elif used == "md5":
        used = 1
    elif used == "sha256":
        used = 2
    elif used == "sha512":
        used = 3
    elif used == "caesar":
        used = 4
    elif used == "reverse":
        used = 5
    elif used == "morse":
        used = 6
    elif used == "base64":
        used = 7
    elif used == "binary":
        used = 8
    elif used == "hexadecimal":
        used = 9
    elif used == "ascii":
        used == 10
    if plaintext == "" or plaintext == None:
        return 1
    global counter
    encryption_writer.writerow(
        [plaintext, ciphertext, length, howManyLetters, letterfreq, chi, used]
    )


#%%
makeCsvLine("hello my name is brandon", "iad jadiw aikjawi", "caesar")


#%%


#%%
# types = ["sha1", "md5", "sha256", "sha512", "caeser", "caeser", "plaintext" ]
import random

for sent in sentences:
    result = random.choice(types)
    try:
        if sent == None or sent == "" or sent == " ":
            continue
        if sent[0] == " ":
            sent = sent[1::]
        if result == "sha1":
            temp = sha1hash(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "sha1")
        elif result == "md5":
            temp = md5hash(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "md5")
        elif result == "sha256":
            temp = sha256hash(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "sha256")
        elif result == "sha512":
            temp = sha512hash(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "sha512")
        elif result == "caeser":
            temp = caesar_cipher(sent, random.randint(1, 25))
            if temp == None:
                continue
            makeCsvLine(sent, temp, "caesar")
        elif result == "reverse":
            temp = reverse(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "reverse")
        elif result == "morse":
            temp = morse(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "morse")
        elif result == "base64":
            temp = b64(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "base64")
        elif result == "binary":
            temp = binary(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "binary")
        elif result == "hexadecimal":
            temp = hexade(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "hexadecimal")
        elif result == "ascii":
            temp = asci(sent)
            if temp == None:
                continue
            makeCsvLine(sent, temp, "ascii")
    except TypeError as e:
        continue


#%%


#%%


#%%
f.close()


#%%
import pandas as pd

df = pd.read_csv("encryptionData.csv", encoding="ISO-8859-15")
# df.replace('Â', ' ')
df.to_csv("output.csv", index=False)


#%%


#%%
