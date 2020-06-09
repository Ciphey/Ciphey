from ciphey.__main__ import main, make_default_config


def test_argument_grep_true():
    cfg = make_default_config("It was the best of times, it was the worst of times")
    cfg["debug"] = "TRACE"
    result = main(cfg)
    assert result == "It was the best of times, it was the worst of times"


def test_main_base64_true():
    cfg = make_default_config("It was the best of times, it was the worst of times")
    cfg["debug"] = "TRACE"
    result = main("SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLiBUaGVyZSBpcyBvbmx5IHNvIG11Y2ggcm9hZCBpbiBEb3ZlciBvbmUgY2FuIGxheS4")
    assert (
        result == "It was the best of times, it was the worst of times. There is only so much road in Dover one can lay."
    )
