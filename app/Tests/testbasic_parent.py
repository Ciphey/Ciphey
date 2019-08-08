import sys
sys.path.append("..")
import unittest
from Decryptor.basicEncryption.basic_parent import BasicParent
from languageCheckerMod.languageChecker import LanguageChecker
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py

class TestBasicParent(unittest.TestCase):
    def test_basic_parent_caesar_yes(self):
        lc = LanguageChecker()
        bp = BasicParent(lc)
        result = bp.decrypt("uryyb zl sngure uryyb zl zbgure naq v ernyyl qb yvxr n tbbq ratyvfu oernxsnfg")
        self.assertEqual(result['IsPlaintext?'], True)
    def test_basic_parent_reverse_yes(self):
        lc = LanguageChecker()
        bp = BasicParent(lc)
        result = bp.decrypt("tsafkaerb hsilgne doog a ekil od yllaer i dna rehtom ym olleh rehtaf ym olleh")
        self.assertEqual(result['IsPlaintext?'], True)
    def test_basic_parent_reverse_yes_2(self):
        lc = LanguageChecker()
        bp = BasicParent(lc)
        result = bp.decrypt("sevom ylpmis rac eht ciffart ruoy lla gnillenut si hcihw redivorp NPV a ekilnU")
        self.assertEqual(result['IsPlaintext?'], True)