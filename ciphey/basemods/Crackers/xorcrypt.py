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
import base64

from loguru import logger
import ciphey
import cipheycore

from ciphey.iface import ParamSpec, Cracker, CrackResult, T, CrackInfo, registry


@registry.register
class XorCrypt(ciphey.iface.Cracker[bytes]):
    def getInfo(self, ctext: bytes) -> CrackInfo:
        if self.keysize is not None:
            analysis = self.cache.get_or_update(
                ctext,
                f"xorcrypt::{self.keysize}",
                lambda: cipheycore.analyse_string(ctext, self.keysize, self.group),
            )

            return CrackInfo(
                success_likelihood=cipheycore.xorcrypt_detect(analysis, self.expected),
                # TODO: actually calculate runtimes
                success_runtime=1e-4,
                failure_runtime=1e-4,
            )

        keysize = self.cache.get_or_update(
            ctext,
            f"xorcrypt::likely_lens",
            lambda: cipheycore.xorcrypt_guess_len(ctext),
        )

        if keysize == 1:
            return CrackInfo(
                success_likelihood=0,
                # TODO: actually calculate runtimes
                success_runtime=2e-3,
                failure_runtime=2e-2,
            )

        return CrackInfo(
            success_likelihood=0.9, # Dunno, but it's quite likely
            # TODO: actually calculate runtimes
            success_runtime=2e-3,
            failure_runtime=2e-2,
        )

    @staticmethod
    def getTarget() -> str:
        return "xorcrypt"

    def crackOne(
        self, ctext: bytes, analysis: cipheycore.windowed_analysis_res
    ) -> List[CrackResult]:
        possible_keys = cipheycore.xorcrypt_crack(
            analysis, self.expected, self.p_value
        )

        logger.trace(f"xorcrypt crack got keys: {[[i for i in candidate.key] for candidate in possible_keys]}")
        return [
            CrackResult(
                value=cipheycore.xorcrypt_decrypt(ctext, candidate.key),
                key_info="0x" + "".join(["{:02x}".format(i) for i in candidate.key]),
            )
            for candidate in possible_keys[:min(len(possible_keys), 10)]
        ]

    def attemptCrack(self, ctext: bytes) -> List[CrackResult]:
        logger.debug(f"Trying xorcrypt cipher on {base64.b64encode(ctext)}")

        # Analysis must be done here, where we know the case for the cache
        if self.keysize is not None:
            return self.crackOne(
                ctext,
                self.cache.get_or_update(
                    ctext,
                    f"xorcrypt::{self.keysize}",
                    lambda: cipheycore.analyse_bytes(ctext, self.keysize),
                ),
            )
        else:
            len = self.cache.get_or_update(
                ctext,
                f"xorcrypt::likely_lens",
                lambda: cipheycore.xorcrypt_guess_len(ctext),
            )

            logger.trace(f"Got possible length {len}")

            if len < 2:
                return []

            ret = []
            # Fuzz around
            for i in range(min(len - 2, 2), len + 2):
                ret += self.crackOne(
                    ctext,
                    self.cache.get_or_update(
                        ctext,
                        f"xorcrypt::{len}",
                        lambda: cipheycore.analyse_bytes(ctext, len),
                    )
                )

            return ret

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "keysize": ciphey.iface.ParamSpec(
                desc="A key size that should be used. If not given, will attempt to work it out",
                req=False,
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for windowed frequency analysis",
                req=False,
                default=0.001,
            ),
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.expected = config.get_resource(self._params()["expected"])
        self.cache = config.cache
        self.keysize = self._params().get("keysize")
        if self.keysize is not None:
            self.keysize = int(self.keysize)
        self.p_value = self._params()["p_value"]
        self.MAX_KEY_LENGTH = 16