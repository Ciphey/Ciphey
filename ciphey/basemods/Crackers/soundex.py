from typing import Optional, Dict, List
from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry, CrackInfo, CrackResult, Translation
from loguru import logger
import ciphey
import cipheycore

def sortlistwithdict(listtosort, hashes):
    """
    This function uses the sum of ranks (based on frequency) of each word in each
    sentence and sorts them according to it.
    """
    return sorted(listtosort, key=lambda x: hashes[x])

def getSentenceCombo(A, sentences, frequency_dict, sentence_freq, word_freq, result="", n=0):
    """
    This function uses recursion to generate a list of sentences from all possible
    words for a given set of soundex codes.
    """
    logger.trace("Creating all possible sentences")
    if n == len(A):
        sentences.append(result[1:])
        for word in result[1:].split():
            # Adding the rank of each word to find out sentence's net frequency
            if word in word_freq:
                sentence_freq += word_freq.index(word)
            # If the word isnt in the frequency list then its a very uncommon word
            # so we add a large number (5000)
            else:
                sentence_freq += 5000
        frequency_dict[result[1:]] = sentence_freq
        sentence_freq = 0
        return 

    for word in A[n]:
        out = result + " " + word  
        getSentenceCombo(A, sentences, frequency_dict, sentence_freq, word_freq, out, n + 1)


@registry.register
class Soundex(ciphey.iface.Cracker[str]):

    def getInfo(self, ctext: str) -> CrackInfo:
        return CrackInfo(
            success_likelihood=0.1, success_runtime=1e-5, failure_runtime=1e-5,
        )

    @staticmethod
    def getTarget() -> str:
        return "soundex"

    def attemptCrack(self, ctext: str) -> List[CrackResult]:

        logger.debug(f"Trying the soundex cracker on {ctext}")

        word_list = []
        codes = ctext.split()

        # Find all words that correspond to each given soundex code
        for code in codes:
            if len(code) != 4:
                return None
            word_list.append(self.soundex_dict[code.upper()])
            

        logger.debug(f"Possible words for given encrypted text : {word_list}")
        sentences = []

        # Find all possible sentences
        getSentenceCombo(word_list, sentences, self.frequency_dict, self.sentence_freq, self.word_freq)

        
        sorted_sentences = sortlistwithdict(sentences, self.frequency_dict)
        
        cracked_result = []
        for sentence in sorted_sentences:
            cracked_result.append(CrackResult(value=sentence))

        logger.trace(f"Soundex cracker - Returning results: {cracked_result}")
        return cracked_result


    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return {
            "dict": ParamSpec(
                desc="The soundex dictionary to use",
                req=False,
                default="cipheydists::translate::soundex",
            ),
            "freq": ParamSpec(
                desc="The word frequency dictionary to use",
                req=False,
                default="cipheydists::list::English5000Freq",
            )
        }

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.soundex_dict = config.get_resource(self._params()["dict"], Translation)
        self.word_freq = config.get_resource(self._params()["freq"], Translation)
        self.frequency_dict = {}
        self.sentence_freq = 0
