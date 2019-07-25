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