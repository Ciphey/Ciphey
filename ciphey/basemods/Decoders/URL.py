from typing import Optional, Dict, List
from urllib.parse import unquote

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class URL(Decoder[T, U]):
    def decode(self, ctext: T) -> Optional[U]:
        """Write the code that decodes here
        ctext -> the input to the function
        returns string
    """
        try:
            ctext = ctext.replace("+", " ")  # replace + sign with spacebar for unquote
            return unquote(ctext)  #built-in function that decodes URL coding
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        """How often is this seen in a CTF out of 1
        Returns float
        """
        return 0.3

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """The parameters this returns"""
        pass

    @staticmethod
    def getTarget() -> str:
        """The name of the decoding ussed
        returns string
        """
        return "URLCoding"