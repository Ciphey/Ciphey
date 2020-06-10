# i need the below code to make tensorflow shut up
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
from scipy.stats import chisquare
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import (
    Activation,
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    MaxPooling2D,
    Reshape,
)
from tensorflow.keras.models import Sequential, load_model
from string import punctuation
import numpy
import sys
import cipheydists

sys.path.append("..")
try:
    import ciphey.mathsHelper as mh
except ModuleNotFoundError:
    import mathsHelper as mh

# i need the below code to make tensorflow shut up. Yup, it's SO bad you have to have 2 LINES TO MAKE IT SHUT UP!!!
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


class NeuralNetwork:
    """
    Class to use the neural network
    """

    def __init__(self):
        self.CATEGORIES = ["sha1", "md5", "sha256", "sha512", "caeser", "plaintext"]
        self.CATEGORIES = [1, 2, 3, 4, 5, 6]
        # self.MODEL = load_model("cipher_detector.h5")
        self.MODEL = load_model(cipheydists.get_model("cipher_detector"))

        self.mh = mh.mathsHelper()

    def formatData(self, text):
        """
        formats the data
        """
        result = []
        result.append(len(text))
        result.append(len(list(set(list(text)))))
        return result

    def editData(self, data):
        """
        Data has to be in format:
        * [length of text, how many unique letters it has, the normalised chi square score]
        """
        new = []
        new.append(self.formatData(data))
        return numpy.asarray(new)

    def predictnn(self, text):
        """
        use this to create predictions for the NN
        returns softmax (probability distribution)
        """
        text = self.editData(text)
        return self.MODEL.predict(text)
