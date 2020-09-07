from typing import Tuple, Any

from cryptography.x509 import Certificate as X509
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey, DHPrivateKey


class PublicKey(Tuple):
    key: Any


class PrivateKey(Tuple):
    key: Any
