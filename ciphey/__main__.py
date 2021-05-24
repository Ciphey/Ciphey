#! /usr/bin/env python3

"""
Ciphey: https://github.com/ciphey/ciphey
"""

import sys
import platform

if __name__ == "__main__":
    major = sys.version_info[0]
    minor = sys.version_info[1]

    python_version = (
        str(sys.version_info[0])
        + "."
        + str(sys.version_info[1])
        + "."
        + str(sys.version_info[2])
    )

    if major != 3 or (major == 3 and minor < 6):
        print(
            f"Ciphey requires Python 3.6+, you are using {python_version}. Please install a higher Python version. https://www.python.org/downloads/"
        )
        print("Alternatively, visit our Discord and use the Ciphey bot in #bots http://discord.skerritt.blog")
        sys.exit(1)
    if platform.system() == "Windows":
        if minor > 8:
            print("Ciphey does not currently support Python 3.9 on Windows. Please use the Discord bot at http://discord.skerritt.blog")
            sys.exit(1)
        # Not in the main imports because I don't fancy importing an entire module
        # For no reason
        import struct

        # see https://marcellodelbono.it/en/detecting-if-python-is-running-as-a-64-bit-application
        if struct.calcsize("P") * 8 == 32:
            print("You are using Python 32 bit and Windows, Ciphey does not support this. Please upgrade to Python 64-bit here https://www.python.org/downloads/")
            sys.exit(1)
    from .ciphey import main

    main()