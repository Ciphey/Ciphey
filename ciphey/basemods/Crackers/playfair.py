# community
# by https://github.com/RotationMatrix

from distutils import util
from typing import Optional, Dict, Union, Set, List
from random import randint, shuffle
import math
import string

from loguru import logger
import ciphey
import cipheydists

from ciphey.iface import ParamSpec, CrackResult, T, CrackInfo, registry, Translation


def count_bigrams(str):
    """Count bigrams which appear in `str`.
    >>> count_bigrams("hello")
    {'he': 1, 'el': 1, 'll': 1, 'lo': 1}
    """
    table = str.maketrans('', '',
                    string.digits +
                    string.punctuation +
                    string.whitespace
                    )
    str = str.translate(table).lower()

    freq = {}
    for (i, c) in enumerate(str[:-1]):
        try:
            freq[c + str[i + 1]] += 1
        except KeyError:
            freq[c + str[i + 1]] = 1

    return freq


def decrypt(ctext: str, ktable: str) -> str:
    """Decrypt a Playfair message given the ciphertext and key table.
    >>> decrypt(
    ...  "kgyvrv kf qpeg cn ihh pti r pcem ivo pqb fyulah pti odkuku",
    ...  "playfirbcdeghkmnoqstuvwxz"
    ... )
    'hello my name is bee and i like dog and apple and tree'
    """
    ptext = ""
    index = 0
    while index < len(ctext):
        index_a = index
        while not ctext[index_a].isalpha():
            ptext += ctext[index_a]
            index_a += 1

        index_b = index_a + 1
        while not ctext[index_b].isalpha():
            ptext += ctext[index_b]
            index_b += 1

        index = index_b + 1

        a_i = ktable.index(ctext[index_a].casefold())
        b_i = ktable.index(ctext[index_b].casefold())

        # Same column, shift up.
        if a_i % 5 == b_i % 5:
            # Insert A at `index_a` instead of appending. There may be
            # non-alphabetic characters adding from shifting `index_b`.
            if math.floor(a_i / 5) == 0:
                ptext = ptext[:index_a] + ktable[a_i % 5 + 20] + ptext[index_a:]
            else:
                ptext = ptext[:index_a] + ktable[a_i - 5] + ptext[index_a:]

            if math.floor(b_i / 5) == 0:
                ptext += ktable[b_i % 5 + 20]
            else:
                ptext += ktable[b_i - 5]

        # Same row, shift left.
        elif math.floor(a_i / 5) == math.floor(b_i / 5):
            # Insert A at `index_a` instead of appending. There may be
            # non-alphabetic characters adding from shifting `index_b`.
            if a_i % 5 == 0:
                ptext = ptext[:index_a] + ktable[a_i + 4] + ptext[index_a:]
            else:
                ptext = ptext[:index_a] + ktable[a_i - 1] + ptext[index_a:]

            if b_i % 5 == 0:
                ptext += ktable[b_i + 4]
            else:
                ptext += ktable[b_i - 1]

        # Rectangle, swap corners, same rows.
        else:
            # Insert A at `index_a` instead of appending. There may be
            # non-alphabetic characters adding from shifting `index_b`.
            ptext = (
                ptext[:index_a]
                + ktable[math.floor(a_i / 5) * 5 + b_i % 5]
                + ptext[index_a:]
            )
            ptext += ktable[math.floor(b_i / 5) * 5 + a_i % 5]

    # Remove trailing pad if it exists.
    ptext = ptext.removesuffix("x")

    # Record padding characters separating repeated digraphs (e.g. ee, bb, aa.)
    padding_chars = []
    x_pos = 0
    # FIXME: This does not consider non-alphabetic characters like we do above.
    # 2021-04-22
    while x_pos != -1:
        # Advance one so we do not get stuck looping on the same character.
        x_pos += 1
        # Find the next x in our plaintext if any.
        # TODO: Detect use of other padding characters such as Q. 2021-04-18
        x_pos = ptext.find("x", x_pos)

        if x_pos % 2 == 1 and ptext[x_pos - 1] == ptext[x_pos + 1]:
            padding_chars.append(x_pos)

    # Remove the padding characters.
    for (offset, x_pos) in enumerate(padding_chars):
        # Offset by the number of padding characters removed to handle
        # shifting indices.
        ptext = ptext[: x_pos - offset] + ptext[x_pos - offset + 1 :]

    return ptext


def random_swap(ktable: str) -> str:
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


@registry.register
class Playfair(ciphey.iface.Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        if self.lower:
            message = ctext.lower()
        else:
            message = ctext

        table = str.maketrans('', '',
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

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        logger.debug("Trying playfair cipher")
        # Convert it to upper case for scoring
        #
        # TODO: handle different alphabets
        message = ctext.upper()

        # We do not handle any ciphertext with "j".
        if 'J' in message:
            return None

        logger.trace("Beginning cipheycore simple analysis")
        alphabet = [
            "a", "b", "c", "d", "e",
            "f", "g", "h", "i", "k",
            "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

        logger.trace("Beginning ciphey.playfair")
        # possible_keys = []

        best_key = alphabet
        shuffle(best_key)
        # TODO: Count bigrams for frequency analysis. 2020-10-25
        key_p_value = self.score(
            count_bigrams(decrypt(message, best_key)))

        # Threshold Acceptance algorithm (similar to Simulated Annealing)
        threshold = 1.0
        while threshold > 0:
            new_key = random_swap(best_key)
            new_score = self.score(
                count_bigrams(decrypt(message, new_key)))

            if (new_score >= key_p_value * (1.0 - threshold)):
                print(''.join(new_key), new_score)

                best_key = new_key
                key_p_value = new_score

            threshold -= 0.00002

        # n_candidates = len(possible_keys)
        # logger.debug(f"Playfair returned {n_candidates} candidates")

        # candidates = []

        # for candidate in possible_keys:
        #     plaintext = decrypt(message, candidate)
        #     candidates.append(CrackResult(
        #         value=plaintext, key_info=''.join(candidate)))

        # return candidates
        return [CrackResult(value=decrypt(ctext, best_key), key_info=''.join(best_key))]

    def score(self, observed):
        score = 0.0
        total = 0
        for (k, v) in observed.items():
            total += v
            try:
                score += self.dist[k] * v
            except:
                pass

        if total <= 0:
            total = 1

        score /= total
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

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dist": ciphey.iface.ParamSpec(
                desc="The bigram distribution to use",
                req=False,
                default="cipheydists::dist::bigrams",
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
        self.dist = config.get_resource(
            self._params()["dist"], Translation)
        self.cache = config.cache
        self.p_value = self._params()["p_value"]
