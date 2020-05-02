"""
██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt

Class to provide helper functions for mathematics
(oh, not entirely mathematics)
"""

from collections import OrderedDict
from string import punctuation


class mathsHelper:
    """Class to provide helper functions for mathematics and other small things"""

    def __init__(self):
        self.ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
        self.LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def gcd(self, a, b):
        # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
        while a != 0:
            a, b = b % a, a
        return b

    def findModInverse(self, a, m):
        # Return the modular inverse of a % m, which is
        # the number x such that a*x % m = 1

        if gcd(a, m) != 1:
            return None  # No mod inverse exists if a & m aren't relatively prime.

        # Calculate using the Extended Euclidean Algorithm:
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3  # Note that // is the integer division operator
            v1, v2, v3, u1, u2, u3 = (
                (u1 - q * v1),
                (u2 - q * v2),
                (u3 - q * v3),
                v1,
                v2,
                v3,
            )
        return u1 % m

    def percentage(self, part, whole):
        """Works with percentages"""
        # yeah uhm sometimes I'm a dummy dum dum and I think dividing by 0 is a good idea
        # this if statememt is to stop my stupidity
        if part <= 0 or whole <= 0:
            return 0
        # works with percentages
        return 100 * float(part) / float(whole)

    def sortDictionary(self, dictionary):
        """Sorts a dictionary"""
        return dict(OrderedDict(sorted(dictionary.items())))

    def isAscii(self, letter):
        """Determines whether a letter (or word) is ASCII"""
        # checks if a charecter is ascii
        # https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
        return bool(lambda s: len(s) == len(s.encode()))

    def checkEqual(self, a):
        """checks if all items in an iterable are the same
        https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical"""
        return a.count(a[0]) == len(a)

    def stripPuncuation(self, text):
        """Strips punctuation from a given string"""
        text = text.translate(str.maketrans("", "", punctuation))
        return text

    def getAllLetters(self, text):
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
                if letter not in punctuation and self.mh.isAscii(letter):
                    letterFreq[letter] = 1
        return letterFreq

    def getLetterCount(self, message):
        # Returns a dictionary with keys of single letters and values of the
        # count of how many times they appear in the message parameter:
        letterCount = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "I": 0,
            "J": 0,
            "K": 0,
            "L": 0,
            "M": 0,
            "N": 0,
            "O": 0,
            "P": 0,
            "Q": 0,
            "R": 0,
            "S": 0,
            "T": 0,
            "U": 0,
            "V": 0,
            "W": 0,
            "X": 0,
            "Y": 0,
            "Z": 0,
        }

        for letter in message.upper():
            if letter in self.LETTERS:
                letterCount[letter] += 1

        return letterCount

    def getItemAtIndexZero(self, items):
        return items[0]

    def getFrequencyOrder(self, message):
        # Returns a string of the alphabet letters arranged in order of most
        # frequently occurring in the message parameter.

        # First, get a dictionary of each letter and its frequency count:
        letterToFreq = self.getLetterCount(message)

        # Second, make a dictionary of each frequency count to each letter(s)
        # with that frequency:
        freqToLetter = {}
        for letter in self.LETTERS:
            if letterToFreq[letter] not in freqToLetter:
                freqToLetter[letterToFreq[letter]] = [letter]
            else:
                freqToLetter[letterToFreq[letter]].append(letter)

        # Third, put each list of letters in reverse "self.self.ETAOIN" order, and then
        # convert it to a string:
        for freq in freqToLetter:
            freqToLetter[freq].sort(key=self.ETAOIN.find, reverse=True)
            freqToLetter[freq] = "".join(freqToLetter[freq])

        # Fourth, convert the freqToLetter dictionary to a list of
        # tuple pairs (key, value), then sort them:
        freqPairs = list(freqToLetter.items())
        freqPairs.sort(key=self.getItemAtIndexZero, reverse=True)

        # Fifth, now that the letters are ordered by frequency, extract all
        # the letters for the final string:
        freqOrder = []
        for freqPair in freqPairs:
            freqOrder.append(freqPair[1])

        return "".join(freqOrder)

    def englishFreqMatchScore(self, message):
        # Return the number of matches that the string in the message
        # parameter has when its letter frequency is compared to English
        # letter frequency. A "match" is how many of its six most frequent
        # and six least frequent letters is among the six most frequent and
        # six least frequent letters for English.
        freqOrder = self.getFrequencyOrder(message)

        matchScore = 0
        # Find how many matches for the six most common letters there are:
        for commonLetter in self.ETAOIN[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        # Find how many matches for the six least common letters there are:
        for uncommonLetter in self.ETAOIN[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1

        return matchScore
