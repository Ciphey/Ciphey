"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt
"""
# Tensorflow always spams my terminal with so many warnings of things I can't change
# so this tells them to shut up
import warnings
warnings.filterwarnings("ignore")


try:
    from languageCheckerMod import LanguageChecker as lc
except ModuleNotFoundError:
    from app.languageCheckerMod import LanguageChecker as lc
try:
    from neuralNetworkMod.nn import NeuralNetwork
except ModuleNotFoundError:
    from app.neuralNetworkMod.nn import NeuralNetwork

try:
    from Decryptor.basicEncryption.basic_parent import BasicParent
except ModuleNotFoundError:
    from app.Decryptor.basicEncryption.basic_parent import BasicParent

try:
    from Decryptor.Hash.hashParent import HashParent
except ModuleNotFoundError:
    from app.Decryptor.Hash.hashParent import HashParent
try:
    from Decryptor.Encoding.encodingParent import EncodingParent
except ModuleNotFoundError:
    from app.Decryptor.Encoding.encodingParent import EncodingParent


import argparse

try:
    import mathsHelper as mh
except ModuleNotFoundError:
    import app.mathsHelper as mh
import collections
from alive_progress import alive_bar


class Ciphey:
    def __init__(self, text, cipher):
        # general purpose modules
        self.ai = NeuralNetwork()
        self.lc = lc.LanguageChecker()
        self.mh = mh.mathsHelper()

        # the one bit of text given to us to decrypt
        self.text = text

        # the decryptor components
        self.basic = BasicParent(self.lc)
        self.hash = HashParent()
        self.encoding = EncodingParent(self.lc)

        self.level = 1
        self.sickomode = False
        self.cipher = cipher

    def decrypt(self):
        """
        this method calls 1 level of decrypt
        The idea is that so long as decrypt doesnt return the plaintext
        to carry on decrypting all subsets of the text until we find one that does decrypt properly
        maybe only 2 levels

        The way probability distribution works is something like this:
        {Encoding: {"Binary": 0.137, "Base64": 0.09, "Hexadecimal": 0.00148}, Hashes: {"SHA1": 0.0906, "MD5": 0.98}}
        If an item in the dictionary is == 0.00 then write it down as 0.001
        Each parental dictiony object (eg encoding, hashing) is the actual object
        So each decipherment class has a parent that controls all of it
        sha1, sha256, md5, sha512 etc all belong to the object "hashes"
        Ciphey passes each probability to these classes
        Sort the dictionary
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


        """
        self.probabilityDistribution = self.ai.predictnn(self.text)[0]
        self.whatToChoose = {
            self.hash: {
                "sha1": self.probabilityDistribution[0],
                "md5": self.probabilityDistribution[1],
                "sha256": self.probabilityDistribution[2],
                "sha512": self.probabilityDistribution[3],
            },
            self.basic: {"caesar": self.probabilityDistribution[4]},
            "plaintext": {"plaintext": self.probabilityDistribution[5]},
            self.encoding: {
                "reverse": self.probabilityDistribution[6],
                "base64": self.probabilityDistribution[7],
                "binary": self.probabilityDistribution[8],
                "hexadecimal": self.probabilityDistribution[9],
                "ascii": self.probabilityDistribution[10],
                "morse": self.probabilityDistribution[11],
            },
        }
        # sorts each indiviudal sub-dictionary
        for key, value in self.whatToChoose.items():
            for k, v in value.items():
                if v < 0.01:
                    self.whatToChoose[key][k] = 0.01

        for key, value in self.whatToChoose.items():
            self.whatToChoose[key] = self.mh.sortDictionary(value)

        # the below code selects the most likely one
        # and places it at the front
        new_dict = {}
        maximum = 0.00
        max_key = None
        max_val = None
        for key, value in self.whatToChoose.items():
            val = next(iter(value))
            val = value[val]
            if val >= maximum:
                maximum = val
                max_key = key
                max_val = value
        new_dict = collections.OrderedDict()
        new_dict[max_key] = max_val
        """
        find key in the main dict, delete it
        go through that dict and add each component to the end of this dict?
        """
        temp = self.whatToChoose
        for key, value in self.whatToChoose.items():
            if key == max_key:
                continue
            new_dict[key] = value

        # ok so this looks wacky but hear me out here
        # a.update(b)
        # adds all content of dict b onto end of dict a
        # no way to add it to front, so I have to do this :)
        self.whatToChoose = new_dict

        """
        for each dictionary in the dictionary
            sort that dictionary
        sort the overall dictionary by the first value of the new dictionary
        """
        if self.level <= 1:
            self.one_level_of_decryption()
        else:
            if self.sickomode:
                print("Sicko mode entered")
            f = open("decryptionContents.txt", "w")
            self.one_level_of_decryption(file=f, sickomode=self.sickomode)

            for i in range(0, self.level):
                # open file and go through each text item
                pass

    def one_level_of_decryption(self, file=None, sickomode=None):
        items = range(1)
        with alive_bar() as bar:
            for key, val in self.whatToChoose.items():
                # https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
                if not isinstance(key, str):
                    key.setProbTable(val)
                    ret = key.decrypt(self.text)
                    if ret["IsPlaintext?"]:
                        print(ret["Plaintext"])
                        if self.cipher:
                            if ret["Extra Information"] != None:
                                print(
                                    "The cipher used is",
                                    ret["Cipher"] + ".",
                                    ret["Extra Information"] + ".",
                                )
                            else:
                                print(ret["Cipher"])

                        bar()
                        return ret
        print("No encryption found. Here's the probabilities we calculated")
        import pprint

        pprint.pprint(self.whatToChoose)


def main():
    parser = argparse.ArgumentParser(
        description="Automated decryption tool. Put in the encrypted text and Ciphey will decrypt it."
    )
    # parser.add_argument('-f','--file', help='File you want to decrypt', required=False)
    # parser.add_argument('-l','--level', help='How many levels of decryption you want (the more levels, the slower it is)', required=False)
    # parser.add_argument('-g','--greppable', help='Are you grepping this output?', required=False)
    parser.add_argument("-t", "--text", help="Text to decrypt", required=False)
    # parser.add_argument('-s','--sicko-mode', help='If it is encrypted Ciphey WILL find it', required=False)
    parser.add_argument(
        "-c", "--cipher", help="What is the cipher used?", required=False
    )

    args = vars(parser.parse_args())
    if args["cipher"] != None:
        cipher = True
    else:
        cipher = False
    """
    ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
    ██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
    ██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
    ██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
    ╚██████╗██║██║     ██║  ██║███████╗   ██║ 
                Made by Brandon Skerritt"""

    # uryyb zl sngure uryyb zl zbgure naq v ernyyl qb yvxr n tbbq ratyvfu oernxsnfg
    if args["text"]:
        cipherObj = Ciphey(args["text"], cipher)
        cipherObj.decrypt()
    else:
        print(
            "You didn't supply any arguments. Look at the help menu with -h or --help"
        )


if __name__ == "__main__":
    main()
