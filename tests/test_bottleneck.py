from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "bottleneck"
    / "scripts"
    / "bottleneck.py"
)
spec = importlib.util.spec_from_file_location("bottleneck_harness", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(mod)


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def call(self, *args, ok=True):
        argv = [*args, "--root", str(self.root)]
        out, err = io.StringIO(), io.StringIO()
        code = 0
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                mod.main(argv)
            except SystemExit as exc:
                code = int(exc.code or 0)
        if ok and code != 0:
            self.fail(f"CLI failed ({code}): {err.getvalue()}\n{out.getvalue()}")
        if not ok and code == 0:
            self.fail(f"CLI unexpectedly succeeded: {out.getvalue()}")
        return code, out.getvalue(), err.getvalue()

    def init(self):
        self.call("init")

    def fill_contract(self):
        p = self.root / ".bottleneck" / "contract.md"
        p.write_text("""# Architecture Contract\n\n- Canonical state ownership: WorldState\n- Module boundaries: explicit services\n- Public schemas/APIs: typed event contract\n- Coordinate/unit conventions: meters, right-handed\n- Time/lifecycle semantics: monotonic update clock\n- Persistence/versioning: schema v1\n- Error semantics: explicit failures\n- Performance envelope: 16.6ms frame target\n""", encoding="utf-8")

    def test_contract_must_be_resolved_before_freeze(self):
        self.init()
        _, _, err = self.call("freeze-contract", ok=False)
        self.assertIn("placeholder", err.lower())
        self.fill_contract()
        self.call("freeze-contract")

    def test_wip_limit_one(self):
        self.init(); self.fill_contract(); self.call("freeze-contract")
        self.call("add", "tree", "--gates", "correctness")
        self.call("add", "water", "--gates", "correctness")
        self.call("activate", "tree")
        _, _, err = self.call("activate", "water", ok=False)
        self.assertIn("wip limit", err.lower())

    def test_close_requires_gate_and_capsule(self):
        self.init(); self.fill_contract(); self.call("freeze-contract")
        self.call("add", "tree", "--gates", "correctness")
        self.call("activate", "tree")
        _, _, err = self.call("close", "tree", ok=False)
        self.assertIn("gates not passed", err.lower())
        self.call("gate", "tree", "correctness", "--pass", "--evidence", "tests/tree.txt")
        _, _, err = self.call("close", "tree", ok=False)
        self.assertIn("capsule", err.lower())
        self.call("capsule", "tree")
        cap = self.root / ".bottleneck" / "capsules" / "tree.md"
        cap.write_text(cap.read_text(encoding="utf-8").replace("TBD", "resolved-value"), encoding="utf-8")
        self.call("close", "tree")
        state = json.loads((self.root / ".bottleneck" / "state.json").read_text())
        self.assertEqual(state["slices"]["tree"]["status"], "CLOSED")
        self.assertIsNone(state["active_slice"])

    def test_reopen_consumes_slot(self):
        self.init(); self.fill_contract(); self.call("freeze-contract")
        self.call("add", "tree", "--gates", "correctness")
        self.call("activate", "tree")
        self.call("gate", "tree", "correctness", "--pass", "--evidence", "evidence.txt")
        self.call("capsule", "tree")
        cap = self.root / ".bottleneck" / "capsules" / "tree.md"
        cap.write_text(cap.read_text(encoding="utf-8").replace("TBD", "resolved"), encoding="utf-8")
        self.call("close", "tree")
        self.call("reopen", "tree", "--reason", "GPU budget regression requires new LOD")
        self.call("add", "water", "--gates", "correctness")
        _, _, err = self.call("activate", "water", ok=False)
        self.assertIn("wip limit", err.lower())

    def test_pass_gate_requires_evidence_by_default(self):
        self.init(); self.fill_contract(); self.call("freeze-contract")
        self.call("add", "chart", "--gates", "correctness")
        self.call("activate", "chart")
        _, _, err = self.call("gate", "chart", "correctness", "--pass", ok=False)
        self.assertIn("evidence", err.lower())

    def test_audit_finds_risky_filename_and_marker(self):
        self.init()
        (self.root / "renderer_final.js").write_text("// TODO remove old path\n", encoding="utf-8")
        _, out, _ = self.call("audit", "--json")
        data = json.loads(out)
        paths = [x["path"] for x in data["suspected_risky_names"]]
        self.assertIn("renderer_final.js", paths)
        self.assertTrue(any(x["marker"] == "TODO" for x in data["placeholder_markers"]))

    def test_score(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = mod.main(["score", "--impact", "5", "--uncertainty", "4", "--reusability", "5"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out.getvalue())["raw"], 100)


if __name__ == "__main__":
    unittest.main()
