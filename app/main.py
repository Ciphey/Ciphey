"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
╚██████╗██║██║     ██║  ██║███████╗   ██║ 
© Brandon Skerritt
Github: brandonskerritt
"""
from languageCheckerMod.languageChecker import LanguageChecker
from neuralNetworkMod.nn import NeuralNetwork

from Decryptor.basicEncryption.basic_parent import BasicParent
from Decryptor.Hash import hashBuster

import argparse
import mathsHelper
import collections

class Ciphey:
    def __init__(self, text):
        # general purpose modules 
        self.ai = NeuralNetwork()
        self.lc = LanguageChecker()
        self.mh = mathsHelper.mathsHelper()

        # the one bit of text given to us to decrypt
        self.text = text

        # the decryptor components
        self.basic = BasicParent(self.lc)
    def decrypt(self, text):
                
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
        self.probabilityDistribution = self.ai.predictnn(text)[0]
        self.whatToChoose = {"Hashing":
            {
            "sha1": self.probabilityDistribution[0], 
            "md5": self.probabilityDistribution[1],
            "sha256": self.probabilityDistribution[2],
            "sha512": self.probabilityDistribution[3]
            },
        self.basic: {
            "caesar": self.probabilityDistribution[4]
        },
        "plaintext":{
            "plaintext": self.probabilityDistribution[5]
        }
        }
        # sorts each indiviudal sub-dictionary
        for key, value in self.whatToChoose.items():
            for k, v in value.items():
                if v < 0.01:
                    self.whatToChoose[key][k] = 0.01
        import pprint
        pprint.pprint(self.whatToChoose)
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
        self.one_level_of_decryption()

    def one_level_of_decryption(self):
        for key, val in self.whatToChoose.items():
            if key == str:
                continue
            # https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
            if not isinstance(key, str):
                key.setProbTable(val)
                ret = key.decrypt(self.text)
            print(ret)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blog')
    parser.add_argument('-f','--file', help='File you want to decrypt', required=False)
    parser.add_argument('-l','--level', help='How many levels of decryption you want (the more levels, the slower it is)', required=False)
    parser.add_argument('-g','--greppable', help='Are you grepping this output?', required=False)
    parser.add_argument('-t','--text', help='Text to decrypt', required=False)

    args = vars(parser.parse_args())
    print("""
    ██████╗██╗██████╗ ██╗  ██╗███████╗██╗   ██╗
    ██╔════╝██║██╔══██╗██║  ██║██╔════╝╚██╗ ██╔╝
    ██║     ██║██████╔╝███████║█████╗   ╚████╔╝ 
    ██║     ██║██╔═══╝ ██╔══██║██╔══╝    ╚██╔╝  
    ╚██████╗██║██║     ██║  ██║███████╗   ██║ """)
    cipherObj = Ciphey("uryyb zl sngure uryyb zl zbgure naq v ernyyl qb yvxr n tbbq ratyvfu oernxsnfg")
    cipherObj.decrypt("this is a test")