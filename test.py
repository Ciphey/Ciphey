import click
import sys


def get_name(ctx, param, value):
    # reads from stdin if the argument wasnt supplied
    if not value and not click.get_text_stream("stdin").isatty():
        return click.get_text_stream("stdin").read().strip()
    else:
        return value


@click.command()
@click.option(
    "-t", "--text", help="The ciphertext you want to decrypt.", type=str,
)
@click.option(
    "-g",
    "--greppable",
    help="Only output the answer. Useful for grep.",
    type=bool,
    is_flag=True,
)
@click.option("-v", "--verbose", count=True, type=int)
@click.option(
    "-a",
    "--checker",
    help="Use the default internal checker. Defaults to brandon",
    type=bool,
)
@click.option(
    "-A",
    "--checker-path",
    help="Uses the language checker at the given path",
    type=click.Path(exists=True),
)
@click.option("-w", "--wordlist", help="Uses the given internal wordlist")
@click.option(
    "-W",
    "--wordlist-file",
    help="Uses the wordlist at the given path",
    type=click.File("rb"),
)
@click.option(
    "-p", "--param", help="Passes a parameter to the language checker", type=str
)
@click.option(
    "-l", "--list-params", help="List the parameters of the selected module", type=str,
)
@click.option(
    "-O",
    "--offline",
    help="Run Ciphey in offline mode (no hash support)",
    type=bool,
    is_flag=True,
)
@click.argument("text_stdin", callback=get_name, required=False)
@click.argument("file_stdin", type=click.File("rb"), required=False)
def click_parse(
    text,
    greppable,
    verbose,
    checker,
    checker_path,
    wordlist,
    wordlist_file,
    param,
    list_params,
    offline,
    text_stdin,
    file_stdin,
):
    test(locals())


def test(x):
    print(f"x is {x}")
    print("*****************8")


def args():
    x = click_parse()
    print("helalldaosdoaso")
    print(x)


if __name__ == "__main__":
    args()
    print("stuff")
