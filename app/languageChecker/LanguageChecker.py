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
    2.2. If the score is not English, but we haven't tested enough to create an average, then test it against the dictionary

Things to optimise:
* We only run the dictionary if it's 20% smaller than the average for chi squared
* We consider it "English" if 45% of the text matches the dictionary
* We run the dictionary if there is less than 10 total chisquared tests

"""
from scipy.stats import chisquare
from string import punctuation
import mathsHelper
import dictionarychecker

class languageChecker:
    """Answers the question 'is this the plaintext?' and also determines what language it is"""
    def __init__(self):
        self.dictionary = dictionarychecker.dictionaryChecker()
        # todo check chi to see if its significant
        # if it is, run this
        #            if percetageOfEnglish > 45:
               # print("I'm pretty sure this is English")
    def __add__(self, otherLanguageObject):
        pass

