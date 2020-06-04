from abc import ABC, abstractmethod

"""Classifiers SHOULD be stateless, so all methods must be static"""
class ClassifierBase(ABC):
    @staticmethod
    @abstractmethod
    def name() -> str: pass


class Classifier(ClassifierBase):
    @staticmethod
    @abstractmethod
    def isImpossible(data: str) -> bool: pass


class EncodingClassifier(ClassifierBase):
    @staticmethod
    @abstractmethod
    def classify(data: str) -> set: pass


class LengthInformedClassifier(ClassifierBase):
    @staticmethod
    @abstractmethod
    def isImpossible(data: str, lengths: set) -> bool: pass
