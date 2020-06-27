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
from typing import Dict, Set, Optional, Any
import ciphey
from string import punctuation

from loguru import logger

import string
import os
import sys
from loguru import logger
from math import ceil

from ciphey.iface import T

sys.path.append("..")
try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import ciphey.mathsHelper as mh


class Brandon(ciphey.iface.Checker[str]):
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
        text = self.mh.strip_puncuation(text)
        text = text.split(" ")
        text = set(text)
        return text

        x = []
        for word in text:
            # poor mans lemisation
            # removes 's from the dict'
            if word.endswith("'s"):
                x.append(word[0:-2])
        text = self.mh.strip_puncuation(x)
        # turns it all into lowercase and as a set
        complete = set([word.lower() for word in x])

        return complete

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

    def __init__(self, config: ciphey.iface.Config):
        # Suppresses warning
        super().__init__(config)
        self.mh = mh.mathsHelper()

        phases = config.get_resource(self._params()["phases"], ciphey.iface.Dict)

        self.thresholds_phase1 = self._params()["phase1"]
        self.thresholds_phase2 = self._params()["phase2"]
        self.top1000Words = self._params().get("top1000")
        self.wordlist = self._params()
        self.stopwords = self._params().get("stopwords")

        self.len_phase1 = len(self.thresholds_phase1)
        self.len_phase2 = len(self.thresholds_phase2)

    def check(self, text: str) -> bool:
        """Checks to see if the text is in English

        Performs a decryption, but mainly parses the internal data packet and prints useful information.

        Args:
            text -> The text we use to perform analysis on

        Returns:
            bool -> True if the text is English, False otherwise.

        """
        logger.trace(f'In Language Checker with "{text}"')
        text = self.clean_text(text)
        logger.trace(f'Text split to "{text}"')
        if text == "":
            return False

        length_text = len(text)

        # "Phase 1": {0: {"check": 0.02}, 110: {"stop": 0.15}, 150: {"stop": 0.28}}

        # Phase 1 checking

        what_to_use = {}

        # this code decides what checker / threshold to use
        # if text is over or equal to maximum size, just use the maximum possible checker
        what_to_use = self.calculateWhatChecker(
            length_text, self.thresholds_phase1.keys()
        )
        what_to_use = self.thresholds_phase1[what_to_use]
        # def checker(self, text: str, threshold: float, text_length: int, var: set) -> bool:
        if "check" in what_to_use:
            # perform check 1k words
            result = self.checker(
                text, what_to_use["check"], length_text, self.top1000Words
            )
            logger.trace(f"The result from check 1k words is {result}")
        elif "stop" in what_to_use:
            # perform stopwords
            result = self.checker(
                text, what_to_use["check"], length_text, self.stopwords
            )
            logger.trace(f"The result from check stopwords is {result}")
        else:
            logger.debug(f"It is neither stop or check, but instead {what_to_use}")

        # return False if phase 1 fails
        if not result:
            return False
        else:
            what_to_use = self.calculateWhatChecker(
                length_text, self.thresholds_phase2.keys()
            )
            what_to_use = self.thresholds_phase2[what_to_use]
            result = self.checker(
                text, what_to_use["check"], length_text, self.wordlist
            )
        logger.trace(f"Result of dictionary checker is {result}")
        return result

    def calculateWhatChecker(self, length_text, key):
        """Calculates what threshold / checker to use

        If the length of the text is over the maximum sentence length, use the last checker / threshold
        Otherwise, traverse the keys backwards until we find a key range that does not fit.
        So we traverse backwards and see if the sentence length is between current - 1 and current
        In this way, we find the absolute lowest checker / percentage threshold. 
        We traverse backwards because if the text is longer than the max sentence length, we already know.
        In total, the keys are only 5 items long or so. It is not expensive to move backwards, nor is it expensive to move forwards.

        Args:
            length_text -> The length of the text
            key -> What key we want to use. I.E. Phase1 keys, Phase2 keys.
        Returns:
            what_to_use -> the key of the lowest checker."""

        _keys = list(key)
        if length_text >= _keys[-1]:
            what_to_use = key[_keys[-1]]
        else:
            # this algorithm finds the smallest possible fit for the text
            for counter, i in reversed(enumerate(_keys)):
                if counter != 0:
                    if _keys[counter - 1] <= length_text <= i:
                        what_to_use = i
        return what_to_use

    @staticmethod
    def getParams() -> Optional[Dict[str, ciphey.iface.ParamSpec]]:
        return {
            "top1000": ciphey.iface.ParamSpec(
                desc="A wordlist of the top 1000 words",
                req=False,
                default="cipheydists::english1000",
            ),
            "wordlist": ciphey.iface.ParamSpec(
                desc="A wordlist of all the words",
                req=False,
                default="cipheydists::english",
            ),
            "stopwords": ciphey.iface.ParamSpec(
                desc="A wordlist of StopWords",
                req=False,
                default="cipheydists::englishStopWords",
            ),
            "threshold": ciphey.iface.ParamSpec(
                desc="The minimum proportion (between 0 and 1) that must be in the dictionary",
                req=False,
                default=0.45,
            ),
            "phases": ciphey.iface.ParamSpec(
                desc="Language-specific phase thresholds",
                req=False,
                default="cipheydists::brandon_english"
            )
            # "phase2": ciphey.iface.ParamSpec(
            #     desc="Tweakables",
            #     req=False,
            #     visible=False,
            #     default={
            #         0: {"dict": 0.92},
            #         75: {"dict": 0.80},
            #         110: {"dict": 0.65},
            #         150: {"dict": 0.55},
            #         190: {"dict": 0.38},
            #     },
            # ),
            # "phase1": ciphey.iface.ParamSpec(
            #     desc="Tweakables",
            #     req=False,
            #     visible=False,
            #     default={
            #         {0: {"check": 0.02}, 110: {"stop": 0.15}, 150: {"stop": 0.28}}
            #     },
            # ),
        }


# Define alias
ciphey.iface.registry.register(Brandon, ciphey.iface.Checker[str])
