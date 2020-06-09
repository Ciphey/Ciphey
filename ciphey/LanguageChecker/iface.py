from abc import ABC, abstractmethod
from typing import Dict


class LanguageChecker(ABC):
    @staticmethod
    @abstractmethod
    def getArgs(**kwargs) -> Dict[str, object]:
        """The returned dictionary must be of the format:
            {<name:string>: {"req": <required:bool>, "desc": <description:string>}, ...}
        """
        pass

    @abstractmethod
    def checkLanguage(self, text: str) -> bool: pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): pass
