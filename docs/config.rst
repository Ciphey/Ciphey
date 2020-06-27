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
        "grep": "bool: The greppable flag",
        "info": "bool: The info flag",
        "debug": "str: The loguru debug level, one of ['TRACE', 'DEBUG', 'WARNING', 'ERROR', None/~]",
        "checker": "str: The name of the language checker class to be used",
        "params": "Dict[str, Dict[str, Union[List[str], str]]]: The given module parameters, indexed by the module name and the param name",
        "modules": "List[str]: Paths to modules that should be loaded",
        "utility_threshold": "float: A value between 0 and 2 representing what Detectors should be used in the first pass",
        "format": "Dict[str, str]: formed of 'in' and 'out', which map to the name of their respective types"
    }

These are the defaults, represented as a YAML config file.
An omission of any field will result in these values being used

.. code:: yaml

    grep: false
    info: false
    debug: WARNING
    checker: brandon
    format:
      in: str
      out: str
    utility_threshold: 1.5
    score_threshold: 0.8

The following internal modules are loaded by default, even if not specified:

* The ``brandon`` LanguageChecker
* The ``cipheydists`` collection of Distributions, CharSets and WordLists
* The ``json`` Distribution, CharSet and WordLists, that load in a json file
* The ``csv`` Distribution, CharSet and WordLists, that load in a csv file
