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
from typing import Optional, Dict, Any

from loguru import logger

import ciphey
from ciphey.iface import registry

thread_count = 4


def alpha(hashvalue, hashtype):
    return None


def beta(hashvalue, hashtype):
    try:
        response = requests.get(
            "https://hashtoolkit.com/reverse-hash/?hash=", hashvalue, timeout=5
        ).text
    except requests.exceptions.ReadTimeout as e:
        logger.debug(f"Beta failed timeout {e}")
    match = re.search(r'/generate-hash/?text=.*?"', response)
    if match:
        return match.group(1)
    else:
        return None


def gamma(hashvalue, hashtype):
    try:
        response = requests.get(
            "https://www.nitrxgen.net/md5db/" + hashvalue, timeout=5
        ).text
    except requests.exceptions.ReadTimeout as e:
        logger.debug(f"Gamma failed with {e}")
    if response:
        return response
    else:
        return None


def delta(hashvalue, hashtype):
    # data = {'auth':'8272hgt', 'hash':hashvalue, 'string':'','Submit':'Submit'}
    # response = requests.post('http://hashcrack.com/index.php' , data).text
    # match = re.search(r'<span class=hervorheb2>(.*?)</span></div></TD>', response)
    # if match:
    #    return match.group(1)
    # else:
    return None


def theta(hashvalue, hashtype):
    try:
        response = requests.get(
            "https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"
            % (hashvalue, hashtype),
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


def crack(hashvalue):

    logger.debug(f"Starting to crack hashes")
    result = False
    if len(hashvalue) == 32:
        for api in md5:
            r = api(hashvalue, "md5")
            if result is not None or r is not None:
                logger.trace("MD5 returns True {r}")
                return result
    elif len(hashvalue) == 40:
        for api in sha1:
            r = api(hashvalue, "sha1")
            if result is not None and r is not None:
                logger.trace("sha1 returns true")
                return result
    elif len(hashvalue) == 64:
        for api in sha256:
            r = api(hashvalue, "sha256")
            if result is not None and r is not None:
                logger.trace("sha256 returns true")
                return result
    elif len(hashvalue) == 96:
        for api in sha384:
            r = api(hashvalue, "sha384")
            if result is not None and r is not None:
                logger.trace("sha384 returns true")
                return result
    elif len(hashvalue) == 128:
        for api in sha512:
            r = api(hashvalue, "sha512")
            if result is not None and r is not None:
                logger.trace("sha512 returns true")
                return result

    logger.debug(f"Returning None packet")
    return None


result = {}


def threaded(hashvalue):
    resp = crack(hashvalue)
    if resp:
        print(hashvalue + " : " + resp)
        result[hashvalue] = resp


@registry.register
class HashBuster(ciphey.iface.Decoder[str, bytes]):
    @staticmethod
    def getTarget() -> str:
        return "hash"

    def decode(self, text: str) -> Optional[bytes]:
        result = crack(text)
        logger.trace(f"Hash buster returning {result}")
        return result

    @staticmethod
    def getParams() -> Optional[Dict[str, Dict[str, Any]]]:
        pass

    @staticmethod
    def priority() -> float:
        return 0.4

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
