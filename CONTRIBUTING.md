Howdy! 

So, you're interested in contributing to Ciphey? 🤔

But maybe you're confused as to where to start, or you believe your coding skills aren't "good enough". Well, for the latter - that's ridiculous! We're perfectly okay with "bad code", and even then, if you're reading this document you're probably a great programmer. I mean, newbies don't often learn to contribute to GitHub projects 😉

Here are some ways you can contribute to Ciphey:
* Add a new language 🧏
* Add more encryption methods 📚
* Create more documentation (very important‼️  We would be eternally grateful)
* Fix bugs submitted via GitHub issues (we can support you in this 😊)
* Refactor the code base 🥺

If these sound hard, do not worry! This document will walk you through exactly how to achieve any of these. And also.... Your name will be added to Ciphey's contributors list, and we'll be eternally grateful! 🙏

# Add a new language 🧏
The default language checker, `brandon`, works with multiple languages. Now, this may sound daunting.
But honestly, all you've got to do is take a dictionary, do a little analysis (we've written code to help you with this), add the dictionaries and analysis to a repo. And then add the option to `settings.yml`. 

When I created the German module, I wrote detailed documentation on how I did it. You can read that here.

# Add more encryption methods 📚

# Create more documentation
Documentation is the most important part of Ciphey. No documentation is extreme code debt, and we don't want that. 

And trust me when I say, if you contribute to great documentation you will be seen on the same level as code contributors. Documentation is absolutely vital.

There's lots of ways you can add documentation.
* Doc strings in the code
* Improving our current documentation (README, this file, our Read The Docs pages)
* Translating documentation

And much more!

# Fix Bugs
Visit our GitHub issues page to find all the bugs Ciphey has! And squash them, you'll be added to the contributors list ;)

# Refacor the code base
Not all of Ciphey follows PEP8, and some of the code is repeated.

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
