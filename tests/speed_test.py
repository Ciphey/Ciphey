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
import pprint


class tester:
    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.f = open("hansard.txt", encoding="ISO-8859-1").read()
        self.f = self.f.split(".")

        self.enciph = enciphey.encipher()

        # all stopwords
        self.all_stopwords = self.nlp.Defaults.stop_words
        self.top1000Words = cipheydists.get_list("english1000")
        self.endings = [
            "al",
            "y",
            "sion",
            "tion",
            "ize",
            "ic",
            "ious",
            "ness",
            "ment",
            "ed",
            "ify",
            "ence",
            "fy",
            "less",
            "ance",
            "ship",
            "ate",
            "dom",
            "ist",
            "ish",
            "ive",
            "en",
            "ical",
            "ful",
            "ible",
            "ise",
            "ing",
            "ity",
            "ism",
            "able",
            "ty",
            "er",
            "or",
            "esque",
            "acy",
            "ous",
        ]
        self.endings_3_letters = list(filter(lambda x: len(x) > 3, self.endings))

    def lem(self, text, thresold):
        sentences = self.nlp(text)
        return set([word.lemma_ for word in sentences])

    def stop(self, text, threshold):
        x = [word for word in text if not word in self.all_stopwords]
        return True if len(x) < len(text) else False

    def check1000Words(self, text, threshold):
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
            if word in self.top1000Words:
                return True
        return False

    def get_random_sentence(self, size):
        if random.randint(0, 1) == 0:
            x = None
            while x is None:
                x = (True, " ".join(random.sample(self.f, k=random.randint(1, size))))
            return x
        else:
            x = None
            while x is None:
                x = self.enciph.getRandomEncryptedSentence()
                x = x["Encrypted Texts"]["EncryptedText"]
            return (False, x)

    def get_words(self, text):
        doc = self.nlp(text)
        toReturn = []
        for token in doc:
            toReturn.append((token.text).lower())
        return toReturn

    def word_endings(self, text, thresold):
        total = len(text)
        if total == 0:
            return False
        positive = 0
        # as soon as we hit 25%, we exit and return True
        for word in text:
            for word2 in self.endings:
                if word.endswith(word2):
                    positive += 1
            # if total / positive >= 0.25:
            # return True
        # return False
        if positive == 0:
            return False
        return True if positive / total > thresold else False

    def word_endings_3(self, text, threshold):
        """Word endings that only end in 3 chars, may be faster to compute"""
        positive = 0
        total = len(text)
        if total == 0:
            return False
        for word in text:
            if word[::-3] in self.endings_3_letters:
                positive += 1
        if positive != 0:
            return True if total / positive > threshold else False
        else:
            return False

    # Now to time it and take measurements

    def perform(self, function, sent_size, threshold):
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
        test_range = 200
        for i in range(0, test_range):
            sent = self.get_random_sentence(sent_size)
            text = sent[1]
            truthy = sent[0]
            sent_size_list.append(len(text))

            # should be length of chars
            text = self.get_words(text)
            old = len(text)

            # timing the function
            tic = time.perf_counter()
            result = function(text, threshold)
            tok = time.perf_counter()
            # new = len(result)
            # print(
            # f"The old text is \n {''.join(text)}\n and the new text is \n {''.join(result)} \n\n"
            # )

            # result = new < old

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
        return {
            "Name": function,
            "Threshold": threshold,
            "Accuracy": (true_positive_returns + true_negative_returns) / total,
            "Average_time": mean(time_list),
            "Average_string_len": mean(sent_size_list),
            "confusion_matrix": [
                [true_positive_returns, false_positive_returns],
                [false_negatives_returns, true_negative_returns],
            ],
        }

    def perform_3_sent_sizes(self, threshold):
        """
        Gives us the average accuracy and time etc
        """
        funcs = [obj.word_endings, obj.word_endings_3, obj.stop, obj.check1000Words]
        # funcs = [obj.word_endings]
        names = [
            "word endings",
            "word endngs with just 3 chars",
            "stop words",
            "check 1000 words",
        ]
        sent_sizes = [1, 5, 20]
        x = {}
        for i in range(0, len(funcs)):
            func = funcs[i]
            for y in sent_sizes:
                x[names[i]] = self.perform(func, y, threshold)
        return x

    def perform_best_percentages(self):
        """
        Tells us the optimal percentage thresholds
        """
        """
        TODO I need to record thresholds for each length of text
        """
        best_thresholds = {
            "Word Endings": {"Threshold": 0, "Accuracy": 0},
            "word endngs with just 3 chars": {"Threshold": 0, "Accuracy": 0},
            "stop words'": {"Threshold": 0, "Accuracy": 0},
            "check 1000 words": {"Threshold": 0, "Accuracy": 0},
        }

        items = range(100)
        with alive_bar(len(items)) as bar:
            for i in range(1, 100):
                x = self.perform_3_sent_sizes(threshold=i)
                print(x)
                for key, value in x:
                    # getting max keys
                    temp1 = x[key]["Accuracy"]
                    temp2 = best_thresholds[key]["Accuracy"]
                    if temp1 > temp2:
                        temp2 = temp1
                        best_thresholds[key]["Threshold"] = i
                pprint.pprint(x)
                bar()
                exit(1)


obj = tester()
x = obj.perform_best_percentages()
pprint.pprint(x)
