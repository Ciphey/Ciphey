# community
# by https://github.com/lukasgabriel

import re
from distutils import util
from typing import Optional, Dict, Union, Set, List
from loguru import logger

from ciphey.iface import ParamSpec, Cracker, CrackResult, CrackInfo, T, registry, Config


@registry.register
class XandY(Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1, success_runtime=1e-5, failure_runtime=1e-5,
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
        except UnicodeDecodeError as e:
            logger.trace(f"X-Y Cracker ecountered UnicodeDecodeError when trying to crack ctext: {e}")
            return ""
    
    @staticmethod
    def getTarget() -> str:
        return "XandY"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
        Checks an input if it only consists of two or three different letters.
        If this is the case, it attempts to regard those letters as
        0 and 1 (with the third characters as an optional delimiter) and then 
        converts it to ascii text.
        """
        logger.trace("Attempting X-Y replacement.")
        variants = []
        candidates = []
        result = []

        # Convert the ctext to all-lowercase and regex-match & replace all whitespace
        ctext = ctext.lower()
        ctext = re.sub(r"\s+", "", ctext, flags=re.UNICODE)

        # cset contains every unique value in the ctext
        cset = list(set(list(ctext)))
        cset_len = len(cset)

        if not 1 < cset_len < 4:
            # We only consider inputs with two or three unique values
            logger.trace("String does not contain two or three unique values. Skipping X-Y...")
            return None

        else:
            logger.trace(f"String contains {cset_len} unique values: {cset}")

            # In case of three unique values, we regard the least frequent character as the delimiter
            if cset_len == 3:
                # Count each unique character in the set to determine the least frequent one
                counting_list = []
                for char in cset:
                    counting_list.append(ctext.count(char))
                val, index = min(
                    (val, index) for (index, val) in enumerate(counting_list)
                )
                delimiter = cset[index]
                logger.trace(
                    f"{delimiter} occurs {val} times and is least frequent character & probable delimiter."
                )
                # Remove the delimiter from the ctext and compute new cset
                ctext = ctext.replace(delimiter, "")
                cset = list(set(list(ctext)))

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
                    logger.trace(f"X-Y cracker - Returning results: {result}")
                    return result

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            )
        }

    def __init__(self, config: Config):
        super().__init__(config)
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
