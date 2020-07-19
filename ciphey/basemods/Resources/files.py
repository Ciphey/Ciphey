from abc import abstractmethod
from typing import Optional, Dict, Any, Set, Generic, Type

from functools import lru_cache

import ciphey
from ciphey.iface import T, ParamSpec, Config, get_args, registry

import json
import csv


# We can use a generic resource loader here, as we can instantiate it later
@registry.register_multi(ciphey.iface.WordList, ciphey.iface.Distribution)
class Json(ciphey.iface.ResourceLoader):
    def whatResources(self) -> T:
        return self._names

    @lru_cache()
    def getResource(self, name: str) -> T:
        prefix, name = name.split("::", 1)
        return {"wordlist": (lambda js: {js}), "dist": (lambda js: js)}[prefix](
            json.load(open(self._paths[int(name) - 1]))
        )

    @staticmethod
    def getName() -> str:
        return "json"

    @staticmethod
    def getParams() -> Optional[Dict[str, ciphey.iface.ParamSpec]]:
        return {"path": ParamSpec(req=True, desc="The path to a JSON file", list=True)}

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self._paths = self._params()["path"]
        self._names = set(range(1, len(self._paths)))


# We can use a generic resource loader here, as we can instantiate it later
@registry.register_multi(ciphey.iface.WordList, ciphey.iface.Distribution)
class Csv(Generic[T], ciphey.iface.ResourceLoader[T]):
    def whatResources(self) -> Set[str]:
        return self._names

    @lru_cache()
    def getResource(self, name: str) -> T:
        prefix, name = name.split("::", 1)
        return {
            "wordlist": (lambda reader: {i[0] for i in reader}),
            "dist": (lambda reader: {i[0]: float(i[1]) for i in reader}),
        }[prefix](csv.reader(open(self._paths[int(name) - 1])))

    @staticmethod
    def getName() -> str:
        return "csv"

    @staticmethod
    def getParams() -> Optional[Dict[str, ciphey.iface.ParamSpec]]:
        return {"path": ParamSpec(req=True, desc="The path to a CSV file", list=True)}

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self._paths = self._params()["path"]
        self._names = set(range(1, len(self._paths)))
