from typing import Optional, Dict, Any, Set

from functools import lru_cache
import ciphey
import cipheydists
from ciphey.iface import T, ParamSpec, Config

import json


class CipheyDists(ciphey.iface.ResourceLoader):
    _wordlists: Set[str] = frozenset({"english", "english1000", "englishStopWords"})
    _brandons: Set[str] = frozenset({"english"})

    def whatResources(self) -> Set[str]:
        return self._wordlists | self._brandons

    @lru_cache
    def getResource(self, name: str) -> T:
        if name in self._wordlists:
            return cipheydists.get_list(name)
        elif name.startswith("brandon_") and name[len("brandon_"):] in self._brandons:
            return cipheydists.get_brandon(name[len("brandon_"):])

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass


ciphey.iface.registry.register(CipheyDists, ciphey.iface.ResourceLoader[ciphey.iface.WordList],  ciphey.iface.ResourceLoader[ciphey.iface.Dict])


# We can use a generic resource loader here, as we can instantiate it later
class Json(ciphey.iface.ResourceLoader):
    def whatResources(self) -> T:
        return self._names

    @lru_cache
    def getResource(self, name: str) -> T:
        return T(json.load(self._paths[int(name)]))

    @staticmethod
    def getName() -> str:
        return "json"

    @staticmethod
    def getParams() -> Optional[Dict[str, ciphey.iface.ParamSpec]]:
        return {
            "path": ParamSpec(req=True, desc="The path to the json file containing the wordlist", list=True)
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self._paths = self._params()["path"]
        self._names = set(range(0, len(self._paths) - 1))


ciphey.iface.registry.register(Json, ciphey.iface.ResourceLoader[ciphey.iface.WordList])
