from typing import FrozenSet, Optional, Dict, List

from ciphey.iface import registry, RSAPublicKey, Cracker, Level, ParamSpec, T, CrackResult, CrackInfo
from ciphey.iface._fwd import config as Config


@registry.register
class RSAFactoriser(Cracker[RSAPublicKey]):
    pass