# How do I install Ciphey?

## TL;DR
```shell
python3 -m pip install -U ciphey
```

## Detailed Explanation

To install Ciphey, you need 2 core things:
1. Python3.6 or above
2. Pip (on Python 3)

Check to see if Python is already installed. Run both of these commands:

```shell
python -c "import sys; print(sys.version)"
```

And/or

```shell
python3 -c "import sys; print(sys.version)"
```

If Python is installed, one of these commands will run and will output the version number. Ciphey onlysupports numbers higher than 3.6. If you see "2" or anything below "3.6", we'll need to install a more up to date version.

Make sure to note what command words. On your compputer, if `python -c "import sys; print(sys.version)"` returns something higher or equal to "3.6", then whenever you see `python3` instead write `python`.


Go to this website [https://www.python.org/](https://www.python.org/) and install Python3. Make sure the version is more than 3.6. By default. unless you expliticly choose a lower version, the version you install will > 3.6.

Next, we need to install **pip**. 

Pip is already installed by default in Python. We just need to upgrade it.

**On Linux or Mac OS** run the command:
```shell
pip3 install -U pip
```

Making sure to replace `pip3` with `pip` if you had to replace `python3` with `python`.

**On Windows**
```shell
python -m pip install -U pip
```

If these commands didn't work. explore the official Pip guide for upgrading [here](https://pip.pypa.io/en/stable/installing/#upgrading-pip).

If you faced any errors with Pip, there's a nice trouble shooting guide on installing Pip [here](https://packaging.python.org/tutorials/installing-packages/).

## Installing Ciphey

Run this command:

```shell
python3 -m pip install -U ciphey
```

Replace `python3` with `python` if you need to. If you're not sure, read the previous section `Detailed Explanation`. 

This command does many things:
* Uses Python3 (Ciphey only supports Python3.6 and above)
* The -m flag tells Python to run the module
* We are telling the version of pip inside of Python3 to install something. The reason why we use Python3 to call Pip instead of calling Pip is that the version of Pip may differ from Python, or you may have multiple versions of Python installed or you may be in a virtual environment.
* The -U flag says "upgrade". Sometimes Python gets stuck on an older version of Ciphey, so if it does -- it says to upgrade it.
* "ciphey" is the name of the package we want to install.

### Trouble Shooting
If you see any of these 3 words causing errors, please submit a GitHub issue as we have done something wrong:
* Ciphey
* CipheyCore
* CipheyDists



