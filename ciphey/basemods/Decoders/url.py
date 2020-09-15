from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

from urllib.parse import unquote


@registry.register
class Url(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs URL decoding
        """
        ctext = ctext.replace("+", " ")  # Replace + sign with a space for unquote
        try:
            result = unquote(ctext)  # Built-in function that decodes URL encoding
            if result != ctext:
                return result
            else:
                return None
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "url"
