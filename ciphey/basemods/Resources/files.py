import csv
import json
from functools import lru_cache
from typing import Dict, Generic, Optional, Set

from ciphey.iface import (
    Config,
    Distribution,
    ParamSpec,
    ResourceLoader,
    T,
    WordList,
    registry,
)


# We can use a generic resource loader here, as we can instantiate it later
@registry.register_multi(WordList, Distribution)
class Json(ResourceLoader):
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
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {"path": ParamSpec(req=True, desc="The path to a JSON file", list=True)}

    def __init__(self, config: Config):
        super().__init__(config)
        self._paths = self._params()["path"]
        self._names = set(range(1, len(self._paths)))


# We can use a generic resource loader here, as we can instantiate it later
@registry.register_multi(WordList, Distribution)
class Csv(Generic[T], ResourceLoader[T]):
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
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {"path": ParamSpec(req=True, desc="The path to a CSV file", list=True)}

    def __init__(self, config: Config):
        super().__init__(config)
        self._paths = self._params()["path"]
        self._names = set(range(1, len(self._paths)))
