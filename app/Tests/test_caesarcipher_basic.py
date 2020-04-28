import sys
# sys.path.append("..")

import unittest

from app.Decryptor.basicEncryption.caesar import Caesar
import app.languageCheckerMod.LanguageChecker
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py

# {"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar"}


class TestChi(unittest.TestCase):
    def test_caesar_yes(self):
        """Checks to see if it returns True (it should)"""
        lc = app.languageCheckerMod.LanguageChecker.LanguageChecker()
        c = Caesar.Caesar(lc)
        result = c.decrypt("uryyb zl sngure uryyb zl zbgure naq v ernyyl qb yvxr n tbbq ratyvfu oernxsnfg")
        self.assertEqual(result['IsPlaintext?'], True)

    def test_caesar_no(self):
        """Checks to see if it returns True (it should)"""
        lc = app.languageCheckerMod.LanguageChecker.LanguageChecker()
        c = Caesar.Caesar(lc)
        result = c.decrypt("o iozad iikwas")
        self.assertEqual(result['IsPlaintext?'], False)

    def test_caesar_plaintext_yes(self):
        """Checks to see if it returns True (it should)
        Ok so this returns false becaues caesar only does up to 25, not 26
        so plaintext returns false!"""
        lc = app.languageCheckerMod.LanguageChecker.LanguageChecker()
        c = Caesar.Caesar(lc)
        result = c.decrypt("What about plaintext?")
        self.assertEqual(result['IsPlaintext?'], True)

    def test_caesar_english_comparison(self):
        lc = app.languageCheckerMod.LanguageChecker.LanguageChecker()
        c = Caesar.Caesar(lc)
        result = c.decrypt("Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.")
        self.assertEqual(result['IsPlaintext?'], True)

    def test_caesar_english_comparison_yeet(self):
        lc = app.languageCheckerMod.LanguageChecker.LanguageChecker()
        c = Caesar.Caesar(lc)
        result = c.decrypt("Onrs hr mnv knbjdc enq fnnc. Sgzmj xnt zkk enq ozqshbhozshmf, zmc okdzrd bnmshmtd sn unsd enq sgd itcfdldms xnt zfqdd vhsg. Zr nsgdq trdqr gzud onhmsdc nts, sgdqd hr zcchshnmzk hmenqlzshnm sgzs NO gzr kdes nts ne sgdhq nqhfhmzk onrs sgzs sgdx gzud zccdc hm sgdhq bnlldmsr, rn okdzrd qdzc etqsgdq sn fds sgd etkk rbnod ne sgd rhstzshnm.")
        self.assertEqual(result['Plaintext'], "Post is now locked for good. Thank you all for participating, and please continue to vote for the judgement you agree with. As other users have pointed out, there is additional information that OP has left out of their original post that they have added in their comments, so please read further to get the full scope of the situation.".lower())

    def test_caesar_what_is_this(self):
        """Checks to see if it returns True (it should)
        Ok so this returns false becaues caesar only does up to 25, not 26
        so plaintext returns false!"""
        lc = app.languageCheckerMod.LanguageChecker.LanguageChecker()
        c = Caesar.Caesar(lc)
        result = c.decrypt("?")
        self.assertEqual(result['IsPlaintext?'], False)