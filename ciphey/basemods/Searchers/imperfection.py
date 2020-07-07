from abc import abstractmethod
from typing import Set, Any, Union, List, Optional, Dict, Tuple
import heapq

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


@registry.register
class Imperfection(AuSearch):
    """The default search module for Ciphey

    Called imperfection because ironically it is pretty perfect.

    """

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    def findBestNode(self, nodes: Set[Node]) -> Node:
        return next(iter(nodes))

    def __init__(self, config: Config):
        super().__init__(config)

    def aStar(graph, current, end):
        """The A* search algorithm
        """
        openSet = set()
        openHeap = []
        closedSet = set()

        def retracePath(c):
            path = [c]
            while c.parent is not None:
                c = c.parent
                path.append(c)
            path.reverse()
            return path

        openSet.add(current)
        openHeap.append((0, current))
        while openSet:
            current = heapq.heappop(openHeap)[1]
            if current == end:
                return retracePath(current)
            openSet.remove(current)
            closedSet.add(current)
            for tile in graph[current]:
                if tile not in closedSet:
                    tile.H = (abs(end.x - tile.x) + abs(end.y - tile.y)) * 10
                    if tile not in openSet:
                        openSet.add(tile)
                        heapq.heappush(openHeap, (tile.H, tile))
                    tile.parent = current
        return []
