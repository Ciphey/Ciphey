import subprocess
from sys import exit

result = subprocess.check_output(["ciphey", "-q", "-t 'hello'"])

if "hello" in result:
    exit(0)
else:
    exit(1)
