from model_registry import *
import pytest
def test_lifecycle():
 r=Registry();r.add(Model("m","1","uri"));r.transition(("m","1"),Status.VALIDATED);r.transition(("m","1"),Status.DEPLOYED);assert r.models[("m","1")].status is Status.DEPLOYED
def test_invalid_transition():
 r=Registry();r.add(Model("m","1","u"))
 with pytest.raises(RegistryError):r.transition(("m","1"),Status.DEPLOYED)
def test_duplicate():
 r=Registry();r.add(Model("m","1","u"))
 with pytest.raises(RegistryError):r.add(Model("m","1","u2"))
