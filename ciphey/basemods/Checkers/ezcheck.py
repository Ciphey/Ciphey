from typing import Dict, List, Optional

from ciphey.iface import Checker, Config, ParamSpec, T, registry

from .brandon import Brandon
from .format import JsonChecker
from .human import HumanChecker
from .quadgrams import Quadgrams
from .regex import RegexList
from .what import What


@registry.register
class EzCheck(Checker[str]):
    """
    This object is effectively a prebuilt quorum (with requirement 1) of common patterns, followed by a human check
    """

    def check(self, text: str) -> Optional[str]:
        for checker in self.checkers:
            res = checker.check(text)
            if (
                res is not None
                and (self.decider is None or self.decider.check(text)) is not None
            ):
                return res
        return None

    def getExpectedRuntime(self, text: T) -> float:
        return sum(
            i.getExpectedRuntime(text) for i in self.checkers
        ) + self.decider.getExpectedRuntime(text)

    def __init__(self, config: Config):
        super().__init__(config)

        self.checkers: List[Checker[str]] = []
        # Disable human checker for automated systems
        self.decider = config(HumanChecker) if config.verbosity >= 0 else None
        # We need to modify the config for each of the objects

        # First PyWhat, as it's the fastest
        self.checkers.append(config(What))

        # Next, the json checker
        self.checkers.append(config(JsonChecker))

        # Second to last, the quadgrams checker
        self.checkers.append(config(Quadgrams))

        # Finally, the Brandon checker, as it is the slowest
        self.checkers.append(config(Brandon))

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
