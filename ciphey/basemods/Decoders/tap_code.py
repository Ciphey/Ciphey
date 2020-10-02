# by https://github.com/RustyDucky and https://github.com/lukasgabriel

from typing import Optional, Dict, FrozenSet

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, Translation, Level


@registry.register
class TapCode(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        output = ""
        combinations = ctext.split(" ")
        for fragment in combinations:
            elem = self.TABLE.get(fragment)
            # Stop if we find something outside the table
            if elem is None:
                return None
            output += elem
        return output

    def __init__(self, config: Config):
        super().__init__(config)
        self.TABLE = config.get_resource(self._params()["dict"], Translation)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The table of letters used for the tap code interpretation.",
                req=False,
                default="cipheydists::translate::tap_code",
            )
        }

    @staticmethod
    def getLevel() -> Level:
        return Level.VeryCommon

    @staticmethod
    def getTags() -> FrozenSet[str]:
        return frozenset({"utf-8", "unicode", "text"})
