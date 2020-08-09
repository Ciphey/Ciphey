# by https://github.com/RustyDucky

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry


@registry.register
class Tap_code(Decoder[str, str]):
    def decode(self, input: T) -> Optional[U]:
        try: #So it doesn't throw an error when its not the right format or just not tap code
            medium = ' '.join(map(str, input)).split(" ") #Dealing with the format of user input
            output = ""

            xone = ["A", "B", "C/K", "D", "E"]
            xtwo =  ["F", "G", "H", "I", "J"]
            xthr =  ["L", "M", "N", "O", "P"]  #Making the tap code table
            xfour = ["Q", "R", "S", "Y", "U"]
            xfive = ["V", "W", "X", "Y", "Z"]

            for combination in medium:
                y,x = combination.split(",")
                x = int(x)
                y = int(y)

                if x == 1:
                    output += xone[y-1]

                elif x == 2:
                    output += xtwo[y-1]

                elif x == 3:
                    output += xthr[y-1]

                elif x == 4:
                    output += xfour[y-1]

                else:
                    output += xfive[y-1]
            return (output)
        except:
            return(input)

    @staticmethod
    def priority() -> float:
        return 0.1 #It's fast enough to be low priority

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    @staticmethod
    def getTarget() -> str:
        return "tap_code"
