from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class LastLetter(Decoder[T, U]):
    def decode(self, text: T) -> Optional[U]:
        """Write the code that decodes here
        text -> the input to the function
        returns string
        """
        decoded = []
        for word in text.split():
            # for each word in the text, append the last letter
            decoded.append(word[-1])
        # return the decoded message
        return ''.join(decoded)

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
        """The name of the decoding used
        returns string
        """
        return "LastLetter"
