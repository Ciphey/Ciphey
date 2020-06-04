from .iface import EncodingClassifier

import cipheydists


<<<<<<< HEAD
def checkCharsIn(data: str, charset: set):
    return all(char in charset for char in data)


class HexClassifier(SimpleClassifier.base.EncodingClassifier):
    def name():
        return "base16"

=======
def checkCharsIn(data : str, charset : set):
    return all(char in charset for char in data)


class HexEncClassifier(EncodingClassifier):
    def name(): return "base16"
>>>>>>> 0c235a7... Refactored Brandon checker
    def classify(data: str):
        # Skip 0x
        if len(data) >= 2 and data[0] == "0" and (data[1] == "x" or data[1] == "X"):
            data = data[2:]
        if not checkCharsIn(data, set(cipheydists.get_charset("encodings")["hex"])):
            return set()
        return {-(-len(data) // 2)}


<<<<<<< HEAD
class Base64Classifier(SimpleClassifier.base.Classifier):
    def name():
        return "base64"

=======
class Base64EncClassifier(EncodingClassifier):
    def name(): return "base64"
>>>>>>> 0c235a7... Refactored Brandon checker
    def classify(data: str):
        if not checkCharsIn(data, set(cipheydists.get_charset("encodings")["base64"])):
            return set()
        return {-(-len(data) // 3) * 4}


<<<<<<< HEAD
class BinaryClassifier(SimpleClassifier.base.Classifier):
    def name():
        return "base2"

=======
class BinaryEncClassifier(EncodingClassifier):
    def name(): return "base2"
>>>>>>> 0c235a7... Refactored Brandon checker
    def classify(data: str):
        if len(data) >= 2 and data[0] == "0" and data[1] == "b":
            data = data[2:]
        if not checkCharsIn(data, {0, 1}):
            return set()
        return {-(-len(data) // 2)}


<<<<<<< HEAD
class DecimalClassifier(SimpleClassifier.base.Classifier):
    def name():
        return "base10"

=======
class DecimalEncClassifier(EncodingClassifier):
    def name(): return "base10"
>>>>>>> 0c235a7... Refactored Brandon checker
    def classify(data: str):
        try:
            return {-(-int(data).bit_length() // 8)}
        except:
            return set()


<<<<<<< HEAD
all_encoding_classifiers = [
    HexClassifier,
    Base64Classifier,
    BinaryClassifier,
    DecimalClassifier,
]
=======
all_encoding_classifiers = [HexEncClassifier, Base64EncClassifier, BinaryEncClassifier, DecimalEncClassifier]
>>>>>>> 0c235a7... Refactored Brandon checker
all_encodings = [i.name() for i in all_encoding_classifiers]
