import re
from typing import Dict, List, Optional

from ciphey.iface import (
    Config,
    Cracker,
    CrackInfo,
    CrackResult,
    ParamSpec,
    Translation,
    registry,
)
from loguru import logger


@registry.register
class Baconian(Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1,
            success_runtime=1e-5,
            failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "baconian"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
        Attempts to decode both variants of the Baconian cipher.
        """
        logger.trace("Attempting Baconian cracker")
        candidates = []
        result = []
        ctext_decoded = ""
        ctext_decoded2 = ""

        # Convert to uppercase and replace delimiters and whitespace with nothing
        ctext = re.sub(r"[,;:\-\s]", "", ctext.upper())

        # Make sure ctext only contains A and B
        if bool(re.search(r"[^AB]", ctext)) is True:
            logger.trace("Failed to crack baconian due to non baconian character(s)")
            return None

        # Make sure ctext is divisible by 5
        ctext_len = len(ctext)
        if ctext_len % 5:
            logger.trace(
                f"Failed to decode Baconian because length must be a multiple of 5, not '{ctext_len}'"
            )
            return None

        # Split ctext into groups of 5
        ctext = " ".join(ctext[i : i + 5] for i in range(0, len(ctext), 5))
        ctext_split = ctext.split(" ")
        baconian_keys = self.BACONIAN_DICT.keys()

        # Decode I=J and U=V variant
        for i in ctext_split:
            if i in baconian_keys:
                ctext_decoded += self.BACONIAN_DICT[i]

        # Decode variant that assigns each letter a unique code
        for i in ctext_split:
            if "+" + i in baconian_keys:
                ctext_decoded2 += self.BACONIAN_DICT["+" + i]

        candidates.append(ctext_decoded)
        candidates.append(ctext_decoded2)
        for candidate in candidates:
            if candidate != "":
                if candidate == candidates[0]:
                    result.append(CrackResult(value=candidate, key_info="I=J & U=V"))
                else:
                    result.append(CrackResult(value=candidate))
        logger.trace(f"Baconian cracker - Returning results: {result}")
        return result

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "dict": ParamSpec(
                desc="The Baconian alphabet dictionary to use",
                req=False,
                default="cipheydists::translate::baconian",
            ),
        }

    def __init__(self, config: Config):
        super().__init__(config)
        self.BACONIAN_DICT = config.get_resource(self._params()["dict"], Translation)
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
