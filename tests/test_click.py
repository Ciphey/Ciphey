from click.testing import CliRunner
from ciphey.ciphey import main

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(main, ['-g', '-t', 'hello'])
  assert result.exit_code == 0
  assert result.output == 'hello\n'

def test_ip_address():
  runner = CliRunner()
  result = runner.invoke(main, ['-g', '-t', 'MTkyLjE2OC4wLjE='])
  assert result.exit_code == 0
  assert result.output == '192.168.0.1\n'