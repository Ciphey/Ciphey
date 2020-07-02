from abc import abstractmethod
from typing import Set, Any, Union, List, Optional, Dict

from loguru import logger

from .ausearch import Node, AuSearch
from ciphey.iface import SearchLevel, Config, registry, CrackResult, Searcher, ParamSpec, Decoder, get_args


class Perfection(AuSearch):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def findBestNode(self, nodes: Set[Node]) -> Node: return next(iter(nodes))

    def handleDecodings(self, target: Any) -> (bool, Union[SearchLevel, List[SearchLevel]]):
        ret = []

        for decoder_type, decoder_class in registry[Decoder][type(target)].items():
            for decoder in decoder_class:
                res = self._config()(decoder).decode(target)
                if res is None:
                    continue
                level = SearchLevel(
                    name=decoder.__name__.lower(),
                    result=CrackResult(value=res)  # FIXME: CrackResult[decoder_type]
                )
                if type(res) == self._final_type:
                    logger.trace(f"checker returned {self._checker(res)}")
                if type(res) == self._final_type and self._checker(res):
                    return True, level
                ret.append(level)
        return False, ret

    def __init__(self, config: Config):
        super().__init__(config)
        self._checker = self._config().objs["checker"]
        self._final_type = config.objs["format"]["out"]


registry.register(Perfection, Searcher)