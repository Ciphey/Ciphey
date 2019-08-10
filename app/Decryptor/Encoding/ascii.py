class Ascii:
    """
    turns ASCII numbers into strings
    """
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        pass
    def deasci(self, text):
        # splits into individual ascii nums
        text = text.split(" ")
        sentence = []
        # for every char in the text (63, for example)
        for char in text:
            # turn it from ascii num to char and append to list
            sentence.append(chr(char))
        # return the list as a string
        return ''.join(sentence)