from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry

 @registry.register_multi((str, str), (bytes, bytes))
  class multiTap(Decoder[str, str]):
       def decode(self, ctext: str) -> Optional[U]:
            """Write the code that decodes here
            ctext -> the input to the function
            returns string
        """
        # TODO

        @staticmethod
        def priority() -> float:
            """How often is this seen in a CTF out of 1
            Returns float
            """
            return 0.05

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
            return "Multi-tap"
