import hashlib
from pathlib import Path


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_artifact(path: str, expected: str) -> bool:
    if not expected:
        raise ValueError("expected digest required")
    return sha256_file(path).lower() == expected.lower()
