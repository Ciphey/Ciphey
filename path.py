"""Adds a directory to sys.path, permanently.

"""

import sys
import os
import site

HEADER = """\
# .pth file created by the pypath script.
# edit at your own risk
"""

SITEDIR = site.getusersitepackages()
PATH = os.path.join(SITEDIR, "pypath.pth")

if not os.path.exists(SITEDIR):
    os.mkdirs(SITEDIR)


def add(path, pth_file=None):
    path = path.strip()
    pth_file = pth_file or PATH
    if not os.path.exists(path):
        raise ValueError("doesn't exist: {}".format(path))
    with open(pth_file, "r") as f:
        for line in f:
            if line.strip(os.linesep) == path:
                # already added
                return
        empty = not f.tell()
    with open(pth_file, "a") as f:
        if empty:
            f.write(HEADER)
        f.write(os.linesep + path)


def remove(path, pth_file=None):
    pth_file = pth_file or PATH
    try:
        with open(pth_file, "r") as f:
            lines = f.read().splitlines()[2:]
    except IOError:
        raise ValueError("not found: {}".format(path))

    try:
        lines.remove(path)
    except ValueError:
        raise ValueError("not found: {}".format(path))

    lines.insert(0, HEADER)
    with open(pth_file, "w") as f:
        f.write(os.linesep.join(lines))


def show(pth_file=None):
    pth_file = pth_file or PATH
    print("current paths ({}):".format(pth_file))
    try:
        f = open(pth_file, "r")
    except IOError:
        return
    with f:
        lines = f.read()
        if not lines.startswith(HEADER):
            raise ValueError(".pth file is invalid: {}".format(pth_file))
        for line in lines.splitlines()[2:]:
            if not line.strip():
                continue
            print(line)


if __name__ == "__main__":
    import argparse

    EPILOG = "If no args are passed, the current contents are shown."
    parser = argparse.ArgumentParser(epilog=EPILOG)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", metavar="PATH")
    group.add_argument("-r", "--remove", metavar="PATH")
    parser.add_argument("-f", "--file", metavar="<path to .pth file>")
    args = parser.parse_args()

    if args.add:
        add(args.add, args.file)
    elif args.remove:
        remove(args.remove, args.file)
    else:
        show(args.file)
