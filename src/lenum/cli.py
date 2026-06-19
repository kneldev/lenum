"""Command line entrypoint for lenum."""

from lenum.controller import LenumController


def main() -> None:
    """Create the singleton controller without running enumeration logic."""
    LenumController()
