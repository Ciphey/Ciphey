from abc import ABC, abstractmethod
from typing import Dict, Optional, List, TypeVar, Generic, Type, Union

from abc import ABC, abstractmethod

import typing

_supported_types = [str, bytes]
_inverse_type = {str: bytes, bytes: str}
T = TypeVar('T', str, bytes)
global registry


class ConfigurableModule(ABC):
    @staticmethod
    @abstractmethod
    def getArgs(**kwargs) -> Optional[Dict[str, object]]:
        """
            The returned dictionary must be of the format:
                {<name:string>: {"req": <required:bool>, "desc": <description:string>}, ...}
            Return None if there are no arguments
        """
        pass

    @staticmethod
    @abstractmethod
    def getName(**kwargs) -> str:
        """
            Prints the user-specifiable name
        """
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): pass


class KnownUtility(ABC):
    @abstractmethod
    def scoreUtility(self) -> int:
        """
            Return speed * reliability

            Speed: for an average string
            5. Runs in microseconds
            4. Runs in milliseconds
            3. Runs in less than a second
            2. Runs in tens of seconds
            1. Runs in minutes

            Reliability:
            5. Will definitely work (cracks all of it's cipher type, completely identifiers ciphers, etc)
            4. Works in most cases
            3. Works on some cases (specific versions of common libraries)
            2. Works on a few cases (old patched bug, rare misconfiguration)
            1. Exploits some extreme edge case
        """
        pass


class LanguageChecker(Generic[T], ConfigurableModule):
    @abstractmethod
    def checkLanguage(self, text: T) -> bool: pass

    def __init__(self, config: Dict[str, object]):
        super().__init__(config)


class Detector(Generic[T], ConfigurableModule, KnownUtility):
    @abstractmethod
    def what(self) -> str:
        """Returns the cipher that this object attempts to detect"""
        pass

    @abstractmethod
    def scoreLikelihood(self, ctext: T, config: Dict[str, object]) -> Dict[str, float]:
        """Should return a dictionary of (cipher_name: score), using config["checker"] as appropriate"""
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Decoder(Generic[T], ConfigurableModule):
    """Represents the undoing of some encoding"""

    @abstractmethod
    def decode(self, ctext: T, config: Dict[str, object]) -> Optional[T]: pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Cracker(Generic[T], ConfigurableModule, KnownUtility):
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
    def transcode(self, src: T) -> Union[str, bytes]:
        """MUST return either None, or a value of the opposite type to T"""
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Charset(Generic[T], ConfigurableModule):
    @abstractmethod
    def get_charset(self) -> T:
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Distribution(Generic[T], ConfigurableModule):
    @abstractmethod
    def get_distribution(self) -> T:
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class WordList(Generic[T], ConfigurableModule):
    @abstractmethod
    def get_wordlist(self) -> T:
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Registry:
    _reg: Dict[Type, Dict[Type, List[Type]]] = {}

    def register(self, i: type, *ts: type) -> None:
        for base_type in ts:
            target_type = typing.get_origin(base_type)
            target_subtype = typing.get_args(base_type)[0]
            target_list = self._reg[target_type].setdefault(target_subtype, [])
            target_list.append(i)

    def __getitem__(self, i: type) -> typing.Any:
        target_type = typing.get_origin(i)
        # Check if this is a non-generic type, and return the dict if it is
        if target_type is None:
            return self._reg[i]

        return self._reg[target_type][typing.get_args(i)[0]]

    def __init__(self):
        for i in [LanguageChecker, Detector, Decoder, Cracker, Transcoder, Charset, Distribution, WordList]:
            self._reg[i] = {}

registry = Registry()
"""
Example:
class Foo(Cracker[str]): pass

registry.register(Foo, Cracker[str])
assert Foo in registry[Cracker[str]]
"""
