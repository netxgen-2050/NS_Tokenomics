---
title: NS_Tokenomics — README and reading instructions
created: 2026-10-02
updated: 2026-10-02 (v0.2, after the Gus–Gabriel call)
status: working repository (private) — design sandbox, not an offer, not legal/tax/investment advice
owners: Gus (design), Gabriel (COO, legal), Vagner (CFO, financial model)
language: English (shared workstream with non-Argentine collaborators)
---

# NS_Tokenomics — how to read this

This repository holds the **token and capital design for the Lighthouse** (~1,000 ha, Macrolote 7, Mainqué, Río Negro, inside BioPueblo's ~10,000 ha). It answers one question:

> **How do we fund the commons and the first communities on land that will never be sold, give each stakeholder (investors, workers, residents without capital, community founders, NetX, the land) a fair kind of return, and stay compliant?**

## 1. The answer in 60 seconds

- **The land is never sold.** It sits in a fideicomiso holding a surface right (DRS) and is protected by perpetual ecological easements held by a Guardian. Communities receive **use licences**, never ownership.
- **Three pots of money, three wrappers, never mixed** (the "diode": rights flow up, no money or debt flows down to the land):

| Pot | Instrument | For whom | Return type | When |
|---|---|---|---|---|
| **Company** (NetX holding, moving out of Próspera) | **SAFE**, USD 5k tickets, ~375–500k | Early believers in NetX | Venture equity | Oct 2026 – Mar 2027 |
| **Commons** (Guardian / Commons Fund) | **RAIZ**: the mother token, a utility. In Feb 2027 a non-transferable Founding Pass | Users, families, "plan-B" investors, supporters worldwide | **In-kind**: stays, community products (airdrops), a voice on the commons fund | Feb 2027 Gathering |
| **Land** (Lighthouse fideicomiso) | **Fideicomiso units**, private, ≤35 per issue | Family offices, regenerative investors | Income from licences/tariffs + NAV growth | After the trust exists |

- RAIZ is a **utility** token. We show what it delivers; **we never promise price or profit**. Profit lives in the SAFE and the fideicomiso, where it's allowed.

## 2. Reading paths by role

| If you are… | Read, in this order | Time |
|---|---|---|
| **Gabriel (COO / legal)** | 13 (call) → 06 (legal friction map, L1–L23) → 01 (context) → 12 §3–4 (who can be offered what) → 05 (community licences) | 40 min |
| **Vagner (CFO)** | 13 → 12 (costs, use of funds) → 09 (investor value model) → `sim/RESULTS_value_model.md` → `sim/RESULTS.md` → 11 ($NETX v2 review) | 45 min |
| **Gus** | 07 (open questions, answered and new) → 09 → 10 → 04 | — |
| **New collaborator, non-crypto** | 08 (glossary) → this README → 03 (vision) "In one breath" sections only | 20 min |
| **Crypto-native collaborator** | 02 (design lens) → 03 → 10 → 09 §4 → 11 | 45 min |

Every document starts with a **🌱 "In one breath"** plain-language summary. Read only those for a quick tour.

## 3. Map of the repository

| # | File | What it gives you |
|---|---|---|
| 00 | README (this) | How to read; conventions; how we collaborate |
| 01 | Context and Constraints | Land, legal walls, product decisions, call updates |
| 02 | Design Lens (the council) | Method: Zargham, McConaghy, Voshmgir, Paruch, Ruddick + *This Is Not a Test* |
| 03 | Long-Term Vision | The full ecosystem 2027–2035: layers, token families, flows, governance, phases, invariants |
| 04 | MVP February 2027 (The Hatch) | What we can launch at the Gathering |
| 05 | Community Token Templates | Kits for associations, steward-owned SAS, TDF-style lodging; licences |
| 06 | Legal Friction Map | Every legal challenge 🧨 and hack 🏴‍☠️, with sources |
| 07 | Open Questions and Research Backlog | Decisions taken, open decisions, research list |
| 08 | Glossary (plain language) | Crypto-economics and Argentine legal terms, without jargon |
| 09 | **Investor Value Model (win-win-win)** | Benchmarks, tensions, RAIZ value accrual, fideicomiso returns, capital stack |
| 10 | **Governance Primitives (options)** | Membership, tokens, presence, sweat, trust graph, roles: recipes and 3 configurations |
| 11 | **Review of $NETX v2 tokenomics (2025)** | Keep / adapt / drop from last year's paper |
| 12 | **Round Inputs (costs and use of funds)** | Costs, use of funds, trust micro-round, who can be offered what |
| 13 | **Call 2026-10-02 (decisions and actions)** | Sanitised decisions, divergences, action items |
| sim | `hatch_sim.py`, `value_model_sim.py` + RESULTS files | Reproducible models (Python, stdlib only) |
| sources | Lighthouse RTMM brief, BioPueblo KMZ | Inputs we can share |
| private | Transcript, financial model, large/third-party files | **Git-ignored**: never pushed |

## 4. Conventions

**Sources (Gabriel's rule, adopted 2026-10-02):** every factual claim carries a footnote `[^x]`, and every document ends with **"Sources & logic used"**: the documents, data and reasoning it relied on. Markers used in claims:
- **[C]** confirmed in a primary source · **[S]** secondary source · **[NC]** not confirmed · **[criterio]** our own judgement, not a fact · **[verify]** to check with counsel.
- Private sources are cited by name and date (e.g. *"Private call Gus–Gabriel, 2026-10-02"*) and stay out of the repo.

**Emoji legend**

| Emoji | Meaning |
|---|---|
| ✅ | Doable now within Argentine law as we understand it (still to be confirmed by counsel) |
| 🧨 | **Legal challenge**: collides with a rule; don't ship without counsel |
| 🏴‍☠️ | **Legal hack**: structural workaround; legitimate only if substance matches form |
| 🌱 / 🔬 | Plain-language / technical section |
| ❓ | Open question (tracked in 07) |
| 🔒 | Private: content kept outside the shared repo |

**Ground rules we design by**
1. **The diode**: financial instruments never govern or encumber land; rights flow upward, recourse never flows down (TDF mortgage lesson).
2. **Commitment precedes organization.**
3. **Separate the rights** tokens usually bundle (funding, voice, access, reputation, return).
4. **Substance over form**: euphemisms help users understand; they don't change the legal nature.
5. **Simulate before launch**; numbers are "what must be true", not forecasts.

**Names:** the mother token is **RAIZ** (decided 2026-10-02). In Argentine-facing UI we follow `../NS_platform/Documentation/Desarrollo/02 - Glosario UX-Legal.md` (no "token", "inversión con retorno", "reservá").

## 5. How we collaborate (Git + Obsidian)

- This folder is both an **Obsidian vault** (open the folder as a vault; `[[links]]` work) and a **private Git repository**.
- Branches: `main` (agreed content), `gustavo`, `gabriel`, `vagner` (personal working branches). Work on your branch, open a pull request to `main`, and discuss in the PR.
- `private/` is git-ignored: the call transcript, the financial model (Vagner's original stays with Vagner) and large third-party files (e.g. the Avedam Kezum deck) live only on Gus's machine.
- `../NS_platform` (product and legal research) is a sibling, read-only source; it isn't part of this repo. Paths starting with `../NS_platform/` refer to it ❓ (decide whether to share it as a second repo).
- Rerun the models: `python3 sim/hatch_sim.py` and `python3 sim/value_model_sim.py`.

## 6. Status (v0.2, 2026-10-02)

- ✅ Vision, MVP, legal map, community kits, glossary (v0.1, morning)
- ✅ After the call: investor value model, governance options, review of $NETX v2, round inputs, call notes, RAIZ rename, sources everywhere (v0.2)
- ⏭ Next: counsel pack (06 §3 + structure diagram), Vagner's bounded Lighthouse model, Council of Regeneration charter, one-page explainer for collaborators.

## Sources & logic used

- This README summarises files 01–13 of this repository; their own source sections apply.
- Collaboration conventions: Gabriel's request for sources and Gus's proposal of a private repo with personal branches, private call 2026-10-02.
