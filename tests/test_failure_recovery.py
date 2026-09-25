from model_registry import Model, Registry, Status


def test_deployed_model_can_rollback_to_validated():
    r = Registry()
    r.add(Model("m", "1", "sha"))
    r.transition(("m", "1"), Status.VALIDATED)
    r.transition(("m", "1"), Status.DEPLOYED)
    assert r.rollback(("m", "1")).status is Status.VALIDATED
