from typing import Optional, Dict, List, Set

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, Level

from urllib.parse import unquote_plus


@registry.register
class Url(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs URL decoding
        """
        try:
            result = unquote_plus(ctext, errors="strict")
            if result != ctext:
                return result
            else:
                return None
        except Exception:
            return None

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getLevel() -> Level:
        return Level.VeryCommon

    @staticmethod
    def getTags() -> Set[str]:
        return {"url", "web"}
