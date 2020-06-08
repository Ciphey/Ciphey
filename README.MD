<p align="center">
  <img src="Pictures_for_README/binoculars.png" alt="Ciphey">
</p>


<p align="center">
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">
  <img src="https://github.com/brandonskerritt/Ciphey/workflows/Python%20application/badge.svg?branch=master" alt="Ciphey">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/ciphey">
<img src="https://codecov.io/gh/ciphey/ciphey/branch/master/graph/badge.svg">
<a href="https://ciphey.readthedocs.io/"><img src="https://readthedocs.org/projects/ciphey/badge/"></a>
</p>

# What is this?
Ciphey is an automated decryption tool. Input encrypted text, get the decrypted text back.
> "What type of encryption?"

That's the point. You don't know, you just know it's possibly encrypted. Ciphey will figure it out for you.

Ciphey uses a deep neural network to guess what something is encrypted with, and then a custom built natural language processing module to determine the output.

Ciphey can solve most things in about 2 seconds.
<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

# Features

- **20+ encryptions supported** such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more.
- **Deep neural network for targetting the right decryption** resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
- **Custom built natural language processing module** Ciphey can determine whether something is plaintext or not. It has an incredibly high accuracy, along with being fast.
- **Multi Language Support** at present, only English.
- **Supports hashes & encryptions** Which the alternatives such as CyberChef do not. 

# Getting Started
## Installation
### Pip
```pip3 install ciphey```

```ciphey -t "encrypted text here"```
To run ciphey.

### Cloning from GitHub
```git clone https://github.com/brandonskerritt/ciphey```
cd ciphey && python3 ciphey -t "encrypted text here"```
To run ciphey
### Running Ciphey
To get rid of the progress bars, probability table, and all the noise use the grep mode.
```ciphey -t "encrypted text here" -g```
For a full list of arguments, run `ciphey -h`.

It is also possible to pipe data into Ciphey, or to use Ciphey like `ciphey 'encrypted text here'`
### Importing Ciphey
You can import Ciphey\'s __main__ and use it in your own programs and code.
This is feature is expected to expand in the next version.
# FAQ

<details>
  <summary>Click to expand!</summary>
  
## Curious about the neural network or language checker? 
* The documentation is your friend at /docs
## The Internal Data packet
* Passed around in the program, it is `{"lc": self.lc, "IsPlaintext?": True, "Plaintext": translated, "Cipher": "Caesar", "Extra Information": "The rotation used is {counter}"}`
## What new features were added?
* Read the [changelog.md](changelog.md)
</details>


# Contributors
Ciphey was invented by [Brandon Skerritt](https://github.com/brandonskerritt) way back in 2008 (don't worry, the code has upgraded since then 😜) but it wouldn't be where it is today without [Cyclic3](https://github.com/Cyclic3).
## Contributing
Please read the contributing file.
## Code Contributors
None, so far....
## Financial Contributors
Please donate to us, we're students and we want Huel.
