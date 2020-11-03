import base64
import types
from typing import Any, Callable, Optional

from loguru import logger
import re

from ciphey.common import id_lambda
from ciphey.iface import Decoder, registry


def _dispatch(self: Any, ctext: str, func: Callable[[str], bytes]) -> Optional[bytes]:
    logger.trace(f"Attempting {self.getTarget()}")

    try:
        # remove all whitespace
        ctext = re.sub(r"\s+", "", ctext, re.UNICODE)
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
    ns["_get_func"] = id_lambda(decoder)
    ns["decode"] = lambda self, ctext: _dispatch(self, ctext, self._get_func())
    ns["getParams"] = id_lambda(None)
    ns["getTarget"] = id_lambda(name)
    ns["priority"] = id_lambda(priority)
    ns["__init__"] = lambda self, config: super(type(self), self).__init__(config)


for name, (decoder, priority) in _bases.items():
    t = types.new_class(
        name,
        (Decoder[str],),
        exec_body=lambda x: gen_class(name, decoder, priority, x),
    )

    registry.register(t)
