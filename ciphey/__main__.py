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
import pydoc

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


def make_default_config(trace: bool = False) -> Dict[str, object]:
    import cipheydists

    return {"params": {}}


def config_load_objs(config: iface.Config):
    config["objs"]["format"] = {key: pydoc.locate(value) for key, value in config["format"].items()}
    config["objs"]["checker"] = config(iface.registry.get_named(config["checker"], iface.LanguageChecker))


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


def decrypt(ctext: Any, config: iface.Config) -> Optional[Dict[str, Any]]:
    # First, we grab all the decoder classes that apply to our data
    decoder_classes = iface.registry[iface.Decoder][config["objs"]["format"]["in"]]
    possible_decodings = []

    for dst_type, decoders in decoder_classes.items():
        for decoder in decoders:
            decoder = config(decoder)
            res = decoder.decode(ctext)
            if res is not None:
                possible_decodings.append(res)
    print(possible_decodings)
    # Now we iterate through the ones that apply to our type
    return {
        "IsPlaintext?": True,
        "Plaintext": self.text,
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

    if len(sys.argv) == 1:
        logger.critical("No arguments were supplied. Look at the help menu with -h or --help")
        return None

    def update_flag(cfg: Dict[str, Any], name: str, cfg_name: Optional[str] = None, default: Optional[Any] = None):
        arg = args.get(name)

        if cfg_name is None:
            cfg_name = name
        if arg is not None:
            cfg[cfg_name] = arg
        elif default is not None and cfg_name not in config:
            cfg[cfg_name] = default

    # Now we can walk through the arguments, expanding them into the config struct
    update_flag(config, "checker", default="brandon")
    update_flag(config, "info", default=False)
    formats = config.setdefault("format", {})
    update_flag(formats, "bytes-input", "in", default='str')
    update_flag(formats, "bytes-output", "out", default='str')

    # Append the module lists:
    mods = config.setdefault("modules", [])
    mods += args["module"]
    load_modules(mods)

    # Now we fill in the params *shudder*
    config["params"] = {}
    for i in args["param"]:
        key, value = i.split("=", 1)
        parent, name = key.split(".", 1)
        config["params"].setdefault(parent, [])[name] = value

    # Now we have parsed and loaded everything else, we can load the objects
    config_load_objs(config)

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
        config = iface.Config({})
    else:
        config = iface.Config(config)

    args = None
    # We must fill in the arguments if they are not provided
    if parse_args:
        # Check if we errored out
        args = arg_parsing(config)
        if not args:
            return None

    # We now load the ciphertext
    if ciphertext is None:
        if args is not None and "text" in args:
            ciphertext = args["text"]
        elif not sys.stdin.isatty():
            ciphertext = sys.stdin.read()
        else:
            logger.critical("No text input given!")
            return None

    # Perform type conversion
    ciphertext = config["objs"]["format"]["in"](ciphertext)

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
