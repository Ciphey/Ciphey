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
    2.2. If the score is not English, but we haven't tested enough to create an average, then test it against
     the dictionary

Things to optimise:
* We only run the dictionary if it's 20% smaller than the average for chi squared
* We consider it "English" if 45% of the text matches the dictionary
* We run the dictionary if there is less than 10 total chisquared test

How to add a language:
* Download your desired dictionary. Try to make it the most popular words, for example. Place this file into this
 folder with languagename.txt
As an example, this comes built in with english.txt
Find the statistical frequency of each letter in that language. 
For English, we have:
self.languages = {
    "English":
    [0.0855, 0.0160, 0.0316, 0.0387, 0.1210,0.0218, 0.0209, 0.0496, 0.0733, 0.0022,0.0081, 0.0421, 0.0253, 0.0717,
    0.0747,0.0207, 0.0010, 0.0633, 0.0673, 0.0894,0.0268, 0.0106, 0.0183, 0.0019, 0.0172,0.0011]
}
In chisquared.py
To add your language, do:
self.languages = {
    "English":
    [0.0855, 0.0160, 0.0316, 0.0387, 0.1210,0.0218, 0.0209, 0.0496, 0.0733, 0.0022,0.0081, 0.0421, 0.0253, 0.0717,
    0.0747,0.0207, 0.0010, 0.0633, 0.0673, 0.0894,0.0268, 0.0106, 0.0183, 0.0019, 0.0172,0.0011]
    "German": [0.0973]
}   
In alphabetical order
And you're.... Done! Make sure the name of the two match up
"""
from string import punctuation

try:
    import languageCheckerMod.dictionaryChecker as dc
except ModuleNotFoundError:
    import ciphey.languageCheckerMod.dictionaryChecker as dc
try:
    import languageCheckerMod.chisquared as cs
except ModuleNotFoundError:
    import ciphey.languageCheckerMod.chisquared as cs

from loguru import logger


class LanguageChecker:
    def __init__(self):
        self.dictionary = dc.dictionaryChecker()
        self.chi = cs.chiSquared()

    def __add__(self, otherLanguageObject):
        """Adds together 2 languageChecker objects


        Args:
            otherLanguageObject -> the other language checker mod

        Returns:
            A single languageCheckerObj comprised of 2

        """
        # sets the added chi squared to be of this one
        new = otherLanguageObject.getChiSquaredObj() + self.getChiSquaredObj()
        self.chi = new
        return self

    def checkLanguage(self, text: str) -> bool:
        """Checks to see if the text is in English
        Uses chisqaured

        Performs a decryption, but mainly parses the internal data packet and prints useful information.

        Args:
            text -> The text we use to perform analysis on

        Returns:
            bool -> True if the text is English, False otherwise.

        """
        logger.debug(f"In Language Checker with {text}")
        if text == "":
            return False
        result: bool = self.chi.checkChi(text)
        if not result:
            logger.debug(
                f"Chi squared failed. Attempting 1000 words"
            )
            if not self.dictionary.check1000Words(text):
                logger.debug(
                    f"1000 words failed. This is not plaintext"
                )
                return False

        logger.debug(
            f"Language check phase 1 complete"
        )
        result2: bool = self.dictionary.confirmlanguage(text, "english")
        logger.debug(f"Result is, dictionary checker, is {result2}")
        if not result2:
            logger.debug(f"Language check phase 2 returns false")
            return False
        return True


    def getChiSquaredObj(self):
        """Returns Chi squared object"""
        return self.chi

    def getChiScore(self):
        """Returns Chi score"""
        return self.chi.totalChi
