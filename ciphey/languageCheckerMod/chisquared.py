"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt

Class calculates the Chi squared score
"""
from string import punctuation
from numpy import std
import sys

sys.path.append("..")
try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import app.mathsHelper as mh

# I had a bug where empty string was being added to letter freq dictionary
# this solves it :)
punctuation += " "
NUMBERS = "1234567890"


class chiSquared:
    """Class that calculates the Chi squared score and tries to work out what language it might be
    to add a new language, go into this class (/app/languageChecker/chisquared.py)
    Find "self.languages" and add it to the dictionary like "German":[0.789, 0.651...]
    The list is the letter frequency ordered in alphabetical order """

    def __init__(self):
        self.languages = {
            "English":
            # [0.0855, 0.0160, 0.0316, 0.0387, 0.1210,0.0218, 0.0209, 0.0496, 0.0733, 0.0022,0.0081, 0.0421, 0.0253, 0.0717, 0.0747,0.0207, 0.0010, 0.0633, 0.0673, 0.0894,0.0268, 0.0106, 0.0183, 0.0019, 0.0172,0.0011]
            # {'A': 8.12, 'B': 1.49, 'C': 2.71, 'D': 4.32, 'E': 12.02, 'F': 2.3, 'G': 2.03, 'H': 5.92, 'I': 7.31, 'J': 0.1, 'K': 0.69, 'L': 3.98, 'M': 2.61, 'N': 6.95, 'O': 7.68, 'P': 1.82, 'Q': 0.11, 'R': 6.02, 'S': 6.28, 'T': 9.1, 'U': 2.88, 'V': 1.11, 'W': 2.09, 'X': 0.17, 'Y': 2.11, 'Z': 0.07}
            [
                0.0812,
                0.0271,
                0.0149,
                0.1202,
                0.0432,
                0.0203,
                0.023,
                0.0731,
                0.0592,
                0.0069,
                0.001,
                0.026099999999999998,
                0.0398,
                0.0768,
                0.0695,
                0.0011,
                0.0182,
                0.06280000000000001,
                0.0602,
                0.0288,
                0.091,
                0.0209,
                0.0111,
                0.021099999999999997,
                0.0017000000000000001,
                0.0007000000000000001,
            ]
        }
        self.average = 0.0
        self.totalDone = 0.0
        self.oldAverage = 0.0
        self.mh = mh.mathsHelper()
        self.highestLanguage = ""
        self.totalChi = 0.0
        self.totalEqual = False
        self.chisAsaList = []

        # these are settings that may impact how the program works overall
        self.chiSquaredSignificaneThreshold = 1  # how many stds you want to go below it
        self.totalDoneThreshold = 10

        self.standarddeviation = 0.00  # the standard deviation I use
        self.oldstandarddeviation = 0.00

    def __add__(self, otherChiSquared):
        """
        each language checker has its own intance of chi squared
        so to add 2 languae checkers together we add their chi squared together
        """
        addedObject = chiSquared()
        addedObject.average = self.average + otherChiSquared.average
        addedObject.totalDone = self.totalDone + otherChiSquared.totalDone
        addedObject.totalChi = self.totalChi + otherChiSquared.totalChi
        addedObject.chisAsaList = self.chisAsaList + otherChiSquared.chisAsaList
        return addedObject

    def checkChi(self, text):
        """Checks to see if the Chi score is good
        if it is, it returns True
        Call this when you want to determine whether something is likely to be Chi or not
        
        Arguments:
            * text - the text you want to run a Chi Squared score on
        
        Outputs:
            * True - if it has a significantly lower chi squared score
            * False - if it doesn't have a significantly lower chi squared score
        """
        # TODO 20% isn't optimal
        # runs after every chi squared to see if it's 1 significantly lower than averae
        # the or statement is bc if the program has just started I don't want it to ignore the
        # ones at the start
        self.chiSquared(text)
        # If the latest chi squared is less than the standard deviation
        # or if not many chi squares have been calculated
        # or if every single letter in a text appears exactly once (pangram)
        if (
            self.chisAsaList[-1]
            <= abs(
                self.average
                - (self.oldstandarddeviation * self.chiSquaredSignificaneThreshold)
            )
            or self.totalDone < self.totalDoneThreshold
            or self.totalEqual
        ):
            return True
        else:
            return False

    def getLetterFreq(self, text):
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
                if (
                    letter not in punctuation
                    and self.mh.isAscii(letter)
                    and letter not in NUMBERS
                ):
                    letterFreq[letter] = 1
        return letterFreq

    def chiSquared(self, text):
        """Creates letter frequency of text and compares that to the letter frequency of the language"""

        # if all items of the dictionary are the same, then it's a normal distribution
        # examples of this could be "the quick brown fox jumped over the lazy dog"

        letterFreq = self.getLetterFreq(text)
        self.totalEqual = self.mh.checkEqual(list(letterFreq.values()))

        # so we dont have to calculate len more than once
        # turns them into probabilities (frequency distribution)
        lenOfString = len(text)
        totalLetterFreq = 0.0
        for key, value in letterFreq.items():
            try:
                letterFreq[key] = value / lenOfString
                totalLetterFreq = totalLetterFreq + value
            except ZeroDivisionError as e:
                print(
                    'Error, you have entered an empty string :( The error is "'
                    + str(e)
                    + '" on line 34 of LanguageChecker.py (function chiSquared)'
                )
                exit(1)

        # calculates chi squared of each language
        maxChiSquare = 0.00
        languagesChi = {}

        for language in self.languages:
            # , list(languages[language].values())
            temp = self.myChi(letterFreq, self.languages[language])
            languagesChi[language] = temp
            if temp > maxChiSquare:
                self.highestLanguage = language
                maxChiSquare = temp
        self.chisAsaList.append(maxChiSquare)
        # calculates running average
        self.oldAverage = self.average
        self.totalDone += 1
        # calculates a running average, maxChiSquare is the new chi score we get
        self.average = (self.totalChi + maxChiSquare) / self.totalDone
        self.oldstandarddeviation = abs(self.standarddeviation)
        self.standarddeviation = abs(std(self.chisAsaList))
        return languagesChi

    def myChi(self, text, distribution):
        """My own implementation of Chi squared using the two resources mention in the comments on this definition as guidance"""
        # chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://cgi.csc.liv.ac.uk/~john/comp105resources/lecture10.pdf
        # http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-statistic/
        # given a text frequency and a distribution, calculate it's Chi score
        chiScore = 0.0
        for counter, letter in enumerate(text.values()):
            try:
                chiScore = (
                    chiScore
                    + ((letter - distribution[counter]) ** 2) / distribution[counter]
                )
            except IndexError as e:
                return True
        return chiScore

    def getMostLikelyLanguage(self):
        """Returns what the most likely language is
        Only used when the threshold of checkChi is reached"""
        return self.highestLanguage
