# What is this?
Ciphey is an automated decryption tool.
You put in encrypted text, and it outputs the decrypted text.

> "What type of encryption?"

That's the point. You don't know. Ciphey will find out and do it for you.

# How does it work?
You input a string (via a file, or via a terminal)

Ciphey uses a Convulutional Neural Network to create a probability distribution (softmax). 

This distribution gives how likely it is to be a hash, a basic encoding (hex, binary) or encryption (such as caeser, aes etc)
Ciphey will then work through each cipher to try and decode it.

Ciphey uses the language module (app/languageChecker) to determine both the language something is written in, and whether or not that string is valid in that language. So Ciphey would say "hello my name is whiteboard" is English. But it wouldn't say "iaid i2iv ria9i" is a language.

# What encryptions can Ciphey deal with?

# How to install

# How to use

the dictionarty.txt is a combination of
* top 30,000 most used words (american)
* top 10,000 most used british words
* 100k of most popular passwords

# The internal data packet
```python
{"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}
```