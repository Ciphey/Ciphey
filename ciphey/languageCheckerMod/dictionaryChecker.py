import string
import os
import sys

sys.path.append("..")
try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import app.mathsHelper as mh


class dictionaryChecker:
    """
    Class designed to confirm whether something is **language** based on how many words of **language** appears
    Call confirmlanguage(text, language)
    * text: the text you want to confirm
    * language: the language you want to confirm

    Find out what language it is by using chisquared.py, the highest chisquared score is the language
    languageThreshold = 45
    if a string is 45% **language** words, then it's confirmed to be english
    """

    def __init__(self):
        self.mh = mh.mathsHelper()
        self.languagePercentage = 0.0
        self.languageWordsCounter = 0.0
        self.languageThreshold = 55

    def checkDictionary(self, text, language):
        """Compares a word with 
        The dictionary is sorted and the text is sorted"""
        # reads through most common words / passwords
        # and calculates how much of that is in language
        text = text.lower()
        text = self.mh.stripPuncuation(text)
        text = text.split(" ")
        text = list(set(text))  # removes duplicate words
        text.sort()
        # can dynamically use languages then
        language = str(language) + ".txt"

        # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "English.txt")
        file = open(file_path, "r")
        f = file.readlines()
        file.close()
        f = [x.strip().lower() for x in f]
        # dictionary is "word\n" so I remove the "\n"

        # so this should loop until it gets to the point in the @staticmethod
        # that equals the word :)

        """
        for every single word in main dictionary
        if that word == text[0] then +1 to counter
        then +1 to text[0 + i]
        so say the dict is ordered
        we just loop through dict 
        and eventually we'll reach a point where word in dict = word in text
        at that point, we move to the next text point
        both text and dict are sorted
        so we only loop once, we can do this in O(n log n) time
        """
        counter = 0
        counter_percent = 0

        for dictLengthCounter, word in enumerate(f):
            # if there is more words counted than there is text
            # it is 100%, sometimes it goes over
            # so this stops that
            if counter >= len(text):
                break
            # if the dictionary word is contained in the text somewhere
            # counter + 1
            if word in text:
                counter = counter + 1
                counter_percent = counter_percent + 1
        self.languageWordsCounter = counter
        self.languagePercentage = self.mh.percentage(
            float(self.languageWordsCounter), float(len(text))
        )
        return counter

    def confirmlanguage(self, text, language):
        self.checkDictionary(text, language)
        if self.languagePercentage > self.languageThreshold:
            return True
        else:
            return False
