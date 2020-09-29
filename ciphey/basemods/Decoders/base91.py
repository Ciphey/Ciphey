from typing import Optional, Dict, List, Set

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

import base91


@registry.register
class Base91(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base91 decoding
        """
        try:
            return base91.decode(ctext).decode("utf-8")
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "base91"

    @staticmethod
    def getTags() -> Set[str]:
        return {"base91", "base"}
