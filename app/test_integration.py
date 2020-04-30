from languageCheckerMod import LanguageChecker

import unittest


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

    def test_chi_maxima(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        result = lc.checkLanguage(
            "Hypertext Transfer Protocol (HTTP) parameters, including HTTP headers, allow the client and the server to pass additional information with the request or the response."
        )
        result = lc.checkLanguage(
            "Hypertext Transfer Protocol (HTTP) parameters, including HTTP headers, allow the client and the server to pass additional information with the request or the response."
        )
        result = lc.checkLanguage(
            "HTTP parameters and headers can often reveal information about how a web application is transmitting data and storing cookies. Clients send parameters including the user agent of the browser."
        )
        result = lc.checkLanguage(
            "You probably build websites and think your shit is special. You think your 13 megabyte parallax-ative home page is going to get you some fucking Awwward banner you can glue to the top corner of your site. You think your 40-pound jQuery file and 83 polyfills give IE7 a boner because it finally has box-shadow. Wrong, motherfucker. Let me describe your perfect-ass website:"
        )
        result = lc.checkLanguage(
            "You. Are. Over-designing. Look at this shit. It's a motherfucking website. Why the fuck do you need to animate a fucking trendy-ass banner flag when I hover over that useless piece of shit? You spent hours on it and added 80 kilobytes to your fucking site, and some motherfucker jabbing at it on their iPad with fat sausage fingers will never see that shit. Not to mention blind people will never see that shit, but they don't see any of your shitty shit."
        )
        result = lc.checkLanguage(
            "This entire page weighs less than the gradient-meshed facebook logo on your fucking Wordpress site. Did you seriously load 100kb of jQuery UI just so you could animate the fucking background color of a div? You loaded all 7 fontfaces of a shitty webfont just so you could say at 100px height at the beginning of your site? You piece of shit."
        )
        result = lc.checkLanguage(
            "You dumbass. You thought you needed media queries to be responsive, but no. Responsive means that it responds to whatever motherfucking screensize it's viewed on. This site doesn't care if you're on an iMac or a motherfucking Tamagotchi."
        )
        result = lc.checkLanguage(
            "Like the man who's never grown out his beard has no idea what his true natural state is, you have no fucking idea what a website is. All you have ever seen are shitty skeuomorphic bastardizations of what should be text communicating a fucking message. This is a real, naked website. Look at it. It's fucking beautiful."
        )
        result = lc.checkLanguage(
            "Have you guys noticed that sometimes the foremost academic websites with lots of scientific information tend to look like this?"
        )
        result = lc.checkLanguage(
            "That's because academics do Save as Website from Microsoft Word and call it a day."
        )
        result = lc.checkLanguage(
            "In case anyone was interested, fuck is used 33 times in the page."
        )
        result = lc.checkLanguage(
            "Hi! I just checked this URL and it appeared to be unavailable or slow loading (Connection timed out after 8113 milliseconds). Here are some mirrors to try:"
        )
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        self.assertEqual(result, False)

    def test_chi_maxima_false(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        result = lc.checkLanguage(
            "Hypertext Transfer Protocol (HTTP) parameters, including HTTP headers, allow the client and the server to pass additional information with the request or the response."
        )
        result = lc.checkLanguage(
            "Hypertext Transfer Protocol (HTTP) parameters, including HTTP headers, allow the client and the server to pass additional information with the request or the response."
        )
        result = lc.checkLanguage(
            "HTTP parameters and headers can often reveal information about how a web application is transmitting data and storing cookies. Clients send parameters including the user agent of the browser."
        )
        result = lc.checkLanguage(
            "You probably build websites and think your shit is special. You think your 13 megabyte parallax-ative home page is going to get you some fucking Awwward banner you can glue to the top corner of your site. You think your 40-pound jQuery file and 83 polyfills give IE7 a boner because it finally has box-shadow. Wrong, motherfucker. Let me describe your perfect-ass website:"
        )
        result = lc.checkLanguage(
            "You. Are. Over-designing. Look at this shit. It's a motherfucking website. Why the fuck do you need to animate a fucking trendy-ass banner flag when I hover over that useless piece of shit? You spent hours on it and added 80 kilobytes to your fucking site, and some motherfucker jabbing at it on their iPad with fat sausage fingers will never see that shit. Not to mention blind people will never see that shit, but they don't see any of your shitty shit."
        )
        result = lc.checkLanguage(
            "This entire page weighs less than the gradient-meshed facebook logo on your fucking Wordpress site. Did you seriously load 100kb of jQuery UI just so you could animate the fucking background color of a div? You loaded all 7 fontfaces of a shitty webfont just so you could say at 100px height at the beginning of your site? You piece of shit."
        )
        result = lc.checkLanguage(
            "You dumbass. You thought you needed media queries to be responsive, but no. Responsive means that it responds to whatever motherfucking screensize it's viewed on. This site doesn't care if you're on an iMac or a motherfucking Tamagotchi."
        )
        result = lc.checkLanguage(
            "Like the man who's never grown out his beard has no idea what his true natural state is, you have no fucking idea what a website is. All you have ever seen are shitty skeuomorphic bastardizations of what should be text communicating a fucking message. This is a real, naked website. Look at it. It's fucking beautiful."
        )
        result = lc.checkLanguage(
            "Have you guys noticed that sometimes the foremost academic websites with lots of scientific information tend to look like this?"
        )
        result = lc.checkLanguage(
            "That's because academics do Save as Website from Microsoft Word and call it a day."
        )
        result = lc.checkLanguage(
            "In case anyone was interested, fuck is used 33 times in the page."
        )
        result = lc.checkLanguage(
            "Hi! I just checked this URL and it appeared to be unavailable or slow loading (Connection timed out after 8113 milliseconds). Here are some mirrors to try:"
        )
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        self.assertEqual(result, False)

    def test_chi_maxima_true(self):
        """
        This returns false because s.d is not over 1 as all inputs are English
        """
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage("The quick brown fox jumped over the lazy dog")
        result = lc.checkLanguage(
            "Hypertext Transfer Protocol (HTTP) parameters, including HTTP headers, allow the client and the server to pass additional information with the request or the response."
        )
        result = lc.checkLanguage(
            "Hypertext Transfer Protocol (HTTP) parameters, including HTTP headers, allow the client and the server to pass additional information with the request or the response."
        )
        result = lc.checkLanguage(
            "HTTP parameters and headers can often reveal information about how a web application is transmitting data and storing cookies. Clients send parameters including the user agent of the browser."
        )
        result = lc.checkLanguage(
            "You probably build websites and think your shit is special. You think your 13 megabyte parallax-ative home page is going to get you some fucking Awwward banner you can glue to the top corner of your site. You think your 40-pound jQuery file and 83 polyfills give IE7 a boner because it finally has box-shadow. Wrong, motherfucker. Let me describe your perfect-ass website:"
        )
        result = lc.checkLanguage(
            "You. Are. Over-designing. Look at this shit. It's a motherfucking website. Why the fuck do you need to animate a fucking trendy-ass banner flag when I hover over that useless piece of shit? You spent hours on it and added 80 kilobytes to your fucking site, and some motherfucker jabbing at it on their iPad with fat sausage fingers will never see that shit. Not to mention blind people will never see that shit, but they don't see any of your shitty shit."
        )
        result = lc.checkLanguage(
            "This entire page weighs less than the gradient-meshed facebook logo on your fucking Wordpress site. Did you seriously load 100kb of jQuery UI just so you could animate the fucking background color of a div? You loaded all 7 fontfaces of a shitty webfont just so you could say at 100px height at the beginning of your site? You piece of shit."
        )
        result = lc.checkLanguage(
            "You dumbass. You thought you needed media queries to be responsive, but no. Responsive means that it responds to whatever motherfucking screensize it's viewed on. This site doesn't care if you're on an iMac or a motherfucking Tamagotchi."
        )
        result = lc.checkLanguage(
            "Like the man who's never grown out his beard has no idea what his true natural state is, you have no fucking idea what a website is. All you have ever seen are shitty skeuomorphic bastardizations of what should be text communicating a fucking message. This is a real, naked website. Look at it. It's fucking beautiful."
        )
        result = lc.checkLanguage(
            "Have you guys noticed that sometimes the foremost academic websites with lots of scientific information tend to look like this?"
        )
        result = lc.checkLanguage(
            "That's because academics do Save as Website from Microsoft Word and call it a day."
        )
        result = lc.checkLanguage(
            "In case anyone was interested, fuck is used 33 times in the page."
        )
        result = lc.checkLanguage(
            "Hi! I just checked this URL and it appeared to be unavailable or slow loading (Connection timed out after 8113 milliseconds). Here are some mirrors to try:"
        )
        result = lc.checkLanguage(
            "There can only be one way to make this work for real and I really do enjoy the long thought out process of drinking milk"
        )
        self.assertEqual(result, False)

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

    def test_integration_unusual_6(self):
        lc = LanguageChecker.LanguageChecker()
        result = lc.checkLanguage('"')
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
