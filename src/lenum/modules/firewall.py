"""Firewall state enumeration placeholder."""

from pathlib import Path
import shutil
import subprocess


# {
#     "module": "firewall",
#     "provider": "ufw",
#     "status": "active",
#     "rules": [...],
#     "errors": [],
# }


# systemctl status ufw
# systemctl status firewalld
# systemctl status nftables
# systemctl status iptables



class FirewallEnumerator:


    name = "firewall"

    def __init__(self) -> None:
        self.path = Path
        self.shutil = shutil
        self.subprocess = subprocess

    def run(self) -> dict[str, object]:
        providers = [
            self._service_status("ufw"),
            self._service_status("firewalld"),
            self._service_status("nftables"),
            self._service_status("iptables"),
        ]
        
        active = [p for p in providers if p["status"] == "active"]
        
        
        return {
            "module": self.name,
            "providers checked": providers,
            "active provider(s)": active if active else None,
            "errors": [],
        }


# def _service_status(self, service_name: str) -> dict[str, object]:
#         result = self.subprocess.run(
#             ["systemctl", "is-active", service_name],
#             capture_output=True,
#             text=True,
#             check=False,
#         )

#         status = result.stdout.strip() or result.stderr.strip()

#         return {
#             "name": service_name,
#             "active": result.returncode == 0,
#             "status": status,
#         }