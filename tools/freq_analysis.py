import json
import sys
import cipheycore

data = sys.stdin.read()

analysis = cipheycore.analyse_string(data)

print(json.dumps({i: j / len(data) for i, j in analysis.freqs.items()}))
