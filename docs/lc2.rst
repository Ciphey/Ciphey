Brandon Interface
==================
The Brandon interface is the default language checking interface for Ciphey. So named because it is an algorithm created by Brandon, and we couldn't come up with any clever names for it at the time.


Contributing your own language
------------------------------
1. Get a dictionary of your language
2. Get stop words of your language
3. Get the top 1000 words of your language
4. Get the alphabet of your language
5. Get the frequency distribution of your language. We suggest taking a very popular large text (for English we used Charles Dickens' complete works) and calculating the frequency distribution yourself.
6. Add these to CipheyDists with the appropriate names and in appropriate folders.
7. Calculate the thresholds / sentence lengths using the program detailed in the secion in this document.
8. Pull requestr and you're done!

How were the thresholds / sentence lengths chosen?
--------------------------------------------------

Brandon (the person) created a program to automatically test which checkers, sentence lengths, and thresholds were best for the newest version of Brandon checker.

The most important thing about the tests was "which is the best metric we can use as a phase 1 checker?" The tests consisted of:
* Lemminization
* Stop words
* Check 1000 words
* Word Endings
* Word endings with 3 chars

Each one was tested 20,000 times for accuracy & speed. Only stop words & check 1000 words survived this testing, both being high accuracy and incredibly fast.

Stopwords is a lot faster than Check 1000 words, but on much smaller texts it has terrible accuracy. Naturally longer plaintexts have higher amounts of stop words.

Naturally, Brandon questioned whether it was worth it to check the length of the text, and change the checker to increase the accuracy whilest maintaining high speed.

Preliminary tests showed that this was true. Stopwords had an accuracy of 85% on shorter texts, whereas check1000 words had an accuracy of 97%. On much higher texts, stopwords had an equal accuracy but is much faster.

A sentence is defined as "a single sentence from the corpus of Hansard.txt". The sentence lengths tested were 1, 2, 3, 4, 5 and 20. 

After Brandon had found the best checkers for the certain sentence lengths, he calculated the mean average len() of each sentence. This is as follows:

1 : The mean is 87.62
2 : The mean is 110.47925
3 : The mean is 132.20016666666666
4 : The mean is 154.817125
5 : The mean is 178.7297
20: The mean is 714.9188

Next, the question of percentage thresholds.

Brandon realised that hard coding in thresholds (such as 55%) was a stupid idea. Surely there exists ideal thresholds that optimise the accuracy of the checker. And surely these thresholds change over the sentence length (stopwords would need a higher threshold for smaller texts but as the text size inceases it can use a lower threshold).

This means that the threshold & checker changes depending on the text size.

What languags are supported?
----------------------------
* English
* German

