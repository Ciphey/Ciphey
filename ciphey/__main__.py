"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
https://github.com/brandonskerritt/ciphey
"""
import warnings
import argparse
import sys
from rich.console import Console
from rich.table import Column, Table
from loguru import logger

logger.add(
    sys.stderr,
    format="{time} {level} {message}",
    filter="my_module",
    level="DEBUG",
    diagnose=True,
    backtrace=True,
)
warnings.filterwarnings("ignore")

# Depending on whether Ciphey is called, or Ciphey/__main__
# we need different imports to deal with both cases
try:
    from languageCheckerMod import LanguageChecker as lc
    from neuralNetworkMod.nn import NeuralNetwork
    from Decryptor.basicEncryption.basic_parent import BasicParent
    from Decryptor.Hash.hashParent import HashParent
    from Decryptor.Encoding.encodingParent import EncodingParent
except ModuleNotFoundError:
    from ciphey.languageCheckerMod import LanguageChecker as lc
    from ciphey.neuralNetworkMod.nn import NeuralNetwork
    from ciphey.Decryptor.basicEncryption.basic_parent import BasicParent
    from ciphey.Decryptor.Hash.hashParent import HashParent
    from ciphey.Decryptor.Encoding.encodingParent import EncodingParent


try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import ciphey.mathsHelper as mh


class Ciphey:
    def __init__(self, text, grep=False, cipher=False, debug=False):
        if not debug:
            logger.remove()
        # general purpose modules
        self.ai = NeuralNetwork()
        self.lc = lc.LanguageChecker()
        self.mh = mh.mathsHelper()
        # the one bit of text given to us to decrypt
        self.text: str = text
        logger.debug(f"The inputted text at __main__ is {self.text}")
        self.basic = BasicParent(self.lc)
        self.hash = HashParent()
        self.encoding = EncodingParent(self.lc)
        self.level: int = 1
        self.sickomode: bool = False
        self.greppable: bool = grep
        self.cipher = cipher
        self.console = Console()
        self.probability_distribution: dict = {}
        self.what_to_choose: dict = {}

    def decrypt(self) -> None:
        """Performs the decryption of text

        Creates the probability table, calls one_level_of_decryption

        Args:
            None, it uses class variables.

        Returns:
            None
        """
        # Read the documentation for more on this function.
        # checks to see if inputted text is plaintext
        result = self.lc.checkLanguage(self.text)
        if result:
            print("You inputted plain text!")
            return None
        self.probability_distribution: dict = self.ai.predictnn(self.text)[0]
        self.what_to_choose: dict = {
            self.hash: {
                "sha1": self.probability_distribution[0],
                "md5": self.probability_distribution[1],
                "sha256": self.probability_distribution[2],
                "sha512": self.probability_distribution[3],
            },
            self.basic: {"caesar": self.probability_distribution[4]},
            "plaintext": {"plaintext": self.probability_distribution[5]},
            self.encoding: {
                "reverse": self.probability_distribution[6],
                "base64": self.probability_distribution[7],
                "binary": self.probability_distribution[8],
                "hexadecimal": self.probability_distribution[9],
                "ascii": self.probability_distribution[10],
                "morse": self.probability_distribution[11],
            },
        }

        logger.debug(
            f"The probability table before 0.1 in __main__ is {self.what_to_choose}"
        )

        # sorts each individual sub-dictionary
        for key, value in self.what_to_choose.items():
            for k, v in value.items():
                # Sets all 0 probabilities to 0.01, we want Ciphey to try all decryptions.
                if v < 0.01:
                    self.what_to_choose[key][k] = 0.01
        logger.debug(
            f"The probability table after 0.1 in __main__ is {self.what_to_choose}"
        )

        self.what_to_choose: dict = self.mh.sort_prob_table(self.what_to_choose)

        # Creates and prints the probability table
        if not self.greppable:
            logger.debug(f"Self.greppable is {self.greppable}")
            self.produceprobtable(self.what_to_choose)

        logger.debug(
            f"The new probability table after sorting in __main__ is {self.what_to_choose}"
        )

        """
        #for each dictionary in the dictionary
         #   sort that dictionary
        #sort the overall dictionary by the first value of the new dictionary
        """
        if self.level <= 1:
            self.one_level_of_decryption()
        else:
            if self.sickomode:
                print("Sicko mode entered")
            f = open("decryptionContents.txt", "w")
            self.one_level_of_decryption(file=f)

            for i in range(0, self.level):
                # open file and go through each text item
                pass
        return None

    def produceprobtable(self, prob_table) -> None:
        """Produces the probability table using Rich's API

        Uses Rich's API to print the probability table.

        Args:
            prob_table -> the probability table generated by the neural network

        Returns:
            None, but prints the probability table.

        """
        logger.debug(f"Producing log table")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name of Cipher")
        table.add_column("Probability", justify="right")
        # for every key, value in dict add a row
        # I think key is self.caesarcipher and not "caesar cipher"
        # i must callName() somewhere else in this code
        sorted_dic: dict = {}
        for k, v in prob_table.items():
            for key, value in v.items():
                # Prevents the table from showing pointless 0.01 probs as they're faked
                if value == 0.01:
                    continue
                logger.debug(f"Key is {str(key)} and value is {str(value)}")
                val: int = round(self.mh.percentage(value, 1), 2)
                key_str: str = str(key).capitalize()
                if "Base" in key_str:
                    key_str = key_str[0:-2]
                sorted_dic[key_str] = val
                logger.debug(f"The value as percentage is {val} and key is {key_str}")
        sorted_dic: dict = {
            k: v
            for k, v in sorted(
                sorted_dic.items(), key=lambda item: item[1], reverse=True
            )
        }
        for k, v in sorted_dic.items():
            table.add_row(k, str(v) + "%")

        self.console.print(table)
        return None

    def one_level_of_decryption(self) -> None:
        """Performs one level of encryption.

        Either uses alive_bar or not depending on if self.greppable is set.

        Returns:
            None.

        """
        # Calls one level of decryption
        # mainly used to control the progress bar
        if self.greppable:
            logger.debug("__main__ is running as greppable")
            self.decrypt_normal()
        else:
            logger.debug("__main__ is running with progress bar")
            self.decrypt_normal()
        return None

    def decrypt_normal(self, bar=None) -> None:
        """Called by one_level_of_decryption

        Performs a decryption, but mainly parses the internal data packet and prints useful information.

        Args:
            bar -> whether or not to use alive_Bar

        Returns:
            None, but prints.

        """
        for key, val in self.what_to_choose.items():
            # https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
            if not isinstance(key, str):
                key.setProbTable(val)
                ret: dict = key.decrypt(self.text)
                logger.debug(f"Decrypt normal in __main__ ret is {ret}")
                logger.debug(
                    f"The plaintext is {ret['Plaintext']} and the extra information is {ret['Cipher']} and {ret['Extra Information']}"
                )

                if ret["IsPlaintext?"]:
                    print(ret["Plaintext"])
                    if self.cipher:
                        if ret["Extra Information"] is not None:
                            print(
                                "The cipher used is",
                                ret["Cipher"] + ".",
                                ret["Extra Information"] + ".",
                            )
                        else:
                            print("The cipher used is " + ret["Cipher"] + ".")
                    return ret

            if not self.greppable:
                bar()
        logger.debug("No encryption found")
        print(
            """No encryption found. Here are some tips to help crack the cipher:
                * Use the probability table to work out what it could be. Base = base16, base32, base64 etc.
                * If the probability table says 'Caesar Cipher' then it is a normal encryption that Ciphey cannot decrypt yet.
                * If Ciphey think's it's a hash, try using hash-identifier to find out what hash it is, and then HashCat to crack the hash.
                * The encryption may not contain normal English plaintext. It could be coordinates or another object no found in the dictionary. Use 'ciphey -d true > log.txt' to generate a log file of all attempted decryptions and manually search it."""
        )
        return None


def main():
    parser = argparse.ArgumentParser(
        description="""Automated decryption tool. Put in the encrypted text and Ciphey will decrypt it.\n
        Examples:
        python3 ciphey -t "aGVsbG8gbXkgYmFieQ==" -d true -c true
        """
    )
    # parser.add_argument('-f','--file', help='File you want to decrypt', required=False)
    # parser.add_argument('-l','--level', help='How many levels of decryption you want (the more levels, the slower it is)', required=False)
    parser.add_argument(
        "-g",
        "--greppable",
        help="Only output the answer, no progress bars or information. Useful for grep",
        action="store_true",
        required=False,
    )
    parser.add_argument("-t", "--text", help="Text to decrypt", required=False)
    # parser.add_argument('-s','--sicko-mode', help='If it is encrypted Ciphey WILL find it', required=False)
    parser.add_argument(
        "-c",
        "--printcipher",
        help="Do you want information on the cipher used?",
        action="store_true",
        required=False,
    )
    # fake argument to stop argparser complaining about no arguments
    # allows sys.argv to be used
    parser.add_argument("-m", action="store_false", default=True, required=False)

    parser.add_argument(
        "-d",
        "--debug",
        help="Activates debug mode",
        required=False,
        action="store_true",
    )
    parser.add_argument("rest", nargs=argparse.REMAINDER)
    args = vars(parser.parse_args())
    if args["printcipher"]:
        cipher = True
    else:
        cipher = False
    if args["greppable"]:
        greppable = True
    else:
        greppable = False
    if args["debug"]:
        debug = True
    else:
        debug = False

    text = None

    # the below text does:
    # if -t is supplied, use that
    # if ciphey is called like:
    # ciphey 'encrypted text' use that
    # else if data is piped like:
    # echo 'hello' | ciphey use that
    # if no data is supplied, no arguments supplied.
    if args["text"]:
        text = args["text"]
    if args["text"] is None and len(sys.argv) > 1:
        text = args["rest"][0]
        print(f"text is {text}")
    if not sys.stdin.isatty():
        text = str(sys.stdin.read())
    if len(sys.argv) == 1 and text == None:
        print("No arguments were supplied. Look at the help menu with -h or --help")

    if text is not None:
        cipher_obj = Ciphey(text, greppable, cipher, debug)
        cipher_obj.decrypt()


if __name__ == "__main__":
    main()
