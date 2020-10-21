from typing import Dict, Optional, Set

from ciphey.iface import Config, ParamSpec, registry

from .ausearch import AuSearch, Node


@registry.register
class Perfection(AuSearch):
    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    def findBestNode(self, nodes: Set[Node]) -> Node:
        return next(iter(nodes))

    def __init__(self, config: Config):
        super().__init__(config)
