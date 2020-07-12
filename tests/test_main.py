from ciphey.ciphey import main
from click.testing import CliRunner


def test_initial():
    runner = CliRunner()
    # result = runner.invoke(main, ["hello my name is bee and i like bees"])
    result = runner.invoke(
        main,
        [
            "SGVsbG8gbXkgbmFtZSBpcyBiZWUgYW5kIEkgbGlrZSBkb2cgYW5kIGFwcGxlIGFuZCB0cmVl",
            "-vvv",
        ],
    )
    print(result)
    print(result.output)
    assert result.exit_code == 0
    assert "dog" in result.output
