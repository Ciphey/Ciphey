<p align="center">
Translations <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID</a>
 <br><br>
➡️ 
<a href="https://docs.ciphey.online">Documentation</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://docs.ciphey.online/en/latest/install.html">Installation Guide</a>
 ⬅️

<br>
  <img src="Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/ciphey/ciphey">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/wM3scnc"><img alt="Discord" src="https://img.shields.io/discord/728245678895136898"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">
  
  <img src="https://github.com/brandonskerritt/Ciphey/workflows/Python%20application/badge.svg?branch=master" alt="Ciphey">
<br>
Fully automated decryption tool using natural language processing & artifical intelligence, along with some common sense.
</p>
<hr>

## [Installation Guide](https://docs.ciphey.online/en/latest/install.html)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python (Universal) </a></p> |
| ----------------------------------------------------------------------------------------- |
| <p align="center"><img src="Pictures_for_README/python.png" /></p>                        |                       |
| `python3 -m pip install ciphey --upgrade`                                                 | 

| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |
  

<hr>

# 🤔 What is this?
Ciphey is an automated decryption tool. Input encrypted text, get the decrypted text back.
> "What type of encryption?"

That's the point. You don't know, you just know it's possibly encrypted. Ciphey will figure it out for you.

Ciphey can solve most things in 3 seconds or less.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

**The technical part.** Ciphey uses a custom built artifical intelligence module (_AuSearch_) with a _Cipher Detection Interface_ to approximate what something is encrypted with. And then a custom-built, customisable natural languge processing _Language Checker Interface_, which can detect when the given text becomes plaintext.

And that's just the tip of the iceberg. For the full technical explanation, check out our [documentation](https://docs.ciphey.online/en/latest).

# ✨ Features

- **20+ encryptions supported** such as encodings (binary, base64) and normal encryptions like Caesar cipher, Transposition and more. **[For the full list, click here](https://docs.ciphey.online/en/latest/ciphers.html)**
- **Custom Built Artificial Intelligence with Augmented Search (AuSearch) for answering the question "what encryption was used?"** Resulting in decryptions taking less than 3 seconds. 
- **Custom built natural language processing module** Ciphey can determine whether something is plaintext or not. It has an incredibly high accuracy, along with being fast.
- **Multi Language Support** at present, only German & English (with AU, UK, CAN, USA variants).
- **Supports encryptions** Which the alternatives such as CyberChef Magic do not. 
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Blazingly fast.

# 🔭 Ciphey vs CyberChef

## 🔁 Base64 Encoded 42 times

<table>
  <tr>
  <th>Name</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Time</th>
    <td>2 seconds</td>
    <td>6 seconds</td>
  </tr>
    <tr>
  <th>Setup</th>
    <td><ul><li>Run ciphey on the file</li></ul></td>
    <td><ul><li>Set the regex param to "{"</li><li>You need to know how many times to recurse</li><li>You need to know it's Base64 all the way down</li><li>You need to load CyberChef (it's a bloated JS app)</li><li>Know enough about CyberChef to create this pipeline</li><li>Invert the match</li></ul></td>
  </tr>
</table>


<sub><b>Note</b> The gifs may load at different times, so one may appear significantly faster than another.</sub><br>
<sub><b>A note on magic </b>CyberChef's most similar feature to Ciphey is Magic. Magic fails instantly on this input and crashes. The only way we could force CyberChef to compete was to manually define it.</sub>


We also tested CyberChef and Ciphey with a **6gb file**. Ciphey cracked it in **5 minutes and 54 seconds**. CyberChef crashed before it even started.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🤡 Katana 🤡 | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Advanced Language Checker                   | ✅          | ❌          | ✅                   |
| Supports Encryptions                       | ✅          | ✅          | ❌                   |
| Releases named after Dystopian themes 🌃    | ✅          | ❌          | ❌                   |
| Supports hashes                            | ✅          | ✅          | ❌                   |
| Easy to set up                             | ✅          | ❌          | ✅                   |
| Can guess what something is encrypted with | ✅          | ❌          | ❌                   |
| Created for hackers by hackers             | ✅          | ✅          | ❌                   |

# 🎬 Getting Started

If you're having trouble with installing Ciphey, [read this.](https://docs.ciphey.online/en/latest/install.html)

## ‼️ Important Links (Docs, Installation guide, Discord Support)

| Installation Guide | Documentation | Discord |
| ------------------ | ------------- | ------- |
| 📖 [Installation Guide](https://docs.ciphey.online/en/latest/install.html) | 📚 [Documentation](https://docs.ciphey.online) | 🦜 [Discord](https://discord.ciphey.online)

## 🏃‍♀️Running Ciphey
There are 3 ways to run Ciphey.
1. File Input `ciphey - encrypted.txt`
2. Unqualified input `ciphey -- "Encrypted input"`
3. Normal way `ciphey -t "Encrypted input"`

![Gif showing 3 ways to run Ciphey](Pictures_for_README/3ways.gif)

To get rid of the progress bars, probability table, and all the noise use the quiet mode.

```ciphey -t "encrypted text here" -q```

For a full list of arguments, run `ciphey --help`.

### ⚗️ Importing Ciphey
You can import Ciphey\'s main and use it in your own programs and code. `from Ciphey.__main__ import main`

# 🎪 Contributors
Ciphey was invented by [Brandon Skerritt](https://github.com/brandonskerritt) in 2008, and revived in 2019. Ciphey wouldn't be where it was today without [Cyclic3](https://github.com/Cyclic3) - president of UoL's Cyber Security Society.

Ciphey was revived & recreated by the [Cyber Security Society](https://www.cybersoc.cf/) for use in CTFs. If you're ever in Liverpool, consider giving a talk or sponsoring our events. Email us at `cybersecurity@society.liverpoolguild.org` to find out more 🤠

**Major Credit** to George H for working out how we could use proper algorithms to speed up the search process.
**Special thanks** to [varghalladesign](https://www.facebook.com/varghalladesign) for designing the logo. Check out their other design work!

## 🐕‍🦺 [Contributing](CONTRIBUTING.md)
Don't be afraid to contribute! We have many, many things you can do to help out. Each of them labelled and easily explained with examples. If you're trying to contribute but stuck, tag @brandonskerritt in the GitHub issue ✨

Alternatively, join the Discord group and send a message there (link in [contrib file](CONTRIBUTING.md)) or at the top of this README as a badge.

Please read the [contributing file](CONTRIBUTING.md) for exact details on how to contribute ✨
## 💰 Financial Contributors
The contributions will be used to fund not only the future of Ciphey and its authors, but also Cyber Security Society at the University of Liverpool.

GitHub doesn't support "sponsor this project and we'll evenly distribute the money", so pick a link and we'll sort it out on our end 🥰

## ✨ Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/TheAlcanian"><img src="https://avatars3.githubusercontent.com/u/22127191?v=4" width="100px;" alt=""/><br /><sub><b>Shardion</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ATheAlcanian" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Bryzizzle"><img src="https://avatars0.githubusercontent.com/u/57810197?v=4" width="100px;" alt=""/><br /><sub><b>Bryan</b></sub></a><br /><a href="#translation-Bryzizzle" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=Bryzizzle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://lukasgabriel.net"><img src="https://avatars0.githubusercontent.com/u/52338810?v=4" width="100px;" alt=""/><br /><sub><b>Lukas Gabriel</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=lukasgabriel" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Alukasgabriel" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DarshanBhoi"><img src="https://avatars2.githubusercontent.com/u/70128281?v=4" width="100px;" alt=""/><br /><sub><b>Darshan</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ADarshanBhoi" title="Bug reports">🐛</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
