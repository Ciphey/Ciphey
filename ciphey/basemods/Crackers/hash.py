"""
his is Hashbuster but slightly modified to work with Ciphey
why reivent the wheel?
Changes (that I can remember)
* timeout set, as hashbuster took AGES before timeout was set.
https://github.com/s0md3v/Hash-Buster
"""


import re
import os
import argparse
import requests
import concurrent.futures

from loguru import logger
from typing import Optional, Dict, Union, Set, List, Any

from loguru import logger

import ciphey
from ciphey.iface import ParamSpec, CrackResult, T, CrackInfo, registry

thread_count = 4


def alpha(ctext, hashtype):
    return None


def beta(ctext, hashtype):
    try:
        response = requests.get(
            "https://hashtoolkit.com/reverse-hash/?hash=", ctext, timeout=5
        ).text
    except requests.exceptions.ReadTimeout as e:
        logger.debug(f"Beta failed timeout {e}")
    match = re.search(r'/generate-hash/?text=.*?"', response)
    if match:
        return match.group(1)
    else:
        return None


def gamma(ctext, hashtype):
    try:
        response = requests.get(
            "https://www.nitrxgen.net/md5db/" + ctext, timeout=5
        ).text
    except requests.exceptions.ReadTimeout as e:
        logger.debug(f"Gamma failed with {e}")
    if response:
        return response
    else:
        return None


def delta(ctext, hashtype):
    return None


def theta(ctext, hashtype):
    try:
        response = requests.get(
            "https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"
            % (ctext, hashtype),
            timeout=5,
        ).text
    except requests.exceptions.ReadTimeout as e:
        logger.debug(f"Gamma failed with {e}")
    if len(response) != 0:
        return response
    else:
        return None


md5 = [gamma, alpha, beta, theta, delta]
sha1 = [alpha, beta, theta, delta]
sha256 = [alpha, beta, theta]
sha384 = [alpha, beta, theta]
sha512 = [alpha, beta, theta]


result = {}


def crack(ctext):
    raise ("Error Crack is called")


def threaded(ctext):
    resp = crack(ctext)
    if resp:
        print(ctext + " : " + resp)
        result[ctext] = resp


@registry.register
class HashBuster(ciphey.iface.Cracker[str]):
    @staticmethod
    def getTarget() -> str:
        return "hash"

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def priority() -> float:
        return 0.05

    def getInfo(self, ctext: T) -> CrackInfo:
        # TODO calculate these properly
        return CrackInfo(success_likelihood=0.5, success_runtime=5, failure_runtime=5,)

    def attemptCrack(self, ctext: T) -> List[CrackResult]:
        logger.debug(f"Starting to crack hashes")
        result = False

        candidates = []
        if len(ctext) == 32:
            for api in md5:
                r = api(ctext, "md5")
                if result is not None or r is not None:
                    logger.trace("MD5 returns True {r}")
                    candidates.append(result, "MD5")
        elif len(ctext) == 40:
            for api in sha1:
                r = api(ctext, "sha1")
                if result is not None and r is not None:
                    logger.trace("sha1 returns true")
                    candidates.append(result, "SHA1")
        elif len(ctext) == 64:
            for api in sha256:
                r = api(ctext, "sha256")
                if result is not None and r is not None:
                    logger.trace("sha256 returns true")
                    candidates.append(result, "SHA256")
        elif len(ctext) == 96:
            for api in sha384:
                r = api(ctext, "sha384")
                if result is not None and r is not None:
                    logger.trace("sha384 returns true")
                    candidates.append(result, "SHA384")
        elif len(ctext) == 128:
            for api in sha512:
                r = api(ctext, "sha512")
                if result is not None and r is not None:
                    logger.trace("sha512 returns true")
                    candidates.append(result, "SHA512")

        # TODO what the fuck is this code?
        logger.trace(f"Hash buster returning {result}")
        # TODO add to 5.1 make this return multiple possible candidates
        return [CrackResult(value=candidates[0][0], misc_info=candidates[1][1])]

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
