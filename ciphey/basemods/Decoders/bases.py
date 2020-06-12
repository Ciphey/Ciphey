import base64
import types

import ciphey
import binascii
from typing import Callable, Optional, Any, Dict

from loguru import logger


def _dispatch(self: Any, ctext: str, func: Callable[[bytes], str]) -> Optional[bytes]:
    logger.trace(f"Attempting {self.getName()}")

    try:
        result = func(ctext)
        logger.debug(f"{self.getName()} successful, returning {result}")
        return result
    except ValueError:
        logger.trace(f"Failed to decode {self.getName()}")
        return None


def _init(self: Any, config: ciphey.iface.Config):
    super(type(self), self).__init__(config)

l = []

for name, decoder in {"base16": base64.b16decode, "base32": base64.b32decode, "base64": base64.b64decode,
                      "base85": base64.b85decode, "ascii85": base64.a85decode}.items():
    t = type(name, (ciphey.iface.Decoder,), {
        "_get_func": ciphey.iface.id_lambda(decoder),
        "decode": lambda self, ctext: _dispatch(self, ctext, self._get_func()),
        "getArgs": ciphey.iface.id_lambda(None),
        "getName": ciphey.iface.id_lambda(name),
        "__init__": lambda self, config: _init(self, config)
    })

    ciphey.iface.registry.register(t, ciphey.iface.Decoder[str, bytes])