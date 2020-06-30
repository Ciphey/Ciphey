[Install](https://github.com/Ciphey/Ciphey#Installation) | [TL;DR](https://github.com/Ciphey/Ciphey#what-is-this) | [Features](https://github.com/Ciphey/Ciphey#features) | [Docs](https://ciphey.readthedocs.io/en/latest/)
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
<br>
Fully automated decryption tool using natural language processing & artifical intelligence, along with some common sense.
</p>
<hr>

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python (Universal) </a></p> | <p align="center"><a href="https://pypi.org/project/ciphey"> Arch </a></p> | <p align="center"><a href="https://pypi.org/project/ciphey"> Windows </a></p> | <p align="center"><a href="https://pypi.org/project/ciphey"> Mac OS </a></p>
| --------------------                    | ---- | ----- | ----
| <p align="center"><img src="Pictures_for_README/python.png" /></p> | <p align="center"><img src="Pictures_for_README/arch.png" /></p>|<p align="center"><img src="Pictures_for_README/windows.png" /></p> | <p align="center"><img src="Pictures_for_README/apple.png" /></p>
| `python3 -m pip install ciphey --upgrade` | `yay ciphey` | `winget ciphey` | `brew ciphey`

|        Linux | Mac OS | Windows
|       -------- | ----- | ------ |
| Put CI here | | Put CI here | Put CI here
<hr>

# 🤔 What is this?
Ciphey is an automated decryption tool. Input encrypted text, get the decrypted text back.
> "What type of encryption?"

That's the point. You don't know, you just know it's possibly encrypted. Ciphey will figure it out for you.
Ciphey uses a custom built artifical intelligence module with a simple filtration system to approximate what something is encrypted with. And then a custom-built, customisable natural languge processing Language Checker Interface, which can detect when the given text becomes plaintext.


Ciphey can solve most things in about 3 seconds.
<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

# ✨ Features

- **20+ encryptions supported** such as hashes, encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more. **[For the full list, click here](https://ciphey.readthedocs.io/en/latest/ciphers.html)**
- **Custom Built Artificial Intelligence with Augmented Search (AuSearch) for answering the question "what encryption was used?"** Resulting in decryptions taking less than 3 seconds. If Ciphey cannot decrypt the text, Ciphey will use the neural network analysis to give you information on how to decrypt it yourself.
- **Custom built natural language processing module** Ciphey can determine whether something is plaintext or not. It has an incredibly high accuracy, along with being fast.
- **Multi Language Support** at present, only German & English (with AU, UK, CAN, USA variants).
- **Supports hashes & encryptions** Which the alternatives such as CyberChef do not. 
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Blazingly fast.


# 🎬 Getting Started
### 🏃 Running Ciphey
There are 3 ways to run Ciphey.

1. `ciphey -t "hello"`
2. `ciphey "hello"`
3. `cat encrypted_text.txt | ciphey`

To get rid of the progress bars, probability table, and all the noise use the grep mode.

```ciphey -t "encrypted text here" -g```

For a full list of arguments, run `ciphey -h`.

### ⚗️ Importing Ciphey
You can import Ciphey\'s main and use it in your own programs and code. `from Ciphey.__main__ import main`
# 📚 Docs
The docs are located at [https://ciphey.readthedocs.io/en/latest/](https://ciphey.readthedocs.io/en/latest/)

# 🎪 Contributors
Ciphey was invented by [Brandon Skerritt](https://github.com/brandonskerritt) in 2008, and revived in 2019. Ciphey wouldn't be where it was today without [Cyclic3](https://github.com/Cyclic3) - president of UoL's Cyber Security Society.

Ciphey was revived & recreated by the [Cyber Security Society](https://www.cybersoc.cf/) for use in CTFs. If you're ever in Liverpool, consider giving a talk or sponsoring our events. Email us at `cybersecurity@society.liverpoolguild.org` to find out more 🤠
## 🐕‍🦺 [Contributing](CONTRIBUTING.md)
Don't be afraid to contribute! We have many, many things you can do to help out. Each of them labelled and easily explained with examples. If you're trying to contribute but stuck, tag @brandonskerritt in the GitHub issue ✨
Please read the [contributing file](CONTRIBUTING.md) for exact details on how to contribute ✨
## 💰 Financial Contributors
The contributions will be used to fund not only the future of Ciphey and its authors, but also Cyber Security Society at the University of Liverpool (by the way, the University doesn't pay us to travel over the country winning competitions and representing the university. We have to pay for that by ourselves....)

GitHub doesn't support "sponsor this project and we'll evenly distribute the money", so pick a link and we'll sort it out on our end 🥰

## ✨ Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
