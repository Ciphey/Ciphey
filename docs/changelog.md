# Change Log
The changelog for Ciphey.

## Coming up next
These are taken from the GitHub Issues tab.
* Improved Neural Network (See /documentation for more information on this)
* Mod + XOR decryptions
* Offline mode (No hash lookups)
* Killswitch - Ciphey kills itself after X seconds. Some decryptions take forever, so if Ciphey is used as a library, waiting 30 - 60 minutes for 1 decryption module to finish sucks. Ciphey will either find the answer in X minutes or seconds, or it will return False.
* Add screenshots to readme.md (ascii cinema)
* Creating a Flask version so Ciphey can be implemented as an API. Useful for creating phone / web apps.
* Ciphey's core (the decryption modules) are now implemented in C++
* The code is now pep8'd
* Move to Poetry from setuptools.py
* Moved to Pytest from unittest
## 4.1
#### Features
* Vigenere is now enabled, due to massive performance gains from the C++ core
* Pytest can now be run over the entire program, from main to the output. This means we can crate tests that test the whole of Ciphey, not just small unit tests.
* Better input handling. Ciphey now supports pipes `echo 'hello' | ciphey` and text with no arguments `ciphey 'hello'.`
#### Bug Fixes
* Chi-squared calcuations are now done _correctly_
* Fixed bug where __main__ didn't return the output.
* Multiple debug statements were printed when not in debug mode.
#### Maintenance
* Offloaded lots of stuff onto C++ core to get much speed
* Disabled addition of language checkers, as no-one could explain why it would make sense
* Bases.py is refactored so users can manually call decryptions. The name has also changed from base64 to bases.
* LanguageChecker now follows PEP8.
* Main and MathsHelper now follow PEP8.
* Now uses Nox to Pytest against multple Python versions (3.6, 3.7, and 3.8).
* Code coverage is now calculated and used.
* Automatic application of Black formatter upon push.
* Automatic uploading to PyPi testing.
## 3.1
#### Features
* Adding a logging library (Loguru) and implemented full logging of the
program when activated. The program is now easier to decrypt.
* Added transposition cipher support
* The program is more verbose, which means in non-grep mode users can see the
program operate in real time.
* Ciphey now takes the first non flagged argument as the text to the input.
* It is now possible to pipe data into ciphey like `echo 'hello' | python3 -m ciphey`
#### Bug Fixes
* Language checker's first phase is now augmented. There was a bug where chi
squared would score low on paragraphs of English text. To amend this, a 2nd
first-phase check was added. If __any__ of the top 1000 English words appear
in the text, go onto the 2nd phase (dictionary checker full).
* Timeouts are now implemented in the hash cracking module.
* Flags previously required arguments when it didn't make sense to have an argument. Now some flags can be ran without arguments.
#### Maintenance
* Updated & added more tests.
* Updated the GitHub action to automatically run tests and Black against the
code base.
* Switch from `alive_bar` to ``Rich``. Rich supports progress bars like alive_bar,
but it also supports rich text output such as tables. The table is used to
prettily display the softmax distribution from the neural network to the user.
The user can now easily read what the neural network thinks the decryption is,
and what's being worked on first.
## 3.0.7
#### Features
* Added other bases
#### Bug Fixes
* Fixed program not installing via Pip
* Fixed basicEncryption module from crashing the program
#### Maintenance
* [Added](Added) program to Pip
