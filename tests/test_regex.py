import pytest

from ciphey import decrypt
from ciphey.iface import Config


def test_regex_ip():
    res = decrypt(
        Config().library_default().complete_config(),
        "MTkyLjE2MC4wLjE=",
    )
    assert res == "192.160.0.1"


def test_regex_domain():
    res = decrypt(
        Config().library_default().complete_config(),
        "aHR0cHM6Ly9nb29nbGUuY29t",
    )
    assert res == "https://google.com"


def test_regex_bitcoin():
    res = decrypt(
        Config().library_default().complete_config(),
        "M0ZaYmdpMjljcGpxMkdqZHdWOGV5SHVKSm5rTHRrdFpjNQ==",
    )
    assert res == "3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5"
