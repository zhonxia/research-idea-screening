#!/usr/bin/env python3
"""Score rapid research-idea screens and expose decision sensitivity."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


WEIGHTS = {
    "significance": 25,
    "differentiation": 20,
    "feasibility": 15,
    "validation_clarity": 15,
    "cost_efficiency": 15,
    "failure_residual": 10,
}
GATES = ("significance", "answerability", "resource_path", "ethics_governance")
UNCERTAINTY = {"high": 0.25, "medium": 0.75, "low": 1.5}
EXAMPLE = {
    "title": "Example idea",
    "gates": {name: "yes" for name in GATES},
    "dimensions": {
        name: {"score": 3.0, "confidence": "medium"} for name in WEIGHTS
    },
    "fatal_risk": False,
}


def fail(message: str) -> None:
    raise ValueError(message)


def normalize_gate(value: object, name: str) -> str:
    normalized = str(value).strip().lower()
    if normalized not in {"yes", "unknown", "no"}:
        fail(f"gate {name!r} must be yes, unknown, or no")
    return normalized


def decision_for(score: float) -> str:
    if score >= 70:
        return "proceed"
    if score >= 50:
        return "probe-first"
    return "park"


def score_one(item: object) -> dict[str, object]:
    if not isinstance(item, dict):
        fail("each screen must be a JSON object")
    title = str(item.get("title", "Untitled idea"))
    gates = item.get("gates")
    dimensions = item.get("dimensions")
    if not isinstance(gates, dict) or not isinstance(dimensions, dict):
        fail(f"{title}: gates and dimensions must be objects")

    normalized_gates = {
        name: normalize_gate(gates.get(name), name) for name in GATES
    }
    missing = set(WEIGHTS) - set(dimensions)
    extra = set(dimensions) - set(WEIGHTS)
    if missing or extra:
        fail(f"{title}: dimension keys mismatch; missing={sorted(missing)}, extra={sorted(extra)}")

    point = low = high = 0.0
    normalized_dimensions: dict[str, dict[str, object]] = {}
    for name, weight in WEIGHTS.items():
        entry = dimensions[name]
        if not isinstance(entry, dict):
            fail(f"{title}: dimension {name!r} must be an object")
        try:
            score = float(entry.get("score"))
        except (TypeError, ValueError):
            fail(f"{title}: dimension {name!r} score must be numeric")
        confidence = str(entry.get("confidence", "")).strip().lower()
        if not 1 <= score <= 5 or score * 2 != round(score * 2):
            fail(f"{title}: dimension {name!r} score must be 1-5 in 0.5 increments")
        if confidence not in UNCERTAINTY:
            fail(f"{title}: dimension {name!r} confidence must be low, medium, or high")
        delta = UNCERTAINTY[confidence]
        point += score / 5 * weight
        low += max(1, score - delta) / 5 * weight
        high += min(5, score + delta) / 5 * weight
        normalized_dimensions[name] = {"score": score, "confidence": confidence}

    failed = [name for name, value in normalized_gates.items() if value == "no"]
    unknown = [name for name, value in normalized_gates.items() if value == "unknown"]
    fatal_risk = bool(item.get("fatal_risk", False))
    if failed or fatal_risk:
        recommendation = "reject"
    elif unknown:
        recommendation = "probe-first"
    else:
        recommendation = decision_for(point)

    plausible_decisions = {decision_for(low), decision_for(high)}
    sensitive = bool(unknown) or len(plausible_decisions) > 1
    if recommendation == "proceed" and sensitive:
        recommendation = "probe-first"

    return {
        "title": title,
        "recommendation": recommendation,
        "score": round(point, 1),
        "score_range": [round(low, 1), round(high, 1)],
        "decision_sensitive": sensitive,
        "failed_gates": failed,
        "unknown_gates": unknown,
        "fatal_risk": fatal_risk,
        "gates": normalized_gates,
        "dimensions": normalized_dimensions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON file containing one screen or a list")
    parser.add_argument("--example", action="store_true", help="print an example input")
    args = parser.parse_args()
    if args.example:
        print(json.dumps(EXAMPLE, indent=2, ensure_ascii=False))
        return 0
    if not args.input:
        parser.error("input is required unless --example is used")
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        items = payload if isinstance(payload, list) else [payload]
        results = [score_one(item) for item in items]
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    output: object = results if isinstance(payload, list) else results[0]
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
