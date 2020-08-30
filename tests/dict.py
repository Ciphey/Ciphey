from ciphey.basemods.Checkers.brandon import Brandon

config = dict()
lc = config["checker"](config)
import unittest
from loguru import logger

logger.remove()


class testDictionary(unittest.TestCase):
    def test_english_yes(self):
        dc = Brandon()
        result = dc.confirmlanguage(
            "hello again my friend this is my name and I like dogs!", "English"
        )
        self.assertEqual(result, True)

    def test_english_yes_two(self):
        dc = Brandon()
        result = dc.confirmlanguage(
            "hello my name is brandon and this is a normal english text timtable fuse kindle hormone",
            "English",
        )
        self.assertEqual(result, True)

    def test_english_false(self):
        dc = Brandon()
        result = dc.confirmlanguage("jdajj kop9u0r 9jjidasjp", "English")
        self.assertEqual(result, False)

    def test_english_false_two(self):
        dc = Brandon()
        result = dc.confirmlanguage(
            "pink jdajj red 9jjidasjp october whisky odiajdq", "English"
        )
        self.assertEqual(result, True)

    # def test_english_percentage(self):
    #     dc = Brandon()
    #     result = dc.confirmlanguage(
    #         "The password for my computer is tyu456q and the username is admin",
    #         "English",
    #     )
    #     self.assertEqual(dc.languagePercentage, 90.0)

    def test_english_perfect(self):
        dc = Brandon()
        result = dc.confirmlanguage(
            "Archimedes famously said: “Give me a lever long enough and a fulcrum on which to place it, and I shall move the world.” But what we are talking about here is not physical leverage. It is the leverage of ideas. When you create content, people can access your knowledge without taking your time. You no longer need to sell knowledge by the hour. Your ideas are the most valuable currency in a knowledge-driven economy. Just as an investment account allows your money to grow day and night without your involvement, content does the same with your ideas. Until recently, the average person wasn’t able to publish and distribute their ideas at a reasonable cost. But on the Internet, anybody, in any corner of the world, in any time zone, can access your best thinking. 24 hours a day. 7 days a week. 365 days a year. When you publish ideas, you create your own “Serendipity Vehicle” – a magnet for ideas and people and opportunities from potentially every corner of the globe. If your ideas resonate with people, people will discover you and bring you unexpected opportunities. They’ll open doors you never knew existed.",
            "English",
        )
        self.assertEqual(result, True)
