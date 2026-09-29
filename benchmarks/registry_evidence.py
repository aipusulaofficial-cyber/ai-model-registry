import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import json
from registry_domain import Version,Lifecycle,verify_digest
v=Version("evidence","1","sha256:abc"); path=[]
for x in (Lifecycle.VALIDATED,Lifecycle.STAGED,Lifecycle.PRODUCTION): v.transition(x); path.append(v.lifecycle.value)
report={"path":path,"final":v.lifecycle.value,"digest_match":verify_digest("sha256:abc","sha256:abc"),"digest_mismatch":verify_digest("bad","sha256:abc")}
if path!=["validated","staged","production"] or not report["digest_match"] or report["digest_mismatch"]: raise SystemExit(report)
print(json.dumps(report,sort_keys=True))
