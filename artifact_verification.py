import hashlib
import hmac
import re
from pathlib import Path


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_artifact(path: str, expected: str) -> bool:
    if not isinstance(expected, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", expected):
        raise ValueError("expected SHA-256 digest must be 64 hex characters")
    return hmac.compare_digest(sha256_file(path), expected.lower())
