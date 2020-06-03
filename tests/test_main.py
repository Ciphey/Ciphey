from Ciphey.ciphey.__main__ import main


def test_argument_grep_true():
    result = main(text="It was the best of times, it was the worst of times")
    print(result)
    assert result == "It was the best of times, it was the worst of times"
