import importlib.util
import json
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_policy.py"
SPEC = importlib.util.spec_from_file_location("validate_policy", SCRIPT)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class PolicyValidationTests(unittest.TestCase):
    def test_example_policy_passes_invariants(self):
        module.main()

    def test_jsonc_comment_and_trailing_comma_handling(self):
        parsed = module.strip_json_comments_and_trailing_commas('{"ok": true, // note\n}')
        self.assertEqual(json.loads(parsed), {"ok": True})


if __name__ == "__main__":
    unittest.main()
