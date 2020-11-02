"""
Create a class that can generate encryptions that ciphey can decrypt
This class takes a random string from a large corpus of data and returns it as :
{"Cipher": c, "Plaintext": p, "CipherUsed": cu, "Succeeds": true}

It would also be good if it could return randomly generate text / plaintext too, so we can get some failure test cases.

This class is used to create the class that contains the tests.
So it'll have a format like:

def test_description(self):
        assert(t, equal)
where t is the decrypted text from Ciphey, and equal is the decrypted text.

So this function does like:

for i in range(1, 20000):
    grabCipher = grabCipher()
    # this returns a random cipher, encrypted text and plaintext combo
    toAppend ='''
    def test_{cipher}_{succeeds}_{plaintext[0:10]}(textToTest):
        cipheyObj = ciphey(text)
        output = cipheyObj.decrypt()
        assert(output, {plaintext})
    '''
    file.append()
"""
import random
import string

import enciphey
from rich.progress import track


class test_generator:
    def __init__(self):
        self.HOW_MANY_TESTS = 30
        self.enCiphey_obj = enciphey.encipher()

    def main(self):
        with open("test_main_generated.py", "w") as f:
            f.write("from ciphey.__main__ import main, make_default_config")
            print("Opened fild")
            for i in track(range(1, self.HOW_MANY_TESTS)):
                print("In the for loop")
                x = self.enCiphey_obj.getRandomEncryptedSentence()
                print(x)
                # if x["CipherUsed"] == "MorseCode":
                # self.make_test_lc_true_template(cipher=x)
                to_append = self.make_test_lc_true_template(cipher=x)
                print(f"Adding {to_append}")
                f.write(to_append)

    def make_test_true_template(self, cipher):
        id = self.randomString(8)
        return f"""
def test_{cipher['Encrypted Texts']['CipherUsed']}_{id}():
    # {cipher}
    res = ciphey.main('''{cipher['Encrypted Texts']['EncryptedText']}''', config={"offline": True})
    assert(res == {cipher['Encrypted Texts']['PlainText']})
        """

    def make_test_lc_true_template(self, cipher):
        id = self.randomString(8)
        return f"""
def test_{cipher['Encrypted Texts']['CipherUsed']}_{id}():
    # {cipher}
    cfg = make_default_config('''{cipher['Encrypted Texts']['EncryptedText']}''')
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True
"""

    def randomString(self, stringLength):
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(stringLength))


t = test_generator()
t.main()


# return {"PlainText": text, "EncryptedText": encryptedText, "CipherUsed": name}
