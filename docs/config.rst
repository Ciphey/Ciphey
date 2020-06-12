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
        "ctext": "str: The ciphertext that is being attacked. Any value will be clobbered on program start",
        "grep": "bool: The greppable flag",
        "info": "bool: The info flag",
        "debug": "str: The loguru debug level, one of ['TRACE', 'DEBUG', 'WARNING', 'ERROR', None/~]",
        "checker": "str: The name of the language checker class to be used",
        "params": "Dict[str, Dict[str, str]]: The given module parameters, indexed by the module name and the param name",
        "modules": "List[str]: Paths to modules that should be loaded",
        "objs": "Dict[str, Any]: Various object instances for internal use"
    }

These are the defaults, represented as a YAML config file.
An omission of any field will result in these values being used

.. code:: yaml

    grep: false
    info: false
    debug: WARNING
    checker: brandon
    params:
      brandon:
        wordlist: english
        top1000: english1000
    modules: []

The following internal modules are loaded by default, even if not specified:

* The ``brandon`` LanguageChecker
* The ``cipheydists`` collection of Distributions, CharSets and WordLists
* The ``json`` Distribution, CharSet and WordLists, that load in a json file
* The ``csv`` Distribution, CharSet and WordLists, that load in a csv file