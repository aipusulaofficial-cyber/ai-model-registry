import re
from dataclasses import dataclass
from enum import StrEnum


class Lifecycle(StrEnum):
    DRAFT = "draft"
    VALIDATED = "validated"
    STAGED = "staged"
    PRODUCTION = "production"
    RETIRED = "retired"


@dataclass
class Version:
    model: str
    version: str
    digest: str
    lifecycle: Lifecycle = Lifecycle.DRAFT

    def __post_init__(self) -> None:
        if not isinstance(self.model, str) or not self.model.strip():
            raise ValueError("model is required")
        if not isinstance(self.version, str) or not self.version.strip():
            raise ValueError("version is required")
        if not isinstance(self.digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", self.digest):
            raise ValueError("digest must be a SHA-256 hex string")

    def transition(self, target: Lifecycle):
        allowed = {
            Lifecycle.DRAFT: {Lifecycle.VALIDATED},
            Lifecycle.VALIDATED: {Lifecycle.STAGED},
            Lifecycle.STAGED: {Lifecycle.PRODUCTION},
            Lifecycle.PRODUCTION: {Lifecycle.RETIRED},
            Lifecycle.RETIRED: set(),
        }
        if target not in allowed[self.lifecycle]:
            raise ValueError("invalid lifecycle transition")
        self.lifecycle = target


def verify_digest(actual: str, expected: str) -> bool:
    return actual == expected
