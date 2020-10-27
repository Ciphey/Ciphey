# by https://github.com/RustyDucky and https://github.com/lukasgabriel

from typing import Dict, Optional

from ciphey.iface import Config, Decoder, ParamSpec, T, Translation, U, registry


@registry.register
class Tap_code(Decoder[str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs Tap code decoding
        """
        try:
            result = ""
            combinations = ctext.split(" ")
            for fragment in combinations:
                result += self.TABLE.get(fragment)
            return result
        except Exception:
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
