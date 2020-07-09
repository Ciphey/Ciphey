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

Copy of the GitHub Issue Comment
-------------------------------

When Brandon checker was made, this information was put into a GitHub issue comment. This will be helpful for you to see how Brandon checker was made.

If I’m reading this correctly: > I would suggest a simple lower bound
test: we pass if we get more than 25%,and fail if we get lower than 5%
(or smth idk) for n consecutive windows. You’re suggesting that we run
all tests and see if we get 25% Imo that would be much slower. What do
you mean by ``n windows``?

Okay, Chi squared is out then!

   Perhaps we can return an object from the cracker which states what
   tests have been performed, to save time on redundant analysis. With
   such information, brandon could make an intelligent decision to just
   use a wordlist if enough analysis was performed, and the more
   detailed analysis if it wasn’t. This is entirely possible. I will add
   support to ``brandon`` checker to skip phase 1 if it receives an
   dictionary with key ``"phase1": True`` for ``True == skip phase 1``.

If you have more tests, let me know and I can factor them in.

In your first reply:
https://github.com/Ciphey/Ciphey/issues/90#issuecomment-645046918 Point
3: > Be aware that the stuff passed to the checker will most likely be
complete gibberish (with a similar freq dist) OR the correct result. A
user will not care about an extra second spent on the final correct
result, but really will care that every false candidate takes an extra
second. The current suggestion seems to be pessimal for the gibberish
inputs: maybe add some sanity checks (have I failed to match any word,
have I failed to lemmatise any word, etc.)

I decided to test how well ``lem`` worked as phase 1. To do this, I
created this program:

.. code:: python

   """
   TL;DR

   Tested over 20,000 times

   Maximum sentence size is 15 sentences
   1/2 chance of getting 'gibberish' (encrypted text)
   1/2 chance of getting English text

   Each test is timed using Time module.
   The accuracy is calculated as to how many true positives we get over the entire run

   """


   import spacy
   import random
   import time
   from statistics import mean
   import ciphey
   import enciphey
   from alive_progress import alive_bar

   nlp = spacy.load("en_core_web_sm")

   f = open("hansard.txt", encoding="ISO-8859-1").read()
   f = f.split(".")

   enciph = enciphey.encipher()


   def lem(text):
       sentences = nlp(text)
       return set([word.lemma_ for word in sentences])


   def get_random_sentence():
       if random.randint(0, 1) == 0:
           x = None
           while x is None:
               x = (True, " ".join(random.sample(f, k=random.randint(1, 50))))
           return x
       else:
           x = None
           while x is None:
               x = enciph.getRandomEncryptedSentence()
               x = x["Encrypted Texts"]["EncryptedText"]
           return (False, x)


   # Now to time it and take measurements


   def perform():
       # calculate accuracy
       total = 0
       true_returns = 0

       # calculate aveager time
       time_list = []

       # average sentance size
       sent_size_list = []
       items = range(20000)
       with alive_bar(len(items)) as bar:
           for i in range(0, 20000):
               sent = get_random_sentence()
               text = sent[1]
               truthy = sent[0]
               sent_size_list.append(len(text))

               # should be length of chars
               old = len(text)

               # timing the function
               tic = time.perf_counter()
               new = lem(text)
               tok = time.perf_counter()

               # checking for accuracy
               new = len(new)
               # the and here means we only count True Positives
               if new < old and truthy:
                   true_returns += 1
               total += 1

               # appending the time
               t = tok - tic
               time_list.append(t)
               bar()

       print(
           f"The accuracy is {str((true_returns / total) * 100)} \n and the time it took is {str(round(mean(time_list), 2))}. \n The average string size was {str(mean(sent_size_list))}"
       )


   perform()

The results were fascinating, to say the least. With a 50/50 chance of
the text being gibberish (ciphertext from enCiphey) or sentences from
Hansard.txt, we had these results for using lemmization as phase 1:

::

   The accuracy is 49.63%
    and the time it took is 0.02 seconds on average.
    The average string size was 1133.63255.

**We get a 50% accuracy with a speed of 0.02 seconds on average, across
20k tests with the average size of a string being 1133 chars.**

The accuracy is quite bad considering that a coin flip is 50/50. On
average, the user would expect Phase 2 to be entered 50% of the time,
which is annoying as phase 2 is quite slow. But by itself it’s quite
fast.

I am going to build the “2nd phase” of phase 1 using the While Loop we
saw earlier. If we can combine just one more metric, we would see much
higher accuracy and again - likely incredibly low latency.

I will create a table of my results:

Table of max sentence length == 50
-----------------------------------------

+----------+----------+----------+----------+--------+----------+
| Name     | Speed    | Accuracy | String   | Epochs | Max      |
|          |          |          | Size     |        | Sentence |
|          |          |          | Average  |        | Size     |
|          |          |          | Chars    |        |          |
+==========+==========+==========+==========+========+==========+
| Lem      | 0.02     | 50%      | 1580     | 20,000 | 50       |
| mization | seconds  |          |          |        |          |
| (lem)    |          |          |          |        |          |
+----------+----------+----------+----------+--------+----------+
| Stop     | 3.05     | 96%      | 1596     | 20,000 | 50       |
| word     | 46505288 |          |          |        |          |
| removal  | 4756e-05 |          |          |        |          |
|          | seconds  |          |          |        |          |
+----------+----------+----------+----------+--------+----------+
| Check1   | 0.0005   | 96%      | 1597     | 20,000 | 50       |
| 000Words | seconds  |          |          |        |          |
+----------+----------+----------+----------+--------+----------+
| Word     | 0.0009   | 95%      | 1597     | 20,000 | 50       |
| endings  | seconds  |          |          |        |          |
+----------+----------+----------+----------+--------+----------+

Table of max sentence length == 5

-----------------------------------------

+----------+----------+----------+----------+--------+----------+
| Name     | Speed    | Accuracy | String   | Epochs | Max      |
|          |          |          | Size     |        | Sentence |
|          |          |          | Average  |        | Size     |
|          |          |          | Chars    |        |          |
+==========+==========+==========+==========+========+==========+
| Lem      |          |          |          |        |          |
| mization |          |          |          |        |          |
| (lem)    |          |          |          |        |          |
+----------+----------+----------+----------+--------+----------+
| Stop     | 1.1574   | 93%      | 569      | 20,000 | 5        |
| word     | 92445399 |          |          |        |          |
| removal  | 8391e-05 |          |          |        |          |
|          | seconds  |          |          |        |          |
+----------+----------+----------+----------+--------+----------+
| Check1   | 0.0006   | 95%      | 586      | 20,000 | 5        |
| 000Words | seconds  |          |          |        |          |
+----------+----------+----------+----------+--------+----------+
| Word     | 0.0003   | 92%      | 482      | 20,000 | 5        |
| endings  | seconds  |          |          |        |          |
+----------+----------+----------+----------+--------+----------+

Table of max sentence length == 1
-----------------------------------------

+--------------+-----------------+---+---+--------------+---+---------+
| Name         | Speed           | A | T | String Size  | E | Max     |
|              |                 | c | h | Average      | p | S       |
|              |                 | c | r | Chars        | o | entence |
|              |                 | u | e |              | c | Size    |
|              |                 | r | s |              | h |         |
|              |                 | a | h |              | s |         |
|              |                 | c | o |              |   |         |
|              |                 | y | l |              |   |         |
|              |                 |   | d |              |   |         |
+==============+=================+===+===+==============+===+=========+
| Lemmization  |                 |   |   |              |   |         |
| (lem)        |                 |   |   |              |   |         |
+--------------+-----------------+---+---+--------------+---+---------+
| Stop word    | 1.253206        | 5 | 4 | 20,000       | 1 |         |
| removal      | 1150591289e-05. | 0 | 8 |              |   |         |
|              | seconds         | % | 1 |              |   |         |
+--------------+-----------------+---+---+--------------+---+---------+
| Ch           | 0.0006 seconds  | 9 | 5 | 20,000       | 5 |         |
| eck1000Words |                 | 5 | 8 |              |   |         |
|              |                 | % | 6 |              |   |         |
+--------------+-----------------+---+---+--------------+---+---------+
| Word endings | 0.0002 seconds  | 8 | 1 | 482          | 2 | 1       |
|              |                 | 6 | 5 |              | 0 |         |
|              |                 | % |   |              | , |         |
|              |                 |   |   |              | 0 |         |
|              |                 |   |   |              | 0 |         |
|              |                 |   |   |              | 0 |         |
+--------------+-----------------+---+---+--------------+---+---------+

Confusion Matrices & Notes
----------------------------

Lemization
----------

::

                   Positive    Negative
   Positive     10031      9967
   Negative     2            0

Stop Words
----------

This test was performed where the text was not ``.lower()``, so the
actual accuracy *may* be a little tiny bit higher since the stop words
list is all lowercase.

50 sentence limit

::

                           Positive    Negative
               Positive     9913            855
               Negative     56            9176

5 sentence limit:

::

                           Positive    Negative
               Positive     9513            967
               Negative     530            8990

Check 1000 words
----------------

50 sentence limit

::

                              Positive    Negative
               Positive     10008            552
               Negative     56            9384

5 sentence limit

::

                           Positive    Negative
               Positive     9563            597
               Negative     397            9443

Analysis
---------

**I believe that the best Brandon checker will look at the length of the
text, and adjust the % threshold and the exact phase 1 checker per
text.**

The below data is taken from calculations performed over many hours. it
shows the best threshold % for the best phase 1 checker with the highest
accuracy. These checkers were chosen as others showed a maximum accuracy
of 58%.

::

   {'check 1000 words': {1: {'Accuracy': 0.925, 'Threshold': 2},
                         2: {'Accuracy': 0.95, 'Threshold': 68},
                         3: {'Accuracy': 0.975, 'Threshold': 62},
                         4: {'Accuracy': 0.98, 'Threshold': 5},
                         5: {'Accuracy': 0.985, 'Threshold': 54}},
    'stop words': {1: {'Accuracy': 0.865, 'Threshold': 50},
                   2: {'Accuracy': 0.93, 'Threshold': 19},
                   3: {'Accuracy': 0.965, 'Threshold': 15},
                   4: {'Accuracy': 0.97, 'Threshold': 28},
                   5: {'Accuracy': 0.985, 'Threshold': 29}}

Where the numbers are:

::

   1 : The mean is 87.62
   2 : The mean is 110.47925
   3 : The mean is 132.20016666666666
   4 : The mean is 154.817125
   5 : The mean is 178.7297

Looking at this test, it is clear that stopwords is better than check
1000 words for speed, but the accuracy is a little bit slower. Stop
words is incredibly faster than check 1k words, but on a smaller input
the stopwords checker breaks.

Therefore, we should use stopword checker on larger texts, and check 1k
words on smaller texts.

More specifically, stopwords checker for len == 110 has an optimal
threshold of 19, whereas check 1k words has an optimal threshold of 68.
This means that while stopwords can potentially end earlier and only
search the first 19% of the list, check 1k words would search 68% of the
list.

Stopwords has a lower accuracy by 2%, but it is much, much faster and
its optimal threshold is greatly reduced.

So ideally, we would have this algorithm: 1. Sentence length less than
110: 1. Use check 1k words with threshold of 2% 2. Sentence length >
110: 1. use Stopwords with threshold of 15 3. Sentence length > 150: 1.
Stopwords threshold increases to 28

This is the ideal optimal phase 1 algorithm for ``brandon`` checker.

Phase 2
-------

Phase 2 is the dictionary checker.

Firstly, we check to find the best thresholds for the dictionary
checker.

::

   'checker': {1: {'Accuracy': 0.97, 'Threshold': 99},
                2: {'Accuracy': 0.98, 'Threshold': 98},
                3: {'Accuracy': 0.965, 'Threshold': 68},
                4: {'Accuracy': 0.99, 'Threshold': 93},
                5: {'Accuracy': 0.97, 'Threshold': 92}},

The accuracies are good, but the thresholds are simply too high. We’re
overfitting!

To fix this, I thought that because the dictionary contained chars <= 2
such as “a” or “an” it was setting off the completion too much,
resulting in a much higher threshold.

To fix this, I only let the checker consider words that are more then 2
chars.

This is the result:

::

    'checker': {1: {'Accuracy': 0.965, 'Threshold': 60},
                2: {'Accuracy': 0.98, 'Threshold': 77},
                3: {'Accuracy': 0.985, 'Threshold': 67},
                4: {'Accuracy': 0.985, 'Threshold': 99},
                5: {'Accuracy': 0.98, 'Threshold': 47}},

The accuracy stayed around the same, but the threshold went down.
Although the threshold was still kind of high. 99% threshold for 4? I
restricted the threshold to 75% and:

::

   'checker': {1: {'Accuracy': 0.945, 'Threshold': 66},
                2: {'accuracy': 0.975, 'threshold': 69},
                3: {'accuracy': 0.98, 'threshold': 71},
                4: {'accuracy': 0.99, 'threshold': 65},
                5: {'accuracy': 0.98, 'threshold': 38}},

We can see that the accuracy stayed roughly the same, but the threshold
went down a lot. The mean appears to be 66% (from just looking at it).

However, the accuracy for smaller sentence sizes tanked.

The highest accuracy we had was with the original one. Words <= 2 chars
and no limit on threshold.

If possible, we want to combine the high accuracy on smaller texts while
maintaining the generalisation found in the latter checker results.

The reason we want a smaller threshold is that due to the chunking
procedure, it will be much faster on larger texts. The lower the
sentence length the higher the threshold is allowed to be.

For phase 2, we are not concerned with speed. We are however concerned
with accuracy.

I believe that threshold > 90% is overfitting. I cannot reasonably see
this successfully working within Ciphey itself.

My next test will be max threshold of 100% with no chars less than or
equal to 1.

::

    'checker': {1: {'Accuracy': 0.97, 'Threshold': 93},
                2: {'Accuracy': 0.975, 'Threshold': 82},
                3: {'Accuracy': 0.97, 'Threshold': 96},
                4: {'Accuracy': 0.965, 'Threshold': 31},
                5: {'Accuracy': 0.965, 'Threshold': 74}},

the accuracy is 97% with a threshold of 93. This is much higher than the
latter test. I think for lower texts, since we don’t care about speed,
we should use a higher threshold. This test was ran 20,000 times. I will
run the tests once much to see if the threshold significantly changes.

The test results were:

::

    'checker': {1: {'Accuracy': 0.96, 'Threshold': 92},
                2: {'Accuracy': 0.97, 'Threshold': 95},
                3: {'Accuracy': 0.965, 'Threshold': 81},
                4: {'Accuracy': 0.96, 'Threshold': 38},
                5: {'Accuracy': 0.975, 'Threshold': 52}},

One last test. No threshold limit with no char limit.

::

    'checker': {1: {'Accuracy': 0.98, 'Threshold': 92},
                2: {'Accuracy': 0.99, 'Threshold': 91},
                3: {'Accuracy': 0.97, 'Threshold': 83},
                4: {'Accuracy': 0.97, 'Threshold': 71},
                5: {'Accuracy': 0.975, 'Threshold': 74}},

In total, we want these ones:

::

   {1: {'Accuracy': 0.98, 'Threshold': 92},
   2: {'accuracy': 0.975, 'threshold': 69},
   3: {'accuracy': 0.98, 'threshold': 71},
   4: {'accuracy': 0.99, 'threshold': 65},
   5: {'accuracy': 0.98, 'threshold': 38}},
   ^^ with 75% threshold limit

Lower thresholds, accuracies look good too.
