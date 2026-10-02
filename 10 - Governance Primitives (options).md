---
title: Governance Primitives — options to combine
created: 2026-10-02
status: v0.1 — answers A5 ("show me options… membership, token holding, presence, sweat, trust graphs, holacratic")
---

# 10 · Governance Primitives (options)

Back to [[00 - README]] · Vision: [[03 - Long-Term Vision]] · Investor stack: [[09 - Investor Value Model (win-win-win)]]

## 🌱 In one breath

Different decisions deserve different voices. Who may live here is decided by residents; how the commons fund is spent mixes funders, stewards and residents; how a community runs its kitchen belongs to that community. We have six **building blocks** (primitives). Each decision type gets a **recipe** that combines them. Money is one ingredient, never the whole meal.

## 1. The six primitives

| Primitive | What it measures | Earned / bought | Transferable | Decays | Strength | Weakness | Source / precedent |
|---|---|---|---|---|---|---|---|
| **M · Membership** (0/1, per network) | Belonging to a holon: Lighthouse, a community, a circle, the wider NetX network | Admitted by that holon's ritual (conduct-based) | ❌ | Lapses if dues/agreements lapse | Clear boundaries (Ostrom 1) | Binary; gatekeeping risk 🧨 Ley 23.592 | Soluna Reglamento art. 36 [^soluna]; TDF citizenship [^tdf] |
| **T · Token holding** (RAIZ) | Financial commitment to the commons | Bought (+ sweat pool) | Later, on rails | No (but voice can be time-locked) | Funds the commons; aligns funders | Plutocracy | TDF 1 token = 1 vote [^tdf]; $NETX ve-lock [^netx] |
| **P · Presence** | Showing up (nights, events, assemblies) | Host-confirmed | ❌ | Yes (recent counts more) | Rewards skin-in-the-place | Penalises remote supporters | OASA Proof of Presence [^oasa]; Closer $Presence [^closer] |
| **S · Sweat** | Work contributed | Peer-assessed agreements | ❌ | Slowly | Lets people without money in | Labour-law risk 🧨; gaming | OASA Proof of Sweat [^oasa]; Collabberry / Semillas [^doc16] |
| **G · Trust graph** | Who vouches for whom, and how far trust propagates | Vouches from trusted members | ❌ | Yes, and revocable | Sybil resistance; curation without central gatekeeper; "if the elephant trusts you…" (Gus [^call]) | Cliques; privacy; needs infrastructure (partner: Unity Hub, in conversation [^call]) | Web-of-trust / EigenTrust family [criterio] |
| **R · Role** | Holding a mandate in a circle | Elected / consented | ❌ | Term-limited | Distributed authority (holacracy/sociocracy) | Coordination overhead | Soluna circles art. 32–34 [^soluna]; Avedam Kezum 12 organs [^doc16] |
| (**D · Dweller**) | Resident status | Adhesion to the PH-especial regulation | ❌ | — | Legal basis for 1 person 1 vote | — | Required by law for residents' matters [^drs] |

## 2. Combining them: a voice formula (template)

For a person *i* in a given holon:

```
Voice_i = M_i × min( cap , w_T·√(RAIZ_i, time-locked) + w_P·Presence_i + w_S·Sweat_i ) × Trust_i
          where M_i ∈ {0,1}, Trust_i ∈ [0.5, 1.5] from the trust graph, cap = max share per person
```

- **√ of tokens** (quadratic-style) dampens whales; **time-lock multiplier** (from $NETX v2's ve-model: 1y ×1 … 5y ×6 [^netx], here softened to ×1…×2) rewards long commitment.
- Compare TDF's suggested formula: *tokens×1 + PoP×5 + Sweat×5* [^oasa]. Ours adds membership gating, a cap and trust.

## 3. Decision types × recipe

| Decision | Who decides | Recipe | Why |
|---|---|---|---|
| Land use, easements, sale/encumbrance of land | Nobody by vote → **Council of Regeneration gate** + legal documents | — (invariant I1) | The diode |
| Residents' life matters (rules of coexistence, sanctions) | Dwellers | **D only, 1 person 1 vote** | Required by the PH-especial regulation [^drs]; can't be bought |
| Commons Fund allocation | Bicameral | Funders' chamber: **M·(T,P,S)·G**, capped + Dwellers' chamber: **D**; above a threshold both must approve | Money + commitment + residents |
| Who joins a community / network | That community | **M** by its own ritual + **G** (vouches) + conduct record | Tribes are sovereign in their entry ritual [^compliance]; trust curates out bad actors (Gus's concern [^call]) |
| Community operations (kitchen, hospitality, production) | Community circles | **R** (holacratic roles) + **S** | Those who do decide |
| Network-level (NetX federation, licences) | Network assembly | Delegates from holons (**R**) | Holonic nesting (Ostrom 8) |
| Emergency / safety | Role holders | **R** with time-limited mandate | Speed |

## 4. Three configurations to choose from

| | **A · Simple bicameral** (Feb 2027) | **B · Holonic weighted** (2027–28) | **C · Trust-graph liquid** (2029+) |
|---|---|---|---|
| Primitives live | M, T (1 pass = 1 voice), P (Genesis), D | + S, R, √T with time-lock, P decay | + G full, delegation along trust paths |
| Tooling | Platform polls + human signatories | Platform + attestations (EAS) | Trust-graph partner (Unity Hub?) + conviction voting |
| Pros | Easy to explain; legally clean | Rewards sweat and presence; whales capped | Self-curating community; scales to 12 tribes |
| Cons | Ignores sweat; coarse | More parameters to calibrate | Complex; privacy and capture risks |
| **Recommendation** | ✅ for the Gathering | ✅ target by end 2027 | Explore with partner; don't promise for Feb |

## 5. Holonic membership ("1 or 0, per network")

A person can be a member of several holons at once: **NetX network ⊃ Lighthouse ⊃ community ⊃ circle**, plus other nodes (Quinta Esencia, TDF…). Membership is **0/1 per holon**, so it's a vector, not a number. Rights cascade **upward by delegation, never downward by command**, which is the diode applied to governance. Reciprocal memberships between nodes (e.g. a TDF citizen gets guest status here) are agreements between holons, not token swaps.

## 6. Open questions

- ❓ Trust-graph partner (Unity Hub) scope for 2027: what data, who owns it, and privacy (Ley 25.326)?
- ❓ Weights w_T, w_P, w_S: calibrate with a simulation of 200 synthetic members (as doc 10 of NS_platform suggested).
- ❓ How does a trust revocation work without becoming a social-exclusion weapon? (Graduated sanctions, appeal to mediation.)

## Sources & logic used

- Logic: Ostrom's design principles and polycentric governance; pace layering; the diode (see [[02 - Design Lens (the council)]]).

[^soluna]: Reglamento de Copropiedad Chacras de Soluna, as synthesised in `../NS_platform/Documentation/01 - Source Synthesis.md` §2.
[^tdf]: $TDF token page: https://www.traditionaldreamfactory.com/token (1 token = 1 vote; 30 tokens for citizenship).
[^oasa]: OASA Whitepaper v1.2 (PoP, Sweat, voting-weight formula): https://oasa.earth/papers/OASA-Whitepaper-V1.2.pdf
[^closer]: Closer docs, as synthesised in `../NS_platform/Documentation/01 - Source Synthesis.md` §4.
[^netx]: *Tokenomics $NETX v2 | NetX State* (2025), ve-lock multipliers; see [[11 - Review of $NETX v2 tokenomics (2025)]].
[^doc16]: `../NS_platform/Documentation/16 - Personas, Acuerdos y Puntos.md`.
[^call]: Private call Gus–Gabriel, 2026-10-02 (private transcript).
[^drs]: DRS/fideicomiso research 2026-09-29 §5 (PH especial; admission by assembly invalid; 1 person 1 vote by regulation).
[^compliance]: `../NS_platform/Documentation/Desarrollo/03 - Compliance by design.md` C8–C10.
