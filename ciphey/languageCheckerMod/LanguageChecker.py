from string import punctuation

try:
    import ciphey.languageCheckerMod.dictionaryChecker as dc
except ModuleNotFoundError:
    import languageCheckerMod.dictionaryChecker as dc

try:
    import ciphey.languageCheckerMod.chisquared as cs
except ModuleNotFoundError:
    import languageCheckerMod.chisquared as cs

from loguru import logger


class LanguageChecker:
    def __init__(self):
        self.dictionary = dc.dictionaryChecker()
        self.chi = cs.chiSquared()

    def __add__(self, otherLanguageObject):
        """Adds together 2 languageChecker objects.


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
        """Checks to see if the text is in English.

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
            logger.debug(f"Chi squared failed. Attempting 1000 words")
            if not self.dictionary.check1000Words(text):
                logger.debug(f"1000 words failed. This is not plaintext")
                return False

        logger.debug(f"Language check phase 1 complete")
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
