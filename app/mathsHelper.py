"""
██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt

Class to provide helper functions for mathematics
(oh, not entirely mathematics)
"""

from collections import OrderedDict

class mathsHelper:
    """Class to provide helper functions for mathematics and other small things"""
    def __init__(self):
        None
    def percentage(self, part, whole):
        """Works with percentages"""
        # works with percentages
        return 100 * float(part)/float(whole)
    def sortDictionary(self, dictionary):
        """Sorts a dictionary"""
        return dict(OrderedDict(sorted(dictionary.items())))
    def isAscii(self, letter):
        """Determines whether a letter (or word) is ASCII"""
        # checks if a charecter is ascii
        # https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
        return bool(lambda s: len(s) == len(s.encode()))