from typing import NamedTuple, Any

from cryptography.x509 import Certificate as X509
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey, DHPrivateKey


class PublicKey(NamedTuple):
    key: Any


class PrivateKey(NamedTuple):
    key: Any
