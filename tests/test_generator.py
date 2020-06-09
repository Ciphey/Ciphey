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
    def test_{cipher}_{suceeds}_{plaintext[0:10]}(textToTest):
        cipheyObj = ciphey(text)
        output = cipheyObj.decrypt()
        assert(output, {plaintext})
    '''
    file.append()
"""
import uuid
import enCiphey


class test_generator:
    def __init__(self):
        self.HOW_MANY_TESTS = 20000
        self.enCiphey_obj = enCiphey.encipher()

    def main(self):
        with open("test_main.py", "w"):
            for i in range(1, self.HOW_MANY_TESTS):
                x = self.enCiphey_obj.getRandomEncryptedSentence()
                if x["CipherUsed"] == "MorseCode":
                    self.make_test_lc_true_template(cipher=x)
                else:
                    self.make_test_true_template(cipher=x)

    def make_test_true_template(self, cipher, id=uuid.uuid4()[0:7]):
        return f"""
        def test_{cipher['CipherUsed']}_{id}():
            res = ciphey.main('{cipher['encryptedText']}')
            assert(res == {cipher['PlainText']})
        """

    def make_test_lc_true_template(self, cipher, id=uuid.uuid4()[0:7]):
        return f"""
        def test_{cipher['CipherUsed']}_{id}():
            res = ciphey.main('{cipher['encryptedText']}')
            assert lc.checkLanguage(res) == True
    """


# return {"PlainText": text, "EncryptedText": encryptedText, "CipherUsed": name}
