"""Model registry with immutable versions and lifecycle guards."""

from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    DRAFT = "draft"
    VALIDATED = "validated"
    DEPLOYED = "deployed"
    RETIRED = "retired"


@dataclass(frozen=True)
class Model:
    name: str
    version: str
    artifact: str
    status: Status = Status.DRAFT


class RegistryError(Exception):
    pass


class Registry:
    def __init__(self):
        self.models = {}

    def add(self, model):
        key = (model.name, model.version)
        if key in self.models:
            raise RegistryError("duplicate version")
        self.models[key] = model

    def rollback(self, key, target=Status.VALIDATED):
        model = self.models[key]
        if model.status is not Status.DEPLOYED or target is not Status.VALIDATED:
            raise RegistryError("rollback requires deployed model and validated target")
        self.models[key] = Model(model.name, model.version, model.artifact, target)
        return self.models[key]

    def transition(self, key, target):
        model = self.models[key]
        allowed = {
            Status.DRAFT: {Status.VALIDATED},
            Status.VALIDATED: {Status.DEPLOYED},
            Status.DEPLOYED: {Status.RETIRED},
            Status.RETIRED: set(),
        }
        if target not in allowed[model.status]:
            raise RegistryError("invalid lifecycle transition")
        self.models[key] = Model(model.name, model.version, model.artifact, target)
        return self.models[key]
