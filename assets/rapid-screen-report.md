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
**Overall confidence**: Low / Medium / High  
**One-sentence reason**: [reason]

## Idea

- **Research question**: [precise, answerable question]
- **Target/system and condition**: [scope]
- **Mechanism/intervention**: [scope]
- **Strongest baseline**: [baseline or alternative explanation]
- **Outcome**: [observable result]
- **Proposed contribution**: [new knowledge, method, evidence, data, measure, or artifact]
- **Explicit exclusions**: [not claimed]

## Existing Work Checked

- **Search scope**: [keywords, databases, date range]
- **Closest existing works**: [list 3-5 closest works with brief overlap/difference notes]

| Work | Overlap | Key difference |
|---|---|---|
| [work] | [overlap] | [difference] |

**Conclusion**: [Preliminary, scope-limited wording — e.g. "No exact match found within searched sources."]  
**Limitations**: [what wasn't searched, what remains uncertain]

## Quick Checks

| Check | Pass? | Notes |
|---|:---:|---|
| Important problem | Yes/Unknown/No | [who cares and what changes] |
| Can be answered | Yes/Unknown/No | [can results prove or disprove the idea] |
| Resources available | Yes/Unknown/No | [data, tools, access, time, money, expertise] |
| Ethical / permissible | Yes/Unknown/No | [risk and permissions] |
| Different enough | Yes/Unknown/No | [how this differs from existing work] |

If any check is "No", the idea is likely not worth pursuing. If "Unknown", a quick test is needed.

## Scoring (if all checks above pass)

| Factor | Weight | Score (1-5) | Why this score |
|---|---|---|---|
| Importance | 25 | X.X | [reason] |
| Differentiation | 20 | X.X | [reason] |
| Feasibility | 15 | X.X | [reason] |
| Test clarity | 15 | X.X | [reason] |
| Cost-value | 15 | X.X | [reason] |
| Fallback value if fails | 10 | X.X | [reason] |

- **Estimated time to first meaningful result**: [range]
- **Estimated total effort**: [range]
- **What else this would displace**: [opportunity cost]

## What Could Go Wrong

- **Biggest risk**: [what's most likely to kill this]
- **Early warning sign**: [what to watch for first]
- **Stopping rule**: [when to cut losses]
- **How to reduce risk**: [mitigation]

## Next Step

- **What we're unsure about**: [uncertainty]
- **Quickest way to check**: [small proof, pilot, data audit, interview, reproduction, prototype]
- **What counts as "it worked"**: [threshold]
- **What counts as "stop trying"**: [threshold]
- **Time/cost for this check**: [budget]

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
