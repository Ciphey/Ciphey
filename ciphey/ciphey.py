"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
https://github.com/ciphey
https://github.com/Ciphey/Ciphey/wiki

The cycle goes:
main -> argparsing (if needed) -> call_encryption -> new Ciphey object -> decrypt() -> produceProbTable ->
one_level_of_decryption -> decrypt_normal
"""
import os
import warnings
import argparse
import sys
from typing import Optional, Dict, Any, List, Union
import bisect

from ciphey.iface import SearchLevel, registry
from . import iface

from rich import print
from loguru import logger
import click
import click_spinner
from appdirs import AppDirs
import yaspin
from yaspin.spinners import Spinners
from yaspin import yaspin

import time

warnings.filterwarnings("ignore")


def decrypt(config: iface.Config, ctext: Any) -> Union[str, bytes]:
    """A simple alias for searching a ctext and makes the answer pretty"""
    res: Optional[iface.SearchResult] = config.objs["searcher"].search(ctext)
    if res is None:
        return "Failed to crack"
    if config.verbosity < 0:
        return res.path[-1].result.value
    else:
        return iface.pretty_search_results(res)


def get_name(ctx, param, value):
    # reads from stdin if the argument wasnt supplied
    if not value and not click.get_text_stream("stdin").isatty():
        click.get_text_stream("stdin").read().strip()
        return click.get_text_stream("stdin").read().strip()
    else:
        return value


def print_help(ctx):
    # prints help menu
    # if no arguments are passed
    click.echo(ctx.get_help())
    ctx.exit()


@click.command()
@click.option(
    "-t", "--text", help="The ciphertext you want to decrypt.", type=str,
)
@click.option(
    "-q", "--quiet", help="Decrease verbosity", type=int, count=True, default=None
)
@click.option(
    "-g",
    "--greppable",
    help="Only print the answer (useful for grep)",
    type=bool,
    is_flag=True,
    default=None,
)
@click.option("-v", "--verbose", count=True, type=int)
@click.option("-C", "--checker", help="Use the given checker", default=None)
@click.option(
    "-c",
    "--config",
    help="Uses the given config file. Defaults to appdirs.user_config_dir('ciphey', 'ciphey')/'config.yml'",
)
@click.option("-w", "--wordlist", help="Uses the given wordlist")
@click.option(
    "-p", "--param", help="Passes a parameter to the language checker", multiple=True,
)
@click.option(
    "-l", "--list-params", help="List the parameters of the selected module", type=bool,
)
@click.option(
    "--searcher", help="Select the searching algorithm to use",
)
# HARLAN TODO XXX
# I switched this to a boolean flag system
# https://click.palletsprojects.com/en/7.x/options/#boolean-flags
# True for bytes input, False for str
@click.option(
    "-b",
    "--bytes",
    help="Forces ciphey to use binary mode for the input",
    is_flag=True,
    default=None,
)
@click.option(
    "--default-dist",
    help="Sets the default character/byte distribution",
    type=str,
    default=None,
)
@click.option(
    "-m",
    "--module",
    help="Adds a module from the given path",
    type=click.Path(),
    multiple=True,
)
@click.option(
    "-A",
    "--appdirs",
    help="Print the location of where Ciphey wants the settings file to be",
    type=bool,
    is_flag=True,
)
@click.option("-f", "--file", type=click.File("rb"), required=False)
@click.argument("text_stdin", callback=get_name, required=False)
def main(**kwargs):
    """Ciphey - Automated Decryption Tool
    
    Documentation: 
    https://github.com/Ciphey/Ciphey/wiki\n
    Discord (support here, we're online most of the day):
    https://discord.ciphey.online/\n
    GitHub: 
    https://github.com/ciphey/ciphey\n

    Ciphey is an automated decryption tool using smart artificial intelligence and natural language processing. Input encrypted text, get the decrypted text back.

    Examples:\n
        Basic Usage: ciphey -t "aGVsbG8gbXkgbmFtZSBpcyBiZWU=" 
        
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
    if "appdirs" in kwargs and kwargs["appdirs"]:
        dirs = AppDirs("Ciphey", "Ciphey")
        path_to_config = dirs.user_config_dir
        print(
            f"The settings.yml file should be at {os.path.join(path_to_config, 'settings.yml')}"
        )
        return None

    # Now we create the config object
    config = iface.Config()

    # Load the settings file into the config
    load_msg: str
    cfg_arg = kwargs["config"]
    if cfg_arg is None:
        # Make sure that the config dir actually exists
        os.makedirs(iface.Config.get_default_dir(), exist_ok=True)
        config.load_file(create=True)
        load_msg = f"Opened config file at {os.path.join(iface.Config.get_default_dir(), 'config.yml')}"
    else:
        config.load_file(cfg_arg)
        load_msg = f"Opened config file at {cfg_arg}"

    # Load the verbosity, so that we can start logging
    verbosity = kwargs["verbose"]
    quiet = kwargs["quiet"]
    if verbosity is None:
        if quiet is not None:
            verbosity = -quiet
    elif quiet is not None:
        verbosity -= quiet
    if kwargs["greppable"] is not None:
        verbosity -= 999
    # Use the existing value as a base
    config.verbosity += verbosity
    config.update_log_level(config.verbosity)
    logger.debug(load_msg)
    logger.trace(f"Got cmdline args {kwargs}")

    # Now we load the modules
    module_arg = kwargs["module"]
    if module_arg is not None:
        config.modules += list(module_arg)

    # We need to load formats BEFORE we instantiate objects
    if kwargs["bytes"] is not None:
        config.update_format("bytes")

    # Next, load the objects
    params = kwargs["param"]
    if params is not None:
        for i in params:
            key, value = i.split("=", 1)
            parent, name = key.split(".", 1)
            config.update_param(parent, name, value)
    config.update("checker", kwargs["checker"])
    config.update("searcher", kwargs["searcher"])
    config.update("default_dist", kwargs["default_dist"])

    config.complete_config()

    logger.trace(f"Command line opts: {kwargs}")
    logger.trace(f"Config finalised: {config}")

    # Finally, we load the plaintext
    if kwargs["text"] is None:
        if kwargs["file"] is not None:
            kwargs["text"] = kwargs["file"].read()
        elif kwargs["text_stdin"] is not None:
            kwargs["text"] = kwargs["text_stdin"]
        else:
            # else print help menu
            print("[bold red]Error. No inputs were given to Ciphey. [bold red]")

            @click.pass_context
            def all_procedure(ctx):
                print_help(ctx)

            all_procedure()

            return None

    if issubclass(config.objs["format"], type(kwargs["text"])):
        pass
    elif config.objs["format"] == str and type(kwargs["text"]) is bytes:
        kwargs["text"] = kwargs["text"].decode("utf-8")
    elif config.objs["format"] == bytes and type(kwargs["text"]) is str:
        kwargs["text"] = kwargs["text"].encode("utf-8")
    else:
        raise TypeError(f"Cannot load type {config.format} from {type(kwargs['text'])}")

    result: Optional[str]

    # if debug or quiet mode is on, run without spinner
    if config.verbosity != 0:
        result = decrypt(config, kwargs["text"])
    else:
        # else, run with spinner if verbosity is 0
        with yaspin(Spinners.earth, "Thinking") as sp:
            config.set_spinner(sp)
            result = decrypt(config, kwargs["text"])
    if result is None:
        result = "Could not find any solutions."

    print(result)
