class ClassifierBase():
    def name() -> str: pass

class Classifier(ClassifierBase):
    def isImpossible(data: str) -> bool: pass

class EncodingClassifier(ClassifierBase):
    def classify(data: str) -> set: pass

class LengthInformedClassifier(ClassifierBase):
    def isImpossible(data: str, lengths: set) -> bool: pass
