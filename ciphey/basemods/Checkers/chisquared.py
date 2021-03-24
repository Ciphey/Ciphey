from typing import Dict, Optional

from loguru import logger

from ciphey.iface import Checker, Config, ParamSpec, T, registry

from collections import Counter


@registry.register
class ChiSquared(Checker[str]):

    """
    Uses Chi Squared to determine plaintext
    """

    def check(self, text: T) -> Optional[str]:
        logger.trace("Trying Chi Squared checker")
        chi_sq = 0.0
        counts = Counter(text)
        for i in list(counts.keys()):
            # If letter is not in dict, don't do it.
            try:
                chi_sq = chi_sq + (
                    (counts[i] - self.wordlist[i]) ** 2 / self.wordlist[i]
                )
            except:
                continue
        logger.debug(f"Chi squared is {chi_sq}")
        logger.debug(chi_sq / len(text))
        if chi_sq / len(text) > 10000.0:
            return True
        return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        # Uses benchmark from Discord
        return 2e-7 * len(text)

    def __init__(self, config: Config):
        super().__init__(config)
        self.wordlist = config.get_resource(self._params()["wordlist"])

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "wordlist": ParamSpec(
                desc="A wordlist of all the words",
                req=False,
                default="cipheydists::dist::lcase",
            )
        }
