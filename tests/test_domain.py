from registry_domain import *
def test_transition():
 v=Version("m","1","sha");v.transition(Lifecycle.VALIDATED);v.transition(Lifecycle.STAGED);v.transition(Lifecycle.PRODUCTION);assert verify_digest("sha","sha")