from typing import Optional, Dict, List, Set

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry, Level


@registry.register_multi(str, bytes)
class Reverse(Decoder):
    def decode(self, ctext):
        return ctext[::-1]

    @staticmethod
    def getLevel() -> Level:
        return Level.Common

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTags() -> Set[str]:
        return {"reverse"}
