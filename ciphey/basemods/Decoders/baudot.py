import re
from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry, Translation


@registry.register_multi((str, str), (bytes, bytes))
class Baudot(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """Write the code that decodes here
        ctext -> the input to the function
        returns string
    """

        ret = ""
        switch_to_digit_map = 0
        if type(ctext) == str:
            if re.search("^[01]{5}$", ctext.split()[0]):
                for i in ctext.split():
                    if i == "11011":
                        switch_to_digit_map = 1
                    if i == "11111":
                        switch_to_digit_map = 0
                    if switch_to_digit_map == 1:
                        ret += self.BAUDOT_DICT["+" + i]
                    if switch_to_digit_map == 0:
                        ret += self.BAUDOT_DICT[i]
                return ret
        else:
            return None

    @staticmethod
    def priority() -> float:
        """How often is this seen in a CTF out of 1
        Returns float
        """
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
        """The name of the decoding ussed
        returns string
        """
        return "baudot"
