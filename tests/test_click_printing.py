from click.testing import CliRunner
from ciphey.ciphey import main
from ciphey.basemods.Checkers import human
import mock 

@mock.patch("ciphey.basemods.Checkers.human.HumanChecker.check", return_value = "")
def test_fix_for_655(mock_click):
    # https://github.com/Ciphey/Ciphey/issues/655
    runner = CliRunner()      
    mock_click.return_value = "y"
    result = runner.invoke(main, ['-t', 'NB2HI4DTHIXS6Z3PN5TWYZJOMNXW2==='])
    assert result.exit_code == 0

  

    # assert "base32" in result.output