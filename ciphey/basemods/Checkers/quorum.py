from math import ceil
from typing import Optional, Dict, Generic

import ciphey
from ciphey.iface import ParamSpec, Config, T


class Quorum(Generic[T], ciphey.iface.Checker[T]):
    def check(self, text: T) -> Optional[str]:
        left = self._params().k
        results = []
        for checker in self.checkers:
            results.append(checker.check(text))
            if results[-1] is None:
                continue
            left -= 1
            # Early return check
            if left == 0:
                return str(results)

    def __init__(self, config: Config):
        super().__init__(config)

        if self._params().k is None:
            k = len(self._params()["checker"])
        # These checks need to be separate, to make sure that we do not have zero members
        if self._params().k == 0 or self._params().k > len(self._params()["checker"]):
            raise IndexError(
                "k must be between 0 and the number of checkers (inclusive)"
            )

        self.checkers = []
        for i in self._params()["checker"]:
            # This enforces type consistency
            self.checkers.append(
                ciphey.iface._registry.get_named(i, ciphey.iface.Checker[T])
            )

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "checker": ParamSpec(
                req=True, desc="The checkers to be used for analysis", list=True
            ),
            "k": ParamSpec(
                req=False,
                desc="The minimum quorum size. Defaults to the number of checkers",
            ),
        }
