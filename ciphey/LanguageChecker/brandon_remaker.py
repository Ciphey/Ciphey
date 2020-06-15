import cipheydists

dictionary_old = set(cipheydists.get_list("english"))

f = open("hansard.txt", encoding="ISO-8859-1").read()

import spacy

nlp = spacy.load("en_core_web_sm")

# I want to work on f rn

"""
ValueError: [E088] Text of length 86544687 exceeds maximum of 1000000. The v2.x parser and NER models require roughly 1GB of temporary memory per 100,000 characters in the input. This means long texts may cause memory allocation errors. If you're not using the parser or NER, it's probably safe to increase the `nlp.max_length` limit. The limit is in number of characters, so you can check whether your inputs are too long by checking `len(text)`.
"""
nlp.max_length = 86545000
doc = nlp(f[0:500])

for token in doc:
    print(token.text)
