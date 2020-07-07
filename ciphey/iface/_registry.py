from abc import ABC, abstractmethod
from collections import defaultdict
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
    Tuple,
)
import pydoc

try:
    from typing import get_origin, get_args
except ImportError:
    from typing_inspect import get_origin, get_args

from loguru import logger
from . import _fwd
from ._modules import *
import datetime


class Registry:
    # I was planning on using __init_subclass__, but that is incompatible with dynamic type creation when we have
    # generic keys

    RegElem = Union[List[Type], Dict[Type, "RegElem"]]

    _reg: Dict[Type, RegElem] = {}
    _names: Dict[str, Tuple[Type, Set[Type]]] = {}
    _targets: Dict[str, Dict[Type, List[Type]]] = {}
    _modules = {Checker, Cracker, Decoder, ResourceLoader, Searcher}

    @classmethod
    def _register_one(cls, module_base, module_args):
        target_reg = cls._reg.setdefault(module_base, {})
        # Seek to the given type
        for subtype in module_args[0:-1]:
            target_reg = target_reg.setdefault(subtype, {})
        target_reg.setdefault(module_args[-1], []).append(input)

    @classmethod
    def _real_register(cls, input_type: type, *args) -> Type:
        name_target = cls._names[input.__name__.lower()] = (input_type, set())

        if issubclass(input_type, Targeted):
            target = input_type.getTarget()
        else:
            target = None

        if issubclass(input_type, Searcher):
            module_type = module_base = Searcher
            module_args = ()
        else:
            module_type: Optional[Type] = None
            module_base: type = type(None)  # Silences pycharm

            if len(args) == 0:
                for i in input_type.__orig_bases__:
                    if module_type is not None:
                        raise TypeError(f"Type derived from multiple registrable base classes {i} and {module_type}")
                    module_base = get_origin(i)
                    if module_base not in cls._modules:
                        continue
                    module_type = i
            else:
                for i in cls._modules:
                    if not issubclass(input_type, i):
                        continue
                    if module_type is not None:
                        raise TypeError(f"Type derived from multiple registrable base classes {i} and {module_type}")
                    module_type = i

            if module_type is None:
                raise TypeError("No registrable base class")

            if len(args) == 0:
                cls._register_one(module_base, get_args(module_type))
            else:
                for module_args in args:
                    if isinstance(module_args, tuple):
                        cls._register_one(module_base, module_args)
                    else:
                        cls._register_one(module_base, (module_args,))

        name_target[1].add(module_type)

        if target is not None and issubclass(module_base, Targeted):
            cls._targets.setdefault(target, {}).setdefault(module_type, []).append(input_type)

        return input_type

    @classmethod
    def register(cls, *x):
        return lambda input_type: cls._real_register(input_type, *x)

    @classmethod
    def __getitem__(cls, i: type) -> Optional[Any]:
        target_type = get_origin(i)
        # Check if this is a non-generic type, and return the whole dict if it is
        if target_type is None:
            return cls._reg[i]

        target_subtypes = get_args(i)
        target_list = cls._reg.setdefault(target_type, {})
        for subtype in target_subtypes:
            target_list = target_list.setdefault(subtype, {})
        return target_list

    @classmethod
    def get_named(cls, name: str, type_constraint: Type = None) -> Any:
        ret = cls._names[name.lower()]
        if type_constraint and type_constraint not in ret[1]:
            raise TypeError(f"Type mismatch: wanted {type_constraint}, got {ret[1]}")
        return ret[0]

    @classmethod
    def get_targeted(
        cls, target: str, type_constraint: Type = None
    ) -> Optional[Union[Dict[Type, Set[Type]], Set[Type]]]:
        x = cls._targets.get(target)
        if x is None or type_constraint is None:
            return x
        return x.get(type_constraint)

    @classmethod
    def __str__(cls):
        return f"ciphey.iface.Registry {{_reg: {cls._reg}, _names: {cls._names}, _targets: {cls._targets}}}"


_fwd.registry = Registry
