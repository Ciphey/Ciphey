import base64
import types

import ciphey
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


_bases = {
    "base16": (base64.b16decode, 0.4),
    "base32": (base64.b32decode, 0.01),
    "base64": (base64.b64decode, 0.4),
    "base85": (base64.b85decode, 0.01),
    "ascii85": (base64.a85decode, 0.1),
}


def gen_class(name, decoder, priority, ns):
    ns["_get_func"] = ciphey.common.id_lambda(decoder)
    ns["decode"] = lambda self, ctext: _dispatch(self, ctext, self._get_func())
    ns["getParams"] = ciphey.common.id_lambda(None)
    ns["getTarget"] = ciphey.common.id_lambda(name)
    ns["priority"] = ciphey.common.id_lambda(priority)
    ns["__init__"] = lambda self, config: super(type(self), self).__init__(config)


for name, (decoder, priority) in _bases.items():
    t = types.new_class(
        name,
        (ciphey.iface.Decoder[str, bytes],),
        exec_body=lambda x: gen_class(name, decoder, priority, x),
    )

    ciphey.iface.registry.register(t)
