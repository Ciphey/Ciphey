import types
from typing import Optional, Dict, Callable, Any

from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key, \
    load_der_private_key, load_der_public_key
from cryptography.x509 import load_pem_x509_certificate, load_der_x509_certificate
from cryptography.hazmat.backends import default_backend
import cryptography.exceptions
from loguru import logger

from ciphey.common import id_lambda
from ciphey.iface import Decoder, PrivateKey, PublicKey, Config, X509, ParamSpec, registry, RSAPrivateKey, RSAPublicKey

backend = default_backend()


def _dispatch(self: Any, ctext: str, func: Callable):
    logger.trace(f"Attempting {self.getTarget()}")
    try:
        result = func(ctext)
        logger.debug(f"{self.getTarget()} successful, returning {result}")
        return result
    except ValueError:
        logger.trace(f"Failed to decode {self.getTarget()}")
    except cryptography.exceptions.UnsupportedAlgorithm:
        logger.trace(f"Unknown key type {self.getTarget()}")


_decoders = {
    "pem_private": ((lambda x: PrivateKey(load_pem_private_key(x.encode(), None, backend=backend))), 0.01, str, PrivateKey),
    "pem_public": ((lambda x: PublicKey(load_pem_public_key(x.encode(), backend=backend))), 0.01, str, PublicKey),
    "pem_x509": ((lambda x: load_pem_public_key(x.encode(), backend=backend)), 0.01, str, X509),
    "der_private": ((lambda x: PrivateKey(load_der_private_key(x.encode(), None, backend=backend))), 0.01, str, bytes),
    "der_public": ((lambda x: PublicKey(load_der_public_key(x.encode(), backend=backend))), 0.01, str, bytes),
    "der_x509": ((lambda x: load_der_x509_certificate(x.encode(), backend=backend)), 0.01, str, X509),
    "rsa_private": ((lambda x: x.key if x.key is RSAPrivateKey else None), 0.01, PrivateKey, RSAPrivateKey),
    "rsa_public": ((lambda x: x.key if x.key is RSAPublicKey else None), 0.01, PublicKey, RSAPublicKey),
}


def gen_class(name, decoder, priority, ns):
    ns["_get_func"] = id_lambda(decoder)
    ns["decode"] = lambda self, ctext: _dispatch(self, ctext, self._get_func())
    ns["getParams"] = id_lambda(None)
    ns["getTarget"] = id_lambda(name)
    ns["priority"] = id_lambda(priority)
    ns["__init__"] = lambda self, config: super(type(self), self).__init__(config)


for name, (decoder, priority, src, dst) in _decoders.items():
    t = types.new_class(
        name,
        (Decoder[src, dst],),
        exec_body=lambda x: gen_class(name, decoder, priority, x),
    )

    registry.register(t)