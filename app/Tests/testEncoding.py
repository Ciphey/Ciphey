import sys
sys.path.append("..")
import unittest
from app.Decryptor.Encoding.encodingParent import EncodingParent
from languageCheckerMod.languageChecker import LanguageChecker
# python3 -m unittest Tests.testchi_squared
# python -m unittest discover -s tests
# python3 -m unittest discover -s Tests -p test*.py
# ["sha1", "md5", "sha256", "sha512", "caeser", "plaintext"]

class TestNN(unittest.TestCase):
    def test_english_yes(self):
        lc = LanguageChecker()
        ep = EncodingParent(lc)
        ep.decrypt("eW91ciB0ZXh0")
        #self.assertEqual(result['IsPlaintext?'], True)