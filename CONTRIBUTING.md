<p align="center">
Translations <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/CONTRIBUTING.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/CONTRIBUTING.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/CONTRIBUTING.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/CONTRIBUTING.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/CONTRIBUTING.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/CONTRIBUTING.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/CONTRIBUTING.md>🇨🇳 ZH   </a>
</p>

Howdy!

So, you're interested in contributing to Ciphey? 🤔

Perhaps you're confused as to where to start, or you believe your coding skills aren't "good enough"? Well, for the latter - that's ridiculous! We're perfectly okay with "bad code" and even then if you're reading this document you're probably a great programmer. I mean, newbies don't often learn to contribute to GitHub projects 😉

Here are some ways you can contribute to Ciphey:

- Add a new language 🧏
- Add more encryption methods 📚
- Create more documentation (very important! We would be eternally grateful)
- Fix bugs submitted via GitHub issues (we can support you in this 😊)
- Refactor the code base 🥺

If these sound hard, do not worry! This document will walk you through exactly how to achieve any of these. Also, your name will be added to Ciphey's contributors list, and we'll be eternally grateful! 🙏

We have a small Discord chat for you to talk to the developers and get some help. Alternatively, you can write a GitHub issue for your suggestion. If you want to be added to the Discord, DM us or ask us somehow.

[Discord Server](https://discord.gg/KfyRUWw)

# How to contribute

Ciphey is always in need of more decryption tools! To learn how to integrate code into ciphey, check out:

- <https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers> for a simple tutorial
- <https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey> for a API reference

It would be nice if you wrote some tests for it, by simply copying a function in the Ciphey/tests/test_main.py and replacing the ciphertext with something encoded with your cipher. If you don't add tests, we will probably still merge it, but it will be much harder for us to diagnose bugs!

It goes without saying that we will add you to the list of contributors for your hard work!

# Add a new language 🧏

The default language checker, `brandon`, works with multiple languages. Now, this may sound daunting.
But honestly, all you've got to do is take a dictionary, do a little analysis (we've written code to help you with this), add the dictionaries and analysis to a repo. And then add the option to `settings.yml`.

# Create more documentation

Documentation is the most important part of Ciphey. No documentation is extreme code debt, and we don't want that.

Trust me when I say if you contribute to great documentation you will be seen on the same level as code contributors. Documentation is absolutely vital.

There are lots of ways you can add documentation.

- Doc strings in the code
- Improving our current documentation (README, this file, our Ciphey Wiki pages)
- Translating documentation

And much more!

# Fix bugs

Visit our GitHub issues page to find all the bugs that Ciphey has! Squash them, and you'll be added to the contributors list. ;)

# Refactor the code base

Not all of Ciphey follows PEP8, and some of the code is repeated.
