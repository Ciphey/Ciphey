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


def test_base16():
    runner = CliRunner()
    # result = runner.invoke(main, ["hello my name is bee and i like bees"])
    result = runner.invoke(
        main,
        [
            "JBSWY3DPEBWXSIDOMFWWKIDJOMQGEZLFEBQW4ZBAJEQGY2LLMUQGI33HEBQW4ZBAMNQXI===",
            "-vvv",
        ],
    )
    assert result.exit_code == 0
    assert "dog" in result.output


def test_caesar():
    runner = CliRunner()
    result = runner.invoke(
        main, ["Uryyb zl anzr vf orr naq V yvxr qbt naq png", "-vvv"],
    )
    assert result.exit_code == 0
    assert "dog" in result.output


def test_base64_caesar():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "01010011 01000111 01010110 01110011 01100010 01000111 00111000 01100111 01100010 01011000 01101011 01100111 01100010 01101101 01000110 01110100 01011010 01010011 01000010 01110000 01100011 01111001 01000010 01101001 01011010 01010111 01010101 01100111 01011001 01010111 00110101 01101011 01001001 01000101 01101011 01100111 01100010 01000111 01101100 01110010 01011010 01010011 01000010 01101011 01100010 00110010 01100011 01100111 01011001 01010111 00110101 01101011 01001001 01000111 01001110 01101000 01100100 01000011 01000010 01101001 01100100 01011000 01010001 01100111 01010011 01010011 01000010 01101000 01100010 01001000 01001110 01110110 01001001 01000111 01010010 01110110 01001001 01000111 01101000 01101000 01100011 01001000 01000010 01101100 01100010 01101001 01000010 00110000 01100010 01111001 01000010 01101100 01100010 01101101 01110000 01110110 01100101 01010011 01000010 00110011 01011001 01010111 01111000 01110010 01100011 01110111 00111101 00111101",
            "-vvv",
        ],
    )
    assert result.exit_code == 0
    assert "dog" in result.output


def test_vigenere():
    runner = CliRunner()
    result = runner.invoke(
        main, ["Omstv uf vhul qz jlm hvk Q sqrm kwn iul jia", "-vvv"],
    )
    assert result.exit_code == 0
    assert "dog" in result.output


def test_binary():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "01001000 01100101 01101100 01101100 01101111 00100000 01101101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01100010 01100101 01100101 00100000 01100001 01101110 01100100 00100000 01001001 00100000 01101100 01101001 01101011 01100101 00100000 01100100 01101111 01100111 00100000 01100001 01101110 01100100 00100000 01100011 01100001 01110100",
            "-vvv",
        ],
    )
    assert result.exit_code == 0
    assert "dog" in result.output


def test_hex():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "48 65 6c 6c 6f 20 6d 79 20 6e 61 6d 65 20 69 73 20 62 65 65 20 61 6e 64 20 49 20 6c 69 6b 65 20 64 6f 67 20 61 6e 64 20 63 61 74",
            "-vvv",
        ],
    )
    assert result.exit_code == 0
    assert "dog" in result.output
