from abc import ABC, abstractmethod


class LanguageChecker(ABC):
    @staticmethod
    @abstractmethod
    def getArgs(**kwargs) -> dict:
        """The returned dictionary must be of the format:
            {<name:string>: {"req": <required:bool>, "desc": <description:string>}, ...}
        """
        pass

    @abstractmethod
    def checkLanguage(self, text: str) -> bool: pass

    @abstractmethod
    def __init__(self, config): pass
