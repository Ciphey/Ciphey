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



import tensorboard

class neuralNetwork:
    def __init__(self):
        self.CATEGORIES = ["sha1", "md5", "sha256", "sha512", "caeser", "plaintext"]
        self.CATEGORIES = [1, 2, 3, 4, 5, 6]
        pass
    def editData(self, data):
        pass
    def useNetwork(self, data):
        pass
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
    def makeTrainingData(self, file):
        pass