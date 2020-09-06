from typing import Optional, Dict

from ciphey.iface import ParamSpec, Config, Decoder, registry


@registry.register
class dna(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        """Write the code that decodes here
        ctext -> the input to the function
        returns string
        """
        print(ctext)
        # A=00 T=01 G=10 C=11
        return ctext.upper().replace("A", "00").replace("T", "01").replace("G", "10").replace("C", "11")

    @staticmethod
    def priority() -> float:
        """How often is this seen in a CTF out of 1
        Returns float
        """
        return 0.2

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