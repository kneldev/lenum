"""Firewall state enumeration placeholder."""

from pathlib import Path
import shutil
import subprocess

from lenum.models import ModuleResult


class FirewallEnumerator:
    """Placeholder for firewall rule and policy enumeration."""

    name = "firewall"

    def __init__(self) -> None:
        self.path = Path
        self.shutil = shutil
        self.subprocess = subprocess

    def run(self) -> ModuleResult:
        """Return firewall enumeration results."""
        return ModuleResult(module=self.name, metadata={"implemented": False})
