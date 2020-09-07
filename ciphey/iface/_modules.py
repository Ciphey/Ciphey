from abc import ABC, abstractmethod
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Optional,
    List,
    NamedTuple,
    TypeVar,
    Type,
    Union,
    Set,
)
import pydoc

from loguru import logger

import datetime

from ._fwd import config as Config

T = TypeVar("T")
U = TypeVar("U")


class ParamSpec(NamedTuple):
    """
    Attributes:
        req         Whether this argument is required
        desc        A description of what this argument does
        default     The default value for this argument. Ignored if req == True or configPath is not None
        config_ref  The path to the config that should be the default value
        list        Whether this parameter is in the form of a list, and can therefore be specified more than once
        visible     Whether the user can tweak this via the command line
    """

    req: bool
    desc: str
    default: Optional[Any] = None
    list: bool = False
    config_ref: Optional[List[str]] = None
    visible: bool = True


class ConfigurableModule(ABC):
    @staticmethod
    @abstractmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """
            Returns a dictionary of `argument name: argument specification`
        """
        pass

    def _checkParams(self):
        """
            Fills the given params dict with default values where arguments are not given,
            using None as the default value for default values
        """

        params = self._params()
        config = self._config()

        for key, value in self.getParams().items():
            # If we already have it, then we don't need to do anything
            if key in params:
                continue
            # If we don't have it, but it's required, then fail
            if value.req:
                raise KeyError(
                    f"Missing required param {key} for {type(self).__name__.lower()}"
                )
            # If it's a reference by default, fill that in
            if value.config_ref is not None:
                tmp = getattr(config, value.config_ref[0])
                params[key] = (
                    tmp[value.config_ref[1:]] if len(value.config_ref) > 1 else tmp
                )
            # Otherwise, put in the default value (if it exists)
            elif value.default is not None:
                params[key] = value.default

    def _params(self):
        return self._params_obj

    def _config(self):
        return self._config_obj

    @abstractmethod
    def __init__(self, config: Config):
        self._config_obj = config
        if self.getParams() is not None:
            self._params_obj = config.params.setdefault(type(self).__name__.lower(), {})
            self._checkParams()


class Targeted(ABC):
    @staticmethod
    @abstractmethod
    def getTarget() -> str:
        """Should return the target that this object attacks/decodes"""
        pass


class PolymorphicChecker(ConfigurableModule):
    @abstractmethod
    def check(self, text) -> Optional[str]:
        """Should return some description (or an empty string) on success, otherwise return None"""
        pass

    @abstractmethod
    def getExpectedRuntime(self, text) -> float:
        pass

    def __call__(self, *args):
        return self.check(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


class Checker(Generic[T], ConfigurableModule):
    @abstractmethod
    def check(self, text: T) -> Optional[str]:
        """Should return some description (or an empty string) on success, otherwise return None"""
        pass

    @abstractmethod
    def getExpectedRuntime(self, text: T) -> float:
        pass

    def __call__(self, *args):
        return self.check(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)

    @classmethod
    def convert(cls, expected: Set[type]):
        class PolyWrapperClass(PolymorphicChecker):
            @staticmethod
            def getParams() -> Optional[Dict[str, ParamSpec]]:
                return cls.getParams()

            def check(self, text) -> Optional[str]:
                """Should return some description (or an empty string) on success, otherwise return None"""
                if type(text) not in expected:
                    return None
                else:
                    return self._base.check(text)

            def getExpectedRuntime(self, text) -> float:
                if type(text) not in expected:
                    return 0
                else:
                    return self._base.getExpectedRuntime(text)

            def __init__(self, config: Config):
                super().__init__(config)
                # This is easier than inheritance
                self._base = cls(config)

        PolyWrapperClass.__name__ = cls.__name__

        return PolyWrapperClass


# class Detector(Generic[T], ConfigurableModule, KnownUtility, Targeted):
#     @abstractmethod
#     def scoreLikelihood(self, ctext: T) -> Dict[str, float]:
#         """Should return a dictionary of (cipher_name: score)"""
#         pass
#
#     def __call__(self, *args): return self.scoreLikelihood(*args)
#
#     @abstractmethod
#     def __init__(self, config: Config): super().__init__(config)


class Decoder(Generic[T, U], ConfigurableModule, Targeted):
    """Represents the undoing of some encoding into a different (or the same) type"""

    @abstractmethod
    def decode(self, ctext: T) -> Optional[U]:
        pass

    @staticmethod
    @abstractmethod
    def priority() -> float:
        """What proportion of decodings are this?"""
        pass

    def __call__(self, *args):
        return self.decode(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


class DecoderComparer:
    value: Type[Decoder]

    def __le__(self, other: "DecoderComparer"):
        return self.value.priority() <= other.value.priority()

    def __ge__(self, other: "DecoderComparer"):
        return self.value.priority() >= other.value.priority()

    def __lt__(self, other: "DecoderComparer"):
        return self.value.priority() < other.value.priority() and self != other

    def __gt__(self, other: "DecoderComparer"):
        return self.value.priority() > other.value.priority() and self != other

    def __init__(self, value: Type[Decoder]):
        self.value = value

    def __repr__(self):
        return f"<DecoderComparer {self.value}:{self.value.priority()}>"


class CrackResult(NamedTuple, Generic[T]):
    value: T
    key_info: Optional[str] = None
    misc_info: Optional[str] = None


class CrackInfo(NamedTuple):
    success_likelihood: float
    success_runtime: float
    failure_runtime: float


class Cracker(Generic[T], ConfigurableModule, Targeted):
    @abstractmethod
    def getInfo(self, ctext: T) -> CrackInfo:
        """Should return some informed guesses on resource consumption when run on `ctext`"""
        pass

    @abstractmethod
    def attemptCrack(self, ctext: T) -> List[CrackResult]:
        """
            This should attempt to crack the cipher `target`, and return a list of candidate solutions
        """
        # FIXME: Actually CrackResult[T], but python complains
        pass

    def __call__(self, *args):
        return self.attemptCrack(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


class ResourceLoader(Generic[T], ConfigurableModule):
    @abstractmethod
    def whatResources(self) -> Optional[Set[str]]:
        """
            Return a set of the names of instances T you can provide.
            The names SHOULD be unique amongst ResourceLoaders of the same type

            These names will be exposed as f"{self.__name__}::{name}", use split_resource_name to recover this

            If you cannot reasonably determine what resources you provide, return None instead
        """
        pass

    @abstractmethod
    def getResource(self, name: str) -> T:
        """
            Returns the requested distribution

            The behaviour is undefined if `name not in self.what_resources()`
        """
        pass

    def __call__(self, *args):
        return self.getResource(*args)

    def __getitem__(self, *args):
        return self.getResource(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


class SearchLevel(NamedTuple):
    name: str
    result: CrackResult

    @staticmethod
    def input(ctext: Any):
        return SearchLevel(name="input", result=CrackResult(ctext))


class SearchResult(NamedTuple):
    path: List[SearchLevel]
    check_res: str


class Searcher(ConfigurableModule):
    """A very basic interface for code that plans out how to crack the ciphertext"""

    @abstractmethod
    def search(self, ctext: Any) -> Optional[SearchResult]:
        """Returns the path to the correct ciphertext"""
        pass

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


def pretty_search_results(res: SearchResult, display_intermediate: bool = False) -> str:
    ret: str = ""
    if len(res.check_res) != 0:
        ret += f"Checker: {res.check_res}\n"
    ret += "Format used:\n"

    def add_one():
        nonlocal ret
        ret += f"  {i.name}"
        already_broken = False
        if i.result.key_info is not None:
            ret += f":\n    Key: {i.result.key_info}\n"
            already_broken = True
        if i.result.misc_info is not None:
            if not already_broken:
                ret += ":\n"
            ret += f"    Misc: {i.result.misc_info}\n"
            already_broken = True
        if display_intermediate:
            if not already_broken:
                ret += ":\n"
            ret += f'    Value: "{i.result.value}"\n'
            already_broken = True
        if not already_broken:
            ret += "\n"

    # Skip the 'input' and print in order
    for i in res.path[1:]:
        add_one()

    # Remove trailing newline
    ret = ret[:-1]

    # If we didn't show intermediate steps, then print the final result
    if not display_intermediate:
        ret += (
            f"""\nFinal result: [bold green]"{res.path[-1].result.value}"[bold green]"""
        )

    return ret


# Some common collection types
Distribution = Dict[str, float]
Translation = Dict[str, str]
WordList = Set[str]
