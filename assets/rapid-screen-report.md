---
screening_id: SCREEN-YYYYMMDD-NN
title: Short title
mode: single | batch | refresh
research_profile: theoretical | computational-experimental | qualitative | clinical-field | design-constructive
screened_on: YYYY-MM-DD
search_budget: "30 minutes; <=12 queries"
---

# Rapid Research Idea Screen

## Decision

**Recommendation**: Proceed / Probe first / Park / Reject  
**Score range**: XX.X-XX.X / 100  
**Overall confidence**: Low / Medium / High  
**Decision sensitivity**: Stable / Sensitive  
**One-sentence reason**: [reason]

## Idea

- **Research question**: [precise, answerable question]
- **Target/system and condition**: [scope]
- **Mechanism/intervention**: [scope]
- **Strongest baseline**: [baseline or alternative explanation]
- **Outcome**: [observable result]
- **Proposed contribution**: [new knowledge, method, evidence, data, measure, or artifact]
- **Explicit exclusions**: [not claimed]

## Rapid Collision Check

- **Narrow differentiation claim**: [claim searched]
- **Channels and date range**: [scope]
- **Query families**: [exact, synonyms, legacy, adjacent, counter-hypothesis]
- **Stopping condition**: budget exhausted / early collision / sufficient for screen
- **Evidence grade**: C / D

| Closest work | Identifier | Overlap | Remaining difference | Threat |
|---|---|---|---|:---:|
| [work] | [DOI/URL] | [overlap] | [difference] | H/M/L |

**Bounded conclusion**: [Use preliminary, scope-limited wording.]  
**Contrary evidence and missing coverage**: [limitations]

## Hard Gates

| Gate | Result | Evidence | Probe if unknown |
|---|:---:|---|---|
| Significance | Yes/Unknown/No | [who cares and what changes] | [probe] |
| Answerability | Yes/Unknown/No | [falsifier or bounding result] | [probe] |
| Resource path | Yes/Unknown/No | [data, tools, access, time, money, expertise] | [probe] |
| Ethics/governance | Yes/Unknown/No | [risk and permissions] | [probe] |

## Value And Effort

| Dimension | Weight | Score | Confidence | Evidence-based reason | Decision-changing evidence |
|---|:---:|:---:|:---:|---|---|
| Significance | 25 | X.X | L/M/H | [reason] | [evidence] |
| Differentiation | 20 | X.X | L/M/H | [reason] | [evidence] |
| Feasibility | 15 | X.X | L/M/H | [reason] | [evidence] |
| Validation clarity | 15 | X.X | L/M/H | [reason] | [evidence] |
| Cost efficiency | 15 | X.X | L/M/H | [reason] | [evidence] |
| Failure residual | 10 | X.X | L/M/H | [reason] | [evidence] |

- **Minimum-probe time/cost**: [range]
- **First credible-result time/cost**: [range]
- **Publishable/reusable-result time/cost**: [range]
- **Primary opportunity cost**: [what is displaced]

## Pre-Mortem

- **Largest failure risk**: [risk]
- **Earliest warning signal**: [signal]
- **Stop rule**: [observable threshold]
- **Mitigation**: [action]
- **Failure residual**: [negative result, boundary, data, benchmark, tool, or reusable method]
- **Residual beneficiary**: [who or what decision can use it]

## Cheapest Decision-Changing Probe

- **Uncertainty tested**: [uncertainty]
- **Procedure**: [small proof, pilot, data audit, interview, reproduction, prototype]
- **Pass criterion**: [threshold]
- **Stop criterion**: [threshold]
- **Budget**: [time/resources]

## Handoff To Research Ideation

```yaml
screening_decision: proceed | probe-first | park | reject
screening_date: YYYY-MM-DD
research_profile: profile
score_range: [low, high]
confidence: low | medium | high
novelty_evidence_level: rapid-bounded-C | rapid-bounded-D
key_evidence: []
fatal_risks: []
minimum_probe: ""
estimated_effort: ""
failure_residual_value: ""
```
