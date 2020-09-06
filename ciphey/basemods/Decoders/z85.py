from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

from loguru import logger

from zmq.utils import z85


@registry.register
class Z85(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Z85 decoding
        """
        ctext_len = len(ctext)
        if ctext_len % 5:
            logger.trace(
                f"Failed to decode Z85 because length must be a multiple of 5, not '{ctext_len}'"
            )
            return None
        try:
            return z85.decode(ctext).decode("utf-8")
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
        return "z85"
