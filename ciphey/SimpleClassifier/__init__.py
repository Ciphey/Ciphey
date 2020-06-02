from SimpleClassifier.encoding import *

def filterOut(data:str) -> set:
    ret = set()
    for c in [HexClassifier, Base64Classifier, BinaryClassifier]:
        if c.isImpossible(data):
            ret.add(c.name())
    return ret
