"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝
╚██████╗██║██║     ██║  ██║███████╗   ██║
© Brandon Skerritt
Github: brandonskerritt
"""
from copy import copy
from distutils import util
from typing import Optional, Dict, Union, Set, List

import re

from loguru import logger
import ciphey
import cipheycore

from ciphey.iface import ParamSpec, Cracker, CrackResult, T, CrackInfo, registry
from ciphey.common import fix_case


@registry.register
class Vigenere(ciphey.iface.Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        if self.keysize is not None:
            analysis = self.cache.get_or_update(
                ctext,
                f"vigenere::{self.keysize}",
                lambda: cipheycore.analyse_string(ctext.lower(), self.keysize, self.group),
            )

            return CrackInfo(
                success_likelihood=cipheycore.vigenere_detect(analysis, self.expected),
                # TODO: actually calculate runtimes
                success_runtime=1e-4,
                failure_runtime=1e-4,
            )

        likely_lens = self.cache.get_or_update(
            ctext,
            f"vigenere::likely_lens",
            lambda: cipheycore.vigenere_likely_key_lens(ctext.lower(), self.expected, self.group, self.p_value),
        )

        for keysize in likely_lens:
            # Store the analysis
            analysis = self.cache.get_or_update(
                ctext, f"vigenere::{keysize.len}", lambda: keysize.tab
            )
        if len(likely_lens) == 0:
            return CrackInfo(
                success_likelihood=0,
                # TODO: actually calculate runtimes
                success_runtime=2e-4,
                failure_runtime=2e-4,
            )

        return CrackInfo(
            success_likelihood=0 * likely_lens[0].p_value,
            # TODO: actually calculate runtimes
            success_runtime=2e-4,
            failure_runtime=2e-4,
        )

    @staticmethod
    def getTarget() -> str:
        return "vigenere"

    def crackOne(
        self, ctext: str, analysis: cipheycore.windowed_analysis_res, real_ctext: str
    ) -> List[CrackResult]:
        possible_keys = cipheycore.vigenere_crack(
            analysis, self.expected, self.group, self.p_value
        )
        logger.trace(
            f"Vigenere crack got keys: {[[i for i in candidate.key] for candidate in possible_keys]}"
        )
        # if len(possible_keys) and possible_keys[0].p_value < 0.9999999:
        #     raise 0
        return [
            CrackResult(
                value=fix_case(cipheycore.vigenere_decrypt(ctext, candidate.key, self.group), real_ctext),
                key_info="".join([self.group[i] for i in candidate.key]),
            )
            for candidate in possible_keys[: min(len(possible_keys), 10)]
        ]

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logger.debug("Trying vigenere cipher")
        # Convert it to lower case
        if self.lower:
            message = ctext.lower()
        else:
            message = ctext

        # Analysis must be done here, where we know the case for the cache
        if self.keysize is not None:
            return self.crackOne(
                message,
                self.cache.get_or_update(
                    ctext,
                    f"vigenere::{self.keysize}",
                    lambda: cipheycore.analyse_string(message, self.keysize, self.group),
                ),
                ctext
            )
        else:
            arrs = []
            likely_lens = self.cache.get_or_update(
                ctext,
                f"vigenere::likely_lens",
                lambda: cipheycore.vigenere_likely_key_lens(message, self.expected, self.group),
            )
            possible_lens = [i for i in likely_lens]
            possible_lens.sort(key=lambda i: i.p_value)
            logger.trace(f"Got possible lengths {[i.len for i in likely_lens]}")
            # TODO: work out length
            for i in possible_lens:
                arrs.extend(
                    self.crackOne(
                        message,
                        self.cache.get_or_update(
                            ctext,
                            f"vigenere::{i.len}",
                            lambda: cipheycore.analyse_string(message, i.len, self.group),
                        ),
                        ctext
                    )
                )

            logger.debug(f"Vigenere returned {len(arrs)} candidates")
            return arrs

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "group": ciphey.iface.ParamSpec(
                desc="An ordered sequence of chars that make up the caesar cipher alphabet",
                req=False,
                default="abcdefghijklmnopqrstuvwxyz",
            ),
            "lower": ciphey.iface.ParamSpec(
                desc="Whether or not the ciphertext should be converted to lowercase first",
                req=False,
                default=True,
            ),
            "keysize": ciphey.iface.ParamSpec(
                desc="A key size that should be used. If not given, will attempt to work it out",
                req=False,
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for windowed frequency analysis",
                req=False,
                default=0.01,
            ),
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.lower: Union[str, bool] = self._params()["lower"]
        if type(self.lower) != bool:
            self.lower = util.strtobool(self.lower)
        self.group = list(self._params()["group"])
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.keysize = self._params().get("keysize")
        if self.keysize is not None:
            self.keysize = int(self.keysize)
        self.p_value = float(self._params()["p_value"])
        self.MAX_KEY_LENGTH = 16
