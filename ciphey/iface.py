from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Any, Callable, Dict, Generic, Optional, List, NamedTuple, TypeVar, Type, Union, Set, \
    Tuple
import pydoc
try:
    from typing import get_origin, get_args
except ImportError:
    from typing_inspect import get_origin, get_args

from loguru import logger

import datetime

T = TypeVar('T')
U = TypeVar('U')


class Cache:
    """Used to track state between levels of recursion to stop infinite loops, and to optimise repeating actions"""
    _cache: Dict[Any, Dict[str, Any]] = {}

    def mark_ctext(self, ctext: Any) -> bool:
        if (type(ctext) == str or type(ctext) == bytes) and len(ctext) < 4:
            logger.trace(f"Candidate {ctext} too short!")
            return False

        if ctext in self._cache:
            logger.trace(f"Deduped {ctext}")
            return False

        self._cache[ctext] = {}
        return True

    def get_or_update(self, ctext: Any, keyname: str, get_value: Callable[[], Any]):
        # Should have been marked first
        target = self._cache[ctext]
        res = target.get(keyname)
        if res is not None:
            return res

        val = get_value()
        target[keyname] = val
        return val


class Config:
    grep: bool = False
    info: bool = False
    debug: Optional[str] = "WARNING"
    searcher: str = "perfection"
    params: Dict[str, Dict[str, Union[str, List[str]]]] = {}
    format: Dict[str, str] = {"in": "str", "out": "str"}
    modules: List[str] = []
    checker: str = "brandon"
    utility_threshold: float = 1.5
    score_threshold: float = 0.8
    default_dist: str = "cipheydists::dist::twist"
    timeout: Optional[int] = None

    _inst: Dict[type, Any] = {}
    objs: Dict[str, Any] = {}
    cache: Cache = Cache()

    def instantiate(self, t: type) -> Any:
        """
            Used to enable caching of a instantiated type after the configuration has settled
        """
        # We cannot use set default as that would construct it again, and throw away the result
        res = self._inst.get(t)
        if res is not None:
            return res
        ret = t(self)
        self._inst[t] = ret
        return ret

    def __call__(self, t: type) -> Any:
        return self.instantiate(t)

    def update(self, attrname: str, value: Optional[Any]):
        if value is not None:
            setattr(self, attrname, value)

    def update_param(self, owner: str, name: str, value: Optional[Any]):
        if value is None:
            return

        target = self.params.setdefault(owner, {})
        if registry.get_named(name).getParams()[name].list:
            target.setdefault(name, []).append(value)
        else:
            target[name] = value

    def update_format(self, paramname: str, value: Optional[Any]):
        if value is not None:
            self.format[paramname] = value

    def load_objs(self):
        # Basic type conversion
        if self.timeout is not None:
            self.objs["timeout"] = datetime.timedelta(seconds=int(self.timeout))
        self.objs["format"] = {key: pydoc.locate(value) for key, value in self.format.items()}

        # Checkers do not depend on anything
        self.objs["checker"] = self(registry.get_named(self.checker, Checker))
        # Searchers only depend on checkers
        self.objs["searcher"] = self(registry.get_named(self.searcher, Searcher))

    def update_log_level(self, level: Optional[str]):
        self.debug = level

        from loguru import logger
        import sys

        logger.remove()
        if self.debug is None:
            return
        logger.configure()
        if self.debug == "TRACE" or self.debug == "DEBUG":
            logger.add(sink=sys.stderr, level=self.debug, colorize=sys.stderr.isatty())
            logger.opt(colors=True)
        else:
            logger.add(sink=sys.stderr, level=self.debug, colorize=False, format="{message}")
        logger.debug(f"""Debug level set to {self.debug}""")

    def load_modules(self):
        import importlib.util
        for i in self.modules:
            spec = importlib.util.spec_from_file_location("ciphey.module_load_site", i)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

    def get_resource(self, res_name: str, t: Optional[Type] = None) -> Any:
        logger.trace(f"Loading resource {res_name} of type {t}")

        # FIXME: Actually returns obj of type `t`, but python is bad
        loader, name = split_resource_name(res_name)
        if t is None:
            return self(registry.get_named(loader, ResourceLoader))(name)
        else:
            return self(registry.get_named(loader, ResourceLoader[t]))(name)

    def merge_dict(self, config_file: Dict[str, Any]):
        # TODO: implement this
        pass

    def __init__(self):
        self.update_log_level(self.debug)


def split_resource_name(full_name: str) -> (str, str):
    return full_name.split("::", 1)


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
    visible: bool = False


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
                raise KeyError(f'Missing required param {key} for {type(self).__name__.lower()}')
            # If it's a reference by default, fill that in
            if value.config_ref is not None:
                tmp = getattr(config, value.config_ref[0])
                params[key] = tmp[value.config_ref[1:]] if len(value.config_ref) > 1 else tmp
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


class KnownUtility(ABC):
    @staticmethod
    @abstractmethod
    def scoreUtility() -> float:
        """
            Return speed^2 + reliability^2

            Speed: for an average string
            1.0: Runs in microseconds
            0.8: Runs in milliseconds
            0.6: Runs in less than a second
            0.4: Runs in tens of seconds
            0.2: Runs in minutes
            0.0: Undecidable

            Reliability:
            1.0: Will definitely work (cracks all of it's cipher type, completely identifiers ciphers, etc)
            0.8: Works in most cases
            0.6: Works on some cases (specific versions of common libraries)
            0.4: Works on a few cases (old patched bug, rare misconfiguration)
            0.2: Exploits some extreme edge case
            0.0: Never works
        """
        pass


class Targeted(ABC):
    @staticmethod
    @abstractmethod
    def getTarget() -> str:
        """Should return the target that this object attacks/decodes"""
        pass


class Checker(Generic[T], ConfigurableModule):
    @abstractmethod
    def check(self, text: T) -> Optional[str]:
        """Should return some description (or an empty string) on success, otherwise return None"""
        pass

    @abstractmethod
    def getExpectedRuntime(self, text: T) -> float: pass

    def __call__(self, *args): return self.check(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


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
    def decode(self, ctext: T) -> Optional[U]: pass

    def __call__(self, *args): return self.decode(*args)

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


class CrackResult(NamedTuple, Generic[T]):
    value: T
    key_info: Optional[str] = None
    misc_info: Optional[str] = None


class CrackInfo(Generic[T], NamedTuple):
    success_likelihood: float
    success_runtime: float
    failure_runtime: float


class Cracker(Generic[T], ConfigurableModule, KnownUtility, Targeted):
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

    def __call__(self, *args): return self.attemptCrack(*args)

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


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

    def __call__(self, *args): return self.getResource(*args)

    def __getitem__(self, *args): return self.getResource(*args)

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


class SearchLevel(NamedTuple):
    name: str
    result: CrackResult


class SearchResult(NamedTuple):
    path: List[SearchLevel]
    check_res: str


class Searcher(ConfigurableModule):
    """A very basic interface for code that plans out how to crack the ciphertext"""

    @abstractmethod
    def search(self, ptext: Any) -> SearchResult:
        """Returns the path to the correct ciphertext"""
        pass

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


def pretty_search_results(res: SearchResult, display_intermediate: bool = True):
    ret: str = f"Checker: {res.check_res}\n" if len(res.check_res) != 0 else ""

    def add_one():
        nonlocal ret
        ret += f'{i.name}'
        already_broken = False
        if i.result.key_info is not None:
            ret += f":\n  Key: {i.result.key_info}\n"
            already_broken = True
        if i.result.misc_info is not None:
            if not already_broken:
                ret += ':\n'
            ret += f'  Misc: {i.result.misc_info}\n'
            already_broken = True
        if display_intermediate:
            if not already_broken:
                ret += ':\n'
            ret += f'  Value: {i.result.value}\n'
            already_broken = True
        if not already_broken:
            ret += " "
        ret += "<-\n"
    for i in res.path[::-1]:
        add_one()

    # Remove trailing arrow
    return ret[:-len("-> ")]


# Some common collection types
Distribution = Dict[str, float]
WordList = Set[str]


class Registry:
    # I was planning on using __init_subclass__, but that is incompatible with dynamic type creation when we have
    # generic keys

    RegElem = Union[List[Type], Dict[Type, 'RegElem']]

    _reg: Dict[Type, RegElem] = {}
    _names: Dict[str, Tuple[Type, Set[Type]]] = {}
    _targets: Dict[str, Dict[Type, List[Type]]] = {}

    def register(self, i: type, *ts: type) -> None:
        name_target = self._names[i.__name__.lower()] = (i, set())

        if issubclass(i, Targeted):
            target = i.getTarget()
        else:
            target = None

        for base_type in ts:
            search_type: type

            if base_type is Searcher:
                search_type = base_type
            else:
                search_type = target_type = get_origin(base_type)
                if target_type not in {Checker, ConfigurableModule, Cracker, Decoder, ResourceLoader}:
                    raise TypeError("Invalid type passed to ciphey.iface.registry.register")
                target_subtypes = get_args(base_type)
                target_reg = self._reg.setdefault(target_type, {})
                # Seek to the given type
                for subtype in target_subtypes[0:-1]:
                    target_reg = target_reg.setdefault(subtype, {})
                target_reg.setdefault(target_subtypes[-1], []).append(i)

                name_target[1].add(target_type)
            name_target[1].add(base_type)

            if target is not None and issubclass(search_type, Targeted):
                self._targets.setdefault(target, {}).setdefault(base_type, []).append(i)

    def __getitem__(self, i: type) -> Optional[Any]:
        target_type = get_origin(i)
        # Check if this is a non-generic type, and return the whole dict if it is
        if target_type is None:
            return self._reg[i]

        target_subtypes = get_args(i)
        target_list = self._reg.setdefault(target_type, {})
        for subtype in target_subtypes:
            target_list = target_list.setdefault(subtype, {})
        return target_list

    def get_named(self, name: str, type_constraint: Type = None) -> Any:
        ret = self._names[name.lower()]
        if type_constraint and type_constraint not in ret[1]:
            raise TypeError(f"Type mismatch: wanted {type_constraint}, got {ret[1]}")
        return ret[0]

    def get_targeted(self, target: str, type_constraint: Type = None) \
            -> Optional[Union[Dict[Type, Set[Type]], Set[Type]]]:
        x = self._targets.get(target)
        if x is None or type_constraint is None:
            return x
        return x.get(type_constraint)

    def __str__(self):
        return f"ciphey.iface.Registry {{_reg: {self._reg}, _names: {self._names}, _targets: {self._targets}}}"


registry = Registry()

"""
Example:
class Foo(Cracker[str]): pass

registry.register(Foo, Cracker[str])
assert Foo in registry[Cracker[str]]
"""
