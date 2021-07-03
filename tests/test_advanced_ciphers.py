import pytest
from click.testing import CliRunner
import mock 
import re

from ciphey import decrypt
from ciphey.iface import Config
from ciphey.ciphey import main
from ciphey.basemods.Checkers import human

def test_xor():
    res = decrypt(Config().library_default().complete_config(),"Uihr!hr!`!udru!gns!YNS-!hu!hr!sd`mmx!mnof!un!l`jd!rtsd!ui`u!YNSunnm!b`o!fdu!hu/!Bhqidx!*!YNSunnm!hr!bnnm/")
    assert re.findall("This is a test for XOR", res)

@pytest.mark.skip("Skipping because it matches on Discover card, this is a PyWhat bug that's being fixed.")
@mock.patch("ciphey.basemods.Checkers.human.HumanChecker.check", return_value = "")
def test_xor_tui_multi_byte(mock_click):
    # https://github.com/Ciphey/Ciphey/issues/655
    runner = CliRunner()      
    mock_click.return_value = "y"
    result = runner.invoke(main, ['-vvv', '-t', '360w0x11450x114504421611100x0y0545000x06171y1511070145150x110z45081709110y45071y1100423w2z3045120z0x060z450x1145080w170042060z0u1509071w45160w040x45160y0y020v0045001x1107453w2w374y422x0y1111000301450w03450w0y091y4510110x0y05450442160x0x02090745071y110042030z104504420v001y45120z0x060z450x11450003161x42110z42071717110042030z10060042041642110w071700420x16420z0y0v1x4550505342150z11160x000x090y11001149450u1009160x45001x1107450v071x1642060z170901420w04140045160w0z170416030y0111450z0445150w16160y070x0v0x110716450u040v0y0y02420x11420w04100145160z450017101600030w1706074y453z2z37160z0z0v450x1145041500160w08004207000104101100450y114501040y42061703060v42070z160w45110x0y05090042071x160045030y014208100v110x42071x1600453z2z3742000y01171x121100064511071w114x452z0x060042260x120w001y450w0316453z2z37160z0z0v450x0x1100051704160001420x0y160z450y1149420x1142120x0v0945000045111015071745030804180x0y0545040x0145150x090v451012021703010042260x120w001y45110w450707450400090042110z42061703060v42060z0u1509071w453z2z3742000y01171x121100064511071w114x45320z1x450y1645160w0x114511071w1142160z42090z0x025z4227000104101100453z2z37160z0z0v45060w1009060y4216450610040609450x1645120z000y422x450u040107450x1645160z0z171600174x455u4z'])
    assert result.exit_code == 0
    assert re.findall("This is a string encrypted with multi", str(result.output))


@mock.patch("ciphey.basemods.Checkers.human.HumanChecker.check", return_value = "")
def test_xor_tui(mock_click):
    # https://github.com/Ciphey/Ciphey/issues/655
    runner = CliRunner()      
    mock_click.return_value = "y"
    result = runner.invoke(main, ['-t', 'Uihr!hr!`!udru!gns!YNS-!hu!hr!sd`mmx!mnof!un!l`jd!rtsd!ui`u!YNSunnm!b`o!fdu!hu/!Bhqidx!*!YNSunnm!hr!bnnm/'])
    assert result.exit_code == 0
    assert re.findall("This is a test for XOR", str(result.output))

@mock.patch("ciphey.basemods.Checkers.human.HumanChecker.check", return_value = "")
def test_xor_tui_verbose_mode_doesnt_break(mock_click):
    # We had a bug where verbose mode broke xor
    # https://discord.com/channels/754001738184392704/814565556027654214/853183178104373310
    runner = CliRunner()      
    mock_click.return_value = "y"
    result = runner.invoke(main, ['-v', '-t', 'Uihr!hr!`!udru!gns!YNS-!hu!hr!sd`mmx!mnof!un!l`jd!rtsd!ui`u!YNSunnm!b`o!fdu!hu/!Bhqidx!*!YNSunnm!hr!bnnm/'])
    assert result.exit_code == 0
    assert re.findall("This is a test for XOR", str(result.output))

def test_xor_atbash():
    # Frsi!si!{!fwif!tmh!BMH-!sf!si!hw{nnc!nmlu!fm!o{qw!ighw!fr{f!BMHfmmn!y{l!uwf!sf/!Ysjrwc!*!BMHfmmn.si!ymmn/
    # This is a test for XOR, it is really long to make sure that XORtool can get it. Ciphey + XORtool/is cool.
    # Previously xor only worked on level 1, this test ensures it always works on levels > 1
    res = decrypt(Config().library_default().complete_config(),"Frsi!si!{!fwif!tmh!BMH-!sf!si!hw{nnc!nmlu!fm!o{qw!ighw!fr{f!BMHfmmn!y{l!uwf!sf/!Ysjrwc!*!BMHfmmn.si!ymmn/")
    assert re.findall("This is a test for XOR", res)