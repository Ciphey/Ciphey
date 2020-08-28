"""
The file for Nox
"""
import nox
from typing import Any
from nox.sessions import Session
import tempfile

locations = "ciphey/", "tests/", "docs/"
nox.options.sessions = "safety", "tests"
package = "ciphey"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Install packages constrained by Poetry's lock file.
    This function is a wrapper for nox.sessions.Session.install. It
    invokes pip to install packages inside of the session's virtualenv.
    Additionally, pip is passed a constraints file generated from
    Poetry's lock file, to ensure that the packages are pinned to the
    versions specified in poetry.lock. This allows you to manage the
    packages as Poetry development dependencies.
    Arguments:
        session: The Session object.
        args: Command-line arguments for pip.
        kwargs: Additional keyword arguments for Session.install.
    """
    session.run(
        "poetry",
        "export",
        "--dev",
        "--format=requirements.txt",
        "--output=requirements.txt",
        external=True,
    )
    session.install("--constraint=requirements.txt", *args, **kwargs)


# noxfile.py
@nox.session
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session
def safety(session):
    session.run(
        "poetry",
        "export",
        "--dev",
        "--format=requirements.txt",
        "--without-hashes",
        "--output=requirements.txt",
        external=True,
    )
    install_with_constraints(session, "safety")
    session.run("safety", "check", "--file=requirements.txt", "--full-report")


@nox.session(python="3.8")
def coverage(session: Session) -> None:
    """Upload coverage data."""
    install_with_constraints(session, "coverage[toml]", "codecov")
    session.run("pip3", "install", "cipheydists")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


# noxfile.py
@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    install_with_constraints(session, "sphinx")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session
def tests(session):
    session.run("pip3", "install", "cipheydists")
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "pytest", "--cov=ciphey")
