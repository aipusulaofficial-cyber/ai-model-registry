from registry_domain import Lifecycle, Version, verify_digest


def test_transition():
    digest = "a" * 64
    v = Version("m", "1", digest)
    v.transition(Lifecycle.VALIDATED)
    v.transition(Lifecycle.STAGED)
    v.transition(Lifecycle.PRODUCTION)
    assert verify_digest(digest, digest)
