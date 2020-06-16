import cipheydists
from math import ceil
from alive_progress import alive_bar

import spacy

"""
This document:
* opens the two dicts up
* combines them together, as a set using union
* turns all words lower case
* filter all words less than or equal to 1 char
* Lemmisatizes the words (greatly -> great)

Phase 1 is O(n), except without the dict lookup (space complexity is O(n) instead of O(n + 1000))
Phase 2 is O(n), with much, much lower space complexity and higher accuracy.
"""

# This is the spell check that Chrome, MacOS, Firefox, Libre & Open office and much more.
# Basically, it should be good at itis job.
dictionary_old = set(cipheydists.get_list("english"))

# f = open("hansard.txt", encoding="ISO-8859-1").read()
f = set(open("aspell.txt", "r").readlines())

nlp = spacy.load("en_core_web_sm")
# uses the mac os version
# I want to work on f rn

"""
ValueError: [E088] Text of length 86544687 exceeds maximum of 1000000. The v2.x parser and NER models require roughly 1GB of temporary memory per 100,000 characters in the input. This means long texts may cause memory allocation errors. If you're not using the parser or NER, it's probably safe to increase the `nlp.max_length` limit. The limit is in number of characters, so you can check whether your inputs are too long by checking `len(text)`.
"""
# nlp.max_length = 86545000


# howMany = ceil(len(f) / 1000)
# current_location = 0
# with alive_bar(howMany) as bar:
#     for i in range(0, howMany):
#         # TODO when we reach the end of the list, we need to +1 the list. How do?
#         doc = nlp(f[current_location : (howMany if i is not howMany else howMany + 1)])

#         i += 1
#         current_location += howMany
#         bar()

#         tokenised_text = []

#         for token in doc:
#             print(token.text)
#             if len(token) > 1:
#                 # so we dont add stuff like "(" to the dictionary or single letters
#                 # as they are not useful
#                 tokenised_text.append(token.text.lower())

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

# since they are sets we get uniques only
# TODO I think this is a bug?
complete = set(f.union(dictionary_old))
print(f"Complete before set union is size {len(f) + len(dictionary_old)}")
print(f"Now complete size after union is {len(complete)}")
print(f"The intersection is {f.intersection(dictionary_old)}")
# turns it all into lowercase
complete = set([word.lower() for word in complete])

# This shouldr remove all words that are of length 1
complete = list(set(filter(lambda x: len(x) > 1, complete)))
print(f"Complete size after removing small chars is {len(complete)}")

# Lemmatization
sentences = nlp(" ".join(complete[0:50000]))
print(f"Length of sentences is {len(sentences)}")
lemmatised_words_set = set([word.lemma_ for word in sentences])
print(f"Lemmatised words is now size {len(lemmatised_words_set)}")

# Now I need to group synomyns into one word
# I heard that word2vec works well for this
