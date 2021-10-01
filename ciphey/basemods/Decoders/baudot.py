import re
from typing import Dict, Optional

from ciphey.iface import Config, Decoder, ParamSpec, T, Translation, U, registry


@registry.register
class Baudot(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        switch_to_digit_map = 0
        if not re.search("^[01]{5}$", ctext.split()[0]):
            return None

        result = ""
        for i in ctext.split():
            if i == "11011":
                switch_to_digit_map = 1
            elif i == "11111":
                switch_to_digit_map = 0
            if switch_to_digit_map == 0:
                result += self.BAUDOT_DICT[i]
            elif switch_to_digit_map == 1:
                result += self.BAUDOT_DICT["+" + i]
        return result

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)
        self.BAUDOT_DICT = config.get_resource(self._params()["dict"], Translation)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The baudot alphabet dictionary to use",
                req=False,
                default="cipheydists::translate::baudot",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "baudot"
