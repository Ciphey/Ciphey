import sys
sys.path.append("..")
import unittest
from app.languageChecker import dictionaryChecker
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py
class TestChi(unittest.TestCase):
    def test_english_yes(self):
        dc = dictionaryChecker.dictionaryChecker()
        result = dc.confirmlanguage("hello again my friend this is my name and I like dogs!", "English")
        self.assertEqual(result, True)
    def test_english_yes_two(self):
        dc = dictionaryChecker.dictionaryChecker()
        result = dc.confirmlanguage("hello my name is brandon and this is a normal english text timtable fuse kindle hormone", "English")
        self.assertEqual(result, True) 
    def test_english_false(self):
        dc = dictionaryChecker.dictionaryChecker()
        result = dc.confirmlanguage("jdajj kop9u0r 9jjidasjp", "English")
        self.assertEqual(result, False)
    def test_english_false_two(self):
        dc = dictionaryChecker.dictionaryChecker()
        result = dc.confirmlanguage("pink jdajj red 9jjidasjp october whisky odiajdq", "English")
        self.assertEqual(result, False)
    def test_english_percentage(self):
        dc = dictionaryChecker.dictionaryChecker()
        result = dc.confirmlanguage("The password for my computer is tyu456q and the username is admin", "English")
        self.assertEqual(dc.languagePercentage, 80.0)