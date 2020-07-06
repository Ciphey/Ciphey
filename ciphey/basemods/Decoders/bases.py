import base64
import types

import ciphey
import binascii
from typing import Callable, Optional, Any, Dict

from loguru import logger


def _dispatch(self: Any, ctext: str, func: Callable[[str], bytes]) -> Optional[bytes]:
    logger.trace(f"Attempting {self.getTarget()}")

    try:
        result = func(ctext)
        logger.debug(f"{self.getTarget()} successful, returning {result}")
        return result
    except ValueError:
        logger.trace(f"Failed to decode {self.getTarget()}")
        return None


def _init(self: Any, config: ciphey.iface.Config):
    super(type(self), self).__init__(config)


_bases = {
    "base16": (base64.b16decode, 0.4),
    "base32": (base64.b32decode, 0.01),
    "base64": (base64.b64decode, 0.4),
    "base85": (base64.b85decode, 0.01),
    "ascii85": (base64.a85decode, 0.1),
}

for name, (decoder, priority) in _bases.items():
    t = type(
        name,
        (ciphey.iface.Decoder,),
        {
            "_get_func": ciphey.common.id_lambda(decoder),
            "decode": lambda self, ctext: _dispatch(self, ctext, self._get_func()),
            "getParams": ciphey.common.id_lambda(None),
            "getTarget": ciphey.common.id_lambda(name),
            "priority": ciphey.common.id_lambda(priority),
            "__init__": lambda self, config: _init(self, config),
        },
    )

    ciphey.iface.registry.register(t, ciphey.iface.Decoder[str, bytes])
