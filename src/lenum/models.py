"""Shared data models for enumeration and reporting."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


Severity = Literal["info", "low", "medium", "high", "critical"]
ModuleStatus = Literal["ok", "warning", "error", "skipped"]


@dataclass(frozen=True)
class Finding:
    """A single reportable observation from an enumeration module."""

    title: str
    description: str
    severity: Severity = "info"
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ModuleResult:
    """Standard result wrapper returned by every enumeration module."""

    module: str
    status: ModuleStatus = "ok"
    findings: list[Finding] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
