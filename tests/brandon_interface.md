
If I'm reading this correctly:
> I would suggest a simple lower bound test: we pass if we get more than 25%,and fail if we get lower than 5% (or smth idk) for n consecutive windows.
You're suggesting that we run all tests and see if we get 25% Imo that would be much slower. What do you mean by `n windows`?

Okay, Chi squared is out then! 

> Perhaps we can return an object from the cracker which states what tests have been performed, to save time on redundant analysis. With such information, brandon could make an intelligent decision to just use a wordlist if enough analysis was performed, and the more detailed analysis if it wasn't.
This is entirely possible. I will add support to `brandon` checker to skip phase 1 if it receives an dictionary with key `"phase1": True` for `True == skip phase 1`. 

If you have more tests, let me know and I can factor them in.

In your first reply:
https://github.com/Ciphey/Ciphey/issues/90#issuecomment-645046918
Point 3:
> Be aware that the stuff passed to the checker will most likely be complete gibberish (with a similar freq dist) OR the correct result. A user will not care about an extra second spent on the final correct result, but really will care that every false candidate takes an extra second. The current suggestion seems to be pessimal for the gibberish inputs: maybe add some sanity checks (have I failed to match any word, have I failed to lemmatise any word, etc.)

I decided to test how well `lem` worked as phase 1. To do this, I created this program:
```python
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
```

The results were fascinating, to say the least.
With a 50/50 chance of the text being gibberish (ciphertext from enCiphey) or sentences from Hansard.txt, we had these results for using lemmization as phase 1:

```
The accuracy is 49.63%
 and the time it took is 0.02 seconds on average.
 The average string size was 1133.63255.
```

**We get a 50% accuracy with a speed of 0.02 seconds on average, across 20k tests with the average size of a string being 1133 chars. **

The accuracy is quite bad considering that a coin flip is 50/50.
On average, the user would expect Phase 2 to be entered 50% of the time, which is annoying as phase 2 is quite slow. But by itself it's quite fast.

I am going to build the "2nd phase" of phase 1 using the While Loop we saw earlier. If we can combine just one more metric, we would see much higher accuracy and again - likely incredibly low latency.

I will create a table of my results:

## Table of max sentence length == 50

| Name                       | Speed                        | Accuracy | String Size Average Chars | Epochs | Max Sentence Size |
| -------------------------- | ---------------------------- | -------- | ------------------------- | ------ | ----------------- |
| Lemmization (lem)          | 0.02 seconds                 | 50%      | 1580                      | 20,000 | 50                |
| Stop word removal          | 3.05465052884756e-05 seconds | 96%      | 1596                      | 20,000 | 50                |
| Check1000Words             | 0.0005 seconds               | 96%      | 1597                      | 20,000 | 50                |
| Regex for numbers in words |
| Word endings               | 0.0009 seconds               | 95%      | 1597                      | 20,000 | 50                |
| Expand contractions        |
| Chi squared                |

## Table of max sentence length == 5

| Name                       | Speed                          | Accuracy | String Size Average Chars | Epochs | Max Sentence Size |
| -------------------------- | ------------------------------ | -------- | ------------------------- | ------ | ----------------- |
| Lemmization (lem)          |
| Stop word removal          | 1.1574924453998391e-05 seconds | 93%      | 569                       | 20,000 | 5                 |
| Check1000Words             | 0.0006 seconds                 | 95%      | 586                       | 20,000 | 5                 |
| Regex for numbers in words |
| Word endings               | 0.0003 seconds                 | 92%      | 482                       | 20,000 | 5                 |
| Expand contractions        |
| Chi Squared                |

## Table of max sentence length == 1

| Name                       | Speed                           | Accuracy | Threshold | String Size Average Chars | Epochs | Max Sentence Size |
| -------------------------- | ------------------------------- | -------- | ------ |------------------------- | ------ | ----------------- |
| Lemmization (lem)          |
| Stop word removal          | 1.2532061150591289e-05. seconds | 50%      | 481                       | 20,000 | 1                 |
| Check1000Words             | 0.0006 seconds                  | 95%      | 586                       | 20,000 | 5                 |
| Regex for numbers in words |
| Word endings               | 0.0002 seconds                  | 86%      | 15| 482                       | 20,000 | 1                 |
| Expand contractions        |
| Chi Squared                |

## Confusion Matrices & Notes
### Lemization
```
                Positive    Negative
Positive     10031      9967
Negative     2            0
```

### Stop Words
This test was performed where the text was not `.lower()`, so the actual accuracy _may_ be a little tiny bit higher since the stop words list is all lowercase.

50 sentence limit

```
                        Positive    Negative
            Positive     9913            855
            Negative     56            9176
```

5 sentence limit:

```
                        Positive    Negative
            Positive     9513            967
            Negative     530            8990
```

### Check 1000 words
50 sentence limit
```
                           Positive    Negative
            Positive     10008            552
            Negative     56            9384
```

5 sentence limit
```
                        Positive    Negative
            Positive     9563            597
            Negative     397            9443
```

# Analysis
**I believe that the best Brandon checker will look at the length of the text, and adjust the % threshold and the exact phase 1 checker per text.**

```{'check 1000 words': {1: {'Accuracy': 0.925, 'Threshold': 2},
                      2: {'Accuracy': 0.95, 'Threshold': 68},
                      3: {'Accuracy': 0.975, 'Threshold': 62},
                      4: {'Accuracy': 0.98, 'Threshold': 5},
                      5: {'Accuracy': 0.985, 'Threshold': 54}},
 'stop words': {1: {'Accuracy': 0.865, 'Threshold': 50},
                2: {'Accuracy': 0.93, 'Threshold': 19},
                3: {'Accuracy': 0.965, 'Threshold': 15},
                4: {'Accuracy': 0.97, 'Threshold': 28},
                5: {'Accuracy': 0.985, 'Threshold': 29}},```

Looking at this test, it is clear that stopwords is better than check 1000 words for speed, but the accuracy is a little bit slower. Stop words is incredibly faster than check 1k words, but on a smaller input the stopwords checker breaks.

Therefore, we should use stopword checker on larger texts, and check 1k words on smaller texts.


# TODO
* [ ] Use the testing system in place to find the optimal percentage thresholds for each phase of language checker. I can use the confusion matrices to help work this out.
* [ ] Only perform phase 1 on {THRESHOLD}% of list etc
* [ ] Look at using different threshold numbers for different lengths of text, and wether or not that dramatically increases accuracy.
* [ ] Calculate speed / accuracy of old language Checker
* [ ] Calculate speed / accuracy of Harlan's neural network
* [ ] Clean this issue into documentation after I'm done
