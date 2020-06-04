Internal configuration packet
=============================

This is a hodge-podge of different command-line options and
configuration; it should represent the complete user input to the
process.

Since trying to work out which variables an arbitrary user module would
need is very difficult, it makes much more sense to just give them the
configuration, so that they can make up their own mind.

To that end, here is the structure. Be aware that new fields may be
implemented added without updating this document, but modification or
deprecation should not.

Structure
---------

.. code:: python

    {
        "ctext": "str: The ciphertext that is being attacked",
        "grep": "bool: The greppable flag",
        "info": "bool: The info flag",
        "debug": "str: The loguru debug level",
        "checker": "LanguageChecker: an instance of the selected language checker",
        "wordlist": "AbstractSet[Str]: The selected wordlist",
        "params": "Dict[Str, str]: The given module parameters"
    }
