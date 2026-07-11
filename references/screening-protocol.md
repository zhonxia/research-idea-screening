# Rapid Screening Protocol

## Contents

1. Idea normalization
2. Bounded novelty search
3. Hard gates
4. Scored dimensions
5. Risk and residual value
6. Decisions and confidence

## 1. Idea Normalization

Capture:

- Target population, system, or domain
- Condition or operating regime
- Proposed mechanism, intervention, method, or explanatory claim
- Strongest native baseline or alternative explanation
- Observable outcome
- Contribution type: theory, method, empirical finding, dataset/measure, artifact, or synthesis
- Explicit exclusions

If these cannot be stated, recommend `Probe first` with a question-formulation task.

## 2. Bounded Novelty Search

Rapid search establishes collision risk, not universal absence.

Build query families from the phenomenon, mechanism, method, outcome, domain, synonyms, and legacy terminology. Search:

1. Exact conjunction
2. Synonym and legacy-term variants
3. Broader mechanism in the target domain
4. Same mechanism in adjacent domains
5. Counter-hypothesis or known limitation
6. Recent reviews or authoritative syntheses

For every closest work, record a stable identifier, overlap, remaining difference, and threat level. Grade the rapid evidence:

- `C`: multiple useful channels and verified close works, but no saturation or citation-chain completion
- `D`: local library or a few preliminary queries

Permitted wording:

> Within the declared rapid-search scope through YYYY-MM-DD, no exact match was found for [narrow claim]. This is preliminary collision evidence, not a validated research-gap claim.

## 3. Hard Gates

| Gate | Yes | Unknown | No |
|---|---|---|---|
| Significance | A credible stakeholder, theory, capability, or decision changes with the answer | Importance rests on an untested stakeholder or consequence assumption | No identifiable beneficiary or consequence |
| Answerability | A result can reject, bound, or materially revise the claim | Outcome or falsifier needs a small design probe | No observable or logical result can adjudicate the claim |
| Resource path | A plausible route exists to data/premises, tools, expertise, access, time, money, and permissions | One or more critical prerequisites require a bounded audit | A critical prerequisite is unavailable with no credible substitute |
| Ethics/governance | Risk is acceptable or has a credible approval and mitigation route | Review or permission status is unresolved | Risk is unacceptable or required approval is implausible |

Any `No` normally implies `Reject`. Any `Unknown` normally implies `Probe first` before a weighted decision.

## 4. Scored Dimensions

Score 1-5 in 0.5 increments only after gates pass.

| Dimension | Weight | 1 | 3 | 5 |
|---|:---:|---|---|---|
| Significance | 25 | Marginal consequence | Useful to a defined audience | Materially changes important knowledge, capability, or decisions |
| Differentiation | 20 | Exact or trivial duplication | Defensible extension | Important bounded difference supported by strong rapid evidence |
| Feasibility | 15 | No credible technical/resource route | Major but probeable uncertainty | Clear route with accessible prerequisites |
| Validation clarity | 15 | Success cannot be judged | Plausible tests with unresolved threats | Decisive tests, strong baselines, and explicit uncertainty analysis |
| Cost efficiency | 15 | High cost and opportunity loss for likely value | Acceptable cost-value tradeoff | High information or impact per unit of time and money |
| Failure residual | 10 | Failure leaves no reliable output | Some reusable learning or artifact | Valuable negative result, boundary, data, benchmark, tool, or method remains |

For each dimension record `Low`, `Medium`, or `High` confidence and the evidence that would most change it.

## 5. Risk And Residual Value

Run a pre-mortem: assume the project failed after its expected duration. Identify:

- Most likely decisive failure
- Highest-consequence failure
- Earliest observable warning signal
- Stop rule
- Mitigation or cheaper design
- Salvage path

Do not award residual value merely because files or code will exist. Require an identifiable user, claim, or later decision that can use the residual.

Estimate effort as ranges, not a single date:

- Time to minimum probe
- Time to first credible result
- Time to publishable or reusable result
- Direct financial/compute cost
- Required specialist effort
- Primary opportunity cost

## 6. Decisions And Confidence

Default score guidance after all gates are `Yes`:

- `70-100`: `Proceed`
- `50-69.9`: `Probe first`
- below `50`: `Park`

Use `Reject` for failed gates, exact duplication without meaningful delta, or an unmitigated fatal risk. Use `Probe first` whenever uncertainty can reverse the decision, even if the point score exceeds 70.

Confidence intervals are decision aids. The bundled script applies default score uncertainty of +/-0.25 for High, +/-0.75 for Medium, and +/-1.5 for Low confidence before weighting. If an interval crosses a decision threshold, label the recommendation sensitive.
