from typing import Optional, Dict, Any, Set

from functools import lru_cache

import loguru

import ciphey
import cipheydists
from ciphey.iface import T, ParamSpec, Config

import json


class CipheyDists(ciphey.iface.ResourceLoader):
    # _wordlists: Set[str] = frozenset({"english", "english1000", "englishStopWords"})
    # _brandons: Set[str] = frozenset({"english"})
    # _dists: Set[str] = frozenset({"twist"})
    # _translates: Set[str] = frozenset({"morse"})
    _getters = {
        "list": cipheydists.get_list,
        "dist": cipheydists.get_dist,
        "brandon": cipheydists.get_brandon,
        "translate": cipheydists.get_translate
    }

    def whatResources(self) -> Optional[Set[str]]:
        pass

    @lru_cache
    def getResource(self, name: str) -> Any:
        loguru.logger.trace(f"Loading cipheydists resource {name}")
        prefix, name = name.split("::", 1)
        return self._getters[prefix](name)

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
        return T(json.load(self._paths[int(name) - 1]))

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
