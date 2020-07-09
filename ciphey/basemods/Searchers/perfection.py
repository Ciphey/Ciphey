from abc import abstractmethod
from typing import Set, Any, Union, List, Optional, Dict, Tuple

from loguru import logger

from .ausearch import Node, AuSearch
from ciphey.iface import (
    SearchLevel,
    Config,
    registry,
    CrackResult,
    Searcher,
    ParamSpec,
    Decoder,
    DecoderComparer,
)

import bisect

import cipheycore


@registry.register
class Perfection(AuSearch):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def findBestNode(self, nodes: List[Node]) -> Node:
        trans_nodes = []
        for node in nodes:
            info = node.cracker.getInfo(node.parents[-1].result.value)
            trans_nodes.append(cipheycore.ausearch_node(info.success_likelihood,
                                                        info.success_runtime, info.failure_runtime))
        ret = nodes[cipheycore.ausearch_minimise(trans_nodes)]
        logger.debug(f"Selected {ret}")
        return ret

    def __init__(self, config: Config):
        super().__init__(config)
