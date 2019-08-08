from Decryptor.basicEncryption.caesar import Caesar
from Decryptor.basicEncryption.reverse import Reverse
"""
So I want to assign the prob distribution to objects
so it makes sense to do this?
list of objects
for each item in the prob distribution
replace that with the appropriate object in the list?
So each object has a getName func that returns the name as a str

new_prob_dict = {}
for key, val in self.prob:
    for obj in list:
        if obj.getName() == key:
            new_prob_dict[obj] = val

But I don't need to do all this, do I?
The dict comes in already sorted. 
So why do I need the probability values if it's sorted?
It'd be easier if I make a list in the same order as the dict?
sooo

list_objs = [caeser, etc]
counter = 0
for key, val in self.prob:
    for listCounter, item in enumerate(list_objs):
        if item.getName() == key:
            # moves the item
            list_objs.insert(counter, list_objs.pop(listCounter))
            counter = counter + 1

Eventually we get a sorted list of objs


"""
class BasicParent:
    def __init__(self, lc):
        self.lc = lc
        self.caesar = Caesar(self.lc)
        self.reverse = Reverse(self.lc)

        self.list_of_objects = [self.caesar, self.reverse]
    def decrypt(self, text):
        self.text = text

        from multiprocessing.dummy import Pool as ThreadPool 
        pool = ThreadPool(4) 
        answers = pool.map(self.callDecrypt, self.list_of_objects)

        """for item in self.list_of_objects:
            result = item.decrypt(text)
            answers.append(result)"""
        for answer in answers:
            # adds the LC objects together
            self.lc = self.lc + answer["lc"]
            if answer["IsPlaintext?"]:
                return answer
        return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": None, "Extra Information": None}
    def callDecrypt(self, obj):
        # i only exist to call decrypt
        return obj.decrypt(self.text) 
            
    def setProbTable(self, prob):
        self.probabilityDistribution = prob
        # we get a sorted list of objects :)
        counter = 0
        for key, val in self.probabilityDistribution.items():
            for listCounter, item in enumerate(self.list_of_objects):
                if item.getName() == key:
                    # moves the item
                    list_objs.insert(counter, list_objs.pop(listCounter))
                    counter = counter + 1

