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
import bisect
from . import iface

from rich.console import Console
from rich.table import Table
from loguru import logger

warnings.filterwarnings("ignore")




def decrypt(ctext: Any, config: iface.Config) -> Optional[Dict[str, Any]]:
    # First, we detect shenanigans
    out_type = config.objs["format"]["in"]
    if type(ctext) == out_type and config.objs["checker"](ctext):
        return {
            "IsPlaintext?": True,
            "Plaintext": ctext,
            "Cipher": "Plaintext",
            "Extra Information": None
        }

    # Next, we grab all the decoder classes that apply to our data
    decoder_classes = iface.registry[iface.Decoder].get(type(ctext))
    possible_decodings = {}

    if decoder_classes is not None:
        for dst_type, decoders in decoder_classes.items():
            target = possible_decodings[dst_type] = {}
            for decoder in decoders:
                decoder = config(decoder)
                res = decoder.decode(ctext)
                if res is None:
                    continue
                target[decoder] = dst_type(res)

    # Now we check the decodings that link to our input
    for decoder, i in possible_decodings.setdefault(out_type, {}).items():
        if config.objs["checker"](i):
            return {
                "IsPlaintext?": True,
                "Plaintext": i,
                "Cipher": decoder.getName(),
                "Extra Information": None
            }

    # With simple decodings out of the way, we now need to build our score dictionary
    cracker_scores: Dict[iface.Cracker, float] = {}
    cracker_held: List[iface.Cracker] = []

    for i in iface.registry[iface.Cracker[type(ctext)]]:
        # TODO: fix this
        print(bisect.bisect_left(map(lambda x: x.getUtility(), cracker_held), i))
        if utility_threshold():
            if prob_threshold():
                do_stuff()

    # Now we have exhausted the easy options, try all the decoded versions
    #
    # XXX: remember to use Memo.test_and_set to stop infinite recursion!
    for dst_type, elems in possible_decodings.items():
        for decoder, val in elems.items():
            res = decrypt(val, config)
            if res["IsPlaintext?"]:
                res["Cipher"] += " inside " + decoder.getName()
                return res


    # Now we do the rest of the cipher checks, executing as necessary

    return {
        "IsPlaintext?": False,
        "Plaintext": None,
        "Cipher": None,
        "Extra Information": None,
    }


def arg_parsing(config: iface.Config) -> Optional[Dict[str, Any]]:
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
        action="store",
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
        "--bytes-input",
        help="Forces ciphey to use binary mode for the input. Rather experimental and may break things!",
        action="store_const",
        const="bytes",
        default="str"
    )
    parser.add_argument(
        "-B",
        "--bytes-output",
        help="Forces ciphey to use binary mode for the output. Rather experimental and may break things!",
        action="store_const",
        const="bytes",
        default="str"
    )

    args = vars(parser.parse_args())

    # First, we should work out how verbose we should be
    if args["trace"]:
        config.update_log_level("TRACE")
    elif args["debug"]:
        config.update_log_level("DEBUG")
    elif args["quiet"]:
        config.update_log_level("ERROR")
    elif args["silent"]:
        config.update_log_level(None)

    # Now we have set the log level, we can start debugging
    logger.trace(f"Got arguments {args}")

    # the below text does:
    # * if -t is supplied, use that
    # * if ciphey is called like:
    # * REMOVED: ciphey 'encrypted text' use that
    # else if data is piped like:
    # echo 'hello' | ciphey use that
    # if no data is supplied, no arguments supplied.

    # if len(sys.argv) == 1:
    #     logger.critical("No arguments were supplied. Look at the help menu with -h or --help")
    #     return None

    # Now we can walk through the arguments, expanding them into the config struct
    config.update("checker", args.get("checker"))
    config.update("info", args.get("info"))
    config.update_format("in", args.get("bytes-input"))
    config.update_format("out", args.get("bytes-output"))

    # Append the module lists:
    config.modules += args["module"]
    config.load_modules()

    # Now we fill in the params *shudder*
    for i in args["param"]:
        key, value = i.split("=", 1)
        parent, name = key.split(".", 1)
        config.update_param(parent, name, value)

    # Now we have parsed and loaded everything else, we can load the objects
    config.load_objs()

    return args


def main(config: Optional[iface.Config] = None, ciphertext=None, parse_args: bool = True) -> Optional[dict]:
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
    # If I don't do this, we end up with the default argument changing
    if config is None:
        config = iface.Config()

    args = None
    # We must fill in the arguments if they are not provided
    if parse_args:
        # Check if we errored out
        args = arg_parsing(config)
        if not args:
            return None

    # We now load the ciphertext
    if ciphertext is None:
        if args is not None and args["text"] is not None:
            ciphertext = args["text"]
        elif not sys.stdin.isatty():
            ciphertext = sys.stdin.read()
        else:
            logger.critical("No text input given!")
            return None

    # Perform type conversion
    ciphertext = config.objs["format"]["in"](ciphertext)
    logger.debug(f"Loaded ciphertext {ciphertext}")

    if len(ciphertext) < 3:
        logger.critical("A string of less than 3 chars cannot be interpreted by Ciphey.")
        return None

    # Now we have working arguments, we can decrypt
    return decrypt(ciphertext, config)


if __name__ == "__main__":
    # withArgs because this function is only called
    # if the program is run in terminal
    result = main()
    if result is not None:
        print(result)
