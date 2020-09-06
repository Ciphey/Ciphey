# by https://github.com/RustyDucky and https://github.com/lukasgabriel

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, WordList


@registry.register
class prisoner_tap_code(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        try:
            output = ""
            print(ctext)
            combinations = ctext.split(" ")
            for fragment in combinations:
                print(fragment)
                if fragment == "":
                    output += ""
                y, x = fragment.split(",")
                y, x = int(y), int(x)
                output += self.TABLE[y][x]
            print(output.lower())
            return output.lower()

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def priority() -> float:
        # Needs to be high so it doesn't get messed up by the other decoders
        return 0.2

    def __init__(self, config: Config):
        super().__init__(config)
        self.TABLE = config.get_resource(self._params()["dict"], WordList)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The table of letters used for the tap code interpretation.",
                req=False,
                default="cipheydists::list::prisonerTapCodeTable",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "prisoner_tap_code"
