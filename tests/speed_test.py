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
from spacy.lang.en.stop_words import STOP_WORDS
import cipheydists


nlp = spacy.load("en_core_web_sm")

f = open("hansard.txt", encoding="ISO-8859-1").read()
f = f.split(".")

enciph = enciphey.encipher()

# all stopwords
all_stopwords = nlp.Defaults.stop_words
top1000Words = cipheydists.get_list("english1000")


def lem(text):
    sentences = nlp(text)
    return set([word.lemma_ for word in sentences])


def stop(text):
    return [word for word in text if not word in all_stopwords]


def check1000Words(text):
    """Checks to see if word is in the list of 1000 words
    the 1000words is a dict, so lookup is O(1)
    Args:
        text -> The text we use to text (a word)
    Returns:
        bool -> whether it's in the dict or not.
    """
    # If we have no wordlist, then we can't reject the candidate on this basis

    if text is None:
        return False
    # If any of the top 1000 words in the text appear
    # return true
    for word in text:
        # I was debating using any() here, but I think they're the
        # same speed so it doesn't really matter too much
        if word in top1000Words:
            return True
    return False


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
    true_positive_returns = 0
    true_negative_returns = 0
    false_positive_returns = 0
    false_negatives_returns = 0

    # calculate aveager time
    time_list = []

    # average sentance size
    sent_size_list = []
    items = range(20000)
    with alive_bar(len(items)) as bar:
        for i in range(0, 5):
            sent = get_random_sentence()
            text = sent[1]
            truthy = sent[0]
            sent_size_list.append(len(text))

            # should be length of chars
            doc = nlp(text)
            text = []
            for token in doc:
                text.append(token.text)
            print(text)

            old = len(text)

            # timing the function
            tic = time.perf_counter()
            result = stop(text)
            tok = time.perf_counter()
            print(text)
            # print(
                # f"The old text is \n {''.join(text)}\n and the new text is \n {''.join(result)} \n\n"
            # )

            new = len(text)
            result = new < old

            # checking for accuracy
            # new = len(new)
            # the and here means we only count True Positives
            # result = new < old
            if result and truthy:
                true_positive_returns += 1
            elif result:
                false_positive_returns += 1
            elif not result and truthy:
                false_negatives_returns += 1
            elif not result:
                true_negative_returns += 1
            else:
                print("ERROR")

            total += 1

            # appending the time
            t = tok - tic
            time_list.append(t)
            bar()

    print(
        f"The accuracy is {str((true_positive_returns+true_negative_returns) / total)} \n and the time it took is {str(mean(time_list))}. \n The average string size was {str(mean(sent_size_list))}"
    )
    print(
        f"""
                        Positive    Negative
            Positive     {true_positive_returns}            {false_positive_returns}
            Negative     {false_negatives_returns}            {true_negative_returns}

            """
    )


perform()
