"""Controller for coordinating Linux state enumeration modules."""

from __future__ import annotations

from collections.abc import Iterable

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