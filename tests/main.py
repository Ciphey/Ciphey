from ciphey.__main__ import main
from click.testing import CliRunner


def test_initial():
    runner = CliRunner()
    result = runner.invoke(main, ["-t", ["Hello my name is bee"], "-q"])

    print(result)


test_initial()
