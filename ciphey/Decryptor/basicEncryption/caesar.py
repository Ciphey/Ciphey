"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt
"""
from loguru import logger
import cipheycore
import cipheydists


class Caesar:
    def __init__(self, lc):
        self.lc = lc

    def getName(self):
        return "Caesar"

    def decrypt(self, message):
        logger.debug("Trying caesar Cipher")
        # Convert it to lower case
        #
        # TODO: handle different alphabets
        message = message.lower()

        # Hand it off to the core
        group = cipheydists.get_charset("english")["lcase"]
        expected = cipheydists.get_dist("lcase")
        analysis = cipheycore.analyse_string(message)
        possible_keys = cipheycore.caesar_crack(analysis, expected, group)
        n_candidates = len(possible_keys)
        logger.debug(f"Caesar cipher core heuristic returned {n_candidates} candidates")

        for candidate in possible_keys:
            translated = cipheycore.caesar_decrypt(message, candidate.key, group)
            result = self.lc.checkLanguage(translated)
            if result:
                logger.debug(f"Caesar cipher returns true {result}")
                return {
                    "lc": self.lc,
                    "IsPlaintext?": True,
                    "Plaintext": translated,
                    "Cipher": "Caesar",
                    "Extra Information": f"The rotation used is {candidate.key}",
                }

        # if none of them match English, return false!
        logger.debug(f"Caesar cipher returns false")
        return {
            "lc": self.lc,
            "IsPlaintext?": False,
            "Plaintext": None,
            "Cipher": "Caesar",
            "Extra Information": None,
        }
