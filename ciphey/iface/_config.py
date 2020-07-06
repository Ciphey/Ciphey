from abc import ABC, abstractmethod
from typing import (
    Any,
    Dict,
    Optional,
    List,
    TypeVar,
    Type,
    Union, Callable,
)
import pydoc

from loguru import logger

import datetime

from . import _registry_fwd


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


def split_resource_name(full_name: str) -> (str, str):
    return full_name.split("::", 1)


class Config:
    grep: bool = False
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

    def merge_dict(self, config_file: Dict[str, Any]):
        for a, b in config_file.items():
            self.update(a, b)
        pass

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

        if Registry.get_named(owner).getParams()[name].list:
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
        self.objs["format"] = {
            key: pydoc.locate(value) for key, value in self.format.items()
        }

        # Checkers do not depend on anything
        self.objs["checker"] = self(Registry.get_named(self.checker, Checker))
        # Searchers only depend on checkers
        self.objs["searcher"] = self(Registry.get_named(self.searcher, Searcher))

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
            logger.add(
                sink=sys.stderr, level=self.debug, colorize=False, format="{message}"
            )
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

    def __init__(self):
        self.update_log_level(self.debug)