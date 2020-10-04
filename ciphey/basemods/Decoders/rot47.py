from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, Decoder, registry


@registry.register
class Rot47(Decoder[str, str]):
    def decode(self, ctext: str) -> Optional[str]:
        decoded = []

        for i in range(len(ctext)):
            encoded = ord(ctext[i])
            decoded.append(
                chr(33 + ((encoded + 14) % 94))
                if encoded >= 33 and encoded <= 126
                else ctext[i]
            )

        return "".join(decoded)

    @staticmethod
    def priority() -> float:
        return 0.25

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "rot47"
