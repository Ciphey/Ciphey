from abc import ABC, abstractmethod
from typing import Dict, Optional, List, TypeVar, Generic, Type

from abc import ABC, abstractmethod
from typing import Dict, Optional

import typing

_supported_types = [str, bytes]
_inverse_type = {str: bytes, bytes: str}
T = TypeVar('T', str, bytes)


class ConfigurableModule(ABC):
    @staticmethod
    @abstractmethod
    def getArgs(**kwargs) -> Dict[str, object]:
        """The returned dictionary must be of the format:
            {<name:string>: {"req": <required:bool>, "desc": <description:string>}, ...}
        """
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): pass


class LanguageChecker(Generic[T], ConfigurableModule):
    @abstractmethod
    def checkLanguage(self, text: T) -> bool: pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Detector(Generic[T], ConfigurableModule):
    @abstractmethod
    def what(self) -> str:
        """Returns the cipher that this object attempts to detect"""
        pass

    @abstractmethod
    def scoreLikelihood(self, ctext: T, config: Dict[str, object]) -> Dict[str, float]:
        """Should return a dictionary of (cipher_name: score), using config["checker"] as appropriate"""
        pass

    @abstractmethod
    def isIntensive(self) -> bool:
        """Return True if this will take a significant amount of time by some metric"""
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Decoder(Generic[T], ConfigurableModule):
    """Represents the undoing of some encoding"""

    @abstractmethod
    def decode(self, ctext: T, config: Dict[str, object]) -> Optional[T]: pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Cracker(Generic[T], ConfigurableModule):
    @abstractmethod
    def what(self) -> str:
        """Return the cipher that this object attempts to crack"""
        pass

    @abstractmethod
    def attemptCrack(self, ctext: T, config: Dict[str, object]) -> Optional[T]:
        """This should attempt to crack the cipher, and use the config["checker"] where appropriate"""
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Transcoder(Generic[T], ConfigurableModule):
    @abstractmethod
    def transcode(self, src: T, dst: _inverse_type[T]):
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Registry:
    _lcs: Dict[Type, List[LanguageChecker]] = {}
    _dct: Dict[Type, List[Detector]] = {}
    _dcd: Dict[Type, List[Decoder]] = {}
    _crk: Dict[Type, List[Cracker]] = {}
    _tcd: Dict[Type, List[Transcoder]] = {}

    def registerLanguageChecker(self, i: LanguageChecker) -> None:
        self._lcs.setdefault(typing.get_args(i)[0], []).append(i)

    def registerDetector(self, i: Detector) -> None:
        self._dct.setdefault(typing.get_args(i)[0], []).append(i)

    def registerDecoder(self, i: Decoder) -> None:
        self._dcd.setdefault(typing.get_args(i)[0], []).append(i)

    def registerCracker(self, i: Cracker) -> None:
        self._crk.setdefault(typing.get_args(i)[0], []).append(i)

    def registerTranscoder(self, i: Transcoder) -> None:
        self._tcd.setdefault(typing.get_args(i)[0], []).append(i)

    def getLanguageCheckers(self, t: Type) -> List[LanguageChecker]:
        return self._lcs[t]

    def getLanguageDetectors(self, t: Type) -> List[Detector]:
        return self._dct[t]

    def getDecoders(self, t: Type) -> List[Decoder]:
        return self._dcd[t]

    def getCracker(self, t: Type) -> List[Cracker]:
        return self._crk[t]

    def getTranscoder(self, t: Type) -> List[Transcoder]:
        return self._tcd[t]


registry = Registry()
