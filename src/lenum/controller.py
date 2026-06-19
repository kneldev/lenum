"""Singleton controller for Linux state enumeration modules."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

from lenum.modules.firewall import FirewallEnumerator
from lenum.modules.ports import PortEnumerator
from lenum.modules.services import ServiceEnumerator
from lenum.modules.shadow import ShadowFileEnumerator
from lenum.modules.users import UserGroupPermissionEnumerator
from lenum.modules.wireless import WirelessEnumerator


class LenumController:
    """Singleton owner for all enumeration modules."""

    _instance: LenumController | None = None

    def __new__(cls) -> LenumController:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        self.project_root = Path.cwd()
        self.os = os
        self.path = Path
        self.shutil = shutil
        self.subprocess = subprocess

        self.shadow = ShadowFileEnumerator()
        self.wireless = WirelessEnumerator()
        self.services = ServiceEnumerator()
        self.ports = PortEnumerator()
        self.firewall = FirewallEnumerator()
        self.users = UserGroupPermissionEnumerator()

        self._initialized = True
