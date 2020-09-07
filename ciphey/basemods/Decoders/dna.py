from typing import Optional, Dict

from ciphey.iface import ParamSpec, Config, Decoder, registry

@registry.register
class Dna(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        """Write the code that decodes here
        ctext -> the input to the function
        returns string
        """
        # print(ctext)
        # A=00 T=01 G=10 C=11
        return ctext.upper().replace("00", "A").replace("01", "T").replace("10", "G").replace("11", "C")

    @staticmethod
    def priority() -> float:
        """How often is this seen in a CTF out of 1
        Returns float
        """
        return 0.02

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
        return "DNA to Binary"
