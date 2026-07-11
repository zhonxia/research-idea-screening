---
name: research-idea-screening
description: "Rapidly screen one or many early-stage research ideas using bounded novelty search, significance and answerability gates, feasibility and cost estimates, validation planning, pre-mortem risk analysis, failure residual value, confidence-aware scoring, and portfolio ranking. Use when deciding whether a research idea is worth deeper evaluation, comparing many candidate topics, triaging an idea backlog, or defining the cheapest next probe before committing substantial time or money."
---

# Research Idea Screening

Decide whether an early research idea deserves deeper evaluation. Keep the screen cheap, expose uncertainty, and recommend the next information-gaining action. Do not present a rapid screen as a novelty proof or full research evaluation.

## Choose A Mode

- Use `single` for one idea.
- Use `batch` to compare multiple ideas under the same research profile and screening budget.
- Use `refresh` when new evidence may change an earlier screen.

Read [references/screening-protocol.md](references/screening-protocol.md) before screening. Select the closest research profile using [references/research-profiles.md](references/research-profiles.md).

## Define The Budget

State the search and reasoning budget before starting. If the user does not provide one, default to:

- 30 minutes of conceptual and literature screening
- at most 12 search queries per idea
- one recent review or authoritative synthesis when available
- 3-5 closest works
- no citation-chain saturation requirement

For a large batch, use a shallow first pass, eliminate clear failures, and spend the remaining budget only on plausible candidates.

## Run The Screen

1. Rewrite the idea as: target or system, condition, mechanism or intervention, comparator, and intended outcome.
2. State the proposed contribution and the narrow differentiation claim before searching.
3. Search exact, synonymous, legacy, adjacent, and counter-hypothesis terms within the declared budget.
4. Verify identifiers and inspect abstracts or primary sources for the closest works. Record exact overlap, partial overlap, adjacent work, contrary evidence, and unresolved scope.
5. Apply the four hard gates: significance, answerability, resource path, and ethics/governance.
6. Stop scoring when a critical gate is `No`. Convert every `Unknown` into a bounded probe.
7. Score only passed candidates on significance, differentiation, feasibility, validation clarity, cost efficiency, and failure residual value. Record confidence and a one-sentence evidence-based reason for every score.
8. Run a pre-mortem: name the largest failure risk, earliest warning signal, stop rule, and salvageable output.
9. Recommend `Proceed`, `Probe first`, `Park`, or `Reject`.
10. Write the report from [assets/rapid-screen-report.md](assets/rapid-screen-report.md). For batch mode, preserve per-idea reports and add a comparison table.

**Plain language rule for all output**: Never expose internal scoring mechanics ("band", "range", "interval", "sensitivity", "threshold crossing") to the user. Every conclusion must be rephrased in everyday language. For example, instead of "score crosses into probe-first band", say "not certain enough yet — suggest a quick test first to confirm". The report template already uses plain labels; preserve that spirit everywhere.

Use `scripts/score_screening.py` for deterministic scoring and sensitivity ranges. The script supports one JSON object or a list of objects. Run `python scripts/score_screening.py --example` to inspect its input contract.

## Interpret Decisions (plain language)

When writing the final recommendation, use everyday language. Do NOT mention internal scoring concepts like "bands", "thresholds", "intervals", or "sensitivity".

| Internal concept | Say this to the user |
|---|---|
| `Proceed` | Worth pursuing — go ahead with deeper evaluation |
| `Probe first` | Not certain enough yet; run a small quick test first before deciding |
| `Park` | Not worth doing right now; revisit later if conditions change |
| `Reject` | Has fundamental problems — recommend letting this one go |

Treat thresholds as defaults, not scientific facts. Override a script recommendation only with an explicit reason.

## Rank A Batch

Compare only ideas screened under compatible profiles and budgets. Rank by decision class first, then score range and opportunity cost. Mark a ranking `unstable` when plausible uncertainty intervals overlap or when one unresolved gate could reverse it. Do not force a total ordering; ties and incomparable ideas are valid outcomes.

## Hand Off Worthwhile Ideas

This skill does not assign idea IDs, mutate a research registry, or perform full novelty validation. When the user wants lifecycle management or formal evaluation, hand the result to `research-ideation` using the YAML block in the report template. Label the novelty evidence `rapid/bounded`; `research-ideation` must independently upgrade it before making a strong novelty claim.

## Non-Negotiable Rules

1. Never turn "not found quickly" into "no one has studied this."
2. Separate problem importance from publication attractiveness.
3. Apply gates before weighted scoring.
4. Include time, money, access, expertise, permissions, and opportunity cost in feasibility.
5. Define how the proposed contribution could be disproved, bounded, or materially revised.
6. Compare against the strongest relevant baseline, not only a weak convenient baseline.
7. Preserve negative and contrary evidence.
8. Report confidence and decision sensitivity, not only a point score.
9. Treat reusable data, code, tools, negative findings, boundary results, and literature maps as possible failure residuals only when a credible path exists.
10. Prefer the cheapest probe that can change the decision.
