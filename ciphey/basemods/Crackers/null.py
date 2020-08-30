# community
# by https://github.com/lukasgabriel

from distutils import util
from typing import Optional, Dict, Union, Set, List
from loguru import logger

from ciphey.iface import ParamSpec, Cracker, CrackResult, CrackInfo, T, registry, Config


@registry.register
class NullCracker(Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=1e-5, success_runtime=1e-5, failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "nullcipher"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
        TODO: docstring
        """
        logger.trace("Attempting to crack with NullCipher cracker.")
        result = []
        ctext = ctext.lower().replace(" ", "").strip()

        # cset contains every unique value in the cstring
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
