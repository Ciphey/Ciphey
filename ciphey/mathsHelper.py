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
from typing import Optional


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
    def mod_inv(a: int, m: int) -> Optional[int]:
        """
        Returns the modular inverse of a mod m, or None if it does not exist.

        The modular inverse of a is the number a_inv that satisfies the equation
        a_inv * a mod m === 1 mod m

        Note: This is a naive implementation, and runtime may be improved in several ways.
        For instance by checking if m is prime to perform a different calculation,
        or by using the extended euclidean algorithm.
        """
        for i in range(1, m):
            if (m * i + 1) % a == 0:
                return (m * i + 1) // a
        return None

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
            logger.trace(
                f"Running while loop in sort_prob_table, counterMax is {counter_max}"
            )
            for key, value in prob_table.items():
                logger.trace(f"Sorting {key}")
                maxLocal = 0
                # for each item in that table
                for key2, value2 in value.items():
                    logger.trace(
                        f"Running key2 {key2}, value2 {value2} for loop for {value.items()}"
                    )
                    maxLocal = maxLocal + value2
                    logger.trace(
                        f"MaxLocal is {maxLocal} and maxOverall is {max_overall}"
                    )
                    if maxLocal > max_overall:
                        logger.trace(f"New max local found {maxLocal}")
                        # because the dict doesnt reset
                        max_dict_pair = {}
                        max_overall = maxLocal
                        # so eventually, we get the maximum dict pairing?
                        max_dict_pair[key] = value
                        highest_key = key
                        logger.trace(f"Highest key is {highest_key}")
                # removes the highest key from the prob table
            logger.trace(f"Prob table is {prob_table} and highest key is {highest_key}")
            logger.trace(f"Removing {prob_table[highest_key]}")
            del prob_table[highest_key]
            logger.trace(f"Prob table after deletion is {prob_table}")
            counter_max += 1
            empty_dict = {**empty_dict, **max_dict_pair}

        # returns the max dict (at the start) with the prob table
        # this way, it should always work on most likely first.
        logger.trace(
            f"The prob table is {prob_table} and the maxDictPair is {max_dict_pair}"
        )
        logger.trace(f"The new sorted prob table is {empty_dict}")
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
        logger.trace(f"The old dictionary before new_sort() is {new_dict}")
        sorted_i = OrderedDict(
            sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
        )
        logger.trace(f"The dictionary after new_sort() is {sorted_i}")
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
    def strip_puncuation(text: str) -> str:
        """Strips punctuation from a given string.

        Uses string.puncuation.

        Args:
            text -> the text to strip puncuation from.

        Returns:
            Returns string without puncuation.

        """
        text: str = (str(text).translate(str.maketrans("", "", punctuation))).strip(
            "\n"
        )
        return text
