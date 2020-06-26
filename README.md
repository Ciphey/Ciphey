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
Ciphey uses a deep neural network with a simple filtration system to approximate what something is encrypted with. And then a custom-built, customisable natural languge processing Language Checker Interface, which can detect when the given text becomes plaintext.


Ciphey can solve most things in about 2 seconds.
<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

# Features

- **20+ encryptions supported** such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more. **[For the full list, click here](https://ciphey.readthedocs.io/en/latest/ciphers.html)**
- **Deep neural network for targetting the right decryption** resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
- **Custom built natural language processing module** Ciphey can determine whether something is plaintext or not. It has an incredibly high accuracy, along with being fast.
- **Multi Language Support** at present, only English.
- **Supports hashes & encryptions** Which the alternatives such as CyberChef do not. 
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Blazingly fast.


# Getting Started
## Installation
### Pip
```python3 -m pip install -U ciphey```

The -U is needed, as sometimes PyPi gets stuck on an older version.

```ciphey -t "encrypted text here"```
To run ciphey.

### Cloning from GitHub

```
  git clone https://github.com/Ciphey/Ciphey
  cd Ciphey
  python3 -m ciphey -t "encrypted text here"
```
### Running Ciphey
To get rid of the progress bars, probability table, and all the noise use the grep mode.

```ciphey -t "encrypted text here" -g```
For a full list of arguments, run `ciphey -h`.

It is also possible to pipe data into Ciphey, or to use Ciphey like `ciphey 'encrypted text here'`
### Importing Ciphey
You can import Ciphey\'s __main__ and use it in your own programs and code.
This is feature is expected to expand in the next major version.
# Docs
The docs are located at [https://ciphey.readthedocs.io/en/latest/](https://ciphey.readthedocs.io/en/latest/)

# Contributors
Ciphey was invented by [Brandon Skerritt](https://github.com/brandonskerritt) way back in 2008 (don't worry, the code has upgraded since then 😜) but it wouldn't be where it is today without [Cyclic3](https://github.com/Cyclic3).
## Contributing
Please read the [contributing file](https://github.com/Ciphey/Ciphey/blob/master/CONTRIBUTING.md) or submit an issue and we can help you.
## Code Contributors
* [Cyclic3](https://github.com/Cyclic3) for various refactorings and for the C++ core
* [Szymex73](https://github.com/szymex73) for providing the TryHackMe answers dataset.
* [Michal](https://github.com/michalani) for helping with Base85 decoding.
## Financial Contributors
Please donate to us, we're students and we want Huel.
