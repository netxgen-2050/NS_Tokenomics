---
title: Design Lens — the council of cryptoeconomic thinkers
created: 2026-10-02
status: v0.1 — method, not dogma
---

# 02 · Design Lens (the council)

Back to [[00 - README]]

## 🌱 In one breath

Most token projects start with "what token do we launch?". The people we learn from start somewhere else: **what system are we steering, what must never break, and what behaviour do we want?** The token is only the last, smallest piece: a way of writing rights down. We borrow five voices and one reading list, and we keep an honest record of where they would disagree with us.

> A note on attribution: below we paraphrase public positions and well-known contributions. These are *lenses we apply*, not quotes or endorsements. Where we're less sure of a thinker's specific view we say so.

## 1. The council

### Michael Zargham (BlockScience) — *economic systems engineering*
**What we take:**
- Treat the ecosystem as a **sociotechnical control system**: state, actions, policies, and **invariants** (things that must stay true whatever happens). Governance is the *control layer* that keeps the system inside its safe region; it doesn't "optimise" it.
- **Requirements before mechanisms**, then **simulation** (cadCAD lineage) before launch, then **monitoring** after.
- From his Commons Stack work: the **Hatch → Augmented Bonding Curve** pattern (a gated initial raise, then a curve with a reserve and a funding pool, with entry/exit "tributes" that fund the commons) and **conviction voting** (preference accumulates over time, which resists flash-capture).
- Institutions as **layered, polycentric** systems: the code doesn't replace law; it should mirror it.

**How it shows up here:** invariants I1–I8 in [[03 - Long-Term Vision]]; the Feb raise is literally called **The Hatch** ([[04 - MVP February 2027 (The Hatch)]]); `sim/hatch_sim.py`.

### Trent McConaghy (Ocean Protocol) — *token engineering & AI*
**What we take:**
- Token design as an **engineering loop**: formulate goals → design → **verify by simulation** (his TokenSPICE work) → deploy → monitor. Tokens are "incentive machines" pointed at an objective function.
- **Nature 2.0 / AI DAOs**: his old thought experiment of land or a forest that "owns itself" via an autonomous agent, accumulating resources for its own regeneration. For us: a **"Voice of the Land" agent** that represents Ledger C (ecological KPIs) inside governance.
- His more recent warnings that autonomous AI agents with resources can become **uncontrollable**, and his "humans must keep up" stance. For us: the land-agent gets **a delay/flag power, never a decision or treasury power**. Humans and the Council of Regeneration decide.
- **Data as an asset with sovereignty**: ecological and community data (MRV, presence) is valuable; communities should hold it, not the platform.

**How it shows up here:** AI layer in the Vision §6; hazard H7 (agent capture).

### Dr. Shermin Voshmgir (Token Kitchen / *Token Economy*) — *tokens as programmable rights*
**What we take:**
- A token is **a bundle of rights plus a purpose**: access, usage, voice, ownership, transfer. Write the bundle down explicitly, token by token.
- **Purpose-driven tokens**: tokens can reward contribution to a public good (regeneration) rather than speculation, but the purpose must be *measurable* and the incentive must not be gameable.
- The token **is** an institution: once issued, it shapes behaviour and expectations; design the social contract, not just the ledger.

**How it shows up here:** the **Rights × Purpose matrix** (§3 below), used for every token in the folder.

### Krzysztof Paruch (WU Vienna, Research Institute for Cryptoeconomics) — *token engineering as a discipline*
**What we take** (we're less certain about his specific positions; we apply the token-engineering education lineage he's associated with):
- Systematic **stakeholder → incentive → mechanism** mapping before any parameter.
- Tokens as **policy instruments** in an institutional and legal context, not as code alone. Regulation is a design input, not an afterthought.
- Explicit **validation** of assumptions with real participants (pilots, workshops), not only simulations.

**How it shows up here:** stakeholder map (§4), legal-as-design-input in [[06 - Legal Friction Map]], and the Feb Gathering as a **live validation** rather than a launch party.

### Will Ruddick (Grassroots Economics) — *commitment pooling* (added; Gus's own lineage since 2019)
Not in the brief, but impossible to ignore: communities issue **vouchers that are redeemable commitments** for their own goods and services; **pools** hold baskets of vouchers with swap limits and fees; value is backed by **productive capacity**, not by speculation. This is the cleanest answer to "access to the commodities our communities produce" and to "keep yield inside the ecosystem".

## 2. *This Is Not a Test* as our design curriculum

Zargham's seminar repo ([github.com/mzargham/thisisnotatest](https://github.com/mzargham/thisisnotatest)) is a reading map in three modules: **Models and their limits**, **Collective action and institutions**, **Design, analysis and governance**. It isn't a toolkit; it's a *posture*: design for adaptation, not prediction. We turn each reading into a **design check** used throughout this folder:

| Reading (module) | Design check for Lighthouse tokenomics |
|---|---|
| Meadows, *Thinking in Systems* / *Leverage Points* (1) | Model stocks and flows (land, commons fund, credits, trust). Intervene at **goals** (needs coverage, regeneration), not just parameters (price) |
| Brand, *Pace Layering* (1) | **Slow layers remember, fast layers learn.** Land & easements (centuries) → charter (decades) → fideicomiso (30 y) → mother token (years) → community vouchers (months) → daily exchange. Never let a fast layer rewrite a slow one: that's the diode in time |
| Alexander, *A Pattern Language* (1) | Community token **templates as patterns**: composable, local, named ([[05 - Community Token Templates]]) |
| Ashby, *Requisite Variety* (1) | The governance system must be as diverse as what it governs → 10–12 communities with **different** token models, one shared protocol |
| Holling, *Panarchy* (1) | Plan for the release/reorganisation phase: what happens when a community fails? (exit, re-pooling) |
| Schumacher, *Small is Beautiful* (1) | 70–110 people per community; token circles at human scale |
| Lessig, *Code 2.0* (2) | Code is a regulator, but here **law is the source of truth**; the ledger is a mirror ("si hay diferencia, manda el fiduciario") |
| North, *Institutions* (2) | Formal rules (statutes, fideicomiso, easements) vs informal norms (convivencia); tokens must fit both |
| Axelrod, *Evolution of Cooperation* (2) | Repeated games + reputation → **non-transferable** presence/sweat; identity continuity matters more than liquidity |
| Ostrom, *Governing the Commons* (2) | The 8 design principles = acceptance checklist for every community token (§5) |
| Scott, *Seeing Like a State* (2) | ⚠️ **Tension**: HIQI and KPIs make communities legible to investors, and legibility can destroy local knowledge. Measure what communities choose to measure; keep some things unmeasured |
| Jacobs, *Death and Life of Great American Cities* (2) | Mixed uses and short loops: communities trading with each other daily beats one big treasury |
| Berkes, *Sacred Ecology*; LaDuke, *All Our Relations* (2, 3) | Relational, place-based governance; ❓ Mapuche/indigenous presence and history in the Río Negro valley must be part of the design, not an afterthought |
| Simon, *Sciences of the Artificial* (3) | Satisficing over optimising: we set **constraints** (invariants), not targets to maximise |
| Carse, *Finite and Infinite Games* (3) | OASA's framing: the commons is an **infinite game**; tokens that reward "winning and exiting" are finite-game tokens |
| Leveson, *Engineering a Safer World* (3) | **STPA-lite hazard analysis** ([[03 - Long-Term Vision]] §7) |
| Beer, *Designing Freedom* (VSM) (3) | Map federation to System 1 (communities) … System 5 (identity: Land Trust principles) |
| Graeber, *Utopia of Rules* (3) | Don't let compliance bureaucracy eat the community: keep rules few and legible |
| Latour, *We Have Never Been Modern* (3) | The land, water and the agent are actors too → the "Voice of the Land" seat |

## 3. Rights × Purpose matrix (Voshmgir lens) — template

Every token in this folder gets this table. Example for the Feb **Founding Pass**:

| Right | Yes/No | Detail |
|---|---|---|
| Access | ✅ | Gathering, commons spaces, community markets, stay credits |
| Usage (redeem) | ✅ | Commons Credits for community goods/services |
| Voice | ✅ | One person one voice in Commons Allocation Rounds (funders' chamber) |
| Ownership of land | ❌ | Never (diode) |
| Financial return | ❌ | None, no buy-back, no dividend |
| Transfer | ❌ | Non-transferable in v0 (🧨 activo virtual) |
| **Purpose** | | Fund the commons and the first communities; create a constituency of stewards |
| **Behaviour rewarded** | | Early commitment, showing up, allocating well |

## 4. Stakeholder map (who wants what)

| Stakeholder | Wants | Gives | Risk they bring |
|---|---|---|---|
| Early supporters / "regen tourists" (often foreign) | Belonging, access, a say, good story | Money (small–mid tickets) | Expect appreciation if we're sloppy with words |
| Future residents | Home, community, affordability | Money + time | Cohesion risk |
| Builders / stewards | Livelihood, recognition, path to stake | Labour, skills | Labour-law recharacterisation 🧨 |
| Real-estate co-investors (AR residents) | Return, security | Capital via fideicomiso | Want liquidity/priority we can't give yet |
| Communities (associations / SAS) | Land access, customers, capital | Goods, services, commitments | Free-riding on commons, or extraction |
| BioPueblo / Lavima | Sales, approvals, reputation | Land (DRS) | Conflict of interest in governance |
| NetX Gen (SAS AR + holding) | Fees, network, replicability | Platform, structuring | Conflict if it receives Pass revenue |
| The land (via guardian + agent) | Regeneration | Everything | Voiceless unless designed in |

## 5. Ostrom checklist (acceptance test for any community token)

1. Clear boundaries (who's in, what's the resource)  2. Rules fit local conditions  3. Those affected can change the rules  4. Monitoring by accountable monitors  5. Graduated sanctions  6. Cheap, local conflict resolution  7. External authorities recognise the right to organise (→ legal wrapper)  8. Nested enterprises (→ federation protocol).

## 6. Sources & logic used

- Zargham, *This Is Not a Test* seminar: https://github.com/mzargham/thisisnotatest
- OASA Whitepaper v1.2: https://oasa.earth/papers/OASA-Whitepaper-V1.2.pdf · bonding-curve note: https://oasa.earth/glossary/bonding-curve/
- $TDF token page: https://www.traditionaldreamfactory.com/token
- Grassroots Economics, commitment pooling: https://grassrootseconomics.org/pages/how-it-works · docs: https://docs.grassecon.org/
- Voshmgir, *Token Economy* (book); Commons Stack / Augmented Bonding Curve & conviction voting (BlockScience research); McConaghy, "Nature 2.0" and token-engineering essays (Medium) — to collect into `sources/` ❓
