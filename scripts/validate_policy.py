#!/usr/bin/env python3
"""Validate security invariants in the project's Tailscale policy example."""
import json
import re
from pathlib import Path

POLICY_PATH = Path(__file__).resolve().parents[1] / "tailscale-policy.hujson"


def strip_json_comments_and_trailing_commas(text: str) -> str:
    # The example intentionally uses Tailscale's JSON-with-comments convention.
    text = re.sub(r"//[^\n]*", "", text)
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text


def main() -> None:
    policy = json.loads(strip_json_comments_and_trailing_commas(POLICY_PATH.read_text()))
    assert "tag:gitlab-ci" in policy["tagOwners"]
    assert "tag:private-host" in policy["tagOwners"]
    assert all("*" not in str(rule.get("dst", "")) for rule in policy["acls"])
    assert any(rule["src"] == ["tag:gitlab-ci"] and rule["users"] == ["deploy"] for rule in policy["ssh"])
    assert not any("root" in rule["users"] for rule in policy["ssh"])
    ci_acl = next(rule for rule in policy["acls"] if rule["src"] == ["tag:gitlab-ci"])
    assert ci_acl["dst"] == ["tag:private-host:22"], "CI must be limited to SSH port 22"
    assert any(rule["action"] == "check" and rule["src"] == ["group:platform-ops"] for rule in policy["ssh"])
    print("Tailnet policy syntax and least-privilege invariants: PASS")


if __name__ == "__main__":
    main()
