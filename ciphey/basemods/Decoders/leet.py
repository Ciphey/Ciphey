from typing import Optional, Dict, Any, FrozenSet

from loguru import logger

import ciphey
from ciphey.iface import registry, Translation, ParamSpec, Level


@registry.register
class Leet(ciphey.iface.Decoder[str]):
    def decode(self, text: str) -> Optional[str]:
        for src, dst in self.translate.items():
            text = text.replace(src, dst)
        return text

    @staticmethod
    def getLevel() -> Level:
        return Level.VeryRare

    @staticmethod
    def getTags() -> FrozenSet[str]:
        return frozenset({"leet", "substitution"})

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.translate = config.get_resource(self._params()["dict"], Translation)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The leetspeak dictionary to use",
                req=False,
                default="cipheydists::translate::leet",
            )
        }
