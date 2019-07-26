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
        text = list(set(text)) # removes duplicate words
        text.sort()
        # can dynamically use languages then
        language = str(language) + ".txt"
        file = open("languageChecker/{}".format(language), "r")
        f = file.readlines()
        file.close()
        counter = 0.00
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
        counterPercent = 0
        for word in f:
            if counter >= len(text):
                break
            if word.strip() == text[counter]:
                counter += 1
                counterPercent += 1
        self.languageWordsCounter = counter
        self.languagePercentage = self.mh.percentage(float(self.languageWordsCounter), float(len(text)))
        return(counter)

    def confirmlanguage(self, text, language):
        self.checkDictionary(text, language)
        
        if self.languagePercentage > self.languageThreshold:
            return True
        else:
            return False
    