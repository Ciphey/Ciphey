# Change Log
## 3.1
* [Feature] Added transposition cipher support
* [Bug / Feature] Language checker's first phase is now augmented. There was a bug where chi
squared would score low on paragraphs of English text. To amend this, a 2nd
first-phase check was added. If __any__ of the top 1000 English words appear
in the text, go onto the 2nd phase (dictionary checker full).
* [Maintenance] Updated & added more tests.
* [Feature] Adding a logging library (Loguru) and implemented full logging of the
program when activated. The program is now easier to decrypt.
* [Maintenance] Updated the GitHub action to automatically run tests and Black against the
code base.
* [Maintenance] Switch from `alive_bar` to ``Rich``. Rich supports progress bars like alive_bar,
but it also supports rich text output such as tables. The table is used to
prettily display the softmax distribution from the neural network to the user.
The user can now easily read what the neural network thinks the decryption is,
and what's being worked on first.
* [Feature] The program is more verbose, which means in non-grep mode users can see the
program operate in real time.
### Coming up next
These are taken from the GitHub Issues tab.
* Improved Neural Network (See /documentation for more information on this)
* Mod + XOR decryptions
* Offline mode (No hash lookups)
* Killswitch - Ciphey kills itself after X seconds. Some decryptions take forever, so if Ciphey is used as a library, waiting 30 - 60 minutes for 1 decryption module to finish sucks. Ciphey will either find the answer in X minutes or seconds, or it will return False.
* Add screenshots to readme.md (ascii cinema)


## 3.0.7
* [Feature] Added other bases
* [Bug] Fixed program not installing via Pip
* [Feature] Added program to Pip
* [Bug] Fixed basicEncryption module from crashing the program
