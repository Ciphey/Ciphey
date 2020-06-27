from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Any, Callable, Dict, Generic, Optional, List, NamedTuple, TypeVar, Type, Union, Set, \
    Tuple
import pydoc
try:
    from typing import get_origin, get_args
except ImportError:
    from typing_inspect import get_origin, get_args

T = TypeVar('T')
U = TypeVar('U')


class Cache:
    """Used to track state between levels of recursion to stop infinite loops, and to optimise repeating actions"""
    _cache: Dict[str, Dict[str, Any]] = {}

    def mark_str(self, ctext: str) -> bool:
        if ctext in self._cache:
            return False

        self._cache[ctext] = defaultdict()
        return True

    def get_or_update(self, ctext: str, keyname: str, get_value: Callable[[], Any]):
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
    checker: str
    params: Dict[str, Dict[str, Union[str, List[str]]]] = {}
    format: Dict[str, str] = {"in": "str", "out": "str"}
    modules: List[str] = []
    checker: str = "brandon"
    utility_threshold: float = 1.5
    score_threshold: float = 0.8
    default_dist: str = "cipheydists::twist"

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
        self.objs["format"] = {key: pydoc.locate(value) for key, value in self.format.items()}
        self.objs["checker"] = self(registry.get_named(self.checker, Checker))

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

    def get_resource(self, res_name: str, t: Type) -> Any:  # Actually returns obj of type `t`, but python is bad
        loader, name = split_resource_name(res_name)
        return self(registry.get_named(loader, ResourceLoader[t]))(name)

    def merge_dict(self, config_file: Dict[str, Any]):
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
        configPath  The path to the config that should be the default value
        list        Whether this parameter is in the form of a list, and can therefore be specified more than once
        visible     Whether the user can tweak this via the command line
    """
    req: bool
    desc: str
    default: Optional[Any] = None
    list: bool = False
    configPath: Optional[List[str]] = None
    visible: bool = False


class ConfigurableModule(ABC):
    @staticmethod
    @abstractmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """
            Returns a dictionary of `argument name: argument specification`
        """
        pass

    def _checkParams(self, params: Dict[str, Any], config: Config):
        """
            Fills the given params dict with default values where arguments are not given,
            using None as the default value for default values
        """
        for key, value in self.getParams().items():
            if key in params:
                continue
            if value.req:
                raise KeyError(f'Missing required param {key} for {self.__name__}')
            if value.configPath is not None:
                tmp = getattr(config, value.configPath[0])
                params[key] = tmp[value.configPath[1:]] if len(value.configPath) > 1 else tmp
            else:
                params[key] = value.default

    def _params(self):
        return self._params_obj

    @abstractmethod
    def __init__(self, config: Config):
        if self.getParams() is not None:
            self._params_obj = config.params.setdefault(self.__name__, {})
            self._checkParams(self._params_obj, config)


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
    def getTargets() -> Set[str]:
        """Should return a list of targets that this object attacks/decodes"""
        pass


class Checker(Generic[T], ConfigurableModule):
    @abstractmethod
    def check(self, text: T) -> bool: pass

    def __call__(self, *args): return self.check(*args)

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)


class Detector(Generic[T], ConfigurableModule, KnownUtility, Targeted):
    @abstractmethod
    def scoreLikelihood(self, ctext: T) -> Dict[str, float]:
        """Should return a dictionary of (cipher_name: score)"""
        pass

    def __call__(self, *args): return self.scoreLikelihood(*args)

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


class Decoder(Generic[T, U], ConfigurableModule, Targeted):
    """Represents the undoing of some encoding into a different (or the same) type"""

    @abstractmethod
    def decode(self, ctext: T) -> Optional[U]: pass

    def __call__(self, *args): return self.decode(*args)

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


class CrackResults(NamedTuple):
    plaintext: str
    keyInfo: Optional[str] = None
    miscInfo: Optional[str] = None


class Cracker(Generic[T], ConfigurableModule, KnownUtility, Targeted):
    @abstractmethod
    def attemptCrack(self, ctext: T, target: str) -> Optional[CrackResults]:
        """
            This should attempt to crack the cipher `target`, and use the config["checker"] where appropriate
        """
        pass

    def __call__(self, *args): return self.attemptCrack(*args)

    @abstractmethod
    def __init__(self, config: Config): super().__init__(config)


class ResourceLoader(Generic[T], ConfigurableModule):
    @abstractmethod
    def whatResources(self) -> Set[str]:
        """
            Return a set of the names of instances T you can provide.
            The names SHOULD be unique amongst ResourceLoaders of the same type

            These names will be exposed as f"{self.__name__}::{name}", use split_resource_name to recover this
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

        targets = None

        if issubclass(i, Targeted):
            targets = i.getTargets()

        for base_type in ts:
            target_type = get_origin(base_type)
            if target_type not in {Checker, Detector, Decoder, Cracker, ResourceLoader}:
                raise TypeError("Invalid type passed to ciphey.iface.registry.register")
            target_subtypes = get_args(base_type)
            target_reg = self._reg.setdefault(target_type, {})
            # Seek to the given type
            for subtype in target_subtypes[0:-1]:
                target_reg = target_reg.setdefault(subtype, {})
            target_reg.setdefault(target_subtypes[-1], []).append(i)

            name_target[1].add(target_type)
            name_target[1].add(base_type)

            if targets is not None and issubclass(target_type, Targeted):
                for target_name in targets:
                    self._targets.setdefault(target_name, {}).setdefault(base_type, []).append(i)

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
        return f"ciphey.iface.Registry {{\n_reg: {self._reg},\n_names: {self._names},\n_targets: {self._targets}\n}}"


registry = Registry()

"""
Example:
class Foo(Cracker[str]): pass

registry.register(Foo, Cracker[str])
assert Foo in registry[Cracker[str]]
"""
