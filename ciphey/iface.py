from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, List, TypeVar, Type, Tuple, Set
import typing

T = TypeVar('T')
U = TypeVar('U')


class ConfigurableModule(ABC):
    @staticmethod
    @abstractmethod
    def getArgs() -> Optional[Dict[str, Dict[str, Any]]]:
        """
            The returned dictionary must be of the format:
                {<name:string>: {"req": <required:bool>, "desc": <description:string>, "default": <default:Any>}, ...}
            The "default" argument is not required, and is ignored if "req" is True
            Return None if there are no arguments
        """
        pass

    @staticmethod
    @abstractmethod
    def getName() -> str:
        """
            Prints the user-specifiable name. MUST NOT contain a '.'; use "::" instead!
        """
        pass

    def fillArgs(self, params: Dict[str, Any]):
        """
            Fills the given params dict with default values where arguments are not given,
            using None as the default value for default values
        """
        for key, value in self.getArgs().items():
            if key in params:
                continue
            if value["req"]:
                raise KeyError(f'Missing required param {key} for {self.getName()}')
            params[key] = value.get("default")

    @abstractmethod
    def __init__(self, config: Dict[str, object]):
        pass


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


class Transcoder(Generic[T, U], ConfigurableModule):
    @abstractmethod
    def transcode(self, src: T) -> U:
        """MUST return either None, or a value of the opposite type to T"""
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class CharSet(Generic[T], ConfigurableModule):
    @abstractmethod
    def get_charset(self) -> Set[T]:
        pass

    @abstractmethod
    def __init__(self, config: Dict[str, object]): super().__init__(config)


class Distribution(Generic[T], ConfigurableModule):
    @abstractmethod
    def get_distribution(self) -> Dict[T, float]:
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
    _reg: Dict[Type, Dict[Tuple, List[Type]]] = {}
    _names: Dict[Type, Dict[Tuple, Dict[str, Type]]] = {}

    def register(self, i: type, *ts: type) -> None:
        for base_type in ts:
            target_type = typing.get_origin(base_type)
            if target_type not in {LanguageChecker, Detector, Decoder, Cracker, Transcoder, CharSet, Distribution, WordList}:
                raise TypeError("Invalid type passed to ciphey.iface.registry.register")
            target_subtypes = typing.get_args(base_type)
            target_list = self._reg.setdefault(target_type, {}).setdefault(target_subtypes, [])
            target_list.append(i)

            self._names.setdefault(target_type, {}).setdefault(target_subtypes, {})[i.getName()] = i
        print(self._reg)
        print(self._names)

    def __getitem__(self, i: type) -> typing.Any:
        target_type = typing.get_origin(i)
        # Check if this is a non-generic type, and return the whole dict if it is
        if target_type is None:
            return self._reg[i]

        return self._reg[target_type][typing.get_args(i)]

    def get_named(self, name: str, i: T) -> T:
        target_type = typing.get_origin(i)
        if target_type is not None:
            target_subtypes = typing.get_args(i)
            return self._names[target_type][target_subtypes][name]
        # If we were not given arguments, then we will have to find it in the list
        #
        # Because we are nice, we will throw an exception on duplicate keys
        ret_value = None
        for subtypes, d in self._names[i].items():
            res = d.get(name)
            if res is not None:
                if ret_value is not None:
                    raise KeyError("Duplicate name of ciphey registered type found!")
                else:
                    ret_value = res
        if ret_value is None:
            raise KeyError(name)
        return ret_value


registry = Registry()
"""
Example:
class Foo(Cracker[str]): pass

registry.register(Foo, Cracker[str])
assert Foo in registry[Cracker[str]]
"""
