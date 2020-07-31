import distutils
from abc import abstractmethod, ABC
import bisect
from copy import copy
from functools import lru_cache
from typing import Generic, List, Optional, Dict, Any, NamedTuple, Union, Set, Tuple, TypeVar
from ciphey.iface import (
    T,
    Cracker,
    Config,
    Searcher,
    ParamSpec,
    CrackInfo,
    registry,
    SearchLevel,
    CrackResult,
    SearchResult,
    Decoder,
    DecoderComparer,
    registry, Checker
)
from datetime import datetime
from loguru import logger
import cipheycore
from dataclasses import dataclass

"""
    We are using a tree structure here, because that makes searching and tracing back easier
    
    As such, when we encounter another possible parent, we remove that edge
"""


class DuplicateNode(Exception):
    pass


@dataclass
class AuSearchSuccessful(Exception):
    target: 'Node'
    info: str


@dataclass
class Node:
    # The root has no parent edge
    level: SearchLevel
    parent: Optional['Edge'] = None
    depth: int = 0

    @staticmethod
    def decoding(config: Config, route: Union[Cracker, Decoder], result: Any, source: 'Node') -> 'Node':
        if not config.cache.mark_ctext(result):
            raise DuplicateNode()

        checker: Checker = config.objs["checker"]
        target_type: type = config.objs["format"]["out"]
        ret = Node(parent=None,
                   level=SearchLevel(name=type(route).__name__.lower(), result=CrackResult(value=result)),
                   depth=source.depth + 1)
        edge = Edge(source=source, route=route, dest=ret)
        ret.parent = edge
        if type(result) == target_type:
            check_res = checker(result)
            if check_res is not None:
                raise AuSearchSuccessful(target=ret, info=check_res)
        return ret

    @staticmethod
    def cracker(config: Config, edge_template: 'Edge', result: CrackResult) -> 'Node':
        if not config.cache.mark_ctext(result.value):
            raise DuplicateNode()

        checker: Checker = config.objs["checker"]
        target_type: type = config.objs["format"]["out"]
        # Edges do not directly contain containers, so this is fine
        edge = copy(edge_template)
        ret = Node(parent=edge,
                   level=SearchLevel(name=type(edge.route).__name__.lower(), result=result),
                   depth=edge.source.depth + 1)
        edge.dest = ret
        if type(result.value) == target_type:
            check_res = checker(result.value)
            if check_res is not None:
                raise AuSearchSuccessful(target=ret, info=check_res)
        return ret

    def get_path(self):
        if self.parent is None:
            return [self.level]
        return self.parent.source.get_path() + [self.level]


def convert_edge_info(info: CrackInfo):
    return cipheycore.ausearch_edge(info.success_likelihood, info.success_runtime, info.failure_runtime)


@dataclass
class Edge:
    source: Node
    route: Union[Cracker, Decoder]
    dest: Optional[Node] = None
    # Info is not filled in for Decoders
    info: Optional[cipheycore.ausearch_edge] = None


PriorityType = TypeVar('PriorityType')


class PriorityWorkQueue(Generic[PriorityType, T]):
    _sorted_priorities: List[PriorityType]
    _queues: Dict[Any, List[T]]

    def add_work(self, priority: PriorityType, work: List[T]) -> None:
        idx = bisect.bisect_left(self._sorted_priorities, priority)
        if idx == len(self._sorted_priorities) or self._sorted_priorities[idx] != priority:
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
        best_priority = self._sorted_priorities.pop(0)
        return self._queues.pop(best_priority)

    def empty(self): return len(self._sorted_priorities) == 0

    def __init__(self):
        self._sorted_priorities = []
        self._queues = {}


@registry.register
class AuSearch(Searcher):
    # Deeper paths get done later
    work: PriorityWorkQueue[int, Edge]

    def get_crackers_for(self, t: type):
        return registry[Cracker[t]]

    @lru_cache()  # To save extra sorting
    def get_decoders_for(self, t: type):
        ret = [j for i in registry[Decoder][t].values() for j in i]
        ret.sort(key=lambda x: x.priority(), reverse=True)
        return ret

    # def expand(self, edge: Edge) -> List[Edge]:
    #     """Evaluates the destination of the given, and adds its child edges to the pool"""
    #     edge.dest = Node(parent=edge, level=edge.route(edge.source.level.result.value))

    def expand_crackers(self, node: Node) -> None:
        res = node.level.result.value

        additional_work = []

        for i in self.get_crackers_for(type(res)):
            inst = self._config()(i)
            additional_work.append(Edge(source=node, route=inst, info=convert_edge_info(inst.getInfo(res))))
        if self.disable_priority:
            priority = 0
        elif self.invert_priority:
            priority = -node.depth
        else:
            priority = node.depth

        self.work.add_work(priority, additional_work)

    def recursive_expand(self, node: Node) -> None:
        logger.trace(f"Expanding depth {node.depth} encodings")

        val = node.level.result.value

        for decoder in self.get_decoders_for(type(val)):
            inst = self._config()(decoder)
            res = inst(val)
            if res is None:
                continue
            try:
                new_node = Node.decoding(config=self._config(), route=inst, result=res, source=node)
            except DuplicateNode:
                continue

            logger.trace(f"Nesting encodings")
            self.recursive_expand(new_node)
            # Now we add the cracker edges
        # Doing this last allows us to catch nested encodings faster
        self.expand_crackers(node)

    def search(self, ctext: Any) -> Optional[SearchResult]:
        logger.add(sink=open("/tmp/foobar", "+w"), level="TRACE", colorize=True)
        logger.trace(f"""Beginning AuSearch with {"inverted" if self.invert_priority else "normal"} priority""")
        root = Node(parent=None, level=SearchLevel.input(ctext))

        if type(ctext) == self._config().objs["format"]["out"]:
            check_res = self._config().objs["checker"](ctext)
            if check_res is not None:
                return SearchResult(check_res=check_res, path=[root.level])

        try:
            self.recursive_expand(root)

            while True:
                if self.work.empty():
                    break
                # Get the highest level result
                chunk = self.work.get_work_chunk()
                infos = [i.info for i in chunk]
                # Work through all of this level's results
                while len(chunk) != 0:
                    logger.trace(f"{len(infos)} remaining on this level")
                    step_res = cipheycore.ausearch_minimise(infos)
                    edge: Edge = chunk.pop(step_res.index)
                    logger.trace(f"Weight is currently {step_res.weight} "
                                 f"when we pick {type(edge.route).__name__.lower()}")
                    del infos[step_res.index]

                    # Expand the node
                    res = edge.route(edge.source.level.result.value)
                    if res is None:
                        continue
                    for i in res:
                        try:
                            node = Node.cracker(config=self._config(), edge_template=edge, result=i)
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
        self._target_type: type = config.objs["format"]["out"]
        self.work = PriorityWorkQueue()  # Has to be defined here because of sharing
        self.invert_priority = bool(distutils.util.strtobool(self._params()["invert_priority"]))
        self.disable_priority = bool(distutils.util.strtobool(self._params()["disable_priority"]))

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "invert_priority": ParamSpec(req=False,
                                         desc="Causes more complex encodings to be looked at first. "
                                              "Good for deeply buried encodings.",
                                         default="False"),
            "disable_priority": ParamSpec(req=False,
                                         desc="Disables the priority queue altogether. "
                                              "May be much faster, but will take *very* odd paths",
                                         default="False")
        }
#
# @registry.register
# class AuSearch(Searcher):
#     def findBestNode(self, nodes: List[Node]) -> Node:
#         res: cipheycore.ausearch_res = cipheycore.ausearch_minimise([i.node_info for i in nodes])
#         ret = nodes[res.index]
#         logger.trace(f"Selected node {ret} with weight {res.weight}")
#         return ret
#
#     def handleDecodings(
#         self, parents: List[SearchLevel]
#     ) -> List[List[SearchLevel]]:
#         """
#             If there exists a decoding that the checker returns true on, returns (True, result).
#             Otherwise, returns (False, names and successful decodings)
#
#             The CrackResult object should only have the value field filled in
#
#             MUST NOT recurse into decodings! evaluate does that for you!
#         """
#         target = parents[-1].result.value
#         ret = []
#
#         decoders = []
#
#         for decoder_type, decoder_class in registry[Decoder][type(target)].items():
#             for decoder in decoder_class:
#                 decoders.append(DecoderComparer(decoder))
#         # Fun fact:
#         #     with Python's glorious lists, inserting n elements into the right position (with bisect) is O(n^2)
#         decoders.sort(reverse=True)
#
#         for decoder_cmp in decoders:
#             logger.trace(f"Inspecting {decoder_cmp}")
#             res = self._config()(decoder_cmp.value).decode(target)
#             if res is None:
#                 continue
#             level = SearchLevel(
#                 name=decoder_cmp.value.__name__.lower(),
#                 result=CrackResult(value=res),
#             )
#             if type(res) == self._final_type:
#                 check_res = self._checker(res)
#                 if check_res is not None:
#                     raise AuSearchSuccessful(parents)
#             ret.append(parents + [level])
#         return ret
#
#     def expand_decodings(self, parents: List[SearchLevel]) -> List[List[SearchLevel]]:
#         dec_res = self.handleDecodings(parents)
#         # Otherwise we go further into the decodings
#
#         ret = []
#
#         for decoding in dec_res:
#             if self._config().cache.mark_ctext(decoding[-1].result.value):
#                 ret += self.expand_decodings(decoding)
#
#         return ret
#
#     def expand(self, parents: List[SearchLevel], check: bool = True) -> List[Node]:
#         result = parents[-1].result.value
#         # logger.debug(f"Expanding {parents}")
#
#         # Deduplication
#         if not self._config().cache.mark_ctext(result):
#             return []
#
#         # We recurse into decodings *only*, as nested ciphers cause unnecessary headaches
#         decodings = self.expand_decodings(parents)
#
#         success, dec_res = self.handleDecodings(result)
#         if success:
#             return True, SearchResult(path=parents + [dec_res[0]], check_res=dec_res[1])
#
#         nodes: List[Node] = []
#
#         for decoding in dec_res:
#             # Don't check, as handleDecodings did that for us
#             success, eval_res = self.expand(parents + [decoding], check=False)
#             if success:
#                 return True, eval_res
#             nodes.extend(eval_res)
#
#         crackers: List[Cracker] = registry[Cracker[type(result)]]
#         expected_time: float
#
#         # Worth doing this check twice to simplify code and allow a early return for decodings
#         if type(result) == self._final_type:
#             expected_time = self._checker.getExpectedRuntime(result)
#         else:
#             expected_time = 0
#         for i in crackers:
#             cracker = self._config()(i)
#             crack_info: CrackInfo = cracker.getInfo(result)
#             nodes.append(
#                 Node(
#                     cracker=cracker,
#                     node_info=cipheycore.ausearch_node(crack_info.success_likelihood, crack_info.success_runtime,
#                                                        crack_info.failure_runtime),
#                     parents=parents,
#                 )
#             )
#
#         return False, nodes
#
#     def evaluate(self, node: Node) -> (bool, Union[List[SearchLevel], List[Node]]):
#         # logger.debug(f"Evaluating {node}")
#
#         res = node.cracker.attemptCrack(node.parents[-1].result.value)
#         # Detect if we succeeded, and if deduplication is needed
#         logger.trace(f"Got {len(res)} results")
#
#         ret = []
#         for i in res:
#             success, res = self.expand(
#                 node.parents
#                 + [SearchLevel(name=type(node.cracker).__name__.lower(), result=i)]
#             )
#             if success:
#                 return True, res
#             ret.extend(res)
#
#         return False, ret
#
#     def search(self, ctext: Any) -> List[SearchLevel]:
#         deadline = (
#             datetime.now() + self._config().objs["timeout"]
#             if self._config().timeout is not None
#             else datetime.max
#         )
#
#         success, expand_res = self.expand(
#             [SearchLevel(name="input", result=CrackResult(value=ctext))]
#         )
#         if success:
#             return expand_res
#
#         nodes = expand_res
#
#         while datetime.now() < deadline:
#             # logger.trace(f"Have node tree {nodes}")
#
#             if len(nodes) == 0:
#                 raise LookupError("Could not find any solutions")
#
#             best_node = self.findBestNode(nodes)
#
#             logger.trace(best_node)
#
#             nodes.remove(best_node)
#             success, eval_res = self.evaluate(best_node)
#             if success:
#                 # logger.trace(f"Success with node {best_node}")
#                 return eval_res
#             nodes += eval_res
#             logger.trace(f"AAA {nodes}")
#
#         raise TimeoutError("Search ran out of time")
#
#     @staticmethod
#     def getParams() -> Optional[Dict[str, ParamSpec]]:
#         pass
#
#     def __init__(self, config: Config):
#         super().__init__(config)
#         self._checker = config.objs["checker"]
#         self._final_type = config.objs["format"]["out"]
