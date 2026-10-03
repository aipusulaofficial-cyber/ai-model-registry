import hashlib

import pytest

from artifact_verification import verify_artifact


def test_valid_artifact_digest(tmp_path):
    path = tmp_path / "model.bin"
    path.write_bytes(b"model-v1")
    digest = hashlib.sha256(b"model-v1").hexdigest()
    assert verify_artifact(str(path), digest)
    assert not verify_artifact(str(path), "0" * 64)


@pytest.mark.parametrize("digest", ["", "not-a-sha256", "g" * 64])
def test_invalid_digest_rejected(tmp_path, digest):
    path = tmp_path / "model.bin"
    path.write_bytes(b"model")
    with pytest.raises(ValueError):
        verify_artifact(str(path), digest)
