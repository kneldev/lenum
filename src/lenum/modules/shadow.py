"""Shadow file enumeration placeholder."""

import os
from pathlib import Path

from lenum.models import ModuleResult


class ShadowFileEnumerator:
    """Placeholder for /etc/shadow metadata and access checks."""

    name = "shadow"

    def __init__(self) -> None:
        self.os = os
        self.shadow_path = Path("/etc/shadow")

    def run(self) -> ModuleResult:
        """Return shadow file enumeration results."""
        return ModuleResult(module=self.name, metadata={"implemented": False})
