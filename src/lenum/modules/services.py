"""Service enumeration placeholder."""

from pathlib import Path
import shutil
import subprocess

from lenum.models import ModuleResult


class ServiceEnumerator:
    """Placeholder for system service enumeration."""

    name = "services"

    def __init__(self) -> None:
        self.path = Path
        self.shutil = shutil
        self.subprocess = subprocess

    def run(self) -> ModuleResult:
        """Return service enumeration results."""
        return ModuleResult(module=self.name, metadata={"implemented": False})
