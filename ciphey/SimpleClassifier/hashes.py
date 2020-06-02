from SimpleClassifier.base import LengthInformedClassifier

import cipheydists

def checkCharsIn(data : str, charset : set):
    return all(char in charset for char in data)


class Md5Classifier(LengthInformedClassifier):
    def name(): return "MD5"
    def isImpossible(data: str, lengths: set):
      return 16 not in lengths

class Sha256Classfier(LengthInformedClassifier):
    def name(): return "SHA2-256"
    def isImpossible(data: str, lengths:set):
        return 32 not in lengths

all_hash_classifiers = [Md5Classifier, Sha256Classfier]
all_hashes = [i.name() for i in all_hash_classifiers]
