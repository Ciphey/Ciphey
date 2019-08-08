class EncodingParent:
    def __init__(self, lc):
        self.lc = lc
    def decrypt(self, text):
        self.text = text
        torun = [self.base64]
        """
        ok so I have an array of functions
        and I want to apply each function to some text
        (text, function)
        but the way it works is you apply text to every item in the array (function)

        """
        from multiprocessing.dummy import Pool as ThreadPool 
        pool = ThreadPool(4) 
        results = pool.map(callFunction, torun)

        """
        Ok so this one will have a list of all functions it can call
        then it'll map.apply that for threading
        """
        pass
    def callFunction(func):
        return func(self.text)

    def binary(self, text):
        import binascii



        try:
            result = text_from_bits(text)
        except ValueError as e:
            return {"lc": self.lc, "IsPlaintext?": False, "Plaintext": None, "Cipher": None, "Extra Information": None}
        return {"lc": self.lc, "IsPlaintext?": True, "Plaintext": result, "Cipher": "ASCII to Binary encoded", "Extra Information": None}
        