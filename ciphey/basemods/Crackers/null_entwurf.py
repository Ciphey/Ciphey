# community
# by https://github.com/lukasgabriel

from typing import Optional, Dict, Union, Set, List

ctext = ''

def decode(ctext):
    pass



def split(text: list, separator: str) -> Optional[List[str]]:
    result = []
    for elem in text:
        if separator in text:
            result.append(elem.split(separator))   
        else:
            continue
    return result

text = "Contrary to popular belief, Lorem Ipsum is not simply random text. \nIt has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \nRichard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. \n\n\nLorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. \nThis book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Lorem ipsum dolor sit amet..', comes from a line in section 1.10.32.\n\n\nThe standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. \nSections 1.10.32 and 1.10.33 from 'de Finibus Bonorum et Malorum' by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.\n"

paragraphs = list(filter(lambda x : x != '', text.split("\n\n")))
lines = text.split("\n")
sentences = text.replace("\n", "").split(". ")
words = text.replace("\n", "").split(" ")
letters = list(text.replace("\n", ""))

'''Treat each new subset as a new text input set'''

class Null():
    def __init__(self, ctext):
        self.ctext = ctext
        self.paragraphs = list(filter(lambda x : x != '', ctext.split("\n\n")))
        self.lines = ctext.split("\n")
        self.sentences = ctext.replace("\n", "").split(". ")
        self.words = ctext.replace("\n", "").split(" ")
        self.letters = list(ctext.replace("\n", ""))

    def crack(self):
        pass
