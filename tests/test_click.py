from click.testing import CliRunner
from ciphey.ciphey import main
from ciphey.basemods.Checkers import human
import mock


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(main, ["-g", "-t", "hello"])
    assert result.exit_code == 0
    assert result.output == "hello\n"


def test_ip_address():
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
