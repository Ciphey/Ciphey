# community
# by https://github.com/RotationMatrix

from distutils import util
from typing import Optional, Dict, Union, Set, List
from random import randint, shuffle
import math
import string

from loguru import logger
import ciphey
import cipheycore
import cipheydists

from ciphey.iface import ParamSpec, CrackResult, T, CrackInfo, registry, Translation


@registry.register
class Playfair(ciphey.iface.Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        if self.lower:
            message = ctext.lower()
        else:
            message = ctext

        table = str.maketrans('', '',
                              string.ascii_uppercase +
                              string.digits +
                              string.punctuation +
                              string.whitespace
                              )
        message = message.translate(table)

        success_likelihood = 0.15  # TODO: Log traces when likelihood goes 0. 2020-10-25

        # message must contain an even number of letters if it's playfair.
        if len(message) % 2 != 0:
            success_likelihood = 0.

        # No playfair ciphertext may contain more than 25 Latin characters.
        if 'j' in message:
            success_likelihood = 0.

        return CrackInfo(
            success_likelihood=success_likelihood,
            # TODO: actually calculate runtimes
            success_runtime=1e-4,
            failure_runtime=1e-4,
        )

    @staticmethod
    def getTarget() -> str:
        return "playfair"

    def decrypt(self, ctext: str, ktable: str) -> str:
        def digraphs(seq):
            return (seq[i:i + 2] for i in range(0, len(seq), 2))

        ptext = ""
        for d in digraphs(ctext):
            a_i = ktable.index(d[0])
            b_i = ktable.index(d[1])

            # Same column, shift up.
            if a_i % 5 == b_i % 5:
                if math.floor(a_i / 5) == 0:
                    ptext += ktable[a_i % 5 + 20]
                else:
                    ptext += ktable[a_i - 5]

                if math.floor(b_i / 5) == 0:
                    ptext += ktable[b_i % 5 + 20]
                else:
                    ptext += ktable[b_i - 5]

            # Same row, shift left.
            elif math.floor(a_i / 5) == math.floor(b_i / 5):
                if a_i % 5 == 0:
                    ptext += ktable[a_i + 4]
                else:
                    ptext += ktable[a_i - 1]

                if b_i % 5 == 0:
                    ptext += ktable[b_i + 4]
                else:
                    ptext += ktable[b_i - 1]

            # Rectangle, swap corners, same rows.
            else:
                ptext += ktable[math.floor(a_i / 5) * 5 + b_i % 5]
                ptext += ktable[math.floor(b_i / 5) * 5 + a_i % 5]

        return ptext

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logger.debug("Trying playfair cipher")
        # Convert it to lower case
        #
        # TODO: handle different alphabets
        if self.lower:
            message = ctext.lower()
        else:
            message = ctext

        # We do not handle any ciphertext with "j".
        if 'j' in message:
            return None

        # Filter out anything except lowercase latin letters.
        table = str.maketrans('', '',
                              string.ascii_uppercase +
                              string.digits +
                              string.punctuation +
                              string.whitespace
                              )
        message = message.translate(table)

        print("Gate 1")

        logger.trace("Beginning cipheycore simple analysis")
        alphabet = [
            "a", "b", "c", "d", "e",
            "f", "g", "h", "i", "k",
            "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

        logger.trace("Beginning ciphey.playfair")
        possible_keys = []

        ktable = alphabet
        shuffle(ktable)
        # TODO: Count bigrams for frequency analysis. 2020-10-25
        # analysis = self.count_bigrams(self.decrypt(message, ktable))
        # analysis = cipheycore.analyse_string(self.decrypt(message, ktable))
        # key_p_value = math.pow(cipheycore.chisq_test(analysis, self.expected), 2)
        key_p_value = math.pow(self.score(
            self.count_bigrams(self.decrypt(message, ktable))), 3)

        print("Gate 2")

        # Threshold Acceptance algorithm (similar to Simulated Annealing)
        r_max = 1000
        threshold = 0.2
        for _r in range(r_max):
            new_score = 0.0
            for _i in range(600):
                new_key = self.random_swap(ktable)
                new_score = math.pow(self.score(
                    self.count_bigrams(self.decrypt(message, new_key))), 3)
                # ptext = self.decrypt(message, new_key)
                # analysis = cipheycore.analyse_string(ptext)
                # new_score = math.pow(cipheycore.chisq_test(analysis, self.expected), 2)

                if (new_score > key_p_value * (1 - threshold)):
                    ktable = new_key
                    key_p_value = new_score

                if new_score >= self.p_value:
                    possible_keys.append(new_key)
                    print(new_score, ''.join(new_key))

            threshold -= 0.0002

        print("Gate 3")

        # ktable = [
        #     "p","l","a","y","f",
        #     "i","r","b","c","d",
        #     "e","g","h","k","m",
        #     "n","o","q","s","t",
        #     "u","v","w","x","z"
        # ]

        # possible_keys.append(ktable)
        # ptext = finalize_ptext(self.decrypt(message, possible_keys[0]), ctext)
        # print(ptext)
        # analysis = cipheycore.analyse_string(decrypt(message, ktable))
        # print(cipheycore.chisq_test(analysis, self.expected))
        # print(self.score(self.count_bigrams(ptext)))

        print("Gate 4")

        n_candidates = len(possible_keys)
        logger.debug(f"Playfair returned {n_candidates} candidates")

        candidates = []

        for candidate in possible_keys:
            plaintext = self.finalize(self.decrypt(message, candidate), ctext)
            candidates.append(CrackResult(
                value=plaintext, key_info=''.join(candidate)))

        return candidates

    def count_bigrams(self, str):
        freq = {}
        lower = str.lower()
        for (i, c) in enumerate(lower[:-1]):
            try:
                freq[c + str[i+1]] += 1
            except KeyError:
                freq[c + str[i+1]] = 1

        return freq

    def score(self, observed):
        score = 0.0
        for (k, v) in observed:
            try:
                score += self.expected[k] * v
            except:
                pass

        score /= len(observed)
        return score

    def finalize(self, ptext, ctext):
        """
        Inserts whitespace, punctuation and other characters which were removed prior to decryption.
        Also removes padding "X"s within the plaintext.
        """
        ret = ""
        offset = 0
        for (i, c) in enumerate(ctext):
            if c.lower() in "abcdefghiklmnopqrstuvwxyz":
                # TODO: Drop padding Xs. 2020-10-26
                # ptext_i = i - offset
                # if ptext[ptext_i] == 'x' and ptext_i < len(ptext) - 1 and ptext[ptext_i - 1] == ptext[ptext_i + 1]:
                #     # Drop the padding x and reduce the offset by one.
                #     offset -= 1
                # else:
                ret += ptext[i - offset]
            else:
                ret += c
                offset += 1

        return ret

    def random_swap(self, ktable: str) -> str:
        """
        Randomly swaps two characters in the key table.
        """
        a = randint(0, 24)
        b = randint(0, 23)

        if a == b:
            b += 1

        swap = ktable[a]
        ktable[a] = ktable[b]
        ktable[b] = swap

        return ktable

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "expected": ciphey.iface.ParamSpec(
                desc="The expected distribution of the plaintext",
                req=False,
                config_ref=["default_dist"],
            ),
            "group": ciphey.iface.ParamSpec(
                desc="An ordered sequence of chars that make up the playfair cipher alphabet",
                req=False,
                default="abcdefghiklmnopqrstuvwxyz",
            ),
            "lower": ciphey.iface.ParamSpec(
                desc="Whether or not the ciphertext should be converted to lowercase first",
                req=False,
                default=True,
            ),
            "p_value": ciphey.iface.ParamSpec(
                desc="The p-value to use for standard frequency analysis",
                req=False,
                default=0.01,
            )
            # TODO: add "filter" param
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.lower: Union[str, bool] = self._params()["lower"]
        if type(self.lower) != bool:
            self.lower = util.strtobool(self.lower)
        self.group = list(self._params()["group"])
        self.expected = config.get_resource(
            self._params()["expected"], Translation)
        self.cache = config.cache
        self.p_value = self._params()["p_value"]