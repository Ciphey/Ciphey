import pathlib
from setuptools import setup, find_packages
import io
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.MD").read_text()
long_description = "An automated decryption tool using machine learning"
DESCRIPTION = "An automated decryption tool using machine learning"

# get list of required installs
with open('requirements.txt') as f:
    required = f.read().splitlines()

# This call to setup() does all the work
setup(
    name="Ciphey",
    version="3.0.3",
    description="Automated decryption tool using machine learning & common sense",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/brandonskerritt/ciphey",
    author="Brandon Skerritt",
    author_email="brandon@skerritt.blog",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages("Ciphey", exclude=("tests",)),
    include_package_data=True,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "ciphey=app.__main__:main",
        ]
    },
)