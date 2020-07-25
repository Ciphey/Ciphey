from typing import Optional, Dict, List

from . import brandon
from ciphey.iface import registry, Checker, ParamSpec, T, Config

from .regex import RegexList
from .brandon import Brandon


@registry.register
class EzCheck(Checker[str]):
    checkers: List[Checker[str]] = []

    """
        This object is effectively a prebuilt quroum (with requirement 1) of common patterns
    """

    def check(self, text: T) -> Optional[str]:
        pass

    def getExpectedRuntime(self, text: T) -> float:
        return sum(i.getExpectedRuntime(text) for i in self.checkers)

    def __init__(self, config: Config):
        super().__init__(config)

        # We need to modify the config for each of the objects

        # First the flag regexes, as they are the fastest
        flags_config = config
        flags_config.update_param("regexlist", "resource", "cipheydists::list::flags")
        # We do not cache, as this uses a different, on-time config
        self.checkers.append(RegexList(flags_config))

        # Then the brandon checker
        self.checkers.append(config(Brandon))


    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass


