"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
https://github.com/brandonskerritt/ciphey
"""
# Tensorflow always spams my terminal with so many warnings of things I can't change
# so this tells them to shut up
import warnings

warnings.filterwarnings("ignore")

# Rich is replacing alive progress
import argparse
import collections

# needed for logger.add()
# so logger can capture exceptions
import sys

from alive_progress import alive_bar

# rich is used because of progress bars + prob table
from rich.console import Console
from rich.table import Column, Table

# Loguru is used for logging as it supprts
# multi threading better
from loguru import logger

logger.add(
    sys.stderr,
    format="{time} {level} {message}",
    filter="my_module",
    level="DEBUG",
    diagnose=True,
    backtrace=True,
)

# Depening on whether ciphey is called, or ciphey/__main__
# we need different imports to deal with both cases
try:
    from languageCheckerMod import LanguageChecker as lc
    from neuralNetworkMod.nn import NeuralNetwork
    from Decryptor.basicEncryption.basic_parent import BasicParent
    from Decryptor.Hash.hashParent import HashParent
    from Decryptor.Encoding.encodingParent import EncodingParent
    from Decryptor.Hash.hashParent import HashParent
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
        self.text = text
        logger.debug(f"The inputted text at __main__ is {self.text}")
        # the decryptor components
        self.basic = BasicParent(self.lc)
        self.hash = HashParent()
        self.encoding = EncodingParent(self.lc)
        self.level = 1
        self.sickomode = False
        self.greppable = grep
        self.cipher = cipher
        self.console = Console()

    def decrypt(self):
        # Read the documentation for more on this function.
        self.probabilityDistribution = self.ai.predictnn(self.text)[0]
        self.whatToChoose = {
            self.hash: {
                "sha1": self.probabilityDistribution[0],
                "md5": self.probabilityDistribution[1],
                "sha256": self.probabilityDistribution[2],
                "sha512": self.probabilityDistribution[3],
            },
            self.basic: {"caesar": self.probabilityDistribution[4]},
            "plaintext": {"plaintext": self.probabilityDistribution[5]},
            self.encoding: {
                "reverse": self.probabilityDistribution[6],
                "base64": self.probabilityDistribution[7],
                "binary": self.probabilityDistribution[8],
                "hexadecimal": self.probabilityDistribution[9],
                "ascii": self.probabilityDistribution[10],
                "morse": self.probabilityDistribution[11],
            },
        }

        logger.debug(
            f"The probability table before 0.1 in __main__ is {self.whatToChoose}"
        )

        # sorts each indiviudal sub-dictionary
        for key, value in self.whatToChoose.items():
            for k, v in value.items():
                # Sets all 0 probabilities to 0.01, we want Ciphey to try all decryptions.
                if v < 0.01:
                    self.whatToChoose[key][k] = 0.01
        logger.debug(
            f"The probability table after 0.1 in __main__ is {self.whatToChoose}"
        )

        for key, value in self.whatToChoose.items():
            self.whatToChoose[key] = self.mh.sortDictionary(value)

        self.whatToChoose = self.mh.sortProbTable(self.whatToChoose)

        # the below code selects the most likely one
        # and places it at the front
        # TODO is this code redundant because of self.mh.sortProbTable?
        new_dict = {}
        maximum = 0.00
        max_key = None
        max_val = None
        for key, value in self.whatToChoose.items():
            val = next(iter(value))
            val = value[val]
            if val >= maximum:
                maximum = val
                max_key = key
                max_val = value
        new_dict = collections.OrderedDict()
        new_dict[max_key] = max_val
        for key, value in self.whatToChoose.items():
            if key == max_key:
                continue
            new_dict[key] = value

        # Creates and prints the probability table
        if not self.greppable:
            self.produceProbTable(new_dict)

        self.whatToChoose = new_dict
        logger.debug(
            f"The new probability table after sorting in __main__ is {self.whatToChoose}"
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

    def produceProbTable(self, probTable):
        """Produces the probability table using Rich's API

        :probTable: the probability distribution table returned by the neural network
        :returns: Nothing, it prints out the prob table.

        """
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name of Cipher")
        table.add_column("Probability", justify="right")
        # for every key, value in dict add a row
        # I think key is self.caesarcipher and not "caesar cipher"
        # i must callName() somewhere else in this code
        for k, v in probTable.items():
            for key, value in v.items():
                # Prevents the table from showing pointless 0.01 probs as they're faked
                if value == 0.01:
                    continue
                logger.debug(f"Key is {str(key)} and value is {str(value)}")
                val_as_percent = str(round(self.mh.percentage(value, 1), 2)) + "%"
                keyStr = str(key).capitalize()
                if "Base" in keyStr:
                    keyStr = keyStr[0:-2]
                logger.debug(
                    f"The value as percentage is {val_as_percent} and key is {keyStr}"
                )
                table.add_row(keyStr, val_as_percent)
        self.console.print(table)

    def one_level_of_decryption(self, file=None, sickomode=None):
        # Calls one level of decryption
        # mainly used to control the progress bar
        if self.greppable:
            logger.debug("__main__ is running as greppable")
            self.decryptNormal()
        else:
            with alive_bar() as bar:
                logger.debug("__main__ is running with progress bar")
                self.decryptNormal(bar)

    def decryptNormal(self, bar=None):
        for key, val in self.whatToChoose.items():
            # https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
            if not isinstance(key, str):
                key.setProbTable(val)
                ret = key.decrypt(self.text)
                logger.debug(f"Decrypt normal in __main__ ret is {ret}")
                logger.debug(
                    f"The plaintext is {ret['Plaintext']} and the extra information is {ret['Cipher']} and {ret['Extra Information']}"
                )

                if ret["IsPlaintext?"]:
                    print(ret["Plaintext"])
                    if self.cipher:
                        if ret["Extra Information"] != None:
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
        print("""No encryption found. Here are some tips to help crack the cipher:
                * Use the probability table to work out what it could be. Base = base16, base32, base64 etc.
                * If the probability table says 'Caesar Cipher' then it is a normal encryption that Ciphey cannot decrypt yet.
                * If Ciphey think's it's a hash, try using hash-identifier to find out what hash it is, and then HashCat to crack the hash.
                * The encryption may not contain normal English plaintext. It could be coordinates or another object no found in the dictionary. Use 'ciphey -d true > log.txt' to generate a log file of all attempted decryptions and manually search it.""")


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
        required=False,
    )
    parser.add_argument("-t", "--text", help="Text to decrypt", required=False)
    # parser.add_argument('-s','--sicko-mode', help='If it is encrypted Ciphey WILL find it', required=False)
    parser.add_argument(
        "-c",
        "--printcipher",
        help="Do you want information on the cipher used?",
        required=False,
    )

    parser.add_argument(
        "-d", "--debug", help="Activates debug mode", required=False,
    )
    args = vars(parser.parse_args())
    if args["printcipher"] != None:
        cipher = True
    else:
        cipher = False
    if args["greppable"] != None:
        greppable = True
    else:
        greppable = False
    if args["debug"] != None:
        debug = True
    else:
        debug = False

    if args["text"]:
        cipherObj = Ciphey(args["text"], greppable, cipher, debug)
        cipherObj.decrypt()
    else:
        print("No arguments were supplied. Look at the help menu with -h or --help")


if __name__ == "__main__":
    main()
