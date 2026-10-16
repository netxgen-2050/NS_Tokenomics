---
title: Open Questions and Research Backlog
created: 2026-10-02
updated: 2026-10-02 (v0.2 — Gus's answers + call action items)
status: living — answer inline; each answer unlocks an iteration
---

# 07 · Open Questions and Research Backlog

Back to [[00 - README]]

## A. Decisions taken (2026-10-02)

| # | Question | Decision | Where it's applied |
|---|---|---|---|
| A1 | One brand with separable rights (pass now, tradable later)? | ✅ **Yes** | Everywhere |
| A2 | Name of the mother token | ✅ **RAIZ** | Everywhere |
| A3 | Who is the land-trust body? | ✅ **A fideicomiso** holds the land rights for Lote 7; a Guardian entity holds easements and the Commons Fund (to confirm with counsel whether the Guardian can be the fideicomiso's fideicomisario) | 01, 03, 06 |
| A4 | Off-chain vs attestations | ✅ Gus delegated → off-chain for money/credits/votes; optional non-transferable Genesis attestation. Plain explanation in [[04 - MVP February 2027 (The Hatch)]] §6 | 04 |
| A5 | Voice rule | ✅ Combine primitives (membership per holon, RAIZ holding, presence, sweat, trust graph, roles). Options in [[10 - Governance Primitives (options)]]; config A for Feb, B by end 2027 | 10 |
| A6 | Credit generosity | 30%, falling per cohort (no change requested) | 04, sim |
| A7 | NetX fee on the Commons side | ✅ "Go as proposed": fixed, disclosed platform fee only. Explanation in [[04 - MVP February 2027 (The Hatch)]] §3 | 04 |
| A8 | Join OASA network for the offshore rail? | ❌ **No** | 06 §2 (option kept as reference only) |

## B. New open decisions (for Gus, Gabriel, Vagner)

| # | Question | Recommendation | Owner |
|---|---|---|---|
| B-1 | Fiduciary: NetX's AR company or an independent fiduciary? (06 L21) | Independent/professional fiduciary; NetX as developer-manager | Gabriel |
| B-2 | Holding jurisdiction: Uruguay or Wyoming? | Decide by investor mix: mostly LatAm/EU plan-B → Uruguay; US investors → Wyoming. Never Próspera for this round | Gabriel |
| B-3 | Early-investor promise: ×2 vs SAFE discount/cap | SAFE/convertible with discount + cap (12 §3) | Gabriel + Vagner |
| B-4 | One pre-seed valuation (four in circulation) | Vagner's 6–12M range; pick one | Vagner |
| B-5 | Offer fideicomiso units before or after Feb? | After the trust is constituted and the Mainqué status is clear | Gabriel |
| B-6 | Share `../NS_platform` as a second private repo? | Yes, read-only for Vagner | Gus |
| B-7 | Settlement licence canon policy (affordability vs investor return, 09 §5) | Sliding scale; premium licences carry more of the canon | Gus + Vagner |

## C. Research backlog

| # | Item | Why | Where / who |
|---|---|---|---|
| C1 | **Pool capacity 2027**: what the first 2–3 communities can commit (kg, hours, bed-nights) | Caps passes and credits (I2) | Communities; Miguel Ángel's group |
| C2 | **Uptake** at 300/1,500/5,000 for the pass; SAFE interest among the ~127 investor contacts | Replaces guesses | Gabriel's list; 10 calls |
| C3 | **Lawyer quotes**: fideicomiso, Guardian, holding flip, RAIZ T&C | Round input | Gabriel |
| C4 | **Lighthouse bounded model** (RTMM Challenge 1) with licences/tariffs (09 §5) | Real IRR for units | Vagner |
| C5 | TDF real data: night value, utility fee, occupancy, token sales; OASA curve formula (whitepaper appendix) | Calibrate 09 §4 | Gus |
| C6 | **TDF mortgage case** timeline and decision path | Precise invariants I1/H1 | Gus |
| C7 | Licence figure for communities (contract vs derecho real de uso on superficiary property) | 05 §0 | Gabriel |
| C8 | Trust-graph partner (Unity Hub): scope, data ownership, timing | 10 config C | Gus |
| C9 | Grassroots Economics pool contracts and LatAm deployments | Phase 2 pool | Gus / Will Ruddick |
| C10 | Indigenous / customary claims around Mainqué / Lote 7 | L17 | Gabriel |
| C11 | Ley de Tierras reform status (foreign ownership) | Foreign route | Gabriel |
| C12 | AR country-risk hurdle for USD real assets | 09 §2 | Vagner |
| C13 | Is Juan Zaninetti (author of $NETX v2) available for the RAIZ activation plan? | 11 §4 | Gabriel |

## D. Diagnostic for collaborators (20-minute warm-up)

1. What's the difference between a token's **price** and its **use-value**? Which do we grow?
2. Why make a governance right **non-transferable**?
3. What does a **bonding curve** do, and what does the reserve do?
4. What does "**rights flow up, recourse never flows down**" protect against?
5. Why can't RAIZ promise a return, and where *can* returns live?

## E. Next iterations

1. Counsel pack: 06 (L1–L25) + structure diagram (company / commons / land).
2. Vagner integration: three separate entities in the model; bounded Lighthouse case.
3. One-page explainer (EN/ES) for collaborators and the CEO review.
4. Council of Regeneration charter + principles v1.
5. Community plug-in agreement + licence template (05).

## F. After the 2026-10-05 team meeting

| # | Question / item | Recommendation | Owner | By |
|---|---|---|---|---|
| F-1 | Adopt the **now / later / never-as-phrased** sorting of micro-investor ideas (15 §1) | Yes | Team | 12 Oct |
| F-2 | **Founding Circle bundle** (SAFE + RAIZ Pass) as the 2–5k product | Yes, split to be set by Vagner | Vagner + Gus | 12 Oct |
| F-3 | Tokenisation platform choice (Hadron, LandToken…) | Not before the design is fixed; evaluate with 15 §3 criteria, for pot 3 only | Juanpi | Nov |
| F-4 | Copy checklist for public talks (BitConf 30/31 Oct, Space Week, Climate Week) | Mandatory review by Gabriel (06 L28) | Franz + Gabriel | before each talk |
| F-5 | BioPueblo LOI (expected mid-October) | Confirm it covers one fideicomiso for Lote 7 and the licence model | Franz + Gabriel | mid-Oct |
| F-6 | River strip / flood line in the masterplan | Keep it as conservation commons (06 L30) | Martín | 15 Oct |
| F-7 | Second legal quote; jurisdiction (Delaware / Wyoming / Uruguay / AR holding) | Compare on: investor base, tax, cost, reputation | Gabriel | Oct |

## G. After the 2026-10-12 call: hybrid model, constitution, legal deep research

The call left the **hybrid model** open [^call12]. Franz then produced a legal architecture with Gemini [^franz], without this repo as context; it departs from decisions in section A. Until the legal deep research is back ([[prompt_legal]]), these are open:

| # | Question | Current repo position | Owner | By |
|---|---|---|---|---|
| G-1 | Run the legal deep research ([[prompt_legal]], in Spanish) against Gabriel's vault; deliver doc 19 | — | Gabriel | Oct |
| G-2 | Confirm **H0 + H1** now (BioPueblo sells its own lots; base camp on Soluna lots) ([[18 - Hybrid model (selling some lots) - options and trade-offs]]) | Recommended | Team | 19 Oct |
| G-3 | **H2**: a sale zone inside 7A? Needs legal answers, Vagner's numbers with and without it, BioPueblo's plans | Never sell (2026-10-02) stands until the team amends rule 1 in writing | Team | before the surveyor brief (first half of Nov) |
| G-4 | Ticket credit against a future lot (Franz) | Not for Lighthouse lots (06 L27, L31); ❓ test a credit against lots of an already approved barrio | Gabriel | G-1 |
| G-5 | Where ticket money goes: NetX runway or commons? | Company money via SAFE; commons via Pass (06 L33) | Franz + Vagner + Gus | 19 Oct |
| G-6 | Commons Fund inside the real-estate fideicomiso and tickets issued by an operating company (Franz) vs Guardian | Guardian; three pots never mixed | Gabriel + Gus | G-1 |
| G-7 | Transferable allowlisted token with platform-run resale from day one (Franz); NFT as a house key (Gus, long term) | Non-transferable in AR in v0 (06 L1, L26, L34) | Gabriel | G-1 |
| G-8 | Votes weighted by ticket size (Franz: 1 vs 3) | One person, one voice | Gus | — |
| G-9 | Which municipality has jurisdiction over Macrolote 7 (south bank)? Status of Soluna's approval? | The BioPueblo parcel lies in the Mainqué municipal area (Ley 4318/2008, upheld by the Supreme Court in 2023), on the south bank [S]; **whether Macrolote 7 itself falls inside is unconfirmed** (no polygon yet). Soluna's definitive approval: not confirmed [^gv] | Gabriel + Martín | G-1 |
| G-10 | Adopt [[17 - Lighthouse Constitution and Rights of Nature (draft)]] as the working draft; put the succession and no-sale clauses into the BioPueblo term sheet | Proposed | Gus + Franz + Gabriel | term sheet |
| G-11 | Thresholds for the Constitution (ecological share, built share, water) from the masterplan | ❓ | Martín + Gus | after 15 Oct |
| G-12 | Swiss vehicle / OASA as a side option (reopens A8 conditionally) | A8 "No" stands; exploratory conversation only | Gus + Franz | — |
| G-13 | Commission for referring BioPueblo lot buyers: lawful form | ❓ (06 L32) | Gabriel | G-1 |

## H. After Gabriel's vault inventory (2026-10-13) and the reply to Franz's research

Gabriel answered the prompt with an inventory of what his vault already holds [^gv]. Its main recommendation: **design the base legal architecture with a law firm, in parallel with the tokenomics**, bottom-up (land and vehicles → instruments → product), because everything above changes when the base changes. The reply to Franz's Gemini research is [[20 - Land structure after Próspera and reply to Franz]].

| # | Question | Current repo position | Owner | By |
|---|---|---|---|---|
| H-1 | Hire NetX's own law firm: a short technical-legal brief, two or three quotes, fixed fee per phase (1 base architecture, 2 instruments, 3 contracts and platform terms), Río Negro real estate + notary, capital markets/fintech, tax, international corporate | Recommended | Gabriel + Gus | first phase before the Feb 2027 Gathering |
| H-2 | Status of Ley 26.737 (foreign ownership of rural land): verify before relying on 06 L8, L30, L38 | ❓ disputed | Gabriel | first |
| H-3 | Any binding term sheet with BioPueblo / the land owner carries no sale and no mortgage of the land, real easements to a Guardian-owned parcel, succession and the Constitution annex (06 L39) | Proposed | Franz + Gabriel | before signature |
| H-4 | Polygon of Macrolote 7 crossed with the Mainqué municipal area; ask the land owner whether a survey of the whole parcel already exists before briefing a new surveyor | ❓ | Martín | before the surveyor brief |
| H-5 | Boletos after preliminary approval only with express municipal authorisation (06 L41) | Proposed | Gabriel | — |
| H-6 | Mortgage restriction for units on the surface right (06 L40) | Proposed | Gabriel | term sheet |
| H-7 | Send Franz's research to Gabriel (his vault's Drive connector couldn't open it) | — | Gus | now |
| H-8 | Adopt from Franz's research into the masterplan and Constitution: camino de sirga, EIA (Ley M 3266) and water permits (DPA) in the roadmap, closed water cycle and phyto-treatment, native cover minimum per plot, platform decoupled from land ownership (SaaS) | Proposed (20 §2) | Martín + Gus | masterplan |
| H-9 | Run the Gemini deep research (`prompt_gemini.md`) and share its audio summary with the team | Prompt ready | Gus | 19 Oct call |
| H-10 | **Land structure for the BioPueblo term sheet** (land for equity, after Próspera): ownership to a purpose land trust with the Guardian as fideicomisario and golden share (optimistic), with fallbacks P1–P10 ([[20 - Land structure after Próspera and reply to Franz]]) | Proposed; the surface right becomes fallback P1 | Gus + Franz + Gabriel | before signature |

## Sources & logic used

- Section G: call of 2026-10-12 and comparison of this repo with Franz's document, read 2026-10-13 [criterio].
- Section H: Gabriel's vault inventory of 2026-10-13 (shareable parts only) and [[20 - Land structure after Próspera and reply to Franz]].
- Team meeting 2026-10-05 (Fathom transcript in NS_platform) for section F.
- Decisions: Gus's message of 2026-10-02 (answers A1–A8) and the private call Gus–Gabriel of the same day (B-items, action items).

[^franz]: Franz, *"Arquitectura Legal, Financiera, Tokenómica y de Gobernanza para el Desarrollo Territorial Regenerativo: Barrio Lighthouse VRN (Biopueblo)"*, Gemini deep research after the 2026-10-12 call (Google Doc, read 2026-10-13).
[^call12]: Call "Plataforma | Tokenomics y MicroFunding", 2026-10-12 (private Fathom transcript); see [[16 - Call 2026-10-12 (hybrid model, inputs and actions)]].
[^gv]: Gabriel, inventory of his vault for the legal deep research, 2026-10-13 (internal working file, kept out of the repo; only its shareable parts are used here: law texts and general criteria). Not reviewed by a licensed lawyer.
