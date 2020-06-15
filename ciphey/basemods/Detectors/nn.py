from typing import Optional, Dict, List

import tflite
import numpy
import sys
import ciphey
import cipheydists
from loguru import logger

from ciphey.iface import ParamSpec, T

sys.path.append("..")
try:
    import ciphey.mathsHelper as mh
except ModuleNotFoundError:
    import mathsHelper as mh

# i need the below code to make tensorflow shut up. Yup, it's SO bad you have to have 2 LINES TO MAKE IT SHUT UP!!!


class NeuralNetwork(ciphey.iface.Detector[str]):
    """
    Class to use the neural network
    """

    def what(self) -> List[str]:
        return ["caesar"]

    def scoreLikelihood(self, ctext: T) -> Dict[str, float]:
        logger.trace("Calling cipheynn")
        ctext = self.editData(ctext)
        caesar_score = self.model.predict(ctext)[4]
        return {"caesar": caesar_score}

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getName() -> str:
        return "cipheynn"

    @staticmethod
    def scoreUtility() -> float:
        return 2

    def __init__(self, config: ciphey.iface.Config):
        super().__init__(config)
        self.CATEGORIES = ["sha1", "md5", "sha256", "sha512", "caeser", "plaintext"]
        #self.CATEGORIES = [1, 2, 3, 4, 5, 6]
        # self.MODEL = load_model("cipher_detector.h5")
        self.model = tflite.Model.GetRootAsModel(cipheydists.get_model("cipher_detector"), 0)
        self.model.
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

ciphey.iface.registry.register(NeuralNetwork, ciphey.iface.Detector[str])