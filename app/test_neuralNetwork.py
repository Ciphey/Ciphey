from neuralNetworkMod.nn import NeuralNetwork
import numpy

import unittest


class testNeuralNetwork(unittest.TestCase):
    def test_english_yes(self):
        """Checks to see if it returns True (it should)"""
        model = NeuralNetwork()
        result = model.predictnn("bcpvu up qvu ifs cpplt bxbz, cvu jotufbe tif qvmmfe")
        numpy.set_printoptions(suppress=True)
        result = numpy.argmax(result)
        self.assertEqual(result, 4)

    def test_sha1_yes(self):
        model = NeuralNetwork()
        result = model.predictnn("6D32263A85C7846D70439026B75758C9FC31A9B7")
        numpy.set_printoptions(suppress=True)
        result = numpy.argmax(result)
        self.assertEqual(result, 0)

    def test_md5_yes(self):
        model = NeuralNetwork()
        result = model.predictnn("5d41402abc4b2a76b9719d911017c592")
        numpy.set_printoptions(suppress=True)
        result = numpy.argmax(result)
        self.assertEqual(result, 1)

    def test_sha512_yes(self):
        model = NeuralNetwork()
        result = model.predictnn(
            "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"
        )
        numpy.set_printoptions(suppress=True)
        result = numpy.argmax(result)
        self.assertEqual(result, 3)

    def test_caesar_yes(self):
        model = NeuralNetwork()
        result = model.predictnn("bcpvu up qvu ifs cpplt bxbz, cvu jotufbe tif qvmmfe")
        numpy.set_printoptions(suppress=True)
        result = numpy.argmax(result)
        self.assertEqual(result, 4)
