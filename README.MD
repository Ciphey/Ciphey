# What is this?
Ciphey is an automated decryption tool.
You put in encrypted text, and it outputs the decrypted text.

> "What type of encryption?"

That's the point. You don't know. Ciphey will find out and do it for you.

# How does it work?
You input a string (via a file, or via a terminal)

Ciphey uses a Deep Neural Network to create a probability distribution (softmax). 

This distribution gives how likely it is to be a hash, a basic encoding (hex, binary) or encryption (such as caeser, aes etc)
Ciphey will then work through each cipher to try and decode it.

Ciphey uses the language module (app/languageChecker) to determine both the language something is written in, and whether or not that string is valid in that language. So Ciphey would say "hello my name is whiteboard" is English. But it wouldn't say "iaid i2iv ria9i" is a language.

Using the probability distribution, Ciphey calls each object on a new thread. Yes, Ciphey is **multi-threaded**.

Ciphey is designed from the groundup to be as fast as physically possible. The second it sees the answer, it will stop and return that answer.

# What encryptions can Ciphey deal with?
Not just encryptions, but hashes and encodings too.

* Vigenère cipher
* Affine cipher
* Transposition Cipher
* Pig Latin
* Morse Code
* Ascii
* Binary
* Base64
* Hexadecimal
* Caesar Cipher
* Reverse (palindrome)
* Sha512
* MD5
* Sha1
* Sha384
* Sha256

# How to install
Just download the GitHub repo.

# How to use

```
pip install -r requirements.txt
```

And then

```
python3 app/main.py -t "Encrypted Text Here"
```

# The internal data packet
This is the data packet specification Ciphey uses.
```python
{"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}
```
