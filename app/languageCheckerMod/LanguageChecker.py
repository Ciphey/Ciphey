"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt

Class to determine whether somethine is English or not.
1. Calculate the Chi Squared score of a sentence
2. If the score is significantly lower than the average score, it _might_ be English
    2.1. If the score _might_ be English, then take the text and compare it to the sorted dictionary
    in O(n log n) time.
    It creates a percentage of "How much of this text is in the dictionary?"
    The dictionary contains:
        * 20,000 most common US words
        * 10,000 most common UK words (there's no repition between the two)
        * The top 10,000 passwords
    If the word "Looks like" English (chi-squared) and if it contains English words, we can conclude it is
    very likely English. The alternative is doing the dictionary thing but with an entire 479k word dictionary (slower)
    2.2. If the score is not English, but we haven't tested enough to create an average, then test it against the dictionary

Things to optimise:
* We only run the dictionary if it's 20% smaller than the average for chi squared
* We consider it "English" if 45% of the text matches the dictionary
* We run the dictionary if there is less than 10 total chisquared test

How to add a language:
* Download your desired dictionary. Try to make it the most popular words, for example. Place this file into this folder with languagename.txt
As an example, this comes built in with english.txt
Find the statistical frequency of each letter in that language. 
For English, we have:
self.languages = {
    "English":
    [0.0855, 0.0160, 0.0316, 0.0387, 0.1210,0.0218, 0.0209, 0.0496, 0.0733, 0.0022,0.0081, 0.0421, 0.0253, 0.0717, 0.0747,0.0207, 0.0010, 0.0633, 0.0673, 0.0894,0.0268, 0.0106, 0.0183, 0.0019, 0.0172,0.0011]
}
In chisquared.py
To add your language, do:
self.languages = {
    "English":
    [0.0855, 0.0160, 0.0316, 0.0387, 0.1210,0.0218, 0.0209, 0.0496, 0.0733, 0.0022,0.0081, 0.0421, 0.0253, 0.0717, 0.0747,0.0207, 0.0010, 0.0633, 0.0673, 0.0894,0.0268, 0.0106, 0.0183, 0.0019, 0.0172,0.0011]
    "German": [0.0973]
}   
In alphabetical order
And you're.... Done! Make sure the name of the two match up
"""
from string import punctuation

try:
    import languageCheckerMod.dictionaryChecker as dc
except ModuleNotFoundError:
    import app.languageCheckerMod.dictionaryChecker as dc
try:
    import languageCheckerMod.chisquared as cs
except ModuleNotFoundError:
    import app.languageCheckerMod.chisquared as cs


class LanguageChecker:
    def __init__(self):
        self.dictionary = dc.dictionaryChecker()
        self.chi = cs.chiSquared()

    def __add__(self, otherLanguageObject):
        # sets the added chi squared to be of this one
        new = otherLanguageObject.getChiSquaredObj() + self.getChiSquaredObj()
        self.chi = new
        return self

    def checkLanguage(self, text):
        if text == "":
            return False
        result = self.chi.checkChi(text)
        if result:
            result2 = self.dictionary.confirmlanguage(text, "English")
            if result2:
                return True
            else:
                return False
        else:
            return False

    def getChiSquaredObj(self):
        return self.chi

    def getChiScore(self):
        return self.chi.totalChi
