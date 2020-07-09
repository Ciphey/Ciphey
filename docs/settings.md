# The Settings File

The settings file contains settings for Ciphey. Specifically, some of these you may want:
* REGEX list. Have a list of REGEX's for the REGEX checker? Use the settings file.
* Default language. Hate how Ciphey always loads in English? Use the settings file to change the default language to whatever you want.
* Is the language checker not working how you want it to work? Fine-tune the details in the settings file.

## Default settings file
Save this as settings.yml in the appdirs location, which can be found by running ciphey -where or --where.

```shell
        ➜ python3 ciphey -where    
        settings.yml should be placed in /home/bee/.config/ciphey
```

From this example, we can see that using the argument we need to place the settings file at /home/bee.config/ciphey/settings.yml

The settings file follows a specific format. **Copy and paste this below!**
```yaml
---
language_checker_options:
        # The language checking options. Basically, this detects plaintext.
        default_language: "english" # What language do you want to use?
        default_checker: "brandon"
        english:
                dict_name: english # the name of the dict in cipheyDists
                stopwords_name: english # The name of the stopwords set in cipheyDists
                brandon: # The brandon checker, the default checker
                        thresholds:
                                # Sentence length: {Checker: percentage threshold}
                                # Want to know how these numbers were selected? Read the docs here TODO
                                "Phase 1": {0: {"check": 0.02}, 110: {"stop": 0.15}, 150: {"stop": 0.28}}
                                "Phase 2": {0: 0.55} # phase 2 threshold
        german:
                brandon:
                        dict_name: german
                        stopwords_name: german
                        thresholds:
                                0.55

regexFile:         
        # Put your custom REGEX here
        # These 4 REGEX's cover the most popular CTF flag formats.
        # {.*} means "any text of any size here" and /i means "ignore case".
        # For example, for the CTf NoobCTF the format would be /NoobCTF{.*}/i
        - /HTB{.*}/i # TODO HTB strings are just md5s
        - /THM{.*}/i
        - /FLAG{*.}/i
        - /CTF{*.}/i
```


Some of the notable options you may want to change:
* Default language
* Default checker

And to add more regex, simply list them under the others.

                

