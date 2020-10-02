# by https://github.com/RustyDucky and https://github.com/lukasgabriel

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, Translation


@registry.register
class tap_code(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        try:
            output = ""
            combinations = ctext.split(" ")
            for fragment in combinations:
                    output += self.TABLE.get(fragment)
            return output

        except Exception as e:
            return None

    @staticmethod
    def priority() -> float:
        return 0.06

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
    def getTarget() -> str:
        return "tap_code"
