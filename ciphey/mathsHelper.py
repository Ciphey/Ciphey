"""
██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt

Class to provide helper functions for mathematics
(oh, not entirely mathematics either. Some NLP stuff and sorting dicts. It's just a helper class
)
"""

from collections import OrderedDict
from string import punctuation
from loguru import logger


class mathsHelper:
    """Class to provide helper functions for mathematics and other small things"""
    def __init__(self):
        # ETAOIN is the most popular letters in order
        self.ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
        self.LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def gcd(a, b) -> int:
        """Greatest common divisor.

        The Greatest Common Divisor of a and b using Euclid's Algorithm.

        Args:
            a -> num 1
            b -> num 2

        Returns:
            Returns  GCD(a, b)

        """
        # Return
        while a != 0:
            a, b = b % a, a
        return b

    @staticmethod
    def find_mod_inverse(a: int, m: int) -> int:
        """Return the modular inverse of a % m.

        Which is the number x such that a*x % m = 1. Calculated using the Extended Euclidean Algorithm.

        Args:
            a -> num 1
            m -> num 2

        Returns:
            Returns modular inverse(u1, m)

        """
        # Return the modular inverse of a % m, which is
        # the number x such that a*x % m = 1

        if gcd(a, m) != 1:
            return None  # No mod inverse exists if a & m aren't relatively prime.

        # Calculate using the Extended Euclidean Algorithm:
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3  # Note that // is the integer division operator
            v1, v2, v3, u1, u2, u3 = (
                (u1 - q * v1),
                (u2 - q * v2),
                (u3 - q * v3),
                v1,
                v2,
                v3,
            )
        return u1 % m

    @staticmethod
    def percentage(part: float, whole: float) -> float:
        """Returns percentage.

        Just a normal algorithm to return the percent.

        Args:
            part -> part of the whole number
            whole -> the whole number

        Returns:
            Returns the percentage of part to whole.

        """
        if part <= 0 or whole <= 0:
            return 0
        # works with percentages
        return 100 * float(part) / float(whole)

    @staticmethod
    def sort_dictionary(dictionary: dict) -> dict:
        """Sorts a dictionary.

        Uses OrderedDict to sort a dictionary.

        Args:
            dictionary -> the dictionary to sort.

        Returns:
            Returns the dictionary, but sorted.

        """
        ret = dict(OrderedDict(sorted(dictionary.items())))
        logger.debug(
            f"The old dictionary was {dictionary} and I am sorting it to {ret}"
        )
        return ret

    def sort_prob_table(self, prob_table: dict) -> dict:
        """Sorts the probability table.

        Sorts a dictionary of dictionaries (and all the sub-dictionaries).

        Args:
            prob_table -> The probability table returned by the neural network to sort.

        Returns:
            Returns the prob_table, but sorted.

        """
        # for each object: prob table in dictionary
        max_overall: int = 0
        max_dict_pair: dict = {}
        highest_key = None
        empty_dict: dict = {}
        # sorts the prob table before we find max, and converts it to order dicts
        for key, value in prob_table.items():
            prob_table[key] = self.new_sort(value)
            prob_table[key] = dict(prob_table[key])

        # gets maximum key then sets it to the front
        counter_max: int = 0
        counter_prob: int = len(prob_table)
        while counter_max < counter_prob:
            max_overall = 0
            highest_key = None
            logger.debug(
                f"Running while loop in sort_prob_table, counterMax is {counter_max}"
            )
            for key, value in prob_table.items():
                logger.debug(f"Sorting {key}")
                maxLocal = 0
                # for each item in that table
                for key2, value2 in value.items():
                    logger.debug(
                        f"Running key2 {key2}, value2 {value2} for loop for {value.items()}"
                    )
                    maxLocal = maxLocal + value2
                    logger.debug(
                        f"MaxLocal is {maxLocal} and maxOverall is {max_overall}"
                    )
                    if maxLocal > max_overall:
                        logger.debug(f"New max local found {maxLocal}")
                        # because the dict doesnt reset
                        max_dict_pair = {}
                        max_overall = maxLocal
                        # so eventually, we get the maximum dict pairing?
                        max_dict_pair[key] = value
                        highest_key = key
                        logger.debug(f"Highest key is {highest_key}")
                # removes the highest key from the prob table
            logger.debug(f"Prob table is {prob_table} and highest key is {highest_key}")
            logger.debug(f"Removing {prob_table[highest_key]}")
            del prob_table[highest_key]
            logger.debug(f"Prob table after deletion is {prob_table}")
            counter_max += 1
            empty_dict = {**empty_dict, **max_dict_pair}

        # returns the max dict (at the start) with the prob table
        # this way, it should always work on most likely first.
        logger.debug(
            f"The prob table is {prob_table} and the maxDictPair is {max_dict_pair}"
        )
        logger.debug(f"The new sorted prob table is {empty_dict}")
        return empty_dict

    @staticmethod
    def new_sort(new_dict: dict) -> dict:
        """Uses OrderedDict to sort a dictionary.

        I think it's faster than my implementation.

        Args:
            new_dict -> the dictionary to sort

        Returns:
            Returns the dict, but sorted.

        """
        # (f"d is {d}")
        logger.debug(f"The old dictionary before new_sort() is {new_dict}")
        sorted_i = OrderedDict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))
        logger.debug(f"The dictionary after new_sort() is {sorted_i}")
        # sortedI = sort_dictionary(x)
        return sorted_i

    @staticmethod
    def is_ascii(s: str) -> bool:
        """Returns the boolean value if is_ascii is an ascii char.

        Does what it says on the tree. Stolen from
        https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii

        Args:
            s -> the char to check.

        Returns:
            Returns the boolean of the char.

        """

        return bool(lambda s: len(s) == len(s.encode()))

    @staticmethod
    def check_equal(a) -> bool:
        """checks if all items in an iterable are the same.

        https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical

        Args:
            a -> an iterable

        Returns:
            Returns boolean.

        """
        return a.count(a[0]) == len(a)

    @staticmethod
    def strip_puncuation(text: str) -> str:
        """Strips punctuation from a given string.

        Uses string.puncuation.

        Args:
            text -> the text to strip puncuation from.

        Returns:
            Returns string without puncuation.

        """
        text: str = str(text).translate(str.maketrans("", "", punctuation))
        return text

    def get_all_letters(self, text: str) -> dict:
        """Gets letter frequency of text.

        Uses a for loop to do it.

        Args:
            text -> the text to get letter frequency of.

        Returns:
            Returns dict of letter frequency.

        """
        # This part creates a letter frequency of the text
        letterFreq: dict = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }

        for letter in text.lower():
            if letter in letterFreq:
                letterFreq[letter] += 1
            else:
                # if letter is not puncuation, but it is still ascii
                # it's probably a different language so add it to the dict
                if letter not in punctuation and self.mh.is_ascii(letter):
                    letterFreq[letter] = 1
        return letterFreq

    def get_letter_count(self, message: str) -> dict:
        """Gets letter count.

        Returns a dictionary with keys of single letters and values of the
        count of how many times they appear in the message parameter:

        Args:
            message -> message to get letter count of.

        Returns:
            Returns dict of letter count.

        """

        letterCount = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "I": 0,
            "J": 0,
            "K": 0,
            "L": 0,
            "M": 0,
            "N": 0,
            "O": 0,
            "P": 0,
            "Q": 0,
            "R": 0,
            "S": 0,
            "T": 0,
            "U": 0,
            "V": 0,
            "W": 0,
            "X": 0,
            "Y": 0,
            "Z": 0,
        }

        for letter in message.upper():
            if letter in self.LETTERS:
                letterCount[letter] += 1

        return letterCount

    @staticmethod
    def get_item_at_index_zero(items):
        """Gets the item at index 0 from an iterable"""
        return items[0]

    def get_frequency_order(self, message: str) -> str:
        """Returns frequency order.

        Returns a string of the alphabet letters arranged in order of most
        frequently occurring in the message parameter.

        Args:
            message -> message to get freq of.

        Returns:
            str of the alphabet letters in most frequently occuring order.

        """

        # First, get a dictionary of each letter and its frequency count:
        letterToFreq = self.get_letter_count(message)

        # Second, make a dictionary of each frequency count to each letter(s)
        # with that frequency:
        freqToLetter = {}
        for letter in self.LETTERS:
            if letterToFreq[letter] not in freqToLetter:
                freqToLetter[letterToFreq[letter]] = [letter]
            else:
                freqToLetter[letterToFreq[letter]].append(letter)

        # Third, put each list of letters in reverse "self.self.ETAOIN" order, and then
        # convert it to a string:
        for freq in freqToLetter:
            freqToLetter[freq].sort(key=self.ETAOIN.find, reverse=True)
            freqToLetter[freq] = "".join(freqToLetter[freq])

        # Fourth, convert the freqToLetter dictionary to a list of
        # tuple pairs (key, value), then sort them:
        freqPairs = list(freqToLetter.items())
        freqPairs.sort(key=self.get_item_at_index_zero, reverse=True)

        # Fifth, now that the letters are ordered by frequency, extract all
        # the letters for the final string:
        freqOrder = []
        for freqPair in freqPairs:
            freqOrder.append(freqPair[1])

        return "".join(freqOrder)

    def english_freq_match_score(self, message: str) -> int:
        """Return number of mathces in the string

        Return the number of matches that the string in the message
        parameter has when its letter frequency is compared to English
        letter frequency. A "match" is how many of its six most frequent
        and six least frequent letters is among the six most frequent and
        six least frequent letters for English.

        Args:
            message -> message to get freq match of

        Returns:
            int, how many matches for the most common letters / least common letters.

        """

        freqOrder = self.get_frequency_order(message)

        matchScore = 0
        # Find how many matches for the six most common letters there are:
        for commonLetter in self.ETAOIN[:6]:
            if commonLetter in freqOrder[:6]:
                matchScore += 1
        # Find how many matches for the six least common letters there are:
        for uncommonLetter in self.ETAOIN[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1

        return matchScore
