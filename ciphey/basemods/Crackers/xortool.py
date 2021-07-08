"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝
╚██████╗██║██║     ██║  ██║███████╗   ██║
© Brandon Skerritt
Github: bee-san
"""
from typing import Dict, List, Optional

import logging
from rich.logging import RichHandler

from xortool_ciphey import tool_main

from ciphey.iface import Config, Cracker, CrackInfo, CrackResult, ParamSpec, registry


@registry.register
class XorTool(Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1,
            # TODO: actually calculate runtimes
            success_runtime=1e-8,
            failure_runtime=1e-8,
        )

    @staticmethod
    def getTarget() -> str:
        return "xortool"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logging.debug("Trying xortool cipher")
        # TODO handle different charsets
        # TODO allow more config over xortool

        logging.debug(f"{ctext}")

        # https://github.com/Ciphey/xortool/discussions/4
        # for docs on this function
        try:
            result = tool_main.api(str.encode(ctext))
        except:
            logging.debug("Xor failed.")
            return

        result = CrackResult(value=result[1]["Dexored"], key_info=result[0]["keys"])

        return [result]

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "p_value": ParamSpec(
                desc="The p-value to use for standard frequency analysis",
                req=False,
                default=0.01,
            ),
        }

    @staticmethod
    def score_utility() -> float:
        return 1.5

    def __init__(self, config: Config):
        super().__init__(config)
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.p_value = self._params()["p_value"]
