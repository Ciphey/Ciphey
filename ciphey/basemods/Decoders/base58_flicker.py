from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

import base58


@registry.register
class Base58_flickr(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base58 (Flickr) decoding
        """
        FLICKR_ALPHABET = b"123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
        try:
            return base58.b58decode(ctext, alphabet=FLICKR_ALPHABET).decode("utf-8")
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
        return "base58_flickr"
