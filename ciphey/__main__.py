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
from alive_progress import alive_bar
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

# Depening on whether ciphey is called, or ciphey/__main__
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
        # checks to see if inputted text is plaintext
        result = self.lc.checkLanguage(self.text)
        if result:
            print("You inputted plain text!")
            return None
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

        self.whatToChoose = self.mh.sortProbTable(self.whatToChoose)

        # Creates and prints the probability table
        if self.greppable == False:
            logger.debug(f"Self.greppable is {self.greppable}")
            self.produceProbTable(self.whatToChoose)

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
        return None

    def produceProbTable(self, probTable):
        """Produces the probability table using Rich's API

        :probTable: the probability distribution table returned by the neural network
        :returns: Nothing, it prints out the prob table.

        """
        logger.debug(f"Producing log table")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name of Cipher")
        table.add_column("Probability", justify="right")
        # for every key, value in dict add a row
        # I think key is self.caesarcipher and not "caesar cipher"
        # i must callName() somewhere else in this code
        sortedDic = {}
        for k, v in probTable.items():
            for key, value in v.items():
                # Prevents the table from showing pointless 0.01 probs as they're faked
                if value == 0.01:
                    continue
                logger.debug(f"Key is {str(key)} and value is {str(value)}")
                valInt = round(self.mh.percentage(value, 1), 2)
                keyStr = str(key).capitalize()
                if "Base" in keyStr:
                    keyStr = keyStr[0:-2]
                sortedDic[keyStr] = valInt
                logger.debug(f"The value as percentage is {valInt} and key is {keyStr}")
        sortedDic = {
            k: v
            for k, v in sorted(
                sortedDic.items(), key=lambda item: item[1], reverse=True
            )
        }
        for k, v in sortedDic.items():
            table.add_row(k, str(v) + "%")
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
        print(
            """No encryption found. Here are some tips to help crack the cipher:
                * Use the probability table to work out what it could be. Base = base16, base32, base64 etc.
                * If the probability table says 'Caesar Cipher' then it is a normal encryption that Ciphey cannot decrypt yet.
                * If Ciphey think's it's a hash, try using hash-identifier to find out what hash it is, and then HashCat to crack the hash.
                * The encryption may not contain normal English plaintext. It could be coordinates or another object no found in the dictionary. Use 'ciphey -d true > log.txt' to generate a log file of all attempted decryptions and manually search it."""
        )


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
    if args["text"] == None and len(sys.argv) > 1:
        text = args["rest"][0]
        print(f"text is {text}")
    if not sys.stdin.isatty():
        text = str(sys.stdin.read())
    if len(sys.argv) == 1 and text == None:
        print("No arguments were supplied. Look at the help menu with -h or --help")

    if text != None:
        cipherObj = Ciphey(text, greppable, cipher, debug)
        cipherObj.decrypt()


if __name__ == "__main__":
    main()
