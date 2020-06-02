import SimpleClassifier.base

import cipheydists

def checkCharsIn(data : str, charset : set):
    return all(char in charset for char in data)


class HexClassifier(SimpleClassifier.base.Classifier):
    def name(): return "base16"
    def isImpossible(data: str):
        # Skip 0x
        if (len(data) >= 2 and data[0] == '0' and (data[1] == 'x' or data[1] == 'X')):
          data = data[2:]
        return not checkCharsIn(data, set(cipheydists.get_charset("encodings")["hex"]))

class Base64Classifier(SimpleClassifier.base.Classifier):
    def name(): return "base64"
    def isImpossible(data: str):
        return not checkCharsIn(data, set(cipheydists.get_charset("encodings")["base64"]))

class BinaryClassifier(SimpleClassifier.base.Classifier):
    def name(): return "base2"
    def isImpossible(data: str):
        return not checkCharsIn(data, set(0,1))

