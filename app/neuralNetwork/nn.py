import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tensorflow.keras.callbacks import TensorBoard
import time
import numpy

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, Reshape
from keras import backend as K


import tensorboard

class neuralNetwork:
    def __init__(self):
        self.CATEGORIES = ["sha1", "md5", "sha256", "sha512", "caeser", "plaintext"]
        self.CATEGORIES = [1, 2, 3, 4, 5, 6]
        pass
    def editData(self, data):
        pass
    def useNetwork(self, data):
        """data is a list containing these 3 things (in this order)
        * length of text
        * how many letters it has (so, abc = 3. aab = 2)
        * the normalised chi square score (not relating to a specific language)"""
        new = []
        final.append(data)
        final = numpy.asarray(final)
        #print(new.shape)
        result = model.predict(new)
        return result
    def refreshEverything(self):
        """creates data and retrains the neural network. warning - can take a long time"""
        pass
    def train(self, data):
        """Run this when you want to retrain the neural network"""
        import csv
        with open('output.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
        
        # prepares the data
        # it should only return the length and how many letters it has     
        # length of text
        # how many letters
        # chi squared score   
        x = []
        y = []
        counter = 0.0
        totals = 0.00
        for item in your_list:
            counter = counter + 1
            y.append([item[-1]])
            # delete y from it
            del item[-1]
            # delete the plaintext
            del item[0]
            # delete the encrypted text
            del item[0]
            # delete the array (this was causing me problems)
            del item[2]
            item[0] = float(item[0])
            item[1] = float(item[1])
            try:
                item[2] = float(item[2])
                totals = totals + item[2]
            except ValueError as e:
                item[2] = float(totals / counter)
                
            x.append(item)
    # turns them into numpy array
    x_train = numpy.asarray(x)
    y_train = numpy.asarray(y)

    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(3,)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Flatten())
    model.add(Dense(6, activation='softmax'))

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  
              metrics=['accuracy'])
    model.fit(x_train, y_train, validation_split=0.2, epochs = 50, batch_size = 25)

    model.save("NeuralNetworkModel.model")


    def makeTrainingData(self, file):
        import os
        import hashlib
        #%%
        from string import punctuation
        from scipy.stats import chisquare

        # by default I use harry potter
        with open("harrypotter.txt", "r") as f:
            text = f.read()

        # replaces new lines with full stops
        text = text.replace('\n', '.').lower()

        # splits it up into sentences
        sentences = text.split(".")

        # gets rid of empty stirngs and get rid of the "i" for chapter numbers
        sentences = list(filter(None, sentences))
        for counter, sent in enumerate(sentences):
            if sent == "i":
                del sentences[counter]

        # So I want the table to look like:
        # text | length | how many letters are used (uniqueness) | maybe the chi squared score ? (normalised distribution not english) | frequency distribution | what it is | the plaintext
        # 
        # I want it to include these things:
        # base64
        # sha1
        # md5
        # sha256
        # caeser cipher
        # plaintext
        # 
        # So the next step would be to create encryption functions
        # then for every sentence in it
        # encrypt it
        # create a csv line
        # plaintext | encrypted text | length | how many letters are used | frequency distribution | chi squared score | what it is (base 64, sha 256, etc)
        # 
        def apply_rotation(c, factor):
            """Applies a shift of factor to the letter denoted by c"""
            if c.isalpha():
                lower = ord('A') if c.isupper() else ord('a')
                c = chr(lower + ((ord(c) - lower + factor) % 26))
            return c
        def caesar_cipher(s, k):
            """Iterates through each letter and constructs the cipher text"""
            new_message = ''
            factor = k % 26
            for c in s:
                new_message += apply_rotation(c, factor)
            return new_message
        def sha1hash(s):
            temp = str.encode(s)
            temp = hashlib.sha1(temp)
            return temp.hexdigest()
        def md5hash(s):
            temp = str.encode(s)
            temp = hashlib.md5(temp)
            return temp.hexdigest()
        def sha256hash(s):
            temp = str.encode(s)
            temp = hashlib.sha256(temp)
            return temp.hexdigest()
        def sha512hash(s):
            temp = str.encode(s)
            temp = hashlib.sha512(temp)
            return temp.hexdigest()
        types = ["sha1", "md5", "sha256", "sha512", "caeser", "caeser", "plaintext" ]
        def howManyLettersUsed(text):
            text = list(set(list(text)))
            return len(text)
        def isAscii(letter):
            """Determines whether a letter (or word) is ASCII"""
            # checks if a charecter is ascii
            # https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
            return bool(lambda s: len(s) == len(s.encode()))
        def getLetterFreq(text):
            # This part creates a letter frequency of the text
            letterFreq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

            for letter in text.lower():
                if letter in letterFreq:
                    letterFreq[letter] +=1
                else:
                    # if letter is not puncuation, but it is still ascii
                    # it's probably a different language so add it to the dict
                    if letter not in punctuation and isAscii(letter):
                        letterFreq[letter] = 1
            return list(letterFreq.values())
        # starts to write the data
        import csv
        f = open("encryptionData.csv", "w")
        counter = 0
        encryption_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        def makeCsvLine(plaintext, text, cipher):
            plaintext = plaintext
            ciphertext = text
            length = len(text)
            howManyLetters = howManyLettersUsed(text)
            letterfreq = getLetterFreq(text)
            chi = chisquare(letterfreq)[1]
            
            used = cipher
            if used == "sha1":
                used = 0
            elif used == "md5":
                used = 1
            elif used == "sha256":
                used = 2
            elif used == "sha512":
                used = 3
            elif used == "caesar":
                used = 4
            elif used == "plaintext":
                used = 5
            if plaintext == "" or plaintext == None:
                return (1)
            global counter
            encryption_writer.writerow([plaintext, ciphertext, length, howManyLetters, letterfreq, chi, used])
        import random
        for sent in sentences:        
            result = random.choice(types)
            if sent == None or sent == "" or sent == " ":
                continue
            if sent[0] == " ":
                sent = sent[1::]
            if result == "sha1":
                temp = sha1hash(sent)
                if temp == None:
                    continue
                makeCsvLine(sent, temp, "sha1")
            elif result == "md5":
                temp = md5hash(sent)
                if temp == None:
                    continue
                makeCsvLine(sent, temp, "md5")
            elif result == "sha256":
                temp = sha256hash(sent)
                if temp == None:
                    continue
                makeCsvLine(sent, temp, "sha256")
            elif result == "sha512":
                temp = sha512hash(sent)
                if temp == None:
                    continue
                makeCsvLine(sent, temp, "sha512")
            elif result == "caeser":
                temp = caesar_cipher(sent, random.randint(1, 25))
                if temp == None:
                    continue
                makeCsvLine(sent, temp, "caesar")
            elif result == "plaintext":
                makeCsvLine(sent, sent, "plaintext")
