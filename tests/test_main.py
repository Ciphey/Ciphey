import pytest

from ciphey import decrypt
from ciphey.iface import Config

answer_str = "Hello my name is bee and I like dog and apple and tree"


def test_a1z26():
    res = decrypt(
        Config().library_default().complete_config(),
        "8 5 12 12 15 13 25 14 1 13 5 9 19 2 5 5 1 14 4 9 12 9 11 5 4 15 7 1 14 4 1 16 16 12 5 1 14 4 20 18 5 5",
    )
    assert res == "hellomynameisbeeandilikedogandappleandtree"


def test_affine():
    res = decrypt(
        Config().library_default().complete_config(),
        "Ihsst bf kxbh rd ghh xky R srjh ytz xky xccsh xky muhh",
    )
    assert res == answer_str


def test_ascii_shift():
    res = decrypt(
        Config().library_default().complete_config(),
        '"?FFIzGSzH;G?zCMz<??z;H>z#zFCE?z>IAz;H>z;JJF?z;H>zNL??',
    )
    assert res == answer_str


def test_atbash():
    res = decrypt(
        Config().library_default().complete_config(),
        "Svool nb mznv rh yvv zmw R orpv wlt zmw zkkov zmw givv",
    )
    assert res == answer_str


def test_baconian_complete_variant():
    res = decrypt(
        Config().library_default().complete_config(),
        "AABBB AABAA ABABB ABABB ABBBA ABBAA BBAAA ABBAB AAAAA ABBAA AABAA ABAAA BAABA AAAAB AABAA AABAA AAAAA ABBAB AAABB ABAAA ABABB ABAAA ABABA AABAA AAABB ABBBA AABBA AAAAA ABBAB AAABB AAAAA ABBBB ABBBB ABABB AABAA AAAAA ABBAB AAABB BAABB BAAAB AABAA AABAA",
    )
    assert res == "HELLOMYNAMEISBEEANDILIKEDOGANDAPPLEANDTREE"


def test_baconian_standard_variant():
    res = decrypt(
        Config().library_default().complete_config(),
        "AABBB AABAA ABABA ABABA ABBAB ABABB BABBA ABBAA AAAAA ABABB AABAA ABAAA BAAAB AAAAB AABAA AABAA AAAAA ABBAA AAABB ABAAA ABABA ABAAA ABAAB AABAA AAABB ABBAB AABBA AAAAA ABBAA AAABB AAAAA ABBBA ABBBA ABABA AABAA AAAAA ABBAA AAABB BAABA BAAAA AABAA AABAA",
    )
    assert res == "HELLOMYNAMEISBEEANDILIKEDOGANDAPPLEANDTREE"


def test_base32():
    res = decrypt(
        Config().library_default().complete_config(),
        "JBSWY3DPEBWXSIDOMFWWKIDJOMQGEZLFEBQW4ZBAJEQGY2LLMUQGI33HEBQW4ZBAMFYHA3DFEBQW4ZBAORZGKZI=",
    )
    assert res == answer_str


def test_base58_bitcoin():
    res = decrypt(
        Config().library_default().complete_config(),
        "6qYhNwsP46Mn4gy6gyANfsMm2icAxGFA6gnFjVm9phYHeby7PZm3vthiXxSU77teQgTFGbHETn",
    )
    assert res == answer_str


def test_base58_ripple():
    res = decrypt(
        Config().library_default().complete_config(),
        "aqY64A1PhaM8hgyagyw4C1Mmp5cwxGEwag8EjVm9F6YHebyfPZmsvt65XxS7ffteQgTEGbHNT8",
    )
    assert res == answer_str


def test_base62():
    res = decrypt(
        Config().library_default().complete_config(),
        "2mQvnz9Yevvb7DRCuyDltsP31vJLToR5pjE9orWkzHMUsht2kbC96PLbZ1sdIocsGHENrzC2n",
    )
    assert res == answer_str


def test_base64():
    res = decrypt(
        Config().library_default().complete_config(),
        "SGVsbG8gbXkgbmFtZSBpcyBiZWUgYW5kIEkgbGlrZSBkb2cgYW5kIGFwcGxlIGFuZCB0cmVl",
    )

    assert res == answer_str


def test_base69():
    res = decrypt(
        Config().library_default().complete_config(),
        "kAZAtABBeB8A-AoB8ADBNAhBLA1AFBgA0AXBfBGATAVAFBgAwAWBHB<ACAkA-AnB0AVBnBNBDARAZBiBQAYAtAhBhABA<ArB4AbAMANBDAFAXBfBQAdAOAmArAUAAA2=",
    )
    assert res == answer_str


def test_base85():
    res = decrypt(
        Config().library_default().complete_config(),
        "87cURD]inB+DtV)AKY].+C\\nn+CT.u+A!\\lBkq9&A8c*'@;]Tu@;p1%AKYE!A0>u7ARt",
    )
    assert res == answer_str


def test_base91():
    res = decrypt(
        Config().library_default().complete_config(),
        ">OwJh>=/fV@$x88j9ZNKB*ge$yV%lE%ZKi,<d,TX2$0t,,cjPD@JY<UCHRWznuWoQPD",
    )
    assert res == answer_str


def test_baudot():
    res = decrypt(
        Config().library_default().complete_config(),
        "10100 00001 10010 10010 11000 00100 11100 10101 00100 01100 00011 11100 00001 00100 00110 00101 00100 11001 00001 00001 00100 00011 01100 01001 00100 00110 00100 10010 00110 01111 00001 00100 01001 11000 11010 00100 00011 01100 01001 00100 00011 10110 10110 10010 00001 00100 00011 01100 01001 00100 10000 01010 00001 00001",
    )
    assert res == answer_str.upper()


def test_binary():
    res = decrypt(
        Config().library_default().complete_config(),
        "01001000 01100101 01101100 01101100 01101111 00100000 01101101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01100010 01100101 01100101 00100000 01100001 01101110 01100100 00100000 01001001 00100000 01101100 01101001 01101011 01100101 00100000 01100100 01101111 01100111 00100000 01100001 01101110 01100100 00100000 01100001 01110000 01110000 01101100 01100101 00100000 01100001 01101110 01100100 00100000 01110100 01110010 01100101 01100101",
    )

    assert res == answer_str


@pytest.mark.skip(
    "Can't decode base64 + caesar https://github.com/Ciphey/Ciphey/issues/606"
)
def test_binary_base64_caesar():
    res = decrypt(
        Config().library_default().complete_config(),
        "01010110 01011000 01001010 00110101 01100101 01010111 01001001 01100111 01100101 01101101 01110111 01100111 01011001 01010111 00110101 00110110 01100011 01101001 01000010 00110010 01011010 01101001 01000010 01110110 01100011 01101110 01001001 01100111 01100010 01101101 01000110 01111000 01001001 01000110 01011001 01100111 01100101 01011000 01011010 00110100 01100011 01101001 01000010 01111000 01011001 01101110 01010001 01100111 01100010 01101101 01000110 01111000 01001001 01000111 00110101 01101010 01011001 00110011 01101100 01111001 01001001 01000111 00110101 01101000 01100011 01010011 01000010 01101110 01011010 01011000 01001010 01111001 00001010",
    )

    assert res == answer_str


def test_braille():
    res = decrypt(
        Config.library_default().complete_config(),
        "⠓⠑⠇⠇⠕⠀⠍⠽⠀⠝⠁⠍⠑⠀⠊⠎⠀⠃⠑⠑⠀⠁⠝⠙⠀⠊⠀⠇⠊⠅⠑⠀⠙⠕⠛⠀⠁⠝⠙⠀⠁⠏⠏⠇⠑⠀⠁⠝⠙⠀⠞⠗⠑⠑",
    )
    assert res == answer_str.lower()


def test_brainfuck():
    res = decrypt(
        Config().library_default().complete_config(),
        "+[+++++++>+<]>-.-[+>-----<]>++.+++++++..+++.+[+>++<]>.[++>+<]>---.--[+++>-<]>.-[+>++++<]>.[++>+<]>--.-[+++>++<]>-.+[-->---<]>.--------.[+++++>+<]>+.-[+++>--<]>-.++++++++++.---[+>++<]>.[+++>-<]>++.+++..[+++++>+<]>+.[+++>-<]>+.+[-->---<]>+.----------.-[+++>-<]>-.-[+++>+<]>--.-[+>----<]>.++[+++>--<]>.---.++.------.[+++++>+<]>+.+[+>---<]>+.+++++++++++.--------.-[+++>-<]>--.[+++>-<]>+.+[-->---<]>+.----------.-[+++>-<]>-.[+++>-<]>+.-[-->---<]>..----.-------.[+++++>+<]>+.[+++>-<]>+.+[-->---<]>+.----------.-[+++>-<]>-.[++>+<]>++++.--.-------------..",
    )
    assert res == answer_str


def test_brandon():
    res = decrypt(
        Config().library_default().complete_config(),
        "R hvv blf tzgsvi yvuliv nv...sfmtib...gviirurvw... Xofgxsrmt blfi yzyvh gl blfi yivzhg. Vnkvili Vnsbi srh nzixsvw srh ovtrlmh rmgl lfi ozmwh... Ozrw hrvtv gl vevib uligivhh uiln sviv gl gsv Yofv Nlfmgzrmh. Izyrw zmw izevmlfh, sv yrgvh zmw yrgvh zdzb. Nvm lu gsv Mligs, blf hgzmw zg gsv kivxrkrxv. Blfi prmth szev uzrovw blf, hl mld blf gfim gl gsv tlwh! Zmw bvg blf wl mlg kovzw? Blf wl mlg pmvvo gl wfhg blfi svzwh drgs zhs? Rmhgvzw blf dzro,  Dsb szev gsv tlwh ulihzpvm fh?  Dv nfhg ollp rmgl gsv girzoh dv uzrovw olmt ztl! Rm z grnv kzhhvw, lfi dliow rmgvigdrmvw drgs zmlgsvi gsilfts zm fksvzezo hxslozih xzoo gsv Xlmqfmxgrlm lu gsv Hksvivh... Gsv tlwh zooldvw fmslob ulixvh gl hork rmgl lfi wlnzrm. Gsv luuhkirmt lu gszg xzgzxobhn dzh gsv mvuvirlfh ulixv xzoovw nztrx... Bvg dv wrw mlg yzmrhs rg, rmhgvzw hgfwbrmt gsv erov zixzmv uli lfi kldvi zmw dvzogs! Zmw gsv nlmhgvih zg lfi wlli...gsv fmslob ivorxgh lu gsrh Xlmqfmxgrlm? ...gsv gilooh...gsv xlikhv vzgvih...gsv dvivdloevh? Wrw dv izrhv lfi hdliwh ztzrmhg gsvn? Li szev dv ozrw gsrh yfiwvm lm lgsvih? Lm hl-xzoovw drgxsvih? Hgizb xsrowivm gzftsg gsv dzbh lu ulfo hlixvib, gsvri ylwrvh nfgzgvw gsilfts yozhksvnlfh irgfzo. Hvmg gl urtsg nlmhgvih gslfts gsvb xlfow mlg wrhgrmtfrhs tllw uiln vero. Gsv uorxpvi lu sfnzmrgb olmt vcgrmtfrhsvw drgsrm gsvn. Bvh, gsvri mfnyvih szev wdrmwovw gsilfts gsv bvzih. Yfg z uvd hgroo ilzn lfi ozmwh, luuvirmt gsvri yollwb dlip uli xlrm. Gl gsrh wzb gsvb hsznv fh drgs gsvri evib vcrhgvmxv! Gsv Mligs yovvwh, uolttvw yb dzi. Gsv yzggovh ziv gsv tlwh' dsrk, xszhgrhvnvmg uli lfi hrmh! Zmw ovg fh mlg ulitvg gsv gviilih, gsv hxlfitvh uiln yvblmw lfi dliow! Gsv Drow Sfmg irwvh gsv hpb drgs vevib ufoo nllm! Gsv wzip izrwvih zywfxg lfi xsrowivm rmgl ozmwh fmpmldm! Hlnv hzb gsvb svizow z hvxlmw Xlmqfmxgrlm! Xzm dv xszig z xlfihv yzxp rmgl gsv ortsg? Droo dv urmw gsv hgivmtgs gl yzmrhs gsv nztvh uiln lfi prmtwlnh? Fmrgv zilfmw gsv dzings lu gsv Vgvimzo Uriv? Mrts rh gsv Grnv lu gsv Hdliw zmw gsv Zcv! Mlmv droo urtsg gsrh dzi rm lfi hgvzw! Mrts rh gsv Grnv lu Nzwmvhh zmw Wrhwzrm!",
    )
    assert bool(res) is True


def test_caesar():
    res = decrypt(
        Config().library_default().complete_config(),
        "Uryyb zl anzr vf orr naq V yvxr qbt naq nccyr naq gerr",
    )
    assert res == answer_str


def test_decimal():
    res = decrypt(
        Config().library_default().complete_config(),
        "72 101 108 108 111 32 109 121 32 110 97 109 101 32 105 115 32 98 101 101 32 97 110 100 32 73 32 108 105 107 101 32 100 111 103 32 97 110 100 32 97 112 112 108 101 32 97 110 100 32 116 114 101 101",
    )
    assert res == answer_str


def test_dna():
    res = decrypt(
        Config().library_default().complete_config(),
        "GAT AAT GCT ATT TCT ATT AAT ACT GAA CGT GAA TCT ACT ATT AAT GGT",
    )
    assert res == "DNAISINTERESTING"


def test_dtmf():
    res = decrypt(
        Config().library_default().complete_config(),
        "1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1336-941 1209-697 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1209-697 1336-941 1336-941 1336-941 1336-941 1336-941 1336-941 1209-697 1209-697 1209-697 1336-941 1209-697 1336-941 1336-941 1336-941 1209-697 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697 1336-941 1209-697 1209-697 1336-941 1336-941 1209-697 1336-941 1209-697",
    )
    assert res == answer_str


def test_galactic():
    res = decrypt(
        Config().library_default().complete_config(),
        "⍑ᒷꖎꖎ𝙹 ᒲ|| リᔑᒲᒷ ╎ᓭ ʖᒷᒷ ᔑリ↸ i ꖎ╎ꖌᒷ ↸𝙹⊣ ᔑリ↸ ᔑ!¡!¡ꖎᒷ ᔑリ↸ ℸ ̣ ∷ᒷᒷ",
    )
    assert res == answer_str.lower()


def test_galactic_Xproblem():
    res = decrypt(
        Config().library_default().complete_config(),
        "⍑ᔑꖎ╎⎓ᔑ ̇/,  ̇/||ꖎ𝙹!¡⍑𝙹リᒷ, ᔑ  ̇/ ᔑꖎ𝙹リᒷ ᔑリ↸  ̇/ᒷ∷𝙹 ̇/ ⎓∷𝙹ᒲ 𝙹 ̇/⎓𝙹∷↸",
    )
    assert res == "halifax, xylophone, a x alone and xerox from oxford"


def test_gzip():
    res = decrypt(
        Config().library_default().complete_config(),
        "H4sIAAzul18A/yXJzQmAMBSEwVa+ckwZT7LIw80P6sXuA3ocZpM9aC89msibXSJ6peA8RR3Hx5jTfzyXtAAbQvCyNgAAAA==",
    )
    assert res == answer_str


def test_hexadecimal():
    res = decrypt(
        Config().library_default().complete_config(),
        "48 65 6c 6c 6f 20 6d 79 20 6e 61 6d 65 20 69 73 20 62 65 65 20 61 6e 64 20 49 20 6c 69 6b 65 20 64 6f 67 20 61 6e 64 20 61 70 70 6c 65 20 61 6e 64 20 74 72 65 65",
    )

    assert res == answer_str


def test_json_problem():
    res = decrypt(
        Config().library_default().complete_config(),
        "0110100001100101011011000110110001101111",
    )
    assert res != "0110100001100101011011000110110001101111"


def test_leetspeak():
    res = decrypt(
        Config().library_default().complete_config(),
        "|-|3ll0 my n4m3 1s 833 4nd 1 l1k3 D06 4ND 4ppl3 4nd 7R33",
    )
    assert res.lower() == answer_str.lower()


def test_morse_code():
    res = decrypt(
        Config().library_default().complete_config(),
        ".... . .-.. .-.. ---/-- -.--/-. .- -- ./.. .../-... . ./.- -. -../../.-.. .. -.- ./-.. --- --./.- -. -../.- .--. .--. .-.. ./.- -. -../- .-. . .",
    )
    assert res == answer_str.upper()


def test_multi_tap():
    res = decrypt(
        Config().library_default().complete_config(),
        "44 33 555 555 666 0 6 999 0 66 2 6 33 0 444 7777 0 22 33 33 0 2 66 3 0 444 0 555 444 55 33 0 3 666 4 0 2 66 3 0 2 7 7 555 33 0 2 66 3 0 8 777 33 33",
    )
    assert res == answer_str.upper()


def test_new_line_at_start_returns():
    # Language Checker should return True by stripping new line
    # but the new line should be returned to the user as new lines are important
    res = decrypt(Config().library_default().complete_config(), "\npass\n")

    assert res == "\npass\n"


def test_new_line_strip_and_return():
    # Language Checker should return True by stripping new line
    # but the new line should be returned to the user as new lines are important
    res = decrypt(Config().library_default().complete_config(), "pass\n")

    assert res == "pass\n"


def test_octal():
    res = decrypt(
        Config().library_default().complete_config(),
        "110 145 154 154 157 40 155 171 40 156 141 155 145 40 151 163 40 142 145 145 40 141 156 144 40 111 40 154 151 153 145 40 144 157 147 40 141 156 144 40 141 160 160 154 145 40 141 156 144 40 164 162 145 145",
    )
    assert res == answer_str


def test_plaintext():
    res = decrypt(Config().library_default().complete_config(), answer_str)
    assert res == answer_str


def test_quadgrams_messed_up_spacing():
    res = decrypt(
        Config().library_default().complete_config(),
        "H ello m y na m e is b ee an d I l ik e do g a n d ap pl e a nd tr e e",
    )
    assert (
        res == "H ello m y na m e is b ee an d I l ik e do g a n d ap pl e a nd tr e e"
    )


def test_quadgrams_no_spaces():
    res = decrypt(
        Config().library_default().complete_config(),
        "HellomynameisbeeandIlikedogandappleandtree",
    )
    assert res == "HellomynameisbeeandIlikedogandappleandtree"


def test_quadgrams_space_between_every_letter():
    res = decrypt(
        Config().library_default().complete_config(),
        "H e l l o m y n a m e i s b e e a n d I l i k e d o g a n d a p p l e a n d t r e e",
    )
    assert (
        res
        == "H e l l o m y n a m e i s b e e a n d I l i k e d o g a n d a p p l e a n d t r e e"
    )


def test_reversed_text():
    res = decrypt(
        Config().library_default().complete_config(),
        "eert dna elppa dna god ekil I dna eeb si eman ym olleH",
    )
    assert res == answer_str


def test_rot47():
    res = decrypt(
        Config().library_default().complete_config(),
        "$A9:?I @7 3=24< BF2CEK[ ;F586 >J G@H",
    )
    assert res == "Sphinx of black quartz, judge my vow"


def test_soundex():
    res = decrypt(
        Config().library_default().complete_config(),
        "H236 I200 I500 T000 P230",
    )
    assert res.lower() == "history is in the past"


def test_tap_code():
    res = decrypt(
        Config().library_default().complete_config(),
        "4,4 1,5 4,3 4,4  3,4 3,3 1,5  4,4 5,2 3,4  4,4 2,3 4,2 1,5 1,5",
    )
    assert res == "test one two three".upper()


def test_url():
    res = decrypt(
        Config().library_default().complete_config(),
        "https%3A%2F%2Fwww%2Egoogle%2Ecom%2Fsearch%3Fq%3Dciphey",
    )
    assert res == "https://www.google.com/search?q=ciphey"


def test_uuencode():
    res = decrypt(
        Config().library_default().complete_config(),
        'begin 644 /dev/stdout\nM2&5L;&\\@;7D@;F%M92!I<R!B964@86YD($D@;&EK92!D;V<@86YD(&%P<&QE\n)(&%N9"!T<F5E\n`\nend\n',
    )
    assert res == answer_str
    res = decrypt(
        Config().library_default().complete_config(),
        'M2&5L;&\\@;7D@;F%M92!I<R!B964@86YD($D@;&EK92!D;V<@86YD(&%P<&QE\n)(&%N9"!T<F5E\n',
    )
    assert res == answer_str


def test_vigenere():
    res = decrypt(
        Config().library_default().complete_config(),
        "Rijvs ki rywi gc fco eln M jsoc nse krb ktnvi yxh rbic",
    )

    assert res == answer_str


def test_xandy():
    res = decrypt(
        Config().library_default().complete_config(),
        "xDxxDxxx xDDxxDxD xDDxDDxx xDDxDDxx xDDxDDDD xxDxxxxx xDDxDDxD xDDDDxxD xxDxxxxx xDDxDDDx xDDxxxxD xDDxDDxD xDDxxDxD xxDxxxxx xDDxDxxD xDDDxxDD xxDxxxxx xDDxxxDx xDDxxDxD xDDxxDxD xxDxxxxx xDDxxxxD xDDxDDDx xDDxxDxx xxDxxxxx xDxxDxxD xxDxxxxx xDDxDDxx xDDxDxxD xDDxDxDD xDDxxDxD xxDxxxxx xDDxxDxx xDDxDDDD xDDxxDDD xxDxxxxx xDDxxxxD xDDxDDDx xDDxxDxx xxDxxxxx xDDxxxxD xDDDxxxx xDDDxxxx xDDxDDxx xDDxxDxD xxDxxxxx xDDxxxxD xDDxDDDx xDDxxDxx xxDxxxxx xDDDxDxx xDDDxxDx xDDxxDxD xDDxxDxD",
    )
    assert res == answer_str
