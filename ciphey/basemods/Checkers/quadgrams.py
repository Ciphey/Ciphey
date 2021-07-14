import logging
import re
from math import log10
from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, T, Translation, registry
from rich.logging import RichHandler


@registry.register
class Quadgrams(Checker[str]):

    """
    Uses Quadgrams to determine plaintext
    """

    def check(self, ctext: T) -> Optional[str]:
        logging.debug("Trying Quadgrams checker")
        # Capitalize and remove everything that's not a letter
        ctext = re.sub("[^A-Z]", "", ctext.upper())
        quadgrams = self.QUADGRAMS_DICT
        quadgrams_sum = sum(quadgrams.values())
        score = 0
        for key in quadgrams.keys():
            quadgrams[key] = float(quadgrams[key]) / quadgrams_sum
        floor = log10(0.01 / quadgrams_sum)
        for i in range(len(ctext) - 4 + 1):
            # Get all quadgrams from ctext and check if they're in the dict
            # If yes then add the score of those quadgrams to the total score
            if ctext[i : i + 4] in quadgrams:
                score += quadgrams[ctext[i : i + 4]]
            else:
                score += floor
        if len(ctext) > 0:
            score = score / len(ctext)
        logging.info(f"Quadgrams is {score}")
        # The default threshold was found to work the best from lots of testing
        if score > self.threshold:
            return ""
        return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 2e-7 * len(text)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The quadgrams dictionary to use",
                req=False,
                default="cipheydists::dist::quadgrams",
            ),
            "score": ParamSpec(
                desc="The score threshold to use",
                req=False,
                default=0.00011,
            ),
        }

    def __init__(self, config: Config):
        super().__init__(config)
        self.QUADGRAMS_DICT = config.get_resource(self._params()["dict"], Translation)
        self.threshold = float(self._params()["score"])
