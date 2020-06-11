from abc import ABC, abstractmethod
from typing import Dict, Optional, List


class LanguageChecker(ABC):
    @staticmethod
    @abstractmethod
    def getArgs(**kwargs) -> Dict[str, object]:
        """The returned dictionary must be of the format:
            {<name:string>: {"req": <required:bool>, "desc": <description:string>}, ...}
        """
        pass

    @abstractmethod
    def checkLanguage(self, text: bytes) -> bool: pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): pass

class Detector(ABC):
    @abstractmethod
    def what(self) -> str:
        """Returns the cipher that this object attempts to detect"""
        pass
    @abstractmethod
    def scoreLikelihood(self, ctext: bytes, config: Dict[str, object]) -> Dict[str, float]:
         """Should return a dictionary of (cipher_name: score), using config["checker"] as appropriate"""
        pass
    @abstractmethod
    def isIntensive(self) -> bool:
        """Return True if this will take a significant amount of time by some metric"""
        pass

class Decoder(ABC):
    """Represents the undoing of some encoding"""
    @staticmethod
    @abstractmethod
    def decode(self, ctext: bytes, config: Dict[str, object]) -> Optional[bytes]: pass

class Cracker(ABC):
    @abstractmethod
    def what(self) -> str:
        """Return the cipher that this object attempts to crack"""
        pass
    @abstractmethod
    def attemptCrack(self, ctext: bytes, config: Dict[str, object]) -> Optional[bytes]:
        """This should attempt to crack the cipher, and use the config["checker"] where appropriate"""
        pass

class Registry:
    _lcs: List[LanguageChecker] = []
    _dct: List[Detector] = []
    _dcd: List[Decoder] = []
    _crk: List[Cracker] = []

    def registerLanguageChecker(self, i: LanguageChecker) -> None:
        self._lcs.append(i)
    def registerDetector(self, i: Detector) -> None:
        self._dct.append(i)
    def registerDecoder(self, i: Decoder) -> None:
        self._dcd.append(i)
    def registerCracker(self, i: Cracker) -> None:
        self._crk.append(i)

    def getLanguageCheckers(self) -> type(_lcs):
        return self._lcs
    def getLanguageDetectors(self) -> type(_dct):
        return self._dct
    def getDecoders(self) -> type(_dcd):
        return self._dcd
    def getCracker(self) -> type(_crk):
        return self._dct
registry = Registry()