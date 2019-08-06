import sys
sys.path.append("..")
import unittest
from app.Decryptor.basicEncryption.caesar import Caesar
from languageCheckerMod.languageChecker import LanguageChecker
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py

class TestChi(unittest.TestCase):
    def test_caesar_yes(self):
        """Checks to see if it returns True (it should)"""
        lc = LanguageChecker()
        c = Caesar(lc)
        result = c.decrypt("uryyb zl sngure uryyb zl zbgure naq v ernyyl qb yvxr n tbbq ratyvfu oernxsnfg")
        self.assertEqual(result, True)
    def test_caesar_no(self):
        """Checks to see if it returns True (it should)"""
        lc = LanguageChecker()
        c = Caesar(lc)
        result = c.decrypt("o iozad iikwas")
        self.assertEqual(result, False)
    def test_caesar_plaintext_yes(self):
        """Checks to see if it returns True (it should)"""
        lc = LanguageChecker()
        c = Caesar(lc)
        result = c.decrypt("What about plaintext?")
        self.assertEqual(result, True)