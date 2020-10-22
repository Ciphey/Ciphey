import re
from typing import Dict, List, Optional

from loguru import logger

from ciphey.iface import (
    Config,
    Cracker,
    CrackInfo,
    CrackResult,
    ParamSpec,
    Translation,
    registry,
)


@registry.register
class Soundex(Cracker[str]):
    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1,
            success_runtime=1e-5,
            failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "soundex"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:
        """
        Attempts to crack Soundex by generating all possible combinations.
        """
        logger.trace("Attempting Soundex cracker")
        word_list = []
        sentences = []
        result = []

        # Convert to uppercase and replace delimiters and whitespace with nothing
        ctext = re.sub(r"[,;:\-\s]", "", ctext.upper())

        # Make sure ctext contains only A-Z and 0-9
        if bool(re.search(r"[^A-Z0-9]", ctext)) is True:
            logger.trace("Failed to crack soundex due to non soundex character(s)")
            return None

        # Make sure ctext is divisible by 4
        ctext_len = len(ctext)
        if ctext_len % 4:
            logger.trace(
                f"Failed to decode Soundex because length must be a multiple of 4, not '{ctext_len}'"
            )
            return None

        # Split ctext into groups of 4
        ctext = " ".join(ctext[i : i + 4] for i in range(0, len(ctext), 4))
        ctext_split = ctext.split(" ")
        soundex_keys = self.SOUNDEX_DICT.keys()

        # Find all words that correspond to each given soundex code
        for code in ctext_split:
            if code in soundex_keys:
                word_list.append(self.SOUNDEX_DICT[code])

        logger.debug(f"Possible words for given encoded text: {word_list}")

        # Find all possible sentences
        self.getSentenceCombo(
            word_list,
            sentences,
            self.frequency_dict,
            self.sentence_freq,
            self.word_freq,
        )

        sorted_sentences = self.sortlistwithdict(sentences, self.frequency_dict)

        for sentence in sorted_sentences:
            result.append(CrackResult(value=sentence))

        logger.trace(f"Soundex cracker - Returning results: {result}")
        return result

    def sortlistwithdict(self, listtosort, hashes):
        """
        This function uses the sum of ranks (based on frequency) of each word in each
        sentence and sorts them according to it.
        """
        return sorted(listtosort, key=lambda x: hashes[x])

    def getSentenceCombo(
        self, A, sentences, frequency_dict, sentence_freq, word_freq, result="", n=0
    ):
        """
        This function uses recursion to generate a list of sentences from all possible
        words for a given set of soundex codes.
        """
        logger.trace("Creating all possible sentences from Soundex")
        if n == len(A):
            sentences.append(result[1:])
            for word in result[1:].split():
                # Adding the rank of each word to find out the sentence's net frequency
                if word in word_freq:
                    sentence_freq += word_freq.index(word)
                # If the word isn't in the frequency list then it's a very uncommon word
                # so we add a large number (5000)
                else:
                    sentence_freq += 5000
            frequency_dict[result[1:]] = sentence_freq
            sentence_freq = 0
            return

        for word in A[n]:
            out = result + " " + word
            self.getSentenceCombo(
                A, sentences, frequency_dict, sentence_freq, word_freq, out, n + 1
            )

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The Soundex dictionary to use",
                req=False,
                default="cipheydists::translate::soundex",
            ),
            "freq": ParamSpec(
                desc="The word frequency dictionary to use",
                req=False,
                default="cipheydists::list::English5000Freq",
            ),
        }

    def __init__(self, config: Config):
        super().__init__(config)
        self.SOUNDEX_DICT = config.get_resource(self._params()["dict"], Translation)
        self.word_freq = config.get_resource(self._params()["freq"], Translation)
        self.frequency_dict = {}
        self.sentence_freq = 0
