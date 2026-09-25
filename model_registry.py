"""Model registry with immutable versions and lifecycle guards."""
from dataclasses import dataclass
from enum import Enum
class Status(str,Enum): DRAFT="draft";VALIDATED="validated";DEPLOYED="deployed";RETIRED="retired"
@dataclass(frozen=True)
class Model: name:str;version:str;artifact:str;status:Status=Status.DRAFT
class RegistryError(Exception):pass
class Registry:
 def __init__(self):self.models={}
 def add(self,m):
  k=(m.name,m.version)
  if k in self.models:raise RegistryError("duplicate version")
  self.models[k]=m
 def rollback(self,k,target=Status.VALIDATED):\n  m=self.models[k]\n  if m.status is not Status.DEPLOYED or target is not Status.VALIDATED:raise RegistryError("rollback requires deployed model and validated target")\n  self.models[k]=Model(m.name,m.version,m.artifact,target);return self.models[k]\n def transition(self,k,target):
  m=self.models[k];allowed={Status.DRAFT:{Status.VALIDATED},Status.VALIDATED:{Status.DEPLOYED},Status.DEPLOYED:{Status.RETIRED},Status.RETIRED:set()}
  if target not in allowed[m.status]:raise RegistryError("invalid lifecycle transition")
  self.models[k]=Model(m.name,m.version,m.artifact,target);return self.models[k]
