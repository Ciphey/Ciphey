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

nlp = spacy.load("en_core_web_sm")

f = open("hansard.txt", encoding="ISO-8859-1").read()
f = f.split(".")

enciph = enciphey.encipher()


def lem(text):
    sentences = nlp(text)
    return set([word.lemma_ for word in sentences])


def get_random_sentence():
    if random.randint(0, 1) == 0:
        return (True, " ".join(f[0 : random.randint(0, 15)]))
    else:
        return (False, enciph.getRandomEncryptedSentence()['Encrypted Texts'])


# Now to time it and take measurements


def perform():
    # calculate accuracy
    total = 0
    true_returns = 0

    # calculate aveager time
    time_list = []

    # average sentance size
    sent_size_list = []

    for i in range(0, 20):
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

    print(
        f"The accuracy is {str((true_returns / total) * 100)} \n and the time it took is {str(round(mean(time_list), 2))}. \n The average sentence siize was {str(mean(sent_size_list))}"
    )


perform()
