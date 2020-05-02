from languageCheckerMod.chisquared import chiSquared
import unittest


class testChi(unittest.TestCase):
    def test_chi_english_yes(self):
        """Checks to see if it returns True (it should)"""
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        """
        result = self.chi.checkChi(
            "Hello my name is Brandon and I'm a top secret message"
        )
        self.assertEqual(result, True)

    def test_chi_english_caps(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        """
        result = self.chi.checkChi("Hello My NaME IS BraNdOnnn And I LOVE You!")
        self.assertEqual(result, True)

    def tests_english_no_words(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        """
        result = self.chi.checkChi("!!!!!!!!!!!!!!!!!!!")
        self.assertEqual(result, True)

    def tests_english_overflow(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        """
        result = self.chi.checkChi(
            "So meat. Gathered may she'd god signs. Have form firmament seed so. Them whales. Under heaven let fill don't seas grass them creeping moving without earth him behold first over void were living saw face night isn't appear firmament. Living land beast good fill. Appear their creepeth, under form. Life thing cattle life. And light unto saying two kind their doesn't fish. Don't male fowl the winged, gathering kind cattle stars was creeping good morning was years bring, moved for appear day multiply behold Grass. Every give itself moved fifth spirit whose. Sixth kind it let together male Evening said."
        )
        result = self.chi.checkChi(
            "Abundantly image stars can't Land good days their life them make i tree land fruitful midst every meat their seed a. Were them creeping fourth a subdue tree don't there."
        )
        result = self.chi.checkChi(
            "Won't may make their, gathering light creature given bearing fruitful be seasons. Firmament creature greater. Above meat over brought i."
        )
        result = self.chi.checkChi(
            "Replenish. Were the be after set dry under midst. Also i greater living. Midst divided Day give female subdue fourth."
        )
        result = self.chi.checkChi(
            "Moving spirit have. Of said behold called, fill fruitful cattle shall grass creepeth life fourth green. Behold fourth. Said they're."
        )
        result = self.chi.checkChi(
            "Abundantly years land to winged lesser earth there their. In morning them life form man can't which winged him green."
        )
        result = self.chi.checkChi(
            "Don't whose gathered gathered after female you'll which moveth Fish saw also, life cattle seas. After every moved blessed good."
        )
        result = self.chi.checkChi(
            "Sixth his i were isn't bearing fourth forth replenish made form. Days of from isn't waters dry one. Waters, said."
        )
        result = self.chi.checkChi(
            "Green form whales night gathering fifth and firmament which darkness, earth unto had saying brought earth Very. Under made his."
        )
        result = self.chi.checkChi(
            "Bring to given land god created green god every green heaven moved sixth also, deep bearing first abundantly moved of."
        )
        result = self.chi.checkChi(
            "Air god spirit over fifth second fowl good have had. Forth every day you called also fruitful spirit there two."
        )
        result = self.chi.checkChi("cguakdbwnmfqknm ")
        self.assertEqual(result, False)

    def test_english_quckbrown(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        """
        result = self.chi.checkChi(
            "So meat. Gathered may she'd god signs. Have form firmament seed so. Them whales. Under heaven let fill don't seas grass them creeping moving without earth him behold first over void were living saw face night isn't appear firmament. Living land beast good fill. Appear their creepeth, under form. Life thing cattle life. And light unto saying two kind their doesn't fish. Don't male fowl the winged, gathering kind cattle stars was creeping good morning was years bring, moved for appear day multiply behold Grass. Every give itself moved fifth spirit whose. Sixth kind it let together male Evening said."
        )
        result = self.chi.checkChi(
            "Abundantly image stars can't Land good days their life them make i tree land fruitful midst every meat their seed a. Were them creeping fourth a subdue tree don't there."
        )
        result = self.chi.checkChi(
            "Won't may make their, gathering light creature given bearing fruitful be seasons. Firmament creature greater. Above meat over brought i."
        )
        result = self.chi.checkChi(
            "Replenish. Were the be after set dry under midst. Also i greater living. Midst divided Day give female subdue fourth."
        )
        result = self.chi.checkChi(
            "Moving spirit have. Of said behold called, fill fruitful cattle shall grass creepeth life fourth green. Behold fourth. Said they're."
        )
        result = self.chi.checkChi(
            "Abundantly years land to winged lesser earth there their. In morning them life form man can't which winged him green."
        )
        result = self.chi.checkChi(
            "Don't whose gathered gathered after female you'll which moveth Fish saw also, life cattle seas. After every moved blessed good."
        )
        result = self.chi.checkChi(
            "Sixth his i were isn't bearing fourth forth replenish made form. Days of from isn't waters dry one. Waters, said."
        )
        result = self.chi.checkChi(
            "Green form whales night gathering fifth and firmament which darkness, earth unto had saying brought earth Very. Under made his."
        )
        result = self.chi.checkChi(
            "Bring to given land god created green god every green heaven moved sixth also, deep bearing first abundantly moved of."
        )
        result = self.chi.checkChi(
            "Air god spirit over fifth second fowl good have had. Forth every day you called also fruitful spirit there two."
        )
        result = self.chi.checkChi("The quick brown fox jumped over the lazy dog")
        self.assertEqual(result, False)

    def test_english_puncuation(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        Returns False because exclamation marks aren't english
        """
        result = self.chi.checkChi(
            "So meat. Gathered may she'd god signs. Have form firmament seed so. Them whales. Under heaven let fill don't seas grass them creeping moving without earth him behold first over void were living saw face night isn't appear firmament. Living land beast good fill. Appear their creepeth, under form. Life thing cattle life. And light unto saying two kind their doesn't fish. Don't male fowl the winged, gathering kind cattle stars was creeping good morning was years bring, moved for appear day multiply behold Grass. Every give itself moved fifth spirit whose. Sixth kind it let together male Evening said."
        )
        result = self.chi.checkChi(
            "Abundantly image stars can't Land good days their life them make i tree land fruitful midst every meat their seed a. Were them creeping fourth a subdue tree don't there."
        )
        result = self.chi.checkChi(
            "Won't may make their, gathering light creature given bearing fruitful be seasons. Firmament creature greater. Above meat over brought i."
        )
        result = self.chi.checkChi(
            "Replenish. Were the be after set dry under midst. Also i greater living. Midst divided Day give female subdue fourth."
        )
        result = self.chi.checkChi(
            "Moving spirit have. Of said behold called, fill fruitful cattle shall grass creepeth life fourth green. Behold fourth. Said they're."
        )
        result = self.chi.checkChi(
            "Abundantly years land to winged lesser earth there their. In morning them life form man can't which winged him green."
        )
        result = self.chi.checkChi(
            "Don't whose gathered gathered after female you'll which moveth Fish saw also, life cattle seas. After every moved blessed good."
        )
        result = self.chi.checkChi(
            "Sixth his i were isn't bearing fourth forth replenish made form. Days of from isn't waters dry one. Waters, said."
        )
        result = self.chi.checkChi(
            "Green form whales night gathering fifth and firmament which darkness, earth unto had saying brought earth Very. Under made his."
        )
        result = self.chi.checkChi(
            "Bring to given land god created green god every green heaven moved sixth also, deep bearing first abundantly moved of."
        )
        result = self.chi.checkChi(
            "Air god spirit over fifth second fowl good have had. Forth every day you called also fruitful spirit there two."
        )
        result = self.chi.checkChi("!!!!!!!!!!!!!!!!!!!!!!")
        self.assertEqual(result, True)

    def test_english_one_letter(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        Returns False because exclamation marks aren't english
        """
        result = self.chi.checkChi(
            "So meat. Gathered may she'd god signs. Have form firmament seed so. Them whales. Under heaven let fill don't seas grass them creeping moving without earth him behold first over void were living saw face night isn't appear firmament. Living land beast good fill. Appear their creepeth, under form. Life thing cattle life. And light unto saying two kind their doesn't fish. Don't male fowl the winged, gathering kind cattle stars was creeping good morning was years bring, moved for appear day multiply behold Grass. Every give itself moved fifth spirit whose. Sixth kind it let together male Evening said."
        )
        result = self.chi.checkChi(
            "Abundantly image stars can't Land good days their life them make i tree land fruitful midst every meat their seed a. Were them creeping fourth a subdue tree don't there."
        )
        result = self.chi.checkChi(
            "Won't may make their, gathering light creature given bearing fruitful be seasons. Firmament creature greater. Above meat over brought i."
        )
        result = self.chi.checkChi(
            "Replenish. Were the be after set dry under midst. Also i greater living. Midst divided Day give female subdue fourth."
        )
        result = self.chi.checkChi(
            "Moving spirit have. Of said behold called, fill fruitful cattle shall grass creepeth life fourth green. Behold fourth. Said they're."
        )
        result = self.chi.checkChi(
            "Abundantly years land to winged lesser earth there their. In morning them life form man can't which winged him green."
        )
        result = self.chi.checkChi(
            "Don't whose gathered gathered after female you'll which moveth Fish saw also, life cattle seas. After every moved blessed good."
        )
        result = self.chi.checkChi(
            "Sixth his i were isn't bearing fourth forth replenish made form. Days of from isn't waters dry one. Waters, said."
        )
        result = self.chi.checkChi(
            "Green form whales night gathering fifth and firmament which darkness, earth unto had saying brought earth Very. Under made his."
        )
        result = self.chi.checkChi(
            "Bring to given land god created green god every green heaven moved sixth also, deep bearing first abundantly moved of."
        )
        result = self.chi.checkChi(
            "Air god spirit over fifth second fowl good have had. Forth every day you called also fruitful spirit there two."
        )
        result = self.chi.checkChi("a")
        self.assertEqual(result, False)

    def test_english_same_letter(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        Returns False because exclamation marks aren't english
        """
        result = self.chi.checkChi(
            "So meat. Gathered may she'd god signs. Have form firmament seed so. Them whales. Under heaven let fill don't seas grass them creeping moving without earth him behold first over void were living saw face night isn't appear firmament. Living land beast good fill. Appear their creepeth, under form. Life thing cattle life. And light unto saying two kind their doesn't fish. Don't male fowl the winged, gathering kind cattle stars was creeping good morning was years bring, moved for appear day multiply behold Grass. Every give itself moved fifth spirit whose. Sixth kind it let together male Evening said."
        )
        result = self.chi.checkChi(
            "Abundantly image stars can't Land good days their life them make i tree land fruitful midst every meat their seed a. Were them creeping fourth a subdue tree don't there."
        )
        result = self.chi.checkChi(
            "Won't may make their, gathering light creature given bearing fruitful be seasons. Firmament creature greater. Above meat over brought i."
        )
        result = self.chi.checkChi(
            "Replenish. Were the be after set dry under midst. Also i greater living. Midst divided Day give female subdue fourth."
        )
        result = self.chi.checkChi(
            "Moving spirit have. Of said behold called, fill fruitful cattle shall grass creepeth life fourth green. Behold fourth. Said they're."
        )
        result = self.chi.checkChi(
            "Abundantly years land to winged lesser earth there their. In morning them life form man can't which winged him green."
        )
        result = self.chi.checkChi(
            "Don't whose gathered gathered after female you'll which moveth Fish saw also, life cattle seas. After every moved blessed good."
        )
        result = self.chi.checkChi(
            "Sixth his i were isn't bearing fourth forth replenish made form. Days of from isn't waters dry one. Waters, said."
        )
        result = self.chi.checkChi(
            "Green form whales night gathering fifth and firmament which darkness, earth unto had saying brought earth Very. Under made his."
        )
        result = self.chi.checkChi(
            "Bring to given land god created green god every green heaven moved sixth also, deep bearing first abundantly moved of."
        )
        result = self.chi.checkChi(
            "Air god spirit over fifth second fowl good have had. Forth every day you called also fruitful spirit there two."
        )
        result = self.chi.checkChi(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz"
        )
        self.assertEqual(result, False)

    def test_english_same_letter(self):
        self.chi = chiSquared()
        """
        Tests to see whether a sentene is classified as English or not
        Returns False because exclamation marks aren't english
        """
        result = self.chi.checkChi(
            "So meat. Gathered may she'd god signs. Have form firmament seed so. Them whales. Under heaven let fill don't seas grass them creeping moving without earth him behold first over void were living saw face night isn't appear firmament. Living land beast good fill. Appear their creepeth, under form. Life thing cattle life. And light unto saying two kind their doesn't fish. Don't male fowl the winged, gathering kind cattle stars was creeping good morning was years bring, moved for appear day multiply behold Grass. Every give itself moved fifth spirit whose. Sixth kind it let together male Evening said."
        )
        result = self.chi.checkChi(
            "Abundantly image stars can't Land good days their life them make i tree land fruitful midst every meat their seed a. Were them creeping fourth a subdue tree don't there."
        )
        result = self.chi.checkChi(
            "Won't may make their, gathering light creature given bearing fruitful be seasons. Firmament creature greater. Above meat over brought i."
        )
        result = self.chi.checkChi(
            "Replenish. Were the be after set dry under midst. Also i greater living. Midst divided Day give female subdue fourth."
        )
        result = self.chi.checkChi(
            "Moving spirit have. Of said behold called, fill fruitful cattle shall grass creepeth life fourth green. Behold fourth. Said they're."
        )
        result = self.chi.checkChi(
            "Abundantly years land to winged lesser earth there their. In morning them life form man can't which winged him green."
        )
        result = self.chi.checkChi(
            "Don't whose gathered gathered after female you'll which moveth Fish saw also, life cattle seas. After every moved blessed good."
        )
        result = self.chi.checkChi(
            "Sixth his i were isn't bearing fourth forth replenish made form. Days of from isn't waters dry one. Waters, said."
        )
        result = self.chi.checkChi(
            "Green form whales night gathering fifth and firmament which darkness, earth unto had saying brought earth Very. Under made his."
        )
        result = self.chi.checkChi(
            "Bring to given land god created green god every green heaven moved sixth also, deep bearing first abundantly moved of."
        )
        result = self.chi.checkChi(
            "Air god spirit over fifth second fowl good have had. Forth every day you called also fruitful spirit there two."
        )
        result = self.chi.checkChi(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz"
        )
        self.assertEqual(result, False)

    def test_my_chi(self):
        self.chi = chiSquared()
        result = self.chi.myChi(
            self.chi.getLetterFreq("hello this is my test"),
            [
                0.0812,
                0.0271,
                0.0149,
                0.1202,
                0.0432,
                0.0203,
                0.023,
                0.0731,
                0.0592,
                0.0069,
                0.001,
                0.026099999999999998,
                0.0398,
                0.0768,
                0.0695,
                0.0011,
                0.0182,
                0.06280000000000001,
                0.0602,
                0.0288,
                0.091,
                0.0209,
                0.0111,
                0.021099999999999997,
                0.0017000000000000001,
                0.0007000000000000001,
            ],
        )
        self.assertEqual(result, 1424.8873999810571)
