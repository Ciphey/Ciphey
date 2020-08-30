from ciphey import decrypt
from ciphey.iface import Config
import pytest

answer_str = "Hello my name is bee and I like dog and apple and tree"


def test_plaintext():
    res = decrypt(Config.library_default().complete_config(), answer_str)

    print(res)

    assert res == answer_str


def test_base64():
    res = decrypt(
        Config().library_default().complete_config(),
        "SGVsbG8gbXkgbmFtZSBpcyBiZWUgYW5kIEkgbGlrZSBkb2cgYW5kIGFwcGxlIGFuZCB0cmVl",
    )

    assert res == answer_str


def test_caesar():
    res = decrypt(
        Config().library_default().complete_config(),
        "Uryyb zl anzr vf orr naq V yvxr qbt naq nccyr naq gerr",
    )

    assert res == answer_str


def test_binary_base64_caesar():
    res = decrypt(
        Config().library_default().complete_config(),
        "01010110 01011000 01001010 00110101 01100101 01010111 01001001 01100111 01100101 01101101 01110111 "
        "01100111 01011001 01010111 00110101 00110110 01100011 01101001 01000010 00110010 01011010 01101001 "
        "01000010 01110110 01100011 01101110 01001001 01100111 01100010 01101101 01000110 01111000 01001001 "
        "01000110 01011001 01100111 01100101 01011000 01011010 00110100 01100011 01101001 01000010 01111000 "
        "01011001 01101110 01010001 01100111 01100010 01101101 01000110 01111000 01001001 01000111 00110101 "
        "01101010 01011001 00110011 01101100 01111001 01001001 01000111 00110101 01101000 01100011 01010011 "
        "01000010 01101110 01011010 01011000 01001010 01111001 00001010",
    )

    assert res == answer_str


def test_vigenere():
    res = decrypt(
        Config().library_default().complete_config(),
        "Rijvs ki rywi gc fco eln M jsoc nse krb ktnvi yxh rbic",
    )

    assert res == answer_str


def test_binary():
    res = decrypt(
        Config().library_default().complete_config(),
        "01001000 01100101 01101100 01101100 01101111 00100000 01101101 01111001 00100000 01101110 01100001 "
        "01101101 01100101 00100000 01101001 01110011 00100000 01100010 01100101 01100101 00100000 01100001 "
        "01101110 01100100 00100000 01001001 00100000 01101100 01101001 01101011 01100101 00100000 01100100 "
        "01101111 01100111 00100000 01100001 01101110 01100100 00100000 01100001 01110000 01110000 01101100 "
        "01100101 00100000 01100001 01101110 01100100 00100000 01110100 01110010 01100101 01100101",
    )

    assert res == answer_str


def test_hex():
    res = decrypt(
        Config().library_default().complete_config(),
        "48656c6c6f206d79206e616d652069732062656520616e642049206c696b6520646f6720616e64206170706c6520616e6420"
        "74726565",
    )

    assert res == answer_str


def test_atbash():
    res = decrypt(
        Config().library_default().complete_config(),
        "Svool nb mznv rh yvv zmw R orpv wlt zmw zkkov zmw givv",
    )
    assert res == answer_str


def test_galactic():
    res = decrypt(
        Config().library_default().complete_config(),
        "⍑ᒷꖎꖎ𝙹 ᒲ|| リᔑᒲᒷ ╎ᓭ ʖᒷᒷ ᔑリ↸ i ꖎ╎ꖌᒷ ↸𝙹⊣ ᔑリ↸ ᔑ!¡!¡ꖎᒷ ᔑリ↸ ℸ ̣ ∷ᒷᒷ",
    )
    assert res.lower() == answer_str.lower()


@pytest.mark.skip(reason="https://github.com/Ciphey/Ciphey/issues/262")
def test_galactic_Xproblem():
    res = decrypt(
        Config().library_default().complete_config(),
        "𝙹 ̇/⎓𝙹∷↸ ℸ ̣ ⍑ᒷ  ̇/ ╎ᓭ ╎リ ℸ ̣ ⍑ᒷ ᒲ╎↸↸ꖎᒷ ℸ ̣ ⍑ᔑℸ ̣ ᓭ ∴⍑|| ╎ℸ ̣  ⎓ᔑ╎ꖎᓭ",
    )
    assert res.lower() == "oxford the x is in the middle thats why it fails"


def test_XandY():
    res = decrypt(
        Config().library_default().complete_config(),
        "xDDxDxxx xDDxxDxD xDDxDDxx xDDxDDxx xDDxDDDD xxDxxxxx xDDxDDxD xDDDDxxD xxDxxxxx xDDxDDDx xDDxxxxD xDDxDDxD xDDxxDxD xxDxxxxx xDDxDxxD xDDDxxDD xxDxxxxx xDDxxxDx xDDxxDxD xDDxxDxD xxDxxxxx xDDxxxxD xDDxDDDx xDDxxDxx xxDxxxxx xDxxDxxD xxDxxxxx xDDxDDxx xDDxDxxD xDDxDxDD xDDxxDxD xxDxxxxx xDDxxDxx xDDxDDDD xDDxxDDD xxDxxxxx xDDxxxxD xDDxDDDx xDDxxDxx xxDxxxxx xDDxxxxD xDDDxxxx xDDDxxxx xDDxDDxx xDDxxDxD xxDxxxxx xDDxxxxD xDDxDDDx xDDxxDxx xxDxxxxx xDDDxDxx xDDDxxDx xDDxxDxD xDDxxDxD",
    )
    assert res.lower() == answer_str.lower()

def leet():
    res = decrypt(
        Config().library_default().complete_config(),
        "|-|3770 my nam3 is 833 and 1 lIke D06 AND 4|>|>13 4 7R33",
    )
    assert res.lower() == answer_str

def test_new_line_strip_and_return():
    # Language Checker should return True by stripping new line
    # but the new line should be returned to the user as new lines are important
    res = decrypt(Config().library_default().complete_config(), "pass\n")

    assert res.lower() == "pass\n"


def test_new_line_at_start_returns():
    # Language Checker should return True by stripping new line
    # but the new line should be returned to the user as new lines are important
    res = decrypt(Config().library_default().complete_config(), "\npass\n")

    assert res.lower() == "\npass\n"


def test_base58_normal():
    res = decrypt(
        Config().library_default().complete_config(), "6qYhNwsP46Mn4gy6gyANfsMm2icAxGFA6gnFjVm9phYHeby7PZm3vthiXxSU77teQgTFGbHETn"
    )
    # res = res.decode("utf-8")
    assert res.lower() == answer_str.lower()


@pytest.mark.skip(reason="This test appears to run infiniitely.")
def test_base62():
    res = decrypt(
        Config().library_default().complete_config(), ".3vQº·îP=.ã.ÿîÌ¤U¤.[hù>.Ñü.¨zj{D"
    )
    res = res.decode("utf-8")
    assert res.lower() == answer_str.lower()

@pytest.mark.skip(reason="This test appears to run infiniitely.")
def test_base91():
    res = decrypt(
        Config().library_default().complete_config(), """>OwJh>=/fV@$x88j9ZNKB*ge$yV%lE%ZKi,<d,TX2$0t,,cjPD@JY<UCHRWznuWoQPD"""
    )
    assert res.lower() == answer_str.lower()