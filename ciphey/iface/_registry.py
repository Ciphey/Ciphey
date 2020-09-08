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
    _modules = {Checker, Cracker, Decoder, ResourceLoader, Searcher, PolymorphicChecker}

    def _register_one(self, input_type, module_base, module_args):
        if len(module_args) == 0:
            self._reg.setdefault(module_base, []).append(input_type)
            return

        target_reg = self._reg.setdefault(module_base, {})
        # Seek to the given type
        for subtype in module_args[0:-1]:
            target_reg = target_reg.setdefault(subtype, {})
        target_reg.setdefault(module_args[-1], []).append(input_type)

    def _real_register(self, input_type: type, *args) -> Type:
        name = input_type.__name__.lower()
        name_target = self._names[name] = (input_type, set())

        if issubclass(input_type, Targeted):
            target = input_type.getTarget()
        else:
            target = None

        if issubclass(input_type, Searcher):
            module_type = module_base = Searcher
            module_args = ()
        else:
            module_type: Optional[Type] = None
            module_base = None

            # Work out what module type this is
            if len(args) == 0 and hasattr(input_type, "__orig_bases__"):
                for i in input_type.__orig_bases__:
                    if module_type is not None:
                        raise TypeError(
                            f"Type derived from multiple registrable base classes {i} and {module_type}"
                        )
                    module_base = get_origin(i)
                    if module_base not in self._modules:
                        continue
                    module_type = i
            else:
                for i in self._modules:
                    if not issubclass(input_type, i):
                        continue
                    if module_type is not None:
                        raise TypeError(
                            f"Type derived from multiple registrable base classes {i} and {module_type}"
                        )
                    module_type = i
            if module_type is None:
                raise TypeError("No registrable base class")

            # Replace input type with polymorphic checker if required
            if issubclass(input_type, Checker):
                if len(args) == 0:
                    arg = [get_args(i) for i in input_type.__orig_bases__ if get_origin(i) == Checker][0]
                    if len(arg) != 1:
                        raise TypeError(f"No argument for Checker")
                    input_type = input_type.convert({arg[0]})
                else:
                    input_type = input_type.convert(set(args))
                self._register_one(input_type, PolymorphicChecker, [])
                # Refresh the names with the new type
                name_target = self._names[name] = (input_type, {PolymorphicChecker})

            # Now handle the difference between register and register_multi
            if len(args) == 0:
                if module_type is PolymorphicChecker:
                    module_base = PolymorphicChecker
                elif module_base is None:
                    raise TypeError("No type argument given")
                self._register_one(input_type, module_base, get_args(module_type))
                name_target[1].add(module_base)
            else:
                if module_base is not None:
                    raise TypeError(f"Redundant type argument for {module_type}")
                module_base = module_type
                for module_args in args:
                    # Correct missing brackets
                    if not isinstance(module_args, tuple):
                        module_args = (module_args,)

                    self._register_one(input_type, module_base, module_args)
                    name_target[1].add(module_type[module_args])

        name_target[1].add(module_type)

        if target is not None and issubclass(module_base, Targeted):
            self._targets.setdefault(target, {}).setdefault(module_type, []).append(
                input_type
            )

        return input_type

    def register(self, input_type):
        return self._real_register(input_type)

    def register_multi(self, *x):
        return lambda input_type: self._real_register(input_type, *x)

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

    def get_targeted(
        self, target: str, type_constraint: Type = None
    ) -> Optional[Union[Dict[Type, Set[Type]], Set[Type]]]:
        x = self._targets.get(target)
        if x is None or type_constraint is None:
            return x
        return x.get(type_constraint)

    def get_all_names(self) -> List[str]:
        return list(self._names.keys())

    def __str__(self):
        return f"ciphey.iface.Registry {{_reg: {self._reg}, _names: {self._names}, _targets: {self._targets}}}"


_fwd.registry = Registry()
