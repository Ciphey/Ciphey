import spacy
import random
import time
from statistics import mean

nlp = spacy.load("en_core_web_sm")

f = open("hansard.txt", encoding="ISO-8859-1").read()
f = f.split(".")


def lem(text):
    sentences = nlp(text)
    return set([word.lemma_ for word in sentences])


def get_random_sentence():
    return " ".join(f[0 : random.randint(0, 15)])


# Now to time it and take measurements


def perform():
    # calculate accuracy
    total = 0
    true_returns = 0

    # calculate aveager time
    time_list = []

    # average sentance size
    sent_size_list = []

    for i in range(0, 20000):
        sent = get_random_sentence()
        sent_size_list.append(len(sent))

        # should be length of chars
        old = len(sent)

        # timing the function
        tic = time.perf_counter()
        new = lem(sent)
        tok = time.perf_counter()

        # checking for accuracy
        new = len(new)
        if new < old:
            true_returns += 1
        total += 1

        # appending the time
        t = tok - tic
        time_list.append(t)

    print(
            f"The accuracy is {str((true_returns / total) * 100)} \n and the time it took is {str(round(mean(time_list), 2))}. \n The average sentence siize was {str(mean(sent_size_list))}"
    )


perform()
