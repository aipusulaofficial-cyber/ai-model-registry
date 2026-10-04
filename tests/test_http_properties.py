from fastapi.testclient import TestClient
from hypothesis import given
from hypothesis import strategies as st

from service import app

c = TestClient(app)
DIGEST = "a" * 64


def test_contract():
    assert c.get("/health/live").status_code == 200


@given(st.from_regex(r"[A-Za-z0-9_-]{1,32}", fullmatch=True))
def test_property(v):
    response = c.post(
        "/v1/registry",
        json={"key": v, "payload": {"version": v, "digest": DIGEST}},
    )
    assert response.status_code == 200
