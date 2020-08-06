# community
# by https://github.com/lukasgabriel

from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry


@registry.register
class Galactic(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Takes a string written in the 'Standard Galactic Alphabet' 
        (aka Minecraft Enchanting Table Symbols) and translates it to ASCII text.
        """

        result = ""
        galactic_letters = [
            "ᔑ",
            "ʖ",
            "ᓵ",
            "↸",
            "ᒷ",
            "⎓",
            "⊣",
            "⍑",
            "╎",
            "⋮",
            "ꖌ",
            "ꖎ",
            "ᒲ",
            "リ",
            "𝙹",
            "!",
            "ᑑ",
            "∷",
            "ᓭ",
            "ℸ",
            "⚍",
            "⍊",
            "∴",
            "|",
            "⨅",
        ]
        letters = list("abcdefghijklmnopqrstuvwyz")
        galactic_dict = {galactic_letters[i]: letters[i] for i in range(25)}

        # Ensure that ciphertext is a string
        if type(ctext) == str:
            # Normalize the string to all-lowercase letters
            ctext = ctext.lower()
        else:
            return None

        ctext = (
            ctext.replace("||", "|")
            .replace("/", "")
            .replace("¡", "")
            .replace(" ̣ ", "")
            .replace(" ̇", " x")
        )
        # Take out the problematic characters consisting of multiple symbols
        print(ctext)
        for letter in ctext:
            print(f"Letter is {letter}")
            if letter in galactic_dict.keys():
                print(f"Letter {letter} matched to {galactic_dict[letter]}")
                # Match every letter of the input to its galactic counterpoint
                result += galactic_dict[letter]
            else:
                print(f"Letter {letter} not matched")
                # If the current character is not in the defined alphabet,
                # just accept it as-is (useful for numbers, punctuation,...)
                result += letter
            print(f"Result is now {result}")

        result = result.replace("x ", "x")
        # Remove the trailing space (appearing as a leading space)
        # from the x that results from the diacritic replacement
        # TODO: Handle edge cases where x still does not show up
        print(f"Final result is {result}")
        return result

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
        return "galactic"
