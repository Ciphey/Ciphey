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
    import ciphey.mathsHelper as mh
from loguru import logger
import cipheycore
import cipheydists

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
        self.language = cipheydists.get_dist("twist")
        self.average = 0.0
        self.totalDone = 0.0
        self.oldAverage = 0.0
        self.mh = mh.mathsHelper()
        self.highestLanguage = ""
        self.totalChi = 0.0
        self.totalEqual = False
        self.chisAsaList = []

        # these are settings that may impact how the program works overall
        self.chiSquaredSignificanceThreshold = 0.001  # The p value that we reject below

    def checkChi(self, text):
        if text is None:
            return False
        if type(text) is bytes:
            try:
                text = text.decode()
            except:
                return None
        """Checks to see if the Chi score is good
        if it is, it returns True
        Call this when you want to determine whether something is likely to be Chi or not
        
        Arguments:
            * text - the text you want to run a Chi Squared score on
        
        Outputs:
            * True - if it has a significantly lower chi squared score
            * False - if it doesn't have a significantly lower chi squared score
        """
        # runs after every chi squared to see if it's 1 significantly lower than averae
        # the or statement is bc if the program has just started I don't want it to ignore the
        # ones at the start
        analysis = cipheycore.analyse_string(text)
        chisq = cipheycore.chisq_test(analysis, self.language)
        logger.debug(f"Chi-squared p-value is {chisq}")
        return chisq > self.chiSquaredSignificanceThreshold

    def getMostLikelyLanguage(self):
        """Returns what the most likely language is
        Only used when the threshold of checkChi is reached"""
        return self.highestLanguage
