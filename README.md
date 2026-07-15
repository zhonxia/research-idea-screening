<div align="center">
  <h1>Research Idea Screening</h1>
  <p><strong>Rapidly evaluate early-stage research ideas — cheaply, systematically, and honestly.</strong></p>

  <p>
    <a href="README.zh.md">中文</a> &nbsp;|&nbsp;
    <strong>English</strong>
  </p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
    <a href="#"><img src="https://img.shields.io/badge/status-stable-brightgreen" alt="Status: Stable"></a>
  </p>
</div>

---

## Why Screen Research Ideas?

Every researcher has experienced this: you come up with an exciting idea, spend weeks reading papers and designing experiments, only to discover someone already published it, or the problem is much harder than it seemed.

**Research Idea Screening** is a lightweight, principled workflow that helps you decide **which early-stage ideas deserve deeper exploration** — before you invest significant time, money, or attention.

It is designed to be:

- **Cheap**: A single screen takes ~30 minutes with a bounded search budget.
- **Honest**: It exposes uncertainty rather than hiding it, and never equates "not found quickly" with "no one has studied this."
- **Actionable**: Every screen ends with a concrete recommendation — proceed, probe first, park, or reject — and the cheapest next step to resolve remaining uncertainty.

---

## What It Does

| Capability | Description |
|---|---|
| **Rapid novelty check** | Bounded search across synonyms, legacy terms, adjacent fields, and counter-hypotheses |
| **Hard-gate filtering** | Four mandatory gates (significance, answerability, resource path, ethics) — fail any gate and the idea is normally rejected |
| **Weighted scoring** | Six dimensions scored 1–5 with confidence intervals and decision-sensitivity analysis |
| **Pre-mortem analysis** | Name the biggest risk, earliest warning signal, stop rule, and salvage path before committing |
| **Batch comparison** | Compare multiple ideas under the same research profile and budget, with confidence-aware portfolio ranking |
| **Plain-language output** | All conclusions rephrased in everyday language — no scoring internals exposed in reports |

---

## The Screening Workflow

```
Input idea
    │
    ▼
Idea Normalization — target, mechanism, comparator, outcome, contribution type
    │
    ▼
Bounded Novelty Search — 6 query families, closest works identified
    │
    ▼
Hard Gates — significance, answerability, resource path, ethics/governance
    │
    ├── Any "No" ──────────► Reject
    ├── Any "Unknown" ────► Probe first (design the cheapest test)
    │
    ▼
Scoring (if all gates pass)
    │
    ├── Significance (25%)
    ├── Differentiation (20%)
    ├── Feasibility (15%)
    ├── Validation clarity (15%)
    ├── Cost efficiency (15%)
    └── Failure residual value (10%)
    │
    ▼
Pre-Mortem — failure risks, warnings, stop rules
    │
    ▼
Decision — Proceed / Probe first / Park / Reject
    │
    ▼
Report — plain-language summary + YAML handoff to research-ideation
```

### Screening Modes

- **single** — Evaluate one idea in depth.
- **batch** — Compare multiple ideas under the same research profile and budget.
- **refresh** — Re-evaluate when new evidence or results become available.

---

## Scoring Dimensions

All dimensions scored 1–5 (0.5 increments) with explicit confidence:

| Dimension | Weight | What It Measures |
|---|---|---|
| **Significance** | 25% | Does the answer change anything for a credible stakeholder, theory, or decision? |
| **Differentiation** | 20% | How clearly does this differ from the strongest existing work? |
| **Feasibility** | 15% | Is there a credible technical or resource route to completion? |
| **Validation clarity** | 15% | Can success or failure be judged unambiguously? |
| **Cost efficiency** | 15% | Is the expected insight or impact worth the investment? |
| **Failure residual** | 10% | If this fails, does something reusable remain (data, negative result, tool, benchmark)? |

### Hard Gates (applied before scoring)

| Gate | Fail Condition |
|---|---|
| Significance | No identifiable beneficiary or consequence |
| Answerability | No observable result can adjudicate the claim |
| Resource path | A critical prerequisite has no credible substitute |
| Ethics/Governance | Unacceptable risk or implausible approval |

---

## Decisions (in plain language)

| Screen Result | Meaning |
|---|---|
| **Proceed** | Worth pursuing — go ahead with deeper evaluation |
| **Probe first** | Not certain enough yet; run a small quick test first |
| **Park** | Not worth doing right now; revisit if conditions change |
| **Reject** | Has fundamental problems — recommend letting this one go |

---

## Quick Start

### Prerequisites

- Python 3.10+
- Git

### Get the workflow

```bash
git clone https://github.com/zhonxia/research-idea-screening.git
cd research-idea-screening
```

### Use the scoring script

```bash
# See the expected input format
python scripts/score_screening.py --example

# Score one idea from a JSON file
python scripts/score_screening.py my_screen.json

# Score a batch
python scripts/score_screening.py batch_screens.json
```

### Input format

```json
{
  "title": "My Research Idea",
  "gates": {
    "significance": "yes",
    "answerability": "yes",
    "resource_path": "yes",
    "ethics_governance": "yes"
  },
  "dimensions": {
    "significance": {"score": 4.0, "confidence": "high"},
    "differentiation": {"score": 3.5, "confidence": "medium"},
    "feasibility": {"score": 3.0, "confidence": "medium"},
    "validation_clarity": {"score": 3.5, "confidence": "high"},
    "cost_efficiency": {"score": 3.0, "confidence": "low"},
    "failure_residual": {"score": 2.5, "confidence": "medium"}
  },
  "fatal_risk": false
}
```

The script returns a deterministic recommendation, weighted score, score range (with confidence-based uncertainty), and a `decision_sensitive` flag.

---

## Project Structure

```
research-idea-screening/
├── SKILL.md                         # Full screening workflow specification
├── README.md                        # This file
├── README.zh.md                     # Chinese documentation
├── LICENSE                          # MIT License
├── agents/
│   └── openai.yaml                  # AI agent interface definition
├── assets/
│   └── rapid-screen-report.md       # Report template (YAML frontmatter + markdown)
├── references/
│   ├── screening-protocol.md        # Detailed protocol (gates, scoring, risk)
│   └── research-profiles.md         # Research-type profiles for fair evaluation
├── scripts/
│   └── score_screening.py           # Deterministic scoring script
└── tests/
    └── test_score_screening.py      # Unit tests for the scoring script
```

---

## Related Projects

This project is part of a research ideation ecosystem:

- **[research-ideation](https://github.com/zhonxia/research-ideation)** — Full lifecycle management for research ideas: generation, formal evaluation, novelty validation, and portfolio tracking. This is the **upstream** workflow — ideas that pass screening can be handed off here for deep evaluation.
- **[personal-literature-survey](https://github.com/zhonxia/personal-literature-survey)** — Systematic literature survey workflow combining academic databases with personal knowledge bases. Runs in **parallel** with idea screening to gather evidence for novelty and feasibility checks.

### How they fit together

```
research-ideation (generate ideas)
       │
       ▼
research-idea-screening (rapid screen — you are here)
       │
       ├── Proceed ──► research-ideation (formal evaluation)
       ├── Probe first ──► cheap experiment, then re-screen
       ├── Park ──► back to idea pool
       └── Reject ──► record reason, move on
       
       │
       ▼
personal-literature-survey (evidence gathering — runs in parallel with screening)
```

---

## Non-Negotiable Rules

1. Never turn "not found quickly" into "no one has studied this."
2. Separate problem importance from publication attractiveness.
3. Apply gates before weighted scoring.
4. Feasibility must include time, money, access, expertise, permissions, and opportunity cost.
5. Compare against the strongest relevant baseline, not only a convenient weak baseline.
6. Preserve negative and contrary evidence.
7. Report confidence and decision sensitivity, not only a point score.
8. Prefer the cheapest probe that can change the decision.

---

## License

MIT © 2026 Wang Xu. See [LICENSE](LICENSE) for details.
