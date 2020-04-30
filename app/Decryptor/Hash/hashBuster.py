"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt

This is Hashbuster but slightly modified to work with Ciphey
why reivent the wheel?

https://github.com/s0md3v/Hash-Buster
"""


import re
import os
import requests
import argparse
import concurrent.futures

thread_count = 4


def alpha(hashvalue, hashtype):
    return False


def beta(hashvalue, hashtype):
    response = requests.get(
        "https://hashtoolkit.com/reverse-hash/?hash=", hashvalue
    ).text
    match = re.search(r'/generate-hash/?text=.*?"', response)
    if match:
        return match.group(1)
    else:
        return False


def gamma(hashvalue, hashtype):
    response = requests.get("https://www.nitrxgen.net/md5db/" + hashvalue).text
    if response:
        return response
    else:
        return False


def delta(hashvalue, hashtype):
    # data = {'auth':'8272hgt', 'hash':hashvalue, 'string':'','Submit':'Submit'}
    # response = requests.post('http://hashcrack.com/index.php' , data).text
    # match = re.search(r'<span class=hervorheb2>(.*?)</span></div></TD>', response)
    # if match:
    #    return match.group(1)
    # else:
    return False


def theta(hashvalue, hashtype):
    response = requests.get(
        "https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"
        % (hashvalue, hashtype)
    ).text
    if len(response) != 0:
        return response
    else:
        return False


md5 = [gamma, alpha, beta, theta, delta]
sha1 = [alpha, beta, theta, delta]
sha256 = [alpha, beta, theta]
sha384 = [alpha, beta, theta]
sha512 = [alpha, beta, theta]


def crack(hashvalue):
    result = False
    if len(hashvalue) == 32:
        for api in md5:
            r = api(hashvalue, "md5")
            if r:
                return {
                    "lc": None,
                    "IsPlaintext?": True,
                    "Plaintext": r,
                    "Cipher": "md5",
                    "Extra Information": None,
                }
    elif len(hashvalue) == 40:
        for api in sha1:
            r = api(hashvalue, "sha1")
            if r:
                return {
                    "lc": None,
                    "IsPlaintext?": True,
                    "Plaintext": r,
                    "Cipher": "sha1",
                    "Extra Information": None,
                }
    elif len(hashvalue) == 64:
        for api in sha256:
            r = api(hashvalue, "sha256")
            if r:
                return {
                    "lc": None,
                    "IsPlaintext?": True,
                    "Plaintext": r,
                    "Cipher": "sha256",
                    "Extra Information": None,
                }
    elif len(hashvalue) == 96:
        for api in sha384:
            r = api(hashvalue, "sha384")
            if r:
                return {
                    "lc": None,
                    "IsPlaintext?": True,
                    "Plaintext": r,
                    "Cipher": "sha384",
                    "Extra Information": None,
                }
    elif len(hashvalue) == 128:
        for api in sha512:
            r = api(hashvalue, "sha512")
            if r:
                return {
                    "lc": None,
                    "IsPlaintext?": True,
                    "Plaintext": r,
                    "Cipher": "sha512",
                    "Extra Information": None,
                }
    else:
        return {
            "lc": None,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": None,
            "Extra Information": "The hash wasn't found. Please try Hashkiller.co.uk first, then use Hashcat to manually crack the hash.",
        }


result = {}


def threaded(hashvalue):
    resp = crack(hashvalue)
    if resp:
        print(hashvalue + " : " + resp)
        result[hashvalue] = resp


def grepper(directory):
    os.system(
        """grep -Pr "[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" %s --exclude=\*.{png,jpg,jpeg,mp3,mp4,zip,gz} |
        grep -Po "[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" >> %s/%s.txt"""
        % (directory, cwd, directory.split("/")[-1])
    )
    print("%s Results saved in %s.txt" % (info, directory.split("/")[-1]))


def miner(file):
    lines = []
    found = set()
    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip("\n"))
    for line in lines:
        matches = re.findall(
            r"[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}", line
        )
        if matches:
            for match in matches:
                found.add(match)
    print("%s Hashes found: %i" % (info, len(found)))
    threadpool = concurrent.futures.ThreadPoolExecutor(max_workers=thread_count)
    futures = (threadpool.submit(threaded, hashvalue) for hashvalue in found)
    for i, _ in enumerate(concurrent.futures.as_completed(futures)):
        if i + 1 == len(found) or (i + 1) % thread_count == 0:
            print("%s Progress: %i/%i" % (info, i + 1, len(found)), end="\r")


def single(args):
    result = crack(args.hash)
    if result:
        print(result)
    else:
        print("%s Hash was not found in any database." % bad)
