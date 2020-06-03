import string
import os
import sys
from loguru import logger

import cipheydists

sys.path.append("..")
try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import ciphey.mathsHelper as mh


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
        self.languagePercentage: float = 0.0
        self.languageWordsCounter: float = 0.0
        self.languageThreshold = 55
        # this is hard coded because i dont want to use a library or rely on reading from files, as it's slow.
        # dictionary because lookup is O(1)
        self.top1000Words = dict.fromkeys(cipheydists.get_list("english1000"))

    def cleanText(self, text: str) -> list:
        """Cleans the texy ready to be checked

        Strips punucation, makes it lower case, turns it into a list seperated by spaces, remvoes duplicate words

        Args:
            text -> The text we use to perform analysis on

        Returns:
            text -> the text as a list, now cleaned

        """
        # makes the text unique words and readable
        text = text.lower()
        text = self.mh.strip_puncuation(text)
        text = text.split(" ")
        text = list(set(text))
        return text

    def check1000Words(self, text: str) -> bool:
        """Checks to see if word is in the list of 1000 words

        the 1000words is a dict, so lookup is O(1)

        Args:
            text -> The text we use to text (a word)

        Returns:
            bool -> whether it's in the dict or not.

        """
        if text is None:
            return False
        check = dict.fromkeys(self.top1000Words)
        logger.debug(f"text before cleaning is {text}")
        text: str = self.cleanText(text)
        logger.debug(f"Check 1000 words text is {text}")
        # If any of the top 1000 words in the text appear
        # return true
        for word in text:
            logger.debug(f"Word in check1000 is {word}")
            # I was debating using any() here, but I think they're the
            # same speed so it doesn't really matter too much
            if word in check:
                logger.debug(f"Check 1000 words returns True for word {word}")
                return True
        return False

    def checkDictionary(self, text: str, language: str) -> int:
        """Sorts & searches the dict

        ompares a word with
        The dictionary is sorted and the text is sorted
        for every single word in main dictionary
        if that word == text[0] then +1 to counter
        then +1 to text[0 + i]
        so say the dict is ordered
        we just loop through dict
        and eventually we'll reach a point where word in dict = word in text
        at that point, we move to the next text point
        both text and dict are sorted
        so we only loop once, we can do this in O(n log n) time

        Args:
            text -> The text we use to perform analysis on
            language -> the language we want to check

        Returns:
            counter -> how many words in text, are in the dict of language

        """
        # reads through most common words / passwords
        # and calculates how much of that is in language
        text: str = self.cleanText(text)
        text.sort()

        f = cipheydists.get_list(language)

        # so this should loop until it gets to the point in the @staticmethod
        # that equals the word :)
        counter: int = 0
        counter_percent: int = 0

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

    def confirmlanguage(self, text: str, language: str) -> True:
        """Confirms whether given text is language

        If the languagePercentage (taken from checkDictionary) is higher than the language threshold, reutrn True

        Args:
            text -> The text we use to text (a word)
            language -> the language we use to check

        Returns:
            bool -> whether it's written in Language or not

        """
        self.checkDictionary(text, language)
        if self.languagePercentage >= self.languageThreshold:
            logger.debug(
                f"The language percentange {self.languagePercentage} is over the threshold {self.languageThreshold}"
            )
            return True
        else:
            return False
