"""User, group, and permission enumeration placeholder."""

import os
from pathlib import Path
import shutil
import subprocess

from lenum.models import ModuleResult


class UserGroupPermissionEnumerator:
    """Placeholder for users, groups, and permission enumeration."""

    name = "users"

    def __init__(self) -> None:
        self.os = os
        self.path = Path
        self.shutil = shutil
        self.subprocess = subprocess

    def run(self) -> ModuleResult:
        """Return user, group, and permission enumeration results."""
        return ModuleResult(module=self.name, metadata={"implemented": False})
