---
title: Long-Term Vision — the Lighthouse token ecosystem
created: 2026-10-02
status: v0.1 — hypothesis to iterate with Gus, counsel, communities
mother_token: RAIZ (name decided 2026-10-02)
---

# 03 · Long-Term Vision (2027 → 2035)

Back to [[00 - README]] · MVP: [[04 - MVP February 2027 (The Hatch)]] · Legal: [[06 - Legal Friction Map]]

## 🌱 In one breath

Picture a **tree**. The **roots** are the land, protected forever by easements and a guardian, and no token can touch them. The **trunk** is a Commons Fund that pays for water, soil, seed banks and shared infrastructure. The **mother token (RAIZ)** is how people around the world join that trunk: they fund it, they help decide where it grows, and they can "eat its fruit": goods and services from the communities. The **branches** are 10–12 communities, each with its own little economy (vouchers, stay credits, contribution points). Whatever a community produces flows back into a **shared pool** that RAIZ holders can draw from. So the more the communities flourish, the more a RAIZ is *worth using*, without anyone paying dividends and without anyone ever mortgaging the roots.

## 1. Architecture: five layers and a diode

```
 LAYER                         SPEED       WHO GOVERNS                     TOKEN / RIGHT
 ─────────────────────────────────────────────────────────────────────────────────────────────
 L0  LAND & ECOLOGY            centuries   Lavima (soil) + perpetual       none, ever
     servidumbres ecológicas               negative easements → Guardian   (Ledger C attestations
     DRS ≤70y per macrolote                entity (NetX Land Trust)         only *read* this layer)
 ───────────────── DIODE: no lien, no collateral, no sale by any upper layer ──────────────────
 L1  CHARTER                   decades     Council of Regeneration         Principles, invariants
     Land Trust principles                 (independent, veto on           (not tokens)
                                           principle breaches only)
 L2  REAL-ESTATE CAPITAL       30 years    Fideicomiso de desarrollo +     Fideicomiso units
     development fideicomiso               beneficiaries' assembly         (private ≤35 now;
                                                                           CNV-tokenised later)
 L3  COMMONS                   years       Commons Assembly (bicameral):   RAIZ (mother):
     Commons Fund + Commons Pool           Funders × Dwellers + Land seat  funding · voice · access
 L4  COMMUNITIES               months      each community's statute        Community vouchers,
     10–12 associations/SAS                (association / steward SAS)     stay credits, Semillas
 L5  DAILY EXCHANGE            days        markets, pools                  swaps, clearing
 ─────────────────────────────────────────────────────────────────────────────────────────────
 rights flow UP (land enables commons enables communities)      recourse never flows DOWN
```

Two kinds of capital, two doors: **L2** is for those who want a real-estate stake (and can legally hold it). **L3** is for those who want to fund and steward the commons and enjoy its fruits. Many people will walk through both doors; **neither door opens the other.** This is also how we handle foreigners (who break fideicomiso tax transparency and can't own riverside rural land): they are naturally L3 citizens. 🏴‍☠️ (see 06)

## 2. The token families

| Family | Layer | Transferable? | Earned / bought | Backed by | Purpose |
|---|---|---|---|---|---|
| **RAIZ** (mother) | L3 | v0–v1: ❌ · v2 (2028+): ✅ only on regulated or offshore rails 🧨/🏴‍☠️ | Bought (Hatch, then curve) + small share earned via sweat | Commons Pool capacity + Commons Fund reserve | Fund commons, steward allocation, access community goods |
| **Steward Voice** | L3 | ❌ never | Derived: 1 per person holding RAIZ, boosted by Presence/Sweat, decays | — | Governance weight that money can't buy beyond a cap |
| **Commons Credits** | L3→L4 | ❌ | Issued to RAIZ holders (allowance) | Community vouchers in the pool | Access to commodities & services |
| **Presence / Sweat** (Semillas family) | L3/L4 | ❌ | Earned, host/peer-confirmed, decaying | — | Reputation, voice boost, path to stake |
| **Community Vouchers** (CAV-style) | L4 | Within pool rules only 🧨 | Issued by each community | That community's goods/services (a commitment to redeem) | Local trade, pre-financing production |
| **Stay Credits** | L4 | ❌ | Bought / earned | Hosting community's capacity | Lodging without timeshare 🧨 |
| **Fideicomiso units** | L2 | Cession by deed (now) → CNV token (later) | Bought, invitation-only | Real estate | Financial participation |
| **Ecological attestations** | L0 read-out | ❌ not a credit | Measured (MRV) | Reality | Gate fund releases (Ledger C) |

### The Rights × Purpose of RAIZ (target state)

| Right | Target state (2028+) | Constraint |
|---|---|---|
| Funding | Purchase mints RAIZ; part of every purchase goes to the Commons Fund (entry tribute) | Never NetX revenue |
| Voice | Through Steward Voice (capped, presence-boosted) in the Funders' chamber | No plutocracy: cap + quadratic or one-person-one-voice |
| Access | Yearly Commons Credits allowance redeemable in the Commons Pool | Credits ≤ pool capacity (I2) |
| Ownership | ❌ No claim on land, no claim on fideicomiso | Diode |
| Return | ❌ No dividends, no buy-back promise. Value = **use-value** of the pool | Keeps it a utility; 🧨 if traded, secondary price still counts |
| Transfer | Only after legal rails exist; exit tribute to Commons Fund | 🧨 PSAV / securities |

## 3. Value flows: how communities "feed the mother" without paying dividends

```
           buy RAIZ (entry tribute ~X%)                    exit tribute (v2)
 supporters ───────────────────────────────▶  COMMONS FUND  ◀──────────────────── secondary market
                                                 │   ▲
           allocation rounds (bicameral)         │   │ canon / tariffs / in-kind commitments
                                                 ▼   │ (legit costs, donations, not profits)
                         grants, infra, incubation   │
                                ┌────────────────────┴────────────────────┐
                                ▼                                         │
   COMMUNITIES (assoc./steward-SAS)  ── issue vouchers ──▶  COMMONS POOL  ── redeem ──▶ RAIZ holders
          ▲                                                    ▲   │                 (Commons Credits)
          └──────── buy inputs / infra services with credits ──┘   └── swap fee → Commons Fund
```

**Six retention loops** (each legal for an asociación civil, to be confirmed 🧨):
1. **Infrastructure tariffs**: water, energy, logistics, cold chain and processing are run by the commons (fideicomiso de administración or coop). Communities pay tariffs = recurring commons income. Brief Challenge 5 answered.
2. **Land-use canon**: communities using commons land pay a canon (sub-arrangement under the DRS / comodato with charges) 🧨 structure TBD.
3. **In-kind commitments ("regenerative tithe")**: each community commits a % of its output as vouchers into the Commons Pool. Between non-profits this is a **donation in kind**; for a SAS it's a **pre-sale** (the Commons Fund buys vouchers at a discount, financing production up front).
4. **Pool swap fees** (small, e.g. 0.5–2%) to the Commons Fund.
5. **Credit circularity**: communities accept Commons Credits for their goods, then spend them on commons services (tariffs, processing, machinery) instead of cashing out. Value circulates; it doesn't leak.
6. **Steward-ownership for SAS**: profit-seeking communities use a **steward-owned SAS** (asset lock + dividend cap + **golden share held by the Guardian** with veto on sale/extraction). Surplus above the cap is reinvested or donated to the Commons Fund (see [[05 - Community Token Templates]]).

**Why RAIZ "gains value" without being a security (in its non-transferable phases):** a RAIZ is worth what its yearly Commons Credits can buy. That grows as more communities commit productive capacity to the pool. It's the **use-value of a membership in a growing economy**, like a CSA share in a farm that keeps adding crops, not a share of profits. 🧨 The moment it's tradable, a market price appears and that argument weakens (Howey-style "efforts of others"). Hence the phased rails.

### 3b. Additions after the 2026-10-02 call [^call]

- **"The land belongs to itself."** Narrative: the trust's purpose is to give the land to itself. Legal translation: the land is never sold; the fideicomiso holds the DRS, perpetual negative easements bind it, and **only licences** are granted to those who follow declared regeneration principles [^drs].
- **Licences, not ownership:** communities, operators and households receive **use rights / licences** from the fideicomiso (a DRS can't be granted on a DRS [^drs]). Licence canons are a recurring commons income (loop 2 above becomes the main one).
- **Community airdrops to RAIZ holders:** each community, when it launches, airdrops **redeemable vouchers** (oil, produce, courses, stays) to RAIZ holders. It's the use-value version of $NETX v2's "launchpool" [^netx]. RAIZ holders get "the first fruits" of all 12 communities.
- **Lighthouse as service provider to BioPueblo:** BioPueblo sells its own lots freely; Lighthouse's communities serve the neighbouring barrios (food, care, learning, repair, energy, events). Neighbours become **customers of the communities and of the pool**, so external cash flows into the ecosystem.
- **Trust graph** for curation (who vouches for whom) joins presence and sweat as a governance primitive: [[10 - Governance Primitives (options)]].
- **Licensing the kit (Phase 4):** the operational, legal, tech and brand manual becomes a **licence** sold to other nodes (Gabriel's expansion model [^call]), with the "desembarco territorial" service for communities landing on a territory.
- **Family-office tension:** RAIZ alone doesn't satisfy financial investors; the full capital stack is in [[09 - Investor Value Model (win-win-win)]].

## 4. Governance: polycentric, bicameral, principle-gated

| Body | Composition | Decides | Can't |
|---|---|---|---|
| **Council of Regeneration** (OASA borrowing) | 5–7 independent people, ecology + law + community, rotating | Whether a proposal violates the Land Trust principles (binary gate); invariant breaches | Allocate money; choose winners |
| **Funders' chamber** | RAIZ holders, **Steward Voice** = 1 per person × presence boost (max ×2), decaying | Commons Fund allocation priorities, rounds | Touch land; override Dwellers on residents' life matters |
| **Dwellers' chamber** | Residents, **one person one vote** (Reglamento / PH especial) | Co-approval of allocations above a threshold; community life | Be bought: no token weighting ever |
| **Voice of the Land seat** | AI agent reading Ledger C + a human ecologist steward | Can **flag** and **delay** (e.g. 30 days) any allocation predicted to degrade KPIs | Vote, spend, veto permanently |
| **Community assemblies** | Per statute | Their own vouchers, admission rituals (by conduct), internal points | Issue claims on the Commons Fund |

Allocation mechanics evolve: **quadratic funding rounds** (2027) → **conviction voting** on a continuous funding pool (2028+, after we have stable identity and enough participants to avoid capture).

## 5. Phased roadmap

| Phase | When | RAIZ form | Key unlock | Legal state |
|---|---|---|---|---|
| **0 · Commitment** | Oct 2026–Jan 2027 | none: commitment registry (no money) | Communities and supporters pledge needs/offers/capital ranges | ✅ |
| **1 · Hatch** | **Feb 2027** | **Founding Pass**: non-transferable membership/service | Commons Fund opens in the guardian association; Allocation Round 0 live at the Gathering | ✅ (to confirm) |
| **2 · Pool** | Mar–Dec 2027 | Pass + Commons Credits; 2–3 community vouchers in the pool; Presence/Sweat live | 7A preliminary approval → lots via fideicomiso (separate) | ✅/🧨 voucher rules |
| **3 · Rails** | 2028 | **RAIZ v2**: transferable on (a) CNV-sandbox-style regulated rails for AR, or (b) offshore utility token for non-AR holders; Augmented Bonding Curve with entry/exit tributes | Hatch passes **carry over** voice, credits and status (not financial value) | 🧨/🏴‍☠️ |
| **4 · Federation** | 2029+ | RAIZ as network keystone: reciprocal access with other nodes (Quinta Esencia, TDF/OASA, Rubania), license of the kit | Post-land-sales steady state: commons funded by tariffs + tributes + pool fees | depends |

## 6. AI layer (McConaghy lens)

- **Facilitator agents**: summarise proposals, check them against principles, run quick simulations of allocation impact before a vote, translate ES/EN/PT. They advise; humans decide.
- **Voice of the Land agent**: reads soil/water/biodiversity MRV (Ledger C), files flags, keeps the long memory of the territory. **Bounded**: no treasury keys, no votes, kill switch held by the Council, open prompts and logs.
- **Data sovereignty**: MRV and presence data are commons assets held by the guardian/communities, licensed (not sold) to researchers and investors. A future "data pool" may become a revenue line 🧨 (Ley 25.326).
- **Horizon (Nature 2.0)**: a land that, through its guardian and agent, accumulates resources for its own restoration. We keep this as a north star, not a v1 feature, because ungoverned autonomous agents with money are exactly the risk Trent himself warns about.

## 7. Invariants and hazards (Zargham + Leveson lens) 🔬

**Invariants** (must hold in every state; enforced by law where possible, by code/process where not):

| # | Invariant | Enforced by |
|---|---|---|
| I1 | **Diode**: no token, fund or community can encumber, collateralise or sell L0 land | Easements, fideicomiso contract, Guardian statute |
| I2 | **Backing**: outstanding Commons Credits ≤ k × pool redeemable capacity (k ≤ 0.8) | Issuance policy, monthly check |
| I3 | **Reserve**: Commons Fund liquid reserve ≥ 3 months commons opex (mirrors Reglamento art. 35) | Treasury policy |
| I4 | **Anti-capture**: no person > 2% of Funders' voice; no single entity > 10% of RAIZ supply | Voice cap, issuance caps |
| I5 | **Principle gate**: no allocation without Council pass | Process |
| I6 | **Ecological floor**: releases for a zone pause if its Ledger C KPIs degrade 2 periods in a row | Voice of the Land flag + Council |
| I7 | **No NetX capture**: Pass/RAIZ proceeds never become NetX revenue; NetX is paid fixed service fees, disclosed | Contracts, audit |
| I8 | **Legal mirror**: if ledger ≠ legal record, legal record wins | Reconciliation |

**Hazards (STPA-lite)**

| # | Hazard | Unsafe control action | Mitigation |
|---|---|---|---|
| H1 | Land encumbered (TDF mortgage case) | Treasury/fideicomiso takes debt secured on land | I1 in deeds; Guardian veto; temperature-check process for last-resort cases |
| H2 | Plutocratic capture of commons | Big buyer accumulates voice | I4, bicameral, presence boost |
| H3 | Credit run / broken promise | Credits issued beyond what communities can deliver | I2, credits expire, sim before issuance |
| H4 | Legal recharacterisation as security / timeshare / lot pre-sale | Marketing promises appreciation, lots or perpetual nights | Copy review, 06 checklist, invariants in T&C |
| H5 | Extractive community | A SAS strips value or degrades land | Steward-owned SAS + golden share; easements; I6 |
| H6 | Commons tragedy inside pool | Communities issue vouchers they don't honour | Swap limits per voucher, reputation, graduated sanctions (Ostrom 5) |
| H7 | Agent capture / opacity | AI agent manipulates or is manipulated | Bounded powers, open logs, Council kill switch |
| H8 | Over-legibility (Scott) | KPIs crowd out local knowledge | Communities choose their own metrics; minimal federation KPIs |
| H9 | Conflict of interest | BioPueblo/NetX sit on both sides | Disclosures, recusal, independent Council |

## 8. How we'd know it's working (federation KPIs, kept few)

- % of commons opex covered by **recurring** flows (tariffs + fees + tributes) vs one-off sales → target >60% by 2030.
- Pool depth: value of goods/services committed per RAIZ outstanding.
- Barrett coverage: Survival goods share of pool (food, water, energy services) vs higher levels.
- Participation: unique allocators per round; Dwellers' turnout.
- Ledger C trends per zone (soil organic matter, water balance, corridor continuity).
- Zero breaches of I1.

## Sources & logic used

- Logic: pace layering, diode, Ostrom polycentricity, STPA-lite hazards ([[02 - Design Lens (the council)]]); commitment pooling (Grassroots Economics); OASA/TDF land-in-a-non-selling-entity pattern.
- Augmented bonding curve / conviction voting: Commons Stack & BlockScience research lineage (Zargham) [S, to collect in `sources/`].
- RTMM brief: `sources/NetX_Lighthouse_Regenerative_Territorial_Model_AI.md` (three ledgers, 12-community ecology, Challenge 5).

[^call]: Private call Gus–Gabriel, 2026-10-02 (private transcript); sanitised in [[13 - Call 2026-10-02 (decisions and actions)]].
[^drs]: `../NS_platform/Documentation/Investigacion — DRS, fideicomisos y tokenizacion (Lighthouse VRN) 2026-09-29.md` §2, §3 A.1 (art. 2118), §5.
[^netx]: *Tokenomics $NETX v2 | NetX State* (2025), §5; see [[11 - Review of $NETX v2 tokenomics (2025)]].
