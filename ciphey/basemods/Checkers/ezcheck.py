from typing import Optional, Dict, List

from . import brandon
from ciphey.iface import registry, PolymorphicChecker, ParamSpec, T, Config

from .regex import RegexList
from .brandon import Brandon
from .format import JsonChecker
from .human import HumanChecker
from .private_key import PrivateKeyChecker


@registry.register
class EzCheck(PolymorphicChecker):
    """
        This object is effectively a prebuilt quorum (with requirement 1) of common patterns, followed by a human check
    """

    def check(self, text: str) -> Optional[str]:
        for checker in self.checkers:
            res = checker.check(text)
            if res is not None and (self.decider is None or self.decider.check(text)) is not None:
                return res
        return None

    def getExpectedRuntime(self, text: T) -> float:
        return sum(i.getExpectedRuntime(text) for i in self.checkers) + self.decider.getExpectedRuntime(text)

    def __init__(self, config: Config):
        super().__init__(config)

        self.checkers: List[PolymorphicChecker[str]] = []
        # Disable human checker for automated systems
        if config.verbosity >= 0:
            self.decider = config(HumanChecker)
        else:
            self.decider = None

        # We need to modify the config for some of the objects to pass them different flags

        # Add the trivial checkers
        self.checkers.append(config(PrivateKeyChecker))

        # Next the flag regexes, as they are the fastest non-trivial modules
        flags_config = config
        flags_config.update_param("regexlist", "resource", "cipheydists::list::flags")
        # We do not cache, as this uses a different, on-time config
        self.checkers.append(RegexList(flags_config))

        # Next, the json checker
        self.checkers.append(config(JsonChecker))

        # Finally, the Brandon checker, as it is the slowest
        self.checkers.append(config(Brandon))

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass
