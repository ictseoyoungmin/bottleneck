from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageLayoutTests(unittest.TestCase):
    def test_manifest_points_to_a_runtime_only_payload(self):
        manifest = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
        payload = ROOT / manifest["payload"]

        self.assertEqual(manifest["entrypoint"], "skills/bottleneck/SKILL.md")
        self.assertTrue((payload / "SKILL.md").is_file())
        self.assertFalse((payload / "README.md").exists())
        self.assertFalse((payload / "tests").exists())
        self.assertFalse((payload / "evals").exists())

    def test_claude_manifests_are_at_repository_level(self):
        plugin = json.loads(
            (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        marketplace = json.loads(
            (ROOT / ".claude-plugin" / "marketplace.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(plugin["name"], "bottleneck")
        self.assertEqual(marketplace["plugins"][0]["source"], "./")

    def test_icon_is_vector_and_text_free(self):
        icon = (ROOT / "skills" / "bottleneck" / "assets" / "icon.svg").read_text(
            encoding="utf-8"
        )

        self.assertNotIn("<image", icon)
        self.assertNotIn("data:image", icon)
        self.assertNotIn("<text", icon)


if __name__ == "__main__":
    unittest.main()
