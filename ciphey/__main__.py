"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
https://github.com/ciphey
https://docs.ciphey.online

The cycle goes:
main -> argparsing (if needed) -> call_encryption -> new Ciphey object -> decrypt() -> produceProbTable ->
one_level_of_decryption -> decrypt_normal
"""
import os
import warnings
import argparse
import sys
from typing import Optional, Dict, Any, List
import bisect

from ciphey.iface import SearchLevel
from . import iface

from rich.console import Console
from rich.table import Table
from loguru import logger
import click
import click_spinner

warnings.filterwarnings("ignore")


def decrypt(ctext: Any, config: iface.Config) -> List[SearchLevel]:
    """A simple alias for searching a ctext and makes the answer pretty"""
    res: iface.SearchResult = config.objs["searcher"].search(ctext)
    if config.verbosity < 0:
        return res.path[-1].result.value
    else:
        return iface.pretty_search_results(res)



# def arg_parsing(config: iface.Config) -> Optional[Dict[str, Any]]:
#     """This function parses arguments.
#
#         Args:
#             config: The configuration object
#         Returns:
#             The config to be passed around for the rest of time
#     """
#
#     # parser.add_argument(
#     #     "--default-wordlist",
#     #     help="Sets the default wordlist",
#     #     action="store",
#     #     default=None
#     # )
#
#     args = config
#
#     # First, we should work out how verbose we should be
#
#     # Now we have set the log level, we can start debugging
#     logger.trace(f"Got arguments {args}")
#
#     # the below text does:
#     # * if -t is supplied, use that
#     # * if ciphey is called like:
#     # * REMOVED: ciphey 'encrypted text' use that
#     # else if data is piped like:
#     # echo 'hello' | ciphey use that
#     # if no data is supplied, no arguments supplied.
#     text = None
#     if args["text"] is not None:
#         text = args["text"]
#     else:
#         print("No input given.")
#         exit(1)
#
#     if len(sys.argv) == 1:
#         print("No arguments were supplied. Look at the help menu with -h or --help")
#         return None
#
#     args["text"] = text
#     if len(args["text"]) < 3:
#         print("A string of less than 3 chars cannot be interpreted by Ciphey.")
#         return None
#
#     # Now we can walk through the arguments, expanding them into the config struct
#     config["checker"] = args.get("checker")
#     config["info"] = args.get("info")
#     config["in"] = args.get("bytes_input")
#     config["out"] = args.get("bytes_output")
#     config["default_dist"] = args.get("default_dist")
#
#     # Append the module lists:
#     if not "modules" in config:
#         config["modules"] = args["module"]
#     else:
#         config["modules"] += args["module"]
#     print(f"Config modules is {config['modules']}")
#     config.load_modules()
#     # Now we can walk through the arguments, expanding them into a canonical form
#     #
#     # First, we go over simple args
#     config["info"] = False
#     config["ctext"] = args["text"]
#     config["grep"] = args["greppable"]
#     config["offline"] = args["offline"]
#
#     # Verbosity levels
#     if args["verbose"] >= 3:
#         config["debug"] = "TRACE"
#         config.update_log_level("TRACE")
#     elif args["verbose"] == 2:
#         config["debug"] = "DEBUG"
#         config.update_log_level("DEBUG")
#     elif args["verbose"] == 1:
#         config["debug"] = "ERROR"
#         config.update_log_level("ERROR")
#     else:
#         config["debug"] = "WARNING"
#
#     if args["silent"]:
#         config.update_log_level(None)
#         config.grep = True
#
#     # Try to locate language checker module
#     # TODO: actually implement this
#     from ciphey.LanguageChecker.brandon import ciphey_language_checker as brandon
#
#     config["checker"] = brandon
#     # Try to locate language checker module
#     # TODO: actually implement this (should be similar)
#     import cipheydists
#
#     # Now we fill in the params *shudder*
#     for i in args["param"]:
#         key, value = i.split("=", 1)
#         parent, name = key.split(".", 1)
#         config.update_param(parent, name, value)
#
#     # Now we have parsed and loaded everything else, we can load the objects
#     config.load_objs()
#
#     return args
#

def get_name(ctx, param, value):
    # reads from stdin if the argument wasnt supplied
    if not value and not click.get_text_stream("stdin").isatty():
        click.get_text_stream("stdin").read().strip()
        return click.get_text_stream("stdin").read().strip()
    else:
        return value

    return locals()


@click.command()
@click.option(
    "-t", "--text", help="The ciphertext you want to decrypt.", type=str,
)
@click.option(
    "-i",
    "--info",
    help="Do you want information on the cipher used?",
    type=bool,
    is_flag=True,
)
@click.option(
    "-q",
    "--quiet",
    help="Decrease verbosity",
    type=int,
    count=True
)
@click.option(
    "-g",
    "--greppable",
    help="Only print the answer (useful for grep)",
    type=bool,
    is_flag=True,
    default=None
)
@click.option("-v", "--verbose", count=True, type=int)
@click.option(
    "-C",
    "--checker",
    help="Use the default internal checker. Defaults to brandon",
    type=bool,
    is_flag=True,
)
@click.option(
    "-c",
    "--config",
    help="Uses the given config file. Defaults to appdirs.user_config_dir('ciphey', 'ciphey')/'config.yml'",
)
@click.option("-w", "--wordlist", help="Uses the given wordlist")
@click.option(
    "-p",
    "--param",
    help="Passes a parameter to the language checker",
    type=list,
    multiple=True,
)
@click.option(
    "-l", "--list-params", help="List the parameters of the selected module", type=bool,
)
@click.option(
    "-O",
    "--offline",
    help="Run Ciphey in offline mode (no hash support)",
    type=bool,
    is_flag=True,
)
# HARLAN TODO XXX
# I switched this to a boolean flag system
# https://click.palletsprojects.com/en/7.x/options/#boolean-flags
# True for bytes input, False for str
@click.option(
    "-s/-b",
    "--string-input/--bytes-input",
    help="Forces ciphey to use binary mode for the input. Rather experimental and may break things!",
    type=bool,
)
# HARLAN TODO XXX
# I switched this to a boolean flag system
# https://click.palletsprojects.com/en/7.x/options/#boolean-flags
@click.option(
    "-S/-B",
    "--string-output/--bytes-output",
    help="Forces ciphey to use binary mode for the output. Rather experimental and may break things!",
    type=bool,
)
@click.option(
    "--default-dist",
    help="Sets the default character/byte distribution",
    type=str,
)
@click.option(
    "-m", "--module", help="Adds a module from the given path", type=click.Path()
)
@click.option(
    "-A",
    "--appdirs",
    help="Print the location of where Ciphey wants the settings file to be",
    type=bool,
)
@click.argument("text_stdin", callback=get_name, required=False)
@click.argument("file_stdin", type=click.File("rb"), required=False)
def main(**kwargs) -> Optional[dict]:
    """Ciphey - Automated Decryption Tool
    
    Documentation: 
    https://docs.ciphey.online\n
    Discord (support here, we're online most of the day):
    https://discord.ciphey.online/\n
    GitHub: 
    https://github.com/ciphey/ciphey\n

    Ciphey is an automated decryption tool using smart artificial intelligence and natural language processing. Input encrypted text, get the decrypted text back.

    Examples:\n
        Basic Usage: ciphey -t "aGVsbG8gbXkgbmFtZSBpcyBiZWU=" -d true -c true
        
    """

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


    # if user wants to know where appdirs is
    # print and exit
    if kwargs["appdirs"] is not None:
        import appdirs
        appname = "ciphey"
        return None

    # Now we create the config object
    config = iface.Config()

    # Default init the config object
    config = iface.Config()

    # Load the settings file into the config
    cfg_arg = kwargs["config"]
    if cfg_arg is None:
        # Make sure that the config dir actually exists
        os.makedirs(iface.Config.get_default_dir(), exist_ok=True)
        config.load_file(create=True)
    else:
        config.load_file(cfg_arg)

    # Load the verbosity, so that we can start logging
    verbosity = kwargs["verbose"] - kwargs["quiet"]
    if kwargs["greppable"] is not None:
        verbosity -= 999
    config.update_log_level(verbosity)
    logger.trace(f"Got cmdline args {kwargs}")

    # First, load the modules
    module_arg = kwargs["module"]
    if module_arg is not None:
        config.modules += module_arg
    config.load_modules()

    # We need to load formats BEFORE we instantiate objects
    if kwargs["string-input"] is not None:
        config.update_format("in", "str")
    elif kwargs["bytes-input"] is not None:
        config.update_format("in", "bytes")
    if kwargs["string-output"] is not None:
        config.update_format("out", "string")
    elif kwargs["bytes-output"] is not None:
        config.update_format("out", "bytes")

    # Next, load the objects
    config.params += kwargs["param"]
    config.update("checker", kwargs["checker"])
    config.update("searcher", kwargs["searcher"])
    config.update("default-dist", kwargs["default-dist"])
    config.load_objs()

    # Finally, we load the plaintext
    if kwargs["text"] is None:
        if kwargs["file_stdin"] is not None:
            kwargs["text"] = kwargs["file_stdin"].read().decode("utf-8")
        elif kwargs["text_stdin"] is not None:
            kwargs["text"] = kwargs["text_stdin"]
        else:
            print("No inputs were given to Ciphey. For usage, run ciphey --help")
            logger.critical("No text input given!")
            return None
    decrypt(kwargs["text"], kwargs["text"])


def main_decrypt(ciphertext, config: Dict[str, object] = None) -> Optional[dict]:
    """Calls the decrypt, acts as a 2nd main

    The problem is that Click fails to run when importing and using main()

    If I make a new function for Click, I have to change so much just to make it work.

    If I make a new function for using the default config, and acting as a 2nd main -- I have to change less
    Thus, this function exists."""

    cipher_obj = Ciphey(config)
    return cipher_obj.decrypt()


if __name__ == "__main__":
    # withArgs because this function is only called
    # if the program is run in terminal
    #with click_spinner.spinner():
    #    result = main()
    result = main()
    if result is not None:
        print(result)
