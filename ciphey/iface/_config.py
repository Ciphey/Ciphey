import os
from abc import ABC, abstractmethod
from typing import (
    Any,
    Dict,
    Optional,
    List,
    Type,
    Union, Callable,
)
import pydoc

from loguru import logger

import datetime

import yaml
import appdirs

from . import _fwd
from ._modules import Checker, Searcher, ResourceLoader


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
    verbosity: int = 0
    searcher: str = "perfection"
    params: Dict[str, Dict[str, Union[str, List[str]]]] = {}
    format: Dict[str, str] = {"in": "str", "out": "str"}
    modules: List[str] = []
    checker: str = "brandon"
    default_dist: str = "cipheydists::dist::twist"
    timeout: Optional[int] = None

    _inst: Dict[type, Any] = {}
    objs: Dict[str, Any] = {}
    cache: Cache = Cache()

    @staticmethod
    def get_default_dir() -> str:
        return appdirs.user_config_dir("ciphey")

    def merge_dict(self, config_file: Optional[Dict[str, Any]]):
        if config_file is None:
            return
        for a, b in config_file.items():
            self.update(a, b)

    def load_file(self, path: str = os.path.join(get_default_dir.__func__(), "config.yml"), create=False):
        try:
            with open(path, "r+") as file:
                return self.merge_dict(yaml.safe_load(file))
        except FileNotFoundError:
            if create:
                open(path, "w+")

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

        if _fwd.registry.get_named(owner).getParams()[name].list:
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
        self.objs["checker"] = self(_fwd.registry.get_named(self.checker, Checker))
        # Searchers only depend on checkers
        self.objs["searcher"] = self(_fwd.registry.get_named(self.searcher, Searcher))

    def update_log_level(self, verbosity: Optional[int]):
        if verbosity is None:
            return
        self.verbosity = verbosity
        quiet_list = [
            "ERROR",
            "CRITICAL",
        ]
        loud_list = [
            "DEBUG",
            "TRACE"
        ]
        verbosity_name: str
        if verbosity == 0:
            verbosity_name = "WARNING"
        elif verbosity >= 0:
            verbosity_name = loud_list[min(len(loud_list), verbosity) - 1]
        else:
            verbosity_name = quiet_list[min(len(quiet_list), -verbosity) - 1]

        from loguru import logger
        import sys

        logger.remove()
        if self.verbosity is None:
            return
        logger.configure()
        if self.verbosity > 0:
            logger.add(sink=sys.stderr, level=verbosity_name, colorize=sys.stderr.isatty())
            logger.opt(colors=True)
        else:
            logger.add(
                sink=sys.stderr, level=verbosity_name, colorize=False, format="{message}"
            )
        logger.debug(f"Verbosity set to level {verbosity} ({verbosity_name})")

    def load_modules(self):
        import importlib.util

        for i in self.modules:
            spec = importlib.util.spec_from_file_location("ciphey.module_load_site", i)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

        logger.debug(f"Loaded modules {_fwd.registry.get_all_names()}")

    # Does all the loading and filling

    def complete_config(self):
        self.load_modules()
        self.load_objs()
        self.update_log_level(self.verbosity)

    def get_resource(self, res_name: str, t: Optional[Type] = None) -> Any:
        logger.trace(f"Loading resource {res_name} of type {t}")

        # FIXME: Actually returns obj of type `t`, but python is bad
        loader, name = split_resource_name(res_name)
        if t is None:
            return self(_fwd.registry.get_named(loader, ResourceLoader))(name)
        else:
            return self(_fwd.registry.get_named(loader, ResourceLoader[t]))(name)

    def __str__(self):
        return str({
            "verbosity": self.verbosity,
            "searcher": self.searcher,
            "params": self.params,
            "format": self.format,
            "modules": self.modules,
            "checker": self.checker,
            "default_dist": self.default_dist,
            "timeout": self.timeout
        })


_fwd.config = Config
