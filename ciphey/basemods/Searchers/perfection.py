from abc import abstractmethod
from typing import Set, Any, Union, List, Optional, Dict, Tuple

from loguru import logger

from .ausearch import Node, AuSearch
from ciphey.iface import (
    SearchLevel,
    Config,
    Registry,
    CrackResult,
    Searcher,
    ParamSpec,
    Decoder,
    DecoderComparer,
)

import bisect


@Registry.register
class Perfection(AuSearch):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def findBestNode(self, nodes: Set[Node]) -> Node:
        return next(iter(nodes))

    def __init__(self, config: Config):
        super().__init__(config)
