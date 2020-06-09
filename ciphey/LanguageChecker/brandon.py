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
from typing import Dict, Set

from .iface import LanguageChecker
from string import punctuation

from loguru import logger

import string
import os
import sys
from loguru import logger
from .chisquared import chiSquared

import cipheydists

sys.path.append("..")
try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import ciphey.mathsHelper as mh


class Brandon(LanguageChecker):
    """
    Class designed to confirm whether something is **language** based on how many words of **language** appears
    Call confirmLanguage(text, language)
    * text: the text you want to confirm
    * language: the language you want to confirm

    Find out what language it is by using chisquared.py, the highest chisquared score is the language
    languageThreshold = 45
    if a string is 45% **language** words, then it's confirmed to be english
    """

    wordlist: set

    def cleanText(self, text: str) -> set:
        """Cleans the text ready to be checked

        Strips punctuation, makes it lower case, turns it into a set separated by spaces, removes duplicate words

        Args:
            text -> The text we use to perform analysis on

        Returns:
            text -> the text as a list, now cleaned

        """
        # makes the text unique words and readable
        text = text.lower()
        text = self.mh.strip_puncuation(text)
        text = text.split(" ")
        text = set(text)
        return text

    def checkWordlist(self, text: Set[str]) -> float:
        """Sorts & searches the dict, and returns the proportion of the words that are in the dictionary

        Args:
            text -> The text we use to perform analysis on
            language -> the language we want to check

        Returns:
            counter -> how many words in text, are in the dict of language

        """
        # reads through most common words / passwords
        # and calculates how much of that is in language
        return len(text.intersection(self.wordlist)) / len(text)

    def check1000Words(self, text: Set[str]) -> bool:
        """Checks to see if word is in the list of 1000 words

        the 1000words is a dict, so lookup is O(1)

        Args:
            text -> The text we use to text (a word)

        Returns:
            bool -> whether it's in the dict or not.

        """
        # If we have no wordlist, then we can't reject the candidate on this basis
        if self.top1000Words is None:
            return True

        if text is None:
            return False
        # If any of the top 1000 words in the text appear
        # return true
        for word in text:
            # I was debating using any() here, but I think they're the
            # same speed so it doesn't really matter too much
            if word in self.top1000Words:
                return True
        return False

    def confirmLanguage(self, text: set) -> True:
        """Confirms whether given text is language

        If the proportion (taken from checkDictionary) is higher than the language threshold, return True

        Args:
            text -> The text we use to text (a word)
            language -> the language we use to check

        Returns:
            bool -> whether it's written in Language or not

        """

        proportion = self.checkWordlist(text)
        if self.checkWordlist(text) >= self.languageThreshold:
            logger.trace(f"The language proportion {proportion} is over the threshold {self.languageThreshold}")
            return True
        else:
            logger.trace(f"The language proportion {proportion} is under the threshold {self.languageThreshold}")
            return False

    def __init__(self, config: dict):
        # Suppresses warning
        super().__init__(config)
        self.mh = mh.mathsHelper()
        self.languageThreshold = config["params"].get("threshold", 0.55)
        self.top1000Words = config["params"].get("top1000")
        self.wordlist = config["wordlist"]

    def checkLanguage(self, text: str) -> bool:
        """Checks to see if the text is in English

        Performs a decryption, but mainly parses the internal data packet and prints useful information.

        Args:
            text -> The text we use to perform analysis on

        Returns:
            bool -> True if the text is English, False otherwise.

        """
        logger.trace(f"In Language Checker with \"{text}\"")
        text = self.cleanText(text)
        logger.trace(f"Text split to \"{text}\"")
        if text == "":
            return False
        if not self.check1000Words(text):
            logger.debug(
                f"1000 words failed. This is not plaintext"
            )
            return False

        logger.trace(
            f"1000words check passed"
        )
        if not self.confirmLanguage(text):
            logger.debug(f"Dictionary check failed. This is not plaintext")
            return False

        logger.trace(f"Dictionary check passed. This is plaintext")
        return True

    @staticmethod
    def getArgs() -> Dict[str, object]:
        return {
            "top1000": {"desc": "A json dictionary of the top 1000 words", "req": False},
            "threshold": {"desc": "The minimum proportion (between 0 and 1) that must be in the dictionary", "req": False}
        }


# Define alias
ciphey_language_checker = Brandon
