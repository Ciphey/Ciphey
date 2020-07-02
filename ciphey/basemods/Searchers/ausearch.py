from abc import ABC, abstractmethod
from typing import Generic, List, Optional, Dict, Any, NamedTuple, Union, Set
from ciphey.iface import ConfigurableModule, T, Cracker, Config, Searcher, ParamSpec, CrackInfo, registry, get_args, \
    SearchLevel, CrackResult
from datetime import datetime
from loguru import logger


class Node(Generic[T], NamedTuple):
    cracker: Cracker
    parents: List[SearchLevel]
    crack_info: CrackInfo
    check_info: float

    def __hash__(self):
        return hash((type(self.cracker).__name__, len(self.parents)))


class AuSearch(Searcher):
    @abstractmethod
    def findBestNode(self, nodes: Set[Node]) -> Node: pass

    @abstractmethod
    def handleDecodings(self, target: Any) -> (bool, Union[SearchLevel, List[SearchLevel]]):
        """
            If there exists a decoding that the checker returns true on, returns (True, result).
            Otherwise, returns (False, names and successful decodings)

            The CrackResult object should only have the value field filled in

            MUST NOT recurse into decodings! evaluate does that for you!
        """
        # This tag is necessary, as we could have a list as a decoding target, which would then screw over type checks
        pass

    def expand(self, parents: List[SearchLevel], check: bool = True) -> (bool, Union[List[SearchLevel], List[Node]]):
        result = parents[-1].result.value

        if check and type(result) == self._final_type and self._checker(result):
            return True, result

        success, dec_res = self.handleDecodings(result)
        if success:
            return True, [dec_res]

        nodes: List[Node] = []

        for decoding in dec_res:
            # Deduplication
            if not self._config().cache.mark_ctext(decoding.result.value):
                continue

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
            nodes.append(Node(
                cracker=cracker,
                crack_info=cracker.getInfo(result),
                check_info=expected_time,
                parents=parents
            ))

        return False, nodes

    def evaluate(self, node: Node) -> (bool, Union[List[SearchLevel], List[Node]]):
        logger.trace(f"Evaluating {node}")

        res = node.cracker.attemptCrack(node.parents[-1].result.value)
        # Detect if we succeeded, and if deduplication is needed
        if res is None:
            return False, []

        return self.expand([SearchLevel(name=type(node.cracker).__name__.lower(), result=res)] + node.parents)

    def search(self, ctext: Any) -> List[SearchLevel]:
        if not self._config().cache.mark_ctext(ctext):
            raise ValueError("Bad ciphertext. Maybe it's too short?")

        deadline = datetime.now() + self._config().objs["timeout"] if self._config().timeout is not None else datetime.max

        success, expand_res = self.expand([SearchLevel(name="input", result=CrackResult(value=ctext))])
        if success:
            return expand_res

        nodes = set(expand_res)

        while datetime.now() < deadline:
            if len(nodes) == 0:
                raise LookupError("Could not find any solutions")

            best_node = self.findBestNode(nodes)
            nodes.remove(best_node)
            success, eval_res = self.evaluate(best_node)
            if success:
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
