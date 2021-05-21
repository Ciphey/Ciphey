import bisect
import distutils
import math
from copy import copy
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from sys import float_info

from loguru import logger

from ciphey.iface import (
    Checker,
    Config,
    Cracker,
    CrackInfo,
    CrackResult,
    Decoder,
    ParamSpec,
    Searcher,
    SearchLevel,
    SearchResult,
    T,
    registry,
)

"""
We are using a tree structure here, because that makes searching and tracing back easier
As such, when we encounter another possible parent, we remove that edge
"""


class DuplicateNode(Exception):
    pass


@dataclass
class AuSearchSuccessful(Exception):
    target: "Node"
    info: str


@dataclass
class Node:
    # The root has no parent edge
    level: SearchLevel
    parent: Optional["Edge"] = None
    depth: int = 0

    @staticmethod
    def decoding(
        config: Config, route: Union[Cracker, Decoder], result: Any, source: "Node"
    ) -> "Node":
        if not config.cache.mark_ctext(result):
            raise DuplicateNode()

        checker: Checker = config.objs["checker"]
        ret = Node(
            parent=None,
            level=SearchLevel(
                name=type(route).__name__.lower(), result=CrackResult(value=result)
            ),
            depth=source.depth + 1,
        )
        edge = Edge(source=source, route=route, dest=ret)
        ret.parent = edge
        check_res = checker(result)
        if check_res is not None:
            raise AuSearchSuccessful(target=ret, info=check_res)
        return ret

    @staticmethod
    def cracker(config: Config, edge_template: "Edge", result: CrackResult) -> "Node":
        if not config.cache.mark_ctext(result.value):
            raise DuplicateNode()

        checker: Checker = config.objs["checker"]
        # Edges do not directly contain containers, so this is fine
        edge = copy(edge_template)
        ret = Node(
            parent=edge,
            level=SearchLevel(name=type(edge.route).__name__.lower(), result=result),
            depth=edge.source.depth + 1,
        )
        edge.dest = ret
        check_res = checker(result.value)
        if check_res is not None:
            raise AuSearchSuccessful(target=ret, info=check_res)
        return ret

    @staticmethod
    def root(config: Config, ctext: Any):
        if not config.cache.mark_ctext(ctext):
            raise DuplicateNode()

        return Node(parent=None, level=SearchLevel.input(ctext))

    def get_path(self):
        if self.parent is None:
            return [self.level]
        return self.parent.source.get_path() + [self.level]

@dataclass
class AusearchEdge:
    # TODO: This is just CrackInfo with failure probability added...
    success_probability: float
    failure_probability: float
    success_time: float
    failure_time: float

    def __init__(self, success_probability, success_time, failure_time):
        self.success_probability = success_probability
        self.failure_probability = 1.0 - success_probability
        self.success_time = success_time
        self.failure_time = failure_time

@dataclass
class AusearchResult:
    weight: float
    index: int

def convert_edge_info(info: CrackInfo):
    return 1

# Equivalent to CPP ausearch_minimise
def minimise_edges(edges) -> AusearchResult: 
    weight = minimise_edges_impl(edges)
    index = len(edges) # TODO: Is this ever different? C++ code seems to just count the number of elements...but in a really cursed way
    return AusearchResult(weight, index)

# Equivalent to cpp minimise_edges
def minimise_edges_impl(edges) -> float:
    num_edges = len(edges)
    if num_edges == 0:
        return float('NaN')
    elif num_edges == 1:
        return calculate_weight(edges)

    # NOTE: Comment originally from C++ code. 
    # TODO: Validate if this is actually true or not in Python
    # It turns out that it is faster to optimise for antiweight (weight in reverse)
    #
    # This is because weight is iteratively calculated from the end, 
    # and most machines run faster when iterating *forwards*

    # First, we calculate a lower bound on the weight
    weight = 0.0
    old_weight = calculate_antiweight(edges)
    while True:
        remaining_weight = old_weight

        # Now, iterating down the edge list, trying to find the minimising value
        for current_pos, _ in enumerate(edges[:-1]):
            max_remaining_weight = float_info.min
            max_pos = -1

            for i, target in enumerate(edges[current_pos:]):
                edge_remaining_weight = remaining_weight
                # We didn't succeed
                edge_remaining_weight -= (target.success_probability * target.success_time)
                # Expand the rest of the weight
                if (target.failure_probability == 0):
                    # If we cannot fail, then there can be no remaining antiweight
                    edge_remaining_weight = 0
                else:
                    edge_remaining_weight /= target.failure_probability
                
                if edge_remaining_weight > max_remaining_weight:
                    max_remaining_weight = edge_remaining_weight
                    max_pos = i
            
            # Swap edges[current_pos] with edges[max]
            edges[current_pos], edges[max_pos] = edges[max_pos], edges[current_pos]
            remaining_weight = max_remaining_weight
        
        weight = calculate_antiweight(edges)

        while True:
            tmp_weight = weight

            for pos, _ in enumerate(edges[:-2]):
                brute_edges(edges, pos)
            
            weight = brute_edges(edges, len(edges)-2)
            if (weight == tmp_weight):
                # No progress made; exit the loop
                break

        if weight == old_weight:
            # No progress made; exit the loop
            break
        
        old_weight = weight
    
    # antiweight -> weight
    edges.reverse()
    return calculate_weight(edges)

def calculate_weight(edges):
    weight = 0.0
    for edge in reversed(edges):
        weight = (edge.success_probability * edge.success_time) + ((edge.failure_probability) * (edge.failure_time + weight))
    return weight

def calculate_antiweight(edges):
    # Original comment from C++ code: "Iterating forward is *way* faster"
    # TODO: Verify that this actually applies in Python
    weight = 0.0
    for edge in edges:
        weight = (edge.success_probability * edge.success_time) + ((edge.failure_probability) * (edge.failure_time + weight))
    return weight

def brute_edges(edges, target: int):
    best_weight = calculate_antiweight(edges)
    # Triangle swaps
    for i in range(target+1, len(edges)):
        edges[i], edges[target] = edges[target], edges[i]
        new_weight = calculate_antiweight(edges)

        if new_weight < best_weight:
            best_weight = new_weight
        else:
            # Swap back
            edges[i], edges[target] = edges[target], edges[i]

    return best_weight


@dataclass
class Edge:
    source: Node
    route: Union[Cracker, Decoder]
    dest: Optional[Node] = None
    # Info is not filled in for Decoders



PriorityType = TypeVar("PriorityType")


class PriorityWorkQueue(Generic[PriorityType, T]):
    _sorted_priorities: List[PriorityType]
    _queues: Dict[Any, List[T]]

    def add_work(self, priority: PriorityType, work: List[T]) -> None:
        logger.trace(f"""Adding work at depth {priority}""")

        idx = bisect.bisect_left(self._sorted_priorities, priority)
        if (
            idx == len(self._sorted_priorities)
            or self._sorted_priorities[idx] != priority
        ):
            self._sorted_priorities.insert(idx, priority)
        self._queues.setdefault(priority, []).extend(work)

    def get_work(self) -> T:
        best_priority = self._sorted_priorities[0]
        target = self._queues[best_priority]
        ret = target.pop(0)
        if len(target) == 0:
            self._sorted_priorities.pop()
        return ret

    def get_work_chunk(self) -> List[T]:
        """Returns the best work for now"""
        if len(self._sorted_priorities) == 0:
            return []
        best_priority = self._sorted_priorities.pop(0)
        return self._queues.pop(best_priority)

    def empty(self):
        return len(self._sorted_priorities) == 0

    def __init__(self):
        self._sorted_priorities = []
        self._queues = {}


@registry.register
class AuSearch(Searcher):
    # Deeper paths get done later
    work: PriorityWorkQueue[int, Edge]

    @staticmethod
    def get_crackers_for(t: type):
        return registry[Cracker[t]]

    @lru_cache()  # To save extra sorting
    def get_decoders_for(self, t: type):
        ret = registry[Decoder[t]]
        ret.sort(key=lambda x: x.priority(), reverse=True)
        return ret

    # def expand(self, edge: Edge) -> List[Edge]:
    #     """Evaluates the destination of the given, and adds its child edges to the pool"""
    #     edge.dest = Node(parent=edge, level=edge.route(edge.source.level.result.value))

    def expand_crackers(self, node: Node) -> None:
        if node.depth >= self.max_cipher_depth:
            return

        res = node.level.result.value
        additional_work = []

        for i in self.get_crackers_for(type(res)):
            inst = self._config()(i)
            additional_work.append(
                Edge(source=node, route=inst)
            )
        priority = min(node.depth, self.priority_cap)
        if self.invert_priority:
            priority = -priority

        self.work.add_work(priority, additional_work)

    def expand_decodings(self, node: Node) -> None:
        val = node.level.result.value

        for decoder in self.get_decoders_for(type(val)):
            inst = self._config()(decoder)
            res = inst(val)
            if res is None:
                continue
            try:
                new_node = Node.decoding(
                    config=self._config(), route=inst, result=res, source=node
                )
            except DuplicateNode:
                continue

            logger.trace("Nesting encodings")
            self.recursive_expand(new_node, False)

    def recursive_expand(self, node: Node, nested: bool = True) -> None:
        if node.depth >= self.max_depth:
            return

        logger.trace(f"Expanding depth {node.depth}")

        self.expand_decodings(node)

        # Doing this last allows us to catch simple nested encodings faster
        if not nested or self.enable_nested:
            self.expand_crackers(node)

    def search(self, ctext: Any) -> Optional[SearchResult]:
        logger.trace(
            f"""Beginning AuSearch with {"inverted" if self.invert_priority else "normal"} priority"""
        )

        try:
            root = Node.root(self._config(), ctext)
        except DuplicateNode:
            return None

        check_res = self._config().objs["checker"](ctext)
        if check_res is not None:
            return SearchResult(check_res=check_res, path=[root.level])

        try:
            self.recursive_expand(root, False)

            while True:
                if self.work.empty():
                    break
                # Get the highest level result
                chunk = self.work.get_work_chunk()
                # Work through all of this level's results
                while len(chunk) != 0:
                    max_depth = 0
                    for i in chunk:
                        if i.source.depth > max_depth:
                            max_depth = i.source.depth
                    logger.debug(f"At depth {chunk[0].source.depth}")

                    # if self.disable_priority:
                    #     chunk += self.work.get_work_chunk()
                    #     infos = [i.info for i in chunk]

                    step_res = 0.1
                    edge: Edge = chunk.pop(0)
                    logger.trace(
                        f"Weight is currently {0} "
                        f"when we pick {type(edge.route).__name__.lower()} "
                        f"with depth {edge.source.depth}"
                    )

                    # Expand the node
                    res = edge.route(edge.source.level.result.value)
                    if res is None:
                        continue
                    for i in res:
                        try:
                            node = Node.cracker(
                                config=self._config(), edge_template=edge, result=i
                            )
                            self.recursive_expand(node)
                        except DuplicateNode:
                            continue

        except AuSearchSuccessful as e:
            logger.debug("AuSearch succeeded")
            return SearchResult(path=e.target.get_path(), check_res=e.info)

        logger.debug("AuSearch failed")

    def __init__(self, config: Config):
        super().__init__(config)
        self._checker: Checker = config.objs["checker"]
        self.work = PriorityWorkQueue()  # Has to be defined here because of sharing
        self.invert_priority = bool(
            distutils.util.strtobool(self._params()["invert_priority"])
        )
        self.priority_cap = int(self._params()["priority_cap"])
        self.enable_nested = bool(
            distutils.util.strtobool(self._params()["enable_nested"])
        )
        self.max_cipher_depth = int(self._params()["max_cipher_depth"])
        if self.max_cipher_depth == 0:
            self.max_cipher_depth = math.inf
        self.max_depth = int(self._params()["max_depth"])
        if self.max_depth == 0:
            self.max_depth = math.inf

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "enable_nested": ParamSpec(
                req=False,
                desc="Enables nested ciphers. "
                "Incredibly slow, and not guaranteed to terminate",
                default="False",
            ),
            "invert_priority": ParamSpec(
                req=False,
                desc="Causes more complex encodings to be looked at first. "
                "Good for deeply buried encodings.",
                default="False",
            ),
            "max_cipher_depth": ParamSpec(
                req=False,
                desc="The depth at which we stop trying to crack ciphers. "
                "Set to 0 to disable",
                default="0",
            ),
            "max_depth": ParamSpec(
                req=False,
                desc="The depth at which we give up. " "Set to 0 to disable",
                default="0",
            ),
            "priority_cap": ParamSpec(
                req=False,
                desc="Sets the maximum depth before we give up ordering items.",
                default="2",
            ),
        }