Language Checker Interface
==========================

This is a simple interface for exposing a custom language checker to Ciphey.
All the internal checkers go through this interface, so use them for worked examples

Specification
-------------

Your module must contain a ``ciphey_language_checker`` variable that points to
an a class derived from LanguageChecker.

The ``getArgs`` function must be static and take no parameters, and return a
dictionary of the following format:

.. code:: python

    {
        "flag name": {
            "desc": "str: A brief description of the flag",
            "req": "bool: whether or not the flag is required
        }
    }

The ``checkLanguage`` should be an instance method, which takes in the candidate text,
and returns True if it is an acceptable plaintext

The constructor take a single argument, the internal configuration packet of type ``Dict[str, object]``