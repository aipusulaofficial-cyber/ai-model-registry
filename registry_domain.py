from dataclasses import dataclass
from enum import StrEnum

class Lifecycle(StrEnum): DRAFT="draft"; VALIDATED="validated"; STAGED="staged"; PRODUCTION="production"; RETIRED="retired"

@dataclass
class Version:
    model:str; version:str; digest:str; lifecycle:Lifecycle=Lifecycle.DRAFT
    def transition(self,target:Lifecycle):
        allowed={Lifecycle.DRAFT:{Lifecycle.VALIDATED},Lifecycle.VALIDATED:{Lifecycle.STAGED},Lifecycle.STAGED:{Lifecycle.PRODUCTION},Lifecycle.PRODUCTION:{Lifecycle.RETIRED},Lifecycle.RETIRED:set()}
        if target not in allowed[self.lifecycle]:raise ValueError("invalid lifecycle transition")
        self.lifecycle=target

def verify_digest(actual:str,expected:str)->bool:return actual==expected
