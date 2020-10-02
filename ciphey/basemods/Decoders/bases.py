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


@dataclass
class BaseSpec:
    decoder: Callable
    level: Level
    other_tags: frozenset = frozenset()


FLICKR_ALPHABET = b"123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"


# Add your single-line decoder here, in order of increasing radix (then specialisation)
#
# "<name>": BaseSpec(<function>, <level>)
#
# or, for specialisations of other decodings
#
# "<name>": BaseSpec(<function>, <level>, frozenset(<root encoding>))
_bases = {
    "base16": BaseSpec(lambda x: base64.b16decode(x, casefold=True), Level.VeryCommon),
    "base32": BaseSpec(lambda x: base64.b32decode(x, casefold=True), Level.Uncommon),
    "base58": BaseSpec(base58.b58decode, Level.Rare),
    "base58_flickr": BaseSpec(lambda x: base58.b58decode(x, alphabet=FLICKR_ALPHABET), Level.VeryRare, frozenset({"base58"})),
    "base58_ripple": BaseSpec(lambda x: base58.b58decode(x, alphabet=base58.RIPPLE_ALPHABET), Level.VeryRare, frozenset({"base58"})),
    "base62": BaseSpec(base62.decode, Level.VeryRare),
    "base64": BaseSpec(base64.b64decode, Level.VeryCommon),
    "base64_url": BaseSpec(lambda x: base64.urlsafe_b64decode(x + "=" * (4 - len(x) % 4)), Level.Uncommon, frozenset({"base64", "web"})),
    "base85": BaseSpec(base64.b85decode, Level.Rare),
    "ascii85": BaseSpec(base64.a85decode, Level.Uncommon, frozenset({"base85"})),
    "z85": BaseSpec(z85.decode, Level.VeryRare, frozenset({"base85"})),
    "base91": BaseSpec(lambda x: bytes(base91.decode(x)), Level.VeryRare),
    "base65536": BaseSpec(base65536.decode, Level.VeryRare),
}


def gen_class(name, spec: BaseSpec, ns):
    ns["_get_func"] = ciphey.common.id_lambda(spec.decoder)
    ns["decode"] = lambda self, ctext: _dispatch(self, ctext, self._get_func())
    ns["getParams"] = ciphey.common.id_lambda(None)
    ns["getTarget"] = ciphey.common.id_lambda(name)
    ns["getLevel"] = ciphey.common.id_lambda(spec.level)
    ns["getTags"] = ciphey.common.id_lambda({name, "base"}.union(spec.other_tags))
    ns["__init__"] = lambda self, config: super(type(self), self).__init__(config)


for name, spec in _bases.items():
    t = types.new_class(
        name,
        (ciphey.iface.Decoder[str],),
        exec_body=lambda x: gen_class(name, spec, x),
    )

    ciphey.iface.registry.register(t)
