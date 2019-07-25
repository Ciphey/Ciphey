import mathsHelper 
import string
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
        self.mh = mathsHelper.mathsHelper()
        self.languagePercentage = 0.0
        self.languageWordsCounter = 0.0
        self.languageThreshold = 45
    def checkDictionary(self, text, language):
        """Compares a word with 
        The dictionary is sorted and the text is sorted"""
        # reads through most common words / passwords
        # and calculates how much of that is in language
        text = text.lower()
        text = self.mh.stripPuncuation(text)
        text = text.split(" ")
        text = text.sort()
        text = list(set(text)) # removes duplicate words
        # can dynamically use languages then
        language = str(language) + ".txt"
        f = open(language, "r")
        f = f.readlines()
        counter = 0.00
        # dictionary is "word\n" so I remove the "\n"
        for word[0:-2] in f:
            if word == text:
                counter = counter + 1
        self.languageWordsCounter = counter
        self.languagePercentage = mh.percentage(self.languageWordsCounter, len(text))
        return(counter)

    def confirmlanguage(self, text, language):
        self.checkDictionary(text, language)
        if self.languagePercentage > self.languageThreshold:
            return True
        else:
            return False
    