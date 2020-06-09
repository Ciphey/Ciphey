from ciphey.LanguageChecker import LanguageChecker

import unittest
from loguru import logger

logger.remove()


class testIntegration(unittest.TestCase):
    """
    tests integration between chi squared and dictionary checker
    """

    def test_basics(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage(
            "Hello my name is new and this is an example of some english text"
        )
        self.assertEqual(result, True)

    def test_basics_german(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("hallo keine lieben leute nach")
        self.assertEqual(result, False)

    def test_basics_quickbrownfox(self):
        """
        This returns true becaue by default chi squared returns true so long as it's less than 10 items it's processed
        """
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        self.assertEqual(result, True)

    def test_basics_quickbrownfox(self):
        """
        This returns true becaue by default chi squared returns true so long as it's less than 10 items it's processed
        """
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        self.assertEqual(result, True)

    def test_chi_maxima_true(self):
        """
        This returns false because s.d is not over 1 as all inputs are English
        """
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("sa dew fea dxza dcsa da fsa d")
        result = lc.checkLanguage("df grtsf a sgrds fgserwqd")
        result = lc.checkLanguage("fd sa fe safsda srmad sadsa d")
        result = lc.checkLanguage(" oihn giuhh7hguygiuhuyguyuyg ig iug iugiugiug")
        result = lc.checkLanguage(
            "oiuhiuhiuhoiuh7 a opokp[poj uyg ytdra4efriug oih kjnbjhb jgv"
        )
        result = lc.checkLanguage("r jabbi tb y jyg ygiuygytff  u0")
        result = lc.checkLanguage("ld oiu oj uh t t er s d gf hg g  h h")
        result = lc.checkLanguage(
            "posa   idijdsa ije i vi ijerijofdj ouhsaf oiuhas  oihd "
        )
        result = lc.checkLanguage(
            "Likwew e wqrew rwr safdsa dawe r3d hg jyrt dwqefp ;g;;' [ [sadqa ]]."
        )
        result = lc.checkLanguage("Her hyt e jytgv  urjfdghbsfd c   ")
        result = lc.checkLanguage("CASSAE X T H WAEASD AFDG TERFADDSFD")
        result = lc.checkLanguage("das te y we fdsbfsd fe a ")
        result = lc.checkLanguage("d pa pdpsa ofoiaoew ifdisa ikrkasd s")
        result = lc.checkLanguage(
            "My friend is a really nice people who really enjoys swimming, dancing, kicking, English."
        )
        self.assertEqual(result, True)

    def test_integration_unusual_one(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("HELLO MY NAME IS BRANDON AND I LIKE DOLLAR")
        self.assertEqual(result, True)

    def test_integration_unusual_two(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertEqual(result, False)

    def test_integration_unusual_three(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("password")
        self.assertEqual(result, True)

    def test_integration_unusual_three(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("")
        self.assertEqual(result, False)

    def test_integration_unusual_four(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage(".")
        self.assertEqual(result, False)

    def test_integration_unusual_five(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("#")
        self.assertEqual(result, False)

    def test_integration_unusual_7(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage(
            "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"
        )
        self.assertEqual(result, False)

    def test_integration_unusual_7(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("")
        self.assertEqual(result, False)

    def test_integration_addition(self):
        """
        Makes sure you can add 2 lanuggae objecs together
        """
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("hello my darling")

        lc2 = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("sad as dasr as s")

        temp = lc.getChiScore()
        temp2 = lc2.getChiScore()
        temp3 = temp + temp2
        lc3 = lc + lc2

        self.assertAlmostEqual(lc3.getChiScore(), temp3)

    def test_integration_charlesBabbage(self):
        """
        I had a bug with this exact string
        Bug is that chi squared does not score this as True
       """
        text = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's original plans. Built to tolerances achievable in the 19th century, the success of the finished engine indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the printer Babbage had designed for the difference engine."""
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage(text)
        self.assertEqual(result, True)
