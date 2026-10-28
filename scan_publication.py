#!/usr/bin/env python3
"""Offline publication guard. Reports locations and rule names, never secret values."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
RULES = [
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----")),
    ("putty-private-key", re.compile(r"PuTTY-User-Key-File-[23]:")),
    ("github-token", re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{20,255}|github_pat_[A-Za-z0-9_]{30,255})")),
    ("api-secret", re.compile(r"sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}")),
    ("aws-access-key", re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}")),
    ("google-api-key", re.compile(r"AIza[A-Za-z0-9_-]{30,}")),
    ("slack-token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}")),
    ("stripe-secret", re.compile(r"(?:sk|rk)_live_[A-Za-z0-9]{16,}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("credential-in-url", re.compile(r"https?://[^\s/@:]+:[^\s/@]+@")),
    ("local-user-path", re.compile(r"/(?:Users|home)/[^/\s]+/")),
]
CREDENTIAL_ASSIGNMENT = re.compile(
    r"\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|private[_-]?key)\b"
    r"\s*[:=]\s*['\"]([^'\"\n]{12,})['\"]", re.I)
FORBIDDEN_NAMES = {".env", "auth.json", "credentials.json", ".npmrc", ".pypirc", ".DS_Store"}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".der", ".pyc", ".pyo", ".sqlite", ".db"}


def inspect_text(text):
    issues = []
    for rule, pattern in RULES:
        for match in pattern.finditer(text):
            issues.append({"rule": rule, "line": text.count("\n", 0, match.start()) + 1})
    for match in CREDENTIAL_ASSIGNMENT.finditer(text):
        value = match.group(1)
        if value.startswith(("$", "<", "YOUR_", "your-", "example", "REDACTED")):
            continue
        issues.append({"rule": "credential-assignment", "line": text.count("\n", 0, match.start()) + 1})
    return issues


def main():
    issues, count = [], 0
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts:
            continue
        if path.is_symlink():
            issues.append({"file": relative.as_posix(), "rule": "symlink-not-allowed"})
            continue
        if not path.is_file():
            continue
        count += 1
        name = path.name.lower()
        if (name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES
                or name.startswith(("id_rsa", "id_ed25519", "id_ecdsa"))
                or (name.startswith(".env.") and name not in {".env.example", ".env.sample"})
                or "__pycache__" in relative.parts):
            issues.append({"file": relative.as_posix(), "rule": "credential-or-cache-file"})
        for issue in inspect_text(path.read_bytes().decode("utf-8", errors="ignore")):
            issues.append({"file": relative.as_posix(), **issue})
    print(json.dumps({"files_checked": count, "findings": issues, "status": "PASS" if not issues else "FAIL"}, ensure_ascii=False, indent=2))
    return bool(issues)


if __name__ == "__main__":
    sys.exit(main())
