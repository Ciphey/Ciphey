from abc import abstractmethod, ABC
from typing import Generic, List, Optional, Dict, Any, NamedTuple, Union, Set, Tuple
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
)
from datetime import datetime
from loguru import logger


class Node(Generic[T], NamedTuple):
    cracker: Cracker
    parents: List[SearchLevel]
    crack_info: CrackInfo
    check_info: float

    def __hash__(self):
        return hash((type(self.cracker).__name__, len(self.parents)))


class AuSearch(Searcher, ABC):
    @abstractmethod
    def findBestNode(self, nodes: Set[Node]) -> Node:
        pass

    def handleDecodings(
        self, target: Any
    ) -> (bool, Union[Tuple[SearchLevel, str], List[SearchLevel]]):
        """
            If there exists a decoding that the checker returns true on, returns (True, result).
            Otherwise, returns (False, names and successful decodings)

            The CrackResult object should only have the value field filled in

            MUST NOT recurse into decodings! evaluate does that for you!
        """
        # This tag is necessary, as we could have a list as a decoding target, which would then screw over type checks
        ret = []

        decoders = []

        for decoder_type, decoder_class in registry[Decoder][type(target)].items():
            for decoder in decoder_class:
                decoders.append(DecoderComparer(decoder))
        # Fun fact:
        #     with Python's glorious lists, inserting n elements into the right position (with bisect) is O(n^2)
        decoders.sort(reverse=True)

        for decoder_cmp in decoders:
            logger.trace(f"Inspecting {decoder_cmp}")
            res = self._config()(decoder_cmp.value).decode(target)
            if res is None:
                continue
            level = SearchLevel(
                name=decoder_cmp.value.__name__.lower(),
                result=CrackResult(value=res),
            )
            if type(res) == self._final_type:
                check_res = self._checker(res)
                if check_res is not None:
                    return True, (level, check_res)
            ret.append(level)
        return False, ret

    def expand(
        self, parents: List[SearchLevel], check: bool = True
    ) -> (bool, Union[SearchResult, List[Node]]):
        result = parents[-1].result.value
        # logger.debug(f"Expanding {parents}")

        # Deduplication
        if not self._config().cache.mark_ctext(result):
            return False, []

        if check and type(result) == self._final_type:
            check_res = self._checker(result)
            if check_res is not None:
                return True, SearchResult(path=parents, check_res=check_res)

        success, dec_res = self.handleDecodings(result)
        if success:
            return True, SearchResult(path=parents + [dec_res[0]], check_res=dec_res[1])

        nodes: List[Node] = []

        for decoding in dec_res:
            # Don't check, as handleDecodings did that for us
            success, eval_res = self.expand(parents + [decoding], check=False)
            if success:
                return True, eval_res
            nodes.extend(eval_res)

        crackers: List[Cracker] = registry[Cracker[type(result)]]
        expected_time: float

        # Worth doing this check twice to simplify code and allow a early return for decodings
        if type(result) == self._final_type:
            expected_time = self._checker.getExpectedRuntime(result)
        else:
            expected_time = 0
        for i in crackers:
            cracker = self._config()(i)
            nodes.append(
                Node(
                    cracker=cracker,
                    crack_info=cracker.getInfo(result),
                    check_info=expected_time,
                    parents=parents,
                )
            )

        return False, nodes

    def evaluate(self, node: Node) -> (bool, Union[List[SearchLevel], List[Node]]):
        # logger.debug(f"Evaluating {node}")

        res = node.cracker.attemptCrack(node.parents[-1].result.value)
        # Detect if we succeeded, and if deduplication is needed
        logger.trace(f"Got {len(res)} results")

        ret = []
        for i in res:
            success, res = self.expand(
                node.parents
                + [SearchLevel(name=type(node.cracker).__name__.lower(), result=i)]
            )
            if success:
                return True, res
            ret.extend(res)

        return False, ret

    def search(self, ctext: Any) -> List[SearchLevel]:
        deadline = (
            datetime.now() + self._config().objs["timeout"]
            if self._config().timeout is not None
            else datetime.max
        )

        success, expand_res = self.expand(
            [SearchLevel(name="input", result=CrackResult(value=ctext))]
        )
        if success:
            return expand_res

        nodes = set(expand_res)

        while datetime.now() < deadline:
            # logger.trace(f"Have node tree {nodes}")

            if len(nodes) == 0:
                raise LookupError("Could not find any solutions")

            best_node = self.findBestNode(nodes)
            nodes.remove(best_node)
            success, eval_res = self.evaluate(best_node)
            if success:
                # logger.trace(f"Success with node {best_node}")
                return eval_res
            nodes.update(eval_res)

        raise TimeoutError("Search ran out of time")

    @staticmethod
    @abstractmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @abstractmethod
    def __init__(self, config: Config):
        super().__init__(config)
        self._checker = config.objs["checker"]
        self._final_type = config.objs["format"]["out"]
