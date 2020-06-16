import cipheydists
from math import ceil
from alive_progress import alive_bar

import spacy

# This is the spell check that Chrome, MacOS, Firefox, Libre & Open office and much more.
# Basically, it should be good at itis job.
from spacy_hunspell import spaCyHunSpell

dictionary_old = set(cipheydists.get_list("english"))

f = open("hansard.txt", encoding="ISO-8859-1").read()


nlp = spacy.load("en_core_web_sm")
# uses the mac os version
hunspell = spaCyHunSpell(nlp, "linux")
nlp.add_pipe(hunspell)
# I want to work on f rn

"""
ValueError: [E088] Text of length 86544687 exceeds maximum of 1000000. The v2.x parser and NER models require roughly 1GB of temporary memory per 100,000 characters in the input. This means long texts may cause memory allocation errors. If you're not using the parser or NER, it's probably safe to increase the `nlp.max_length` limit. The limit is in number of characters, so you can check whether your inputs are too long by checking `len(text)`.
"""
nlp.max_length = 86545000


howMany = ceil(len(f) / 1000)
current_location = 0
with alive_bar(howMany) as bar:
    for i in range(0, howMany):
        # TODO when we reach the end of the list, we need to +1 the list. How do?
        doc = nlp(f[current_location : (howMany if i is not howMany else howMany + 1)])

        i += 1
        current_location += howMany
        bar()

        tokenised_text = []

        for token in doc:
            print(token.text)
            if len(token) > 1:
                # so we dont add stuff like "(" to the dictionary or single letters
                # as they are not useful
                tokenised_text.append(token.text.lower())

# TODO
"""
TODO
* spell check hansard.txt
* Strip it of puncuation
remove empty objects (some words are just puncuation on its own)
lemmisate it
turn words into synomyns


create the new dict of hansard.txt


then do the same for the real dict
"""
