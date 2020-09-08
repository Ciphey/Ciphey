from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry

import base64


@registry.register
class Base64_url(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Base64 URL decoding
        """
        ctext_padding = ctext + "=" * (4 - len(ctext) % 4)
        try:
            return base64.urlsafe_b64decode(ctext_padding).decode("utf-8")
        except Exception:
            return None

    @staticmethod
    def priority() -> float:
        # Not expected to show up often, but also very fast to check.
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "base64_url"
