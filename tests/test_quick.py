import pytest

from ciphey import decrypt
from ciphey.iface import Config
from click.testing import CliRunner
from ciphey.ciphey import main
from ciphey.basemods.Checkers import human
import mock

answer_str = "Hello my name is bee and I like dog and apple and tree"


def test_quick_base32():
    res = decrypt(
        Config().library_default().complete_config(),
        "JBSWY3DPEBWXSIDOMFWWKIDJOMQGEZLFEBQW4ZBAJEQGY2LLMUQGI33HEBQW4ZBAMFYHA3DFEBQW4ZBAORZGKZI=",
    )
    assert res.lower() == answer_str.lower()


def test_quick_base58_ripple():
    res = decrypt(
        Config().library_default().complete_config(),
        "aqY64A1PhaM8hgyagyw4C1Mmp5cwxGEwag8EjVm9F6YHebyfPZmsvt65XxS7ffteQgTEGbHNT8",
    )
    assert res.lower() == answer_str.lower()


def test_quick_greppable_works_with_ip_address():
    runner = CliRunner()
    result = runner.invoke(main, ["-g", "-t", "MTkyLjE2OC4wLjE="])
    assert result.exit_code == 0
    assert result.output == "192.168.0.1\n"


@mock.patch("ciphey.basemods.Checkers.human.HumanChecker.check", return_value="")
def test_quick_visual_output(mock_click):
    # https://github.com/Ciphey/Ciphey/issues/655
    runner = CliRunner()
    mock_click.return_value = "y"
    result = runner.invoke(main, ["-t", "NB2HI4DTHIXS6Z3PN5TWYZJOMNXW2==="])
    assert result.exit_code == 0
    assert "base32" in result.output
