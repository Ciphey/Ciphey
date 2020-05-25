# How to contribute
Ciphey is always in need of more decryption tools! 
1. Write a decryption tool (this can include encodings such as Base64 too). Make sure it has a `decrypt` function and is a class.
2. For each possible decryption, call `self.lc.checkLanguage(translated)` where `translated` is the decrypted text.
**Note** by default, all decryption modules when instantiated get passed Language Checker (lc). Look at this for example:
```python
    def __init__(self, lc):
        self.lc = lc
```
3. If result returns `True`, it is successfully decrypted to English. Return the internal data packet but make sure to change the information to match your decryption module.
4. Create a new object in the parent class. For example, in Encoding the parent is `encodingParent.py`. Simply add your object to the list of other objects. For `encodingParent.py` this list of objects is currently:
```python
        self.binary = Binary(self.lc)
        self.base64 = Base64(self.lc)
        self.ascii = Ascii(self.lc)
        self.hex = Hexadecimal(self.lc)
        self.morse = MorseCode(self.lc)
```
And then add the new object to the list of objects:
```python
self.list_of_objects = [self.caesar, self.reverse, self.pig]
```
5. It'd be nice if you wrote some tests for it, but if you don't know much about testing no worries! I can write the tests for you :)
6. I'll put your name on the list of contributors!
