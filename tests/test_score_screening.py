import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "score_screening.py"
SPEC = importlib.util.spec_from_file_location("score_screening", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def screen(score=4.0, confidence="high"):
    return {
        "title": "Candidate",
        "gates": {name: "yes" for name in MODULE.GATES},
        "dimensions": {
            name: {"score": score, "confidence": confidence} for name in MODULE.WEIGHTS
        },
        "fatal_risk": False,
    }


class ScoreScreeningTest(unittest.TestCase):
    def test_high_confidence_candidate_proceeds(self):
        result = MODULE.score_one(screen())
        self.assertEqual("proceed", result["recommendation"])
        self.assertEqual(80.0, result["score"])
        self.assertFalse(result["decision_sensitive"])

    def test_unknown_gate_forces_probe(self):
        candidate = screen()
        candidate["gates"]["resource_path"] = "unknown"
        result = MODULE.score_one(candidate)
        self.assertEqual("probe-first", result["recommendation"])
        self.assertEqual(["resource_path"], result["unknown_gates"])

    def test_failed_gate_rejects(self):
        candidate = screen()
        candidate["gates"]["answerability"] = "no"
        self.assertEqual("reject", MODULE.score_one(candidate)["recommendation"])

    def test_uncertain_high_score_is_downgraded_to_probe(self):
        result = MODULE.score_one(screen(score=4.0, confidence="low"))
        self.assertTrue(result["decision_sensitive"])
        self.assertEqual("probe-first", result["recommendation"])

    def test_rejects_invalid_score_increment(self):
        candidate = screen()
        candidate["dimensions"]["feasibility"]["score"] = 3.2
        with self.assertRaises(ValueError):
            MODULE.score_one(candidate)


if __name__ == "__main__":
    unittest.main()
