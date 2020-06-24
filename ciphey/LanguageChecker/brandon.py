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
from math import ceil

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

    def clean_text(self, text: str) -> set:
        """Cleans the text ready to be checked

        Strips punctuation, makes it lower case, turns it into a set separated by spaces, removes duplicate words

        Args:
            text -> The text we use to perform analysis on

        Returns:
            text -> the text as a list, now cleaned

        """
        # makes the text unique words and readable
        text = text.lower()
        text = text.split(" ")
        new_text = []
        # TODO how did I do this in the other class.....
        for i in text:
            if i.endswith("'s"):
                new_text.append()
        text = self.mh.strip_puncuation(text)

        return set(text)

    def __name__(self):
        return "brandon"

    def checker(self, text: str, threshold: float, text_length: int, var: set) -> bool:
        """Given text determine if it passes checker

        The checker uses the vairable passed to it. I.E. Stopwords list, 1k words, dictionary

        Args:
            text -> The text to check
            threshold -> at what point do we return True? The percentage of text that is in var before we return True
            text_length -> the length of the text
            var -> the variable we are checking against. Stopwords list, 1k words list, dictionray list.
        Returns:
            boolean -> True for it passes the test, False for it fails the test."""
        if text is None:
            logger.trace(f"Checker's text is None, so returning False")
            return False
        if var is None:
            logger.trace(f"Checker's input var is None, so returning False")
            return False

        percent = ceil(text_length * threshold)
        logger.trace(f"Checker's chunks are size {percent}")
        meet_threshold = 0
        location = 0
        end = percent

        while location <= text_length:
            # chunks the text, so only gets THRESHOLD chunks of text at a time
            to_analyse = text[location:end]
            for word in to_analyse:
                # if word is a stopword, + 1 to the counter
                if word in var:
                    logger.trace(
                        f"{word} is in var, which means I am +=1 to the meet_threshold which is {meet_threshold}"
                    )
                    meet_threshold += 1
                if meet_threshold / text_length >= threshold:
                    logger.trace(
                        f"Returning true since the percentage is {meet_threshold / text_length} and the threshold is {threshold}"
                    )
                    # if we meet the threshold, return True
                    # otherwise, go over again until we do
                    # We do this in the for loop because if we're at 24% and THRESHOLD is 25
                    # we don't want to wait THRESHOLD to return true, we want to return True ASAP
                    return True
        logger.trace(
            f"The language proportion {meet_threshold} is under the threshold {threshold}"
        )
        return False

    def __init__(self, config: dict):
        # Suppresses warning
        super().__init__(config)
        self.mh = mh.mathsHelper()
        self.thresholds_phase1 = config["thresholds_phase1"]
        self.thresholds_phase2 = config["thresholds_phase2"]
        self.top1000Words = config["params"].get("top1000")
        self.wordlist = config["wordlist"]
        self.stopwords = config["params"].get("stopwords")

    def checkLanguage(self, text: str) -> bool:
        """Checks to see if the text is in English

        Performs a decryption, but mainly parses the internal data packet and prints useful information.

        Args:
            text -> The text we use to perform analysis on

        Returns:
            bool -> True if the text is English, False otherwise.

        """
        logger.trace(f'In Language Checker with "{text}"')
        text = self.cleanText(text)
        logger.trace(f'Text split to "{text}"')
        if text == "":
            return False
        if not self.check1000Words(text):
            logger.debug(f"1000 words failed. This is not plaintext")
            return False

        logger.trace(f"1000words check passed")
        if not self.confirmLanguage(text):
            logger.debug(f"Dictionary check failed. This is not plaintext")
            return False

        logger.trace(f"Dictionary check passed. This is plaintext")
        return True

    @staticmethod
    def getArgs() -> Dict[str, object]:
        return {
            "top1000": {
                "desc": "A json dictionary of the top 1000 words",
                "req": False,
            },
            "threshold": {
                "desc": "The minimum proportion (between 0 and 1) that must be in the dictionary",
                "req": False,
            },
        }


# Define alias
ciphey_language_checker = Brandon
