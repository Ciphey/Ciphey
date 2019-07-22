import sys
sys.path.append("..")
import unittest
from app.languageChecker import chisquared

# python -m unittest discover -s tests


class TestSum(unittest.TestCase):
    def test_chi_english_yes(self):
        self.chi = chisquared.chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        """
        data = [1, 2, 3]
        result = self.chi.checkChi("Hello my name is Brandon and I'm a top secret message")
        self.assertEqual(result, True)
    

if __name__ == '__main__':
    unittest.main()