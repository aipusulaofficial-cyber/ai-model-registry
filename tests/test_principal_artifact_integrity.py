import hashlib

import pytest

from artifact_verification import verify_artifact


def test_matching_digest_is_accepted(tmp_path):
    artifact = tmp_path / "model.bin"
    artifact.write_bytes(b"model-v1")
    digest = hashlib.sha256(b"model-v1").hexdigest()
    assert verify_artifact(str(artifact), digest)
    assert verify_artifact(str(artifact), digest.upper())


def test_tampered_artifact_is_rejected(tmp_path):
    artifact = tmp_path / "model.bin"
    artifact.write_bytes(b"model-v2")
    previous_digest = hashlib.sha256(b"model-v1").hexdigest()
    assert not verify_artifact(str(artifact), previous_digest)


@pytest.mark.parametrize("digest", ["", "abc", "g" * 64, "a" * 65, None])
def test_invalid_checksum_fails_closed(tmp_path, digest):
    artifact = tmp_path / "model.bin"
    artifact.write_bytes(b"model-v1")
    with pytest.raises(ValueError):
        verify_artifact(str(artifact), digest)
