Features
==========

-  20+ encryptions supported
   <ciphers.rst>\ ``click here for the full list``.
-  Advance cipher targetting system, making use of artifical
   intelligence and common sense. Are you sick of artifical intelligence
   bloating everything? We only use it when it is **absolutely
   necessary**. The common sense part is important. If we see a string
   like “010100010100000111” we assume it is binary.
-  Custom built natural language processing module(s). Language Checker
   checks to see if the given text is plaintext. We do this either with
   the Brandon checker (the default checker), the deep neural network,
   or regex.
-  Regex checker If you have text you know is plaintext, such as
   *HTB{e563d8ae4b557d21060bfeb2a06d5cb2}* but clearly won’t be picked
   up as a language, use the regex checker.
-  Multi language support Also to note, Ciphey’s default checker,
   Brandon, has multi language support and currently supports English &
   German.
-  C++ Core -Ciphey has a C++ core for cryptanalysis tidbits. Python is
   very slow, but C++ is very fast. By offloading the bruteforcing of
   the program, we saw speed increases such as Caesar Cipher’s 30% speed
   increase.
-  Supports Hashes & Encryptions Other online tools may only support
   encodings, hashes, or encryptions. Ciphey supports all of them!
-  Tweakable -Ciphey has a settings.yml file. This file lets you tweak
   the internal procedures of Ciphey. Want to use the German dictionary
   for phase 1 of language checker, and then the English dictionary? No
   worries! You can do that. Do you have a bunch of regexes, but hate
   inputting them manually? Store them in the settings file.
-  Extensively tested with a lot of documentation -Everytime Ciphey goes
   for a release, it gets tested by many hand-written unit tests. And
   then, an automated testing system tests Ciphey 20,000 times over to
   make sure nothing breaks.
-  Not opionatedBase64 has an alternative syntax, but many online
   decoders don’t make use of the alternative syntax. Opting to give you
   the most popular one. Thus, they are optionated. Ciphey strays from
   this as much as possible. We try not to hold an opinion on anything
   we don’t need to. Alternative syntax is available for many modules,
   and is automatically tested against. No more worrying if Ciphey
-  Easy to contribute to. Want to add a new language? We have an easy to
   follow guide on this documentation. Want to add more decryption
   methods? Again, easy to follow guide. Ciphey is designed to be as
   modular as possible, so anyone wishing to contribute simply has to
   push their module and Ciphey will work with it.
-  Built by the CTF community, for the CTF community. Ciphey was
   originally built for the Geocaching community, but is now built
   mainly for the CTF community. Although, it can be used by anyone.
   Cyclic3 & Brandon (core maintainers) are commitee members of the
   Liverpool Cyber Security Society. Both regularly attend CTFs and win
   some too. Brandon was #2 on the TryHackMe leaderboards. All code
   contributors or maintainers have been in CTFs, and


