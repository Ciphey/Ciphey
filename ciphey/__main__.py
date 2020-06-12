"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
https://github.com/brandonskerritt/ciphey

The cycle goes:
main -> argparsing (if needed) -> call_encryption -> new Ciphey object -> decrypt() -> produceProbTable ->
one_level_of_decryption -> decrypt_normal

Ciphey can be called 3 ways:
echo 'text' | ciphey
ciphey 'text'
ciphey -t 'text'
main captures the first 2
argparsing captures the last one (-t)
it sends this to call_encryption, which can handle all 3 arguments using dict unpacking

decrypt() creates the prob table and prints it.

one_level_of_decryption() allows us to repeatedly call one_level_of_decryption on the inputs
so if something is doubly encrypted, we can use this to find it.

Decrypt_normal is one round of decryption. We need one_level_of_decryption to call it, as
one_level_of_decryption handles progress bars and stuff.
"""
import warnings
import argparse
import sys
from typing import Optional, Dict, Any, List

from rich.console import Console
from rich.table import Table
from loguru import logger

warnings.filterwarnings("ignore")

# Depending on whether Ciphey is called, or Ciphey/__main__
# we need different imports to deal with both cases
try:
    from . import iface
    from ciphey.neuralNetworkMod.nn import NeuralNetwork
    from ciphey.Decryptor.basicEncryption.basic_parent import BasicParent
    from ciphey.Decryptor.Hash.hashParent import HashParent
    from ciphey.Decryptor.Encoding.encodingParent import EncodingParent
    import ciphey.mathsHelper as mh
except ModuleNotFoundError:
    from neuralNetworkMod.nn import NeuralNetwork
    from Decryptor.basicEncryption.basic_parent import BasicParent
    from Decryptor.Hash.hashParent import HashParent
    from Decryptor.Encoding.encodingParent import EncodingParent
    import mathsHelper as mh


def make_default_config(ctext: str, trace: bool = False) -> Dict[str, object]:
    from ciphey.basemods.LC.brandon import ciphey_language_checker as brandon
    import cipheydists

    return {
        "ctext": ctext,
        "grep": False,
        "info": False,
        "debug": "TRACE" if trace else "WARNING",
        "checker": brandon,
        "wordlist": set(cipheydists.get_list("english")),
        "params": {},
    }


def update_log_levels(level: Optional[str]):
    logger.remove()
    if level is None:
        return
    logger.configure()
    if level == "TRACE" or level == "DEBUG":
        logger.add(sink=sys.stderr, level=level, colorize=sys.stderr.isatty())
        logger.opt(colors=True)
    else:
        logger.add(sink=sys.stderr, level=level, colorize=False, format="{message}")
    logger.debug(f"""Debug level set to {level}""")

def load_modules(mods: List[str]):
    import importlib.util
    for i in mods:
        spec = importlib.util.spec_from_file_location("ciphey.module_load_site", i)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

class Ciphey:
    config = dict()
    params = dict()

    def __init__(self, config: Dict[str, Any]):

        # general purpose modules
        self.ai = NeuralNetwork()
        self.lc = config["objs"]["checker"](config)
        self.mh = mh.mathsHelper()
        # the one bit of text given to us to decrypt
        self.text: str = config["ctext"]
        self.basic = BasicParent(self.lc)
        self.hash = HashParent(self.lc)
        self.encoding = EncodingParent(self.lc)
        self.level: int = 1
        self.greppable: bool = config["debug"] is None
        self.cipher_info = config["info"]
        self.console = Console()
        self.probability_distribution: dict = {}
        self.what_to_choose: dict = {}

    def decrypt(self) -> Optional[Dict]:
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
            logger.critical("You inputted plain text!")
            return {
                "lc": self.lc,
                "IsPlaintext?": True,
                "Plaintext": self.text,
                "Cipher": None,
                "Extra Information": None,
            }
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

        logger.trace(
            f"The probability table before 0.1 in __main__ is {self.what_to_choose}"
        )

        # sorts each individual sub-dictionary
        for key, value in self.what_to_choose.items():
            for k, v in value.items():
                # Sets all 0 probabilities to 0.01, we want Ciphey to try all decryptions.
                if v < 0.01:
                    self.what_to_choose[key][k] = 0.01
        logger.trace(
            f"The probability table after 0.1 in __main__ is {self.what_to_choose}"
        )

        self.what_to_choose: dict = self.mh.sort_prob_table(self.what_to_choose)

        # Creates and prints the probability table
        if not self.greppable:
            self.produceprobtable(self.what_to_choose)

        logger.debug(
            f"The new probability table after sorting in __main__ is {self.what_to_choose}"
        )

        """
        #for each dictionary in the dictionary
         #   sort that dictionary
        #sort the overall dictionary by the first value of the new dictionary
        """
        output = None
        if self.level <= 1:
            output = self.one_level_of_decryption()
        else:
            # TODO: make tmpfile
            f = open("decryptionContents.txt", "w")
            output = self.one_level_of_decryption(file=f)

            for i in range(0, self.level):
                # open file and go through each text item
                pass
        logger.debug(f"decrypt is outputting {output}")
        return output

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
                # gets the string ready to print
                logger.debug(f"Key is {str(key)} and value is {str(value)}")
                val: int = round(self.mh.percentage(value, 1), 2)
                key_str: str = str(key).capitalize()
                # converts "Bases" to "Base"
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

    def one_level_of_decryption(self) -> Optional[dict]:
        """Performs one level of encryption.

        Either uses alive_bar or not depending on if self.greppable is set.

        Returns:
            None.

        """
        # Calls one level of decryption
        # mainly used to control the progress bar
        output = None
        if self.greppable:
            logger.debug("__main__ is running as greppable")
            output = self.decrypt_normal()
        else:
            logger.debug("__main__ is running with progress bar")
            output = self.decrypt_normal()
        return output

    def decrypt_normal(self, bar=None) -> Optional[dict]:
        """Called by one_level_of_decryption

        Performs a decryption, but mainly parses the internal data packet and prints useful information.

        Args:
            bar -> whether or not to use alive_Bar

        Returns:
            str if found, or None if not

        """

        logger.debug(f"In decrypt_normal")
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
                    logger.debug(f"Ret is plaintext")
                    if self.cipher_info:
                        logger.trace("Self.cipher_info runs")
                        if ret["Extra Information"] is not None:
                            logger.critical(
                                "The cipher used is",
                                ret["Cipher"] + ".",
                                ret["Extra Information"] + ".",
                            )
                        else:
                            logger.critical("The cipher used is " + ret["Cipher"] + ".")
                    return ret

        logger.critical(
            """No encryption found. Here are some tips to help crack the cipher:
                * Use the probability table to work out what it could be. Base = base16, base32, base64 etc.
                * If the probability table says 'Caesar Cipher' then it is a normal encryption that \
                 Ciphey cannot decrypt yet.
                * If Ciphey think's it's a hash, try using hash-identifier to find out what hash it is, \
                and then HashCat to crack the hash.
                * The encryption may not contain normal English plaintext. It could be coordinates or \
                another object no found in the dictionary. Use 'ciphey -d true > log.txt' to generate a log \
                file of all attempted decryptions and manually search it."""
        )
        return None


def arg_parsing(config: Dict[str, Any]) -> bool:
    """This function parses arguments.

        Args:
            config: The configuration object
        Returns:
            The config to be passed around for the rest of time
    """
    parser = argparse.ArgumentParser(
        description="""Automated decryption tool. Put in the encrypted text and Ciphey will decrypt it.\n
        Examples:
        python3 ciphey -t "aGVsbG8gbXkgYmFieQ==" -d true -c true
        """
    )
    parser.add_argument(
        "-t",
        "--text",
        help="Text to decrypt",
    )
    parser.add_argument(
        "-i",
        "--info",
        help="Do you want information on the cipher used?",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="Activates debug mode",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-D",
        "--trace",
        help="More verbose than debug mode. Shadows --debug",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-q",
        "--quiet",
        help="Supress warnings",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-Q",
        "--silent",
        help="Only output the answer, no progress bars or information. Useful for grep",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-C",
        "--checker",
        help="Uses the given language checker. Defaults to brandon",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-c",
        "--config",
        help="Uses the given config file. Defaults to appdirs.user_config_dir('ciphey', 'ciphey')/'config.yml'",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-w",
        "--wordlist",
        help="Uses the given wordlist",
    )
    parser.add_argument(
        "-p",
        "--param",
        help="Passes a parameter to the language checker",
        action="append",
        default=[]
    )
    parser.add_argument(
        "-l",
        "--list-params",
        help="Lists the parameters of the selected module",
        action="store_const",
        const=True,
    )
    parser.add_argument(
        "-m",
        "--module",
        help="Adds a module from the given path",
        action="append",
        default=[]
    )
    parser.add_argument(
        "-b",
        "--bytes",
        help="Forces ciphey to use binary mode. Rather experimental and may break things!",
        action="store_const",
        const=True,
    )

    args = vars(parser.parse_args())

    # First, we should work out how verbose we should be
    if args["trace"]:
        config["debug"] = "TRACE"
    elif args["debug"]:
        config["debug"] = "DEBUG"
    elif args["quiet"]:
        config["debug"] = "ERROR"
    elif args["silent"]:
        config["debug"] = None
    else:
        config.setdefault("debug", "WARNING")
    update_log_levels(config["debug"])

    logger.trace(f"Got arguments {args}")

    # Initialise the object list
    config["objs"] = {}

    # the below text does:
    # * if -t is supplied, use that
    # * if ciphey is called like:
    # * REMOVED: ciphey 'encrypted text' use that
    # else if data is piped like:
    # echo 'hello' | ciphey use that
    # if no data is supplied, no arguments supplied.

    text = None
    if args["text"] is not None:
        text = args["text"]
    elif not sys.stdin.isatty():
        text = str(sys.stdin.read())
    else:
        logger.critical("No text input given!")
        return False

    if len(sys.argv) == 1:
        logger.critical("No arguments were supplied. Look at the help menu with -h or --help")
        return False

    args["text"] = text
    if len(args["text"]) < 3:
        logger.critical("A string of less than 3 chars cannot be interpreted by Ciphey.")
        return False

    def update_flag(name: str, cfg_name: Optional[str] = None, default: Optional[Any] = None):
        arg = args.get(name)

        if cfg_name is None:
            cfg_name = name
        if arg is not None:
            config[cfg_name] = arg
        elif default is not None and cfg_name not in config:
            config[cfg_name] = default

    # Now we can walk through the arguments, expanding them into the config struct
    config["ctext"] = args["text"]  # Squash config for ctext
    update_flag("checker", default="brandon")
    update_flag("info", default=False)
    update_flag("bytes", default=False)

    # Append the module lists:
    mods = config.setdefault("modules", [])
    mods += args["module"]
    load_modules(mods)

    config["objs"]["checker"] = iface.registry.get_named(config["checker"], iface.LanguageChecker)

    # Now we fill in the params *shudder*
    config["params"] = {}
    for i in args["param"]:
        key, value = i.split("=", 1)
        parent, name = key.split(".", 1)
        config["params"].setdefault(parent, [])[name] = value

    return True


def main(config: Dict[str, Any] = {}, parse_args: bool = True) -> Optional[dict]:
    """Function to deal with arguments. Either calls with args or not. Makes Pytest work.

    It gets the arguments in the function definition using locals()
    if withArgs is True, that means this is being called with command line args
    so go to arg_parsing() to get those args
    we then update locals() with the new command line args and remove "withArgs"
    This function then calls call_encryption(**result) which passes our dict of args
    to the function as its own arguments using dict unpacking.
    
        Returns:
            The output of the decryption.
    """
    # We must fill in the arguments if they are not provided
    if parse_args:
        # Check if we errored out
        if not arg_parsing(config):
            return None

    # Now we have working arguments, we can expand it and pass it to the Ciphey constructor
    cipher_obj = Ciphey(config)
    return cipher_obj.decrypt()


if __name__ == "__main__":
    # withArgs because this function is only called
    # if the program is run in terminal
    result = main()
    if result is not None:
        print(result)
