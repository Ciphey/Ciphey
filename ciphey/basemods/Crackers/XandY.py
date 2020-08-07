# community
# by https://github.com/lukasgabriel

from distutils import util
from typing import Optional, Dict, Union, Set, List
from loguru import logger

from ciphey.iface import ParamSpec, Cracker, CrackResult, CrackInfo, T, registry, Config


@registry.register
class XandY(Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        # TODO Write something useful here
        return CrackInfo(
            success_likelihood=1, success_runtime=1e-5, failure_runtime=1e-5,
        )

    @staticmethod
    def binary_to_ascii(variant):
        # Convert the binary string to an integer with base 2
        binary_int = int(variant, 2)
        byte_number = binary_int.bit_length() + 7 // 8

        # Convert the resulting int to a bytearray and then decode it to ascii text
        binary_array = binary_int.to_bytes(byte_number, "big")
        try:
            ascii_text = binary_array.decode()
            logger.trace(f"Found possible solution: {ascii_text[:32]}...")
            return ascii_text
        except UnicodeDecodeError:
            return ""

    @staticmethod
    def getTarget() -> str:
        return "XandY"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
        Checks an input if it only consists of two different letters.
        If this is the case, it attempts to regard those two letters as
        0 and 1 and then converts it to ascii text.
        """
        logger.trace("Attempting X-Y replacement.")
        variants = []
        candidates = []
        result = []
        ctext = ctext.lower().replace(" ", "").strip()

        # cset contains every unique value in the cstring
        cset = list(set(list(ctext)))
        if len(cset) != 2:
            # We only consider inputs with exactly two unique values
            logger.trace("String contains more than two unique values. Skipping X-Y...")
            return None
        else:
            logger.trace(f"String contains two unique values: {cset[0], cset[1]}")
            # Form both variants of the substitution
            for i in range(2):
                if i:
                    variants.append(ctext.replace(cset[0], "1").replace(cset[1], "0"))
                else:
                    variants.append(ctext.replace(cset[0], "0").replace(cset[1], "1"))
            # Apply function to both variants and strip stray NULL characters
            for variant in variants:
                candidates.append(self.binary_to_ascii(variant).strip("\x00"))
            for i, candidate in enumerate(candidates):
                if candidate != "":
                    keyinfo = f"{cset[0]} -> {i} & {cset[1]} -> {str(int(not i))}"
                    result.append(CrackResult(value=candidate, key_info=keyinfo))
                    return result

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "group": ParamSpec(
                desc="An ordered sequence of chars that make up the caesar cipher alphabet",
                req=False,
                default="",
            ),
            "lower": ParamSpec(
                desc="Whether or not the ciphertext should be converted to lowercase first",
                req=False,
                default=True,
            ),
            "p_value": ParamSpec(
                desc="The p-value to use for standard frequency analysis",
                req=False,
                default=0.01,
            )
            # TODO: Change this to match this class (it's copied over from caesar)
        }

    def __init__(self, config: Config):
        # TODO: Change this to match this class (it's copied over from caesar)
        super().__init__(config)
        self.lower: Union[str, bool] = self._params()["lower"]
        if type(self.lower) != bool:
            self.lower = util.strtobool(self.lower)
        self.group = list(self._params()["group"])
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.p_value = self._params()["p_value"]
