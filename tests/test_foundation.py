from model_registry import Model, Registry, RegistryError, Status


def test_registry_lifecycle_and_rollback():
    registry = Registry()
    model = Model("demo", "1", "artifact://demo-1")

    registry.add(model)
    assert registry.transition(("demo", "1"), Status.VALIDATED).status is Status.VALIDATED
    assert registry.transition(("demo", "1"), Status.DEPLOYED).status is Status.DEPLOYED
    assert registry.rollback(("demo", "1")).status is Status.VALIDATED


def test_registry_rejects_duplicate_version():
    registry = Registry()
    model = Model("demo", "1", "artifact://demo-1")

    registry.add(model)

    try:
        registry.add(model)
    except RegistryError as exc:
        assert str(exc) == "duplicate version"
    else:
        raise AssertionError("duplicate model version must be rejected")
