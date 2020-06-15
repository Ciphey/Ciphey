from typing import Optional, Dict, Any, Set

from functools import lru_cache
import ciphey
import cipheydists
from ciphey.iface import T, ParamSpec, Config

import json


class CipheyDistsWordLists(ciphey.iface.ResourceLoader[ciphey.iface.WordList]):
    _names: Set[str] = {"english", "english1000"}

    def what_resources(self) -> Set[str]:
        return self._names

    @lru_cache
    def get_resource(self, name: str) -> T:
        x = cipheydists.get_list(name)
        return cipheydists.get_list(name)

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getName() -> str:
        return "cipheydists"


ciphey.iface.registry.register(CipheyDistsWordLists, ciphey.iface.ResourceLoader[ciphey.iface.WordList])


# We can use a generic resource loader here, as we can instantiate it later
class Json(ciphey.iface.ResourceLoader):
    def what_resources(self) -> T:
        return self._names

    @lru_cache
    def get_resource(self, name: str) -> T:
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
