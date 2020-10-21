from functools import lru_cache
from typing import Any, Dict, Optional, Set

import cipheydists
import loguru

from ciphey.iface import (
    Config,
    Distribution,
    ParamSpec,
    ResourceLoader,
    Translation,
    WordList,
    registry,
)


@registry.register_multi(WordList, Distribution, Translation)
class CipheyDists(ResourceLoader):
    # _wordlists: Set[str] = frozenset({"english", "english1000", "englishStopWords"})
    # _brandons: Set[str] = frozenset({"english"})
    # _dists: Set[str] = frozenset({"twist"})
    # _translates: Set[str] = frozenset({"morse"})
    _getters = {
        "list": cipheydists.get_list,
        "dist": cipheydists.get_dist,
        "brandon": cipheydists.get_brandon,
        "translate": cipheydists.get_translate,
    }

    def whatResources(self) -> Optional[Set[str]]:
        pass

    @lru_cache()
    def getResource(self, name: str) -> Any:
        loguru.logger.trace(f"Loading cipheydists resource {name}")
        prefix, name = name.split("::", 1)
        return self._getters[prefix](name)

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None
