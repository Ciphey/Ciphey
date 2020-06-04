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
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


# noxfile.py
@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.8")
def coverage(session: Session) -> None:
    """Upload coverage data."""
    install_with_constraints(session, "coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)



# noxfile.py
@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the documentation."""
    install_with_constraints(session, "sphinx")
    session.run("sphinx-build", "docs", "docs/_build")

# python=["3.8", "3.7", "3.6"])
@nox.session(python="3.8")
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov=ciphey")
