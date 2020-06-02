from Ciphey.ciphey.__main__ import main


def test_argument_grep_true():
    result = main(text="hello")
    print(result)
    assert result["Plaintext"] == "hello"
