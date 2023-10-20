# community
# by https://github.com/mklarz

from typing import Optional, Dict 

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register
class Citrix_ctx1(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        if len(ctext) % 4 != 0:
            return None

        rev = ctext[::-1].encode()
        result = b""
        temp = 0

        for i in range(0, len(rev), 2):
            if i + 2 >= len(rev):
                temp = 0
            else:
                temp = ((rev[i + 2] - 0x41) & 0xF) ^ (((rev[i + 3] - 0x41) << 4) & 0xF0)
            temp = (
                (((rev[i] - 0x41) & 0xF) ^ (((rev[i + 1] - 0x41) << 4) & 0xF0))
                ^ 0xA5
                ^ temp
            )
            result += bytes([temp])

        return result.replace(b"\x00", b"")[::-1]

    @staticmethod
    def priority() -> float:
        return 0.01

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "citrix_ctx1"
