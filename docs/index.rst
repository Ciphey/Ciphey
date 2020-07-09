.. Ciphey documentation master file, created by
   sphinx-quickstart on Thu Jun  4 18:32:21 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ciphey - Automated Decryption Tool
==================================

Ciphey is an automated decryption tool. Input text, get the decrypted text back.

        "But what type of encryption?"

That's the point. You don't know. 
Ciphey will figure it out for you.

Ciphey uses a deep neural network with a simple filtration system to approximate what something is encrypted with. And then a custom-built, customisable natural languge processing Language Checker Interface, which can detect when the given text becomes plaintext.

Usage
-----
To use as a console application:
.. code-block:: console

        ciphey [OPTIONS]

.. option:: -t <encrypted text>, --text <encrypted text>

        The encrypted text you want to decrypt.

.. option:: -g, --greppable

        Don't print out extra information such as the probability table. Useful for grepping the answer.

.. option:: -c, --cipher

        Use this option to get mroe information on the cipher used.

.. option:: -d, --debug

        Turn on debug mode, which prints out the logs of the file.

Alternatively, Ciphey can also be used with these methods:

.. code-block:: console

        $ ciphey "encrypted text here"

.. code-block:: console

        $ echo 'encrypted text' | ciphey


It is also possible to import ciphey:

.. code-block:: console

        >> from ciphey.__main__ import Ciphey

Importing Ciphey's __main__ function allows us to create a Ciphey Object:

.. code-block:: console

        >> cipheyObj = Ciphey(text = "encrypted text")

Once we've done this, the function we normally want is decrypt()

.. code-block:: console

        >> cipheyObj.decrypt()

Read the documentation if you want to learn more about the functions.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

        References <reference.rst>
        Installation Guide <install.rst>
        Language Checker <lc2.rst>
        Neural Network <nn.rst>
        What encryptions are implemented? <ciphers.rst>
        Configuration File <config.rst>
        Features <features.rst>
        How does it work? <howWork.rst>
        Settings File <settings.rst>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
