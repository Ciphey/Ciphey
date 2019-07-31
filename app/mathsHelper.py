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
        None
    def percentage(self, part, whole):
        """Works with percentages"""
        # yeah uhm sometimes I'm a dummy dum dum and I think dividing by 0 is a good idea
        # this if statememt is to stop my stupidity
        if part <= 0 or whole <= 0:
            return 0
        # works with percentages
        return 100 * float(part)/float(whole)
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
        text = text.translate(str.maketrans('','',punctuation))
        return text
    def getAllLetters(self, text):
        # This part creates a letter frequency of the text
        letterFreq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        
        for letter in text.lower():
            if letter in letterFreq:
                letterFreq[letter] +=1
            else:
                # if letter is not puncuation, but it is still ascii
                # it's probably a different language so add it to the dict
                if letter not in punctuation and self.mh.isAscii(letter) :
                    letterFreq[letter] = 1
        return letterFreq