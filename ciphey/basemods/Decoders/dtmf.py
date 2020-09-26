from typing import Optional, Dict, List

from ciphey.iface import Config, ParamSpec, T, U, Decoder, registry, Translation

from loguru import logger

import re


@registry.register
class Dtmf(Decoder[str, str]):
    def decode(self, ctext: T) -> Optional[U]:
        """
        Performs DTMF decoding
        """
        logger.trace("Attempting DTMF decoder")
        ctext_decoded = ""
        ctext = re.sub(r"[,;:\-\/\s]", "", ctext)
        ctext = " ".join(ctext[i : i + 7] for i in range(0, len(ctext), 7))
        ctext_split = ctext.split(" ")
        dtmf_keys = self.DTMF_DICT.keys()

        for i in ctext_split:
            if i in dtmf_keys:
                ctext_decoded += self.DTMF_DICT[i]
            else:
                return None
        logger.debug(f"DTMF successful, returning '{ctext_decoded}'")
        return ctext_decoded

    @staticmethod
    def priority() -> float:
        return 0.2

    def __init__(self, config: Config):
        super().__init__(config)
        self.DTMF_DICT = config.get_resource(self._params()["dict"], Translation)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The DTMF alphabet dictionary to use",
                req=False,
                default="cipheydists::translate::dtmf",
            )
        }

    @staticmethod
    def getTarget() -> str:
        return "dtmf"
