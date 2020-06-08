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

    def main(self):
        for i in range(1, self.HOW_MANY_TESTS):
            x = enCiphey.randomSentence()

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
            lc_res = lc.check(res)
            assert lc['IsPlaintext'] == True
    """


# return {"PlainText": text, "EncryptedText": encryptedText, "CipherUsed": name}
