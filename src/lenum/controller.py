"""Controller for coordinating Linux state enumeration modules."""

from __future__ import annotations

from collections.abc import Iterable

from lenum.models import ModuleResult
from lenum.modules.firewall import FirewallEnumerator
from lenum.modules.ports import PortEnumerator
from lenum.modules.services import ServiceEnumerator
from lenum.modules.shadow import ShadowFileEnumerator
from lenum.modules.users import UserGroupPermissionEnumerator
from lenum.modules.wireless import WirelessEnumerator


class LenumController:
    """Orchestrates selected enumeration modules and aggregates results."""

    def __init__(self) -> None:
        self.modules = {
            "shadow": ShadowFileEnumerator(),
            "wireless": WirelessEnumerator(),
            "services": ServiceEnumerator(),
            "ports": PortEnumerator(),
            "firewall": FirewallEnumerator(),
            "users": UserGroupPermissionEnumerator(),
        }

    def run(self, selected_modules: Iterable[str] | None = None) -> list[ModuleResult]:
        """Run selected modules, or all modules when no selection is provided."""
        module_names = list(selected_modules) if selected_modules is not None else list(self.modules)
        results: list[ModuleResult] = []

        for module_name in module_names:
            module = self.modules.get(module_name)
            if module is None:
                results.append(
                    ModuleResult(
                        module=module_name,
                        status="error",
                        errors=[f"Unknown module: {module_name}"],
                    )
                )
                continue

            results.append(module.run())

        return results
