---
title: Investor Value Model — tensions and a win-win-win capital stack
created: 2026-10-02
status: v0.1 — answers Gus's challenge after the 2026-10-02 call; numbers are illustrative ("what must be true"), never a promise
audience: Gus, Gabriel (COO), Vagner (CFO)
---

# 09 · Investor Value Model (win-win-win)

Back to [[00 - README]] · Numbers: [[sim/RESULTS_value_model]] · Legal: [[06 - Legal Friction Map]] · Governance: [[10 - Governance Primitives (options)]]

## 🌱 In one breath

A family office won't put serious money in for "access and a good story" alone. People who want to live on the land often have no capital at all. **One token can't serve both, and it shouldn't try.** We propose a **capital stack**: each stakeholder gets the *kind* of return they actually value, through the wrapper that can legally carry it:

- **Real-estate investors** get income and value growth through **fideicomiso units**.
- **Early believers in NetX** get venture upside through a **SAFE in the holding**.
- **Users and families** get a big in-kind yield (stays, products) through **RAIZ**.
- **Workers and residents without capital** get **use rights and RAIZ earned by work**.
- **The land** gets a veto nobody can buy.

RAIZ stays a **utility** token. We can show, honestly and with data, how its *use-value* grows. What we can't do is promise a price.

## 1. The question behind the question

> "How do we sell profit to the investor without legally offering profit?" (Gus, call 2026-10-02 [^call])

**Short answer: we can't, and we don't need to.** Any instrument marketed with an expectation of profit from others' work is a security in Argentina (Ley 26.831 art. 2) and almost everywhere else (US *Howey*), whatever we call it [^ley26831]. The honest way out:
1. **Profit lives where profit is allowed.** Fideicomiso units (private, ≤35 per issue in AR) and holding equity (SAFE, private placement) are *meant* to carry returns. They're compliant if offered privately.
2. **Utility lives in RAIZ.** Its value to the holder is in-kind and measurable (nights, products, services, voice). We publish facts (capacity built, pool depth, the curve formula, in-kind value delivered) and **never** price forecasts.
3. **The bundle is a portfolio, not a token.** A family office can hold units + RAIZ (+ SAFE). Each piece is clean, and the combination is attractive.

## 2. Benchmarks: what is "competitive" for patient ecological capital?

| Benchmark | Figure | Period / note | Source |
|---|---|---|---|
| US farmland (NCREIF Farmland Index), total return | **10.29%/yr**, s.d. 6.74%, worst year +2% | 33 years | [^ncreif-farm] |
| US timberland (NCREIF Timberland Index), total return | **10.74%/yr** | 1987–2021 | [^ncreif-timber] |
| NetX thesis: regenerative vs extractive (illustrative) | **13–14%** vs 9–10% risk-adjusted | Modelling, not track record (the thesis says so) | [^thesis] |
| Land appreciation, NetX financial model "Insights" | conservative 2–3%, **base 4–6%**, upside 7–10%/yr | Patagonian land, model assumption | [^model] |
| Family offices: allocation to private equity / real estate | PE ~21%; real estate 6–18% by region | 317 single family offices, 2024 | [^ubs] |
| Argentina country-risk premium | Not quantified here | ❓ Vagner: USD hurdle for AR real assets is plausibly **12–15%** [criterio] | — |

**Reading:** a family office comparing us to farmland or timberland expects **~8–10% USD net** in a stable jurisdiction, and **more for Argentina** (FX, legal, macro). "Plan-B" investors (Gabriel's profile: people from conflict zones looking for a soft landing [^call]) accept lower financial return in exchange for **optionality to live there**. That's exactly what the utility layer can sell.

## 3. The tensions of regenerative investing (and what we do with each)

| # | Tension | Why it bites here | Our move |
|---|---|---|---|
| T1 | **Horizon**: fund cycles 7–10 y vs regeneration 20–50 y | Soil, forest and community mature slowly | Evergreen fideicomiso (≤30 y by law [^drs]) with **cession windows**; RAIZ for the long tail |
| T2 | **Yield vs affordability** | Higher licence canons raise investor IRR but squeeze residents with no capital (see §5) | **Sliding-scale canon** (sweat can pay part); cross-subsidy from hospitality and premium licences; cap canon at a % of local median income |
| T3 | **Never-sell vs appreciation** | Land is never sold (Gus [^call]), so appreciation is unrealised | Capture value through **income + NAV-based cessions**, not land sales; early entry below post-approval value |
| T4 | **Liquidity vs stewardship** | Liquid tokens attract speculators; illiquid units scare investors | Units: cession windows + community preference; RAIZ: non-transferable now, **time-locked** later (ve-lock, borrowed from $NETX v2 [^netx]) with exit tribute |
| T5 | **Capital vs control** | Money wants votes | Diode + bicameral governance: money buys capped voice on the commons, never on land or residents' lives ([[10 - Governance Primitives (options)]]) |
| T6 | **MRV theatre vs real regeneration** | Investors like carbon/biodiversity credits; measuring takes years | Minimal baseline now; MRV in the pitch as *roadmap*, not revenue (Gus [^call]); Ledger C gates fund releases, it's not sold |
| T7 | **Promise vs utility** | Legal line (§1) | Facts, not forecasts; utility value is verifiable |
| T8 | **Whales** | One large early ticket can dominate (concern raised in call [^call]) | Per-person caps on RAIZ voice; SAFE pro-rata caps; investor chamber separate from dwellers |
| T9 | **Argentina macro & FX** | USD investors, ARS costs | USD-denominated units; costs partly in-kind (sweat, vouchers); FX section in data room ❓ Vagner |

## 4. RAIZ: how a TDF-like utility token accrues value (honestly)

**The mechanism (phase 3, after units exist and the timeshare question is solved 🧨 [^timeshare]):**
- 1 RAIZ = **1 stay-night per year** in standard lodging (pay a utility fee) **+ a share of community airdrops**: product/service vouchers each community commits to the Commons Pool (oil, vegetables, courses, workshop hours) [^call].
- **Supply capped by real capacity** (beds × 365), as at TDF (18,600 = beds × 365) [^oasa].
- **Price on a public bonding curve** that rises as capacity sells out (TDF: ~€222 → asymptote ~€420) [^oasa][^bc].
- In AR: non-transferable until legal rails exist. Later: transferable on a regulated or offshore rail with an **exit tribute** to the Commons Fund.

**Simulated value per RAIZ bought at USD 250** (full table in [[sim/RESULTS_value_model]]):

| Scenario | In-kind value in year 5 (stay − fee + airdrops) | = "consumption yield" on price | Curve price in year 10 | IRR if you use 35–65% of it | IRR use + exit at curve (if legal) |
|---|---:|---:|---:|---:|---:|
| conservative | USD 56 | 22% | 374 | −2% | 11% |
| **base** | **USD 95** | **38%** | **432** | **15%** | **21%** |
| upside | USD 150 | 60% | 542 | 31% | 34% |

**What this tells us:**
1. **Utility tokens are a superb deal for users** (families, regulars, plan-B households): prepaying a perpetual night gives an in-kind yield far above any bond. That's why TDF sells.
2. **For a pure financial investor who never comes, use-value is ~zero** (the conservative case even goes negative). Their return would depend on a secondary market we can't promise. **So RAIZ alone is the wrong product for family offices**: it's the *kicker*, not the core.
3. The curve gives early holders a visible, rules-based entry advantage. Communicate it as **pricing policy** ("the earlier you commit, the lower the price, as at TDF"), never as "appreciation" 🧨.

## 5. Fideicomiso units: what must be true for family-office returns

Set-up (illustrative): investors put **USD 6M** cash for infrastructure; BioPueblo contributes the DRS in kind (~USD 4M, the land value mentioned in the call [^call]). Land is never sold. Income comes from **community use licences** (derecho de uso / canon, since a DRS can't be granted on a DRS [^drs][^call]), productive leases, infrastructure tariffs and a hospitality share. Exit by **cession of units in year 15** at NAV (net income / cap rate).

| Scenario | Net income at maturity | Investor IRR (15 y) |
|---|---:|---:|
| conservative | USD 0.46M/yr | ~0% |
| base | USD 0.83M/yr | **5.9%** |
| upside | USD 1.39M/yr | **12.0%** |

**What must be true** (base, varying the settlement licence canon on the ~70 ha of Z0 settlements):

| Canon USD/ha/yr | ≈ per resident/month | IRR @ cap 8% |
|---:|---:|---:|
| 12,000 | ~USD 70 | 5.9% |
| 18,000 | ~USD 105 | 8.6% |
| 25,000 | ~USD 145 | 11.2% |

Plus the **early-entry lever**: buying in at 30–45% below post-approval value (entering before Mainqué's approval de-risks the project) lifts the base IRR to **9–12%**.

**Reading (the honest one):** a never-sell land trust living only on licences and tariffs is a **5–9% USD income asset**, the right profile for *patient, impact-first* capital. Reaching the **10–12%** family-office hurdle needs (a) an early-entry discount, (b) premium licences (hospitality, wellness) carrying more of the canon than affordable housing, and (c) development margin captured by **steward-owned community SAS** that build and operate. Pushing the housing canon up for investor IRR breaks T2. We should say this openly in the room: credibility comes from naming the gaps [^narrative].

## 6. The win-win-win capital stack

| Stakeholder | Puts in | Gets | Instrument / wrapper | Return type | Protection |
|---|---|---|---|---|---|
| **Family office / regenerative investor** | USD 100k–1M+ | Income + NAV growth; reporting; optional family access | **Fideicomiso units** (private ≤35/issue) + RAIZ kicker | Cash (target 6–9% base, 10–12% with early entry) + in-kind | Land never encumbered (I1); trustee duties; cession window |
| **Plan-B investor** (Gabriel's profile) | USD 5k–50k | Network membership, priority **stay** access (service, not lots), community | RAIZ Founding Pass (+ SAFE if they want company upside) | In-kind (22–60% consumption yield when used) | Non-transferable now; carry-over to RAIZ v2 |
| **Early company investors** | USD 5k SAFE tickets | Equity upside in NetX (platform, licences, development fees) | **SAFE in the holding** (new jurisdiction, not Próspera) [^call] | Venture | Standard SAFE terms; no fixed "x2" (see 06 L20) |
| **Workers / builders** | Labour, skills | Wages + **Sweat → RAIZ** (a reserved pool, TDF reserves 20% for sweat [^oasa]) + path to use licence | Labour/volunteer agreement + Semillas | Cash + in-kind + use rights | Insurance; LCT-compliant modality 🧨 |
| **Residents without capital** | Time, care, presence | **Use licence** paid partly by work; affordable canon tier; voice as dweller | Licence (derecho de uso) from the fideicomiso; community membership | Housing security + belonging | Dwellers' chamber (1p1v); canon cap; no eviction by token |
| **Community founders / project directors** | Vision, organisation | Founder stake in a **steward-owned SAS**, salaries, community-token founder allocation | Steward SAS (golden share to Guardian) or association | Capped dividends + salary | Asset lock; principles |
| **NetX Gen** | Platform, structuring, network | Development fee from the fideicomiso, platform fees (fixed, disclosed), **licence of the kit** to other nodes (Gabriel's licensing model [^call]) | NetX SA/SAS AR + holding | Business revenue | Never a % of investors' money; never Commons Fund revenue (I7) |
| **BioPueblo / Lavima** | Land (DRS) | Fiduciante-beneficiary share; neighbours served by Lighthouse services | Fideicomiso | Income share | Contract |
| **The land** | Everything | Perpetual easements, Voice-of-the-Land seat, Ledger C gates | Guardian + easements | Regeneration | Diode; Council veto |

**Why it's win-win-win:** nobody gets paid with someone else's kind of return. Investors aren't paid with residents' affordability (canon cap), residents don't carry investors' risk (land never mortgaged), workers' sweat turns into the same use-rights capital buys, and the commons is funded by the RAIZ layer, which every other layer feeds (tariffs, airdrops, exit tributes).

## 7. What to tell a family office (draft framing, needs counsel review)

> "Lighthouse is a 1,000-ha regenerative land trust that will never be sold. You can participate in its infrastructure through private fideicomiso units that earn from community licences and services, with exits through periodic unit cessions. Separately, your family can hold RAIZ: prepaid access to stays and to what our communities produce, and a voice in how the commons fund is spent. We don't promise returns on RAIZ; we publish what it delivers."

## 8. Next steps

- Vagner: replace the illustrative canon, capex and cap-rate inputs with the Lighthouse bounded model (the RTMM brief's Challenge 1) and an AR country-risk hurdle ❓.
- Gabriel: confirm (a) whether units can be USD-denominated, (b) cession windows with community preference, (c) foreign investors' route, since a foreign beneficiary taxes the whole fideicomiso [^drs].
- Gus: validate the in-kind numbers (night value, utility fee, airdrop basket) with TDF's real data ❓ (B5/B6 in 07).

## Sources & logic used

- Logic: separate return *types* by wrapper (layer separation / diode); "what must be true" modelling instead of forecasts (Zargham/McConaghy lens, [[02 - Design Lens (the council)]]).
- Simulation: `sim/value_model_sim.py` → [[sim/RESULTS_value_model]] (all inputs listed in the script).

[^call]: Private call Gus–Gabriel, 2026-10-02 (transcript held privately, not in the shared repo; see [[13 - Call 2026-10-02 (decisions and actions)]]).
[^ley26831]: Ley 26.831 art. 2 (oferta pública; "contrato de inversión"), as summarised in `../NS_platform/Documentation/Investigacion — DRS, fideicomisos y tokenizacion (Lighthouse VRN) 2026-09-29.md` §6 D.1.
[^ncreif-farm]: Peoples Company, "NCREIF Farmland Returns: 30+ Years of Evidence": https://peoplescompany.com/blog/national-council-of-real-estate-investment-fiduciaries-farmland-returns-30-years-of-evidence-about-farmland-as-an-investment-class
[^ncreif-timber]: AcreTrader, "What's the Return on Timber Investments?" (NCREIF Timberland 10.74% 1987–2021): https://acretrader.com/learn/farmland-investing/whats-the-return-on-timber-investments
[^thesis]: NetX Gen, *Regenerative Assets Investment Thesis* v3 (Google Doc 13e8WJ68…), as synthesised in `../NS_platform/Documentation/01 - Source Synthesis.md` §1.
[^model]: *NetX Financial Model 20012026.xlsx*, sheet "Insights" (land appreciation ranges; legal/technical cost ranges); file kept in `private/`.
[^ubs]: UBS Global Family Office Report 2025 press release: https://www.ubs.com/global/en/media/display-page-ndp/en-20250521-global-family-office-report-2025.html
[^drs]: DRS/fideicomiso research 2026-09-29 (§1, §4, §4 B.5), `../NS_platform/Documentation/`.
[^timeshare]: CCyC arts. 2087–2102; Ley 26.356, per the same research §7 E.
[^oasa]: OASA Whitepaper v1.2: https://oasa.earth/papers/OASA-Whitepaper-V1.2.pdf ; $TDF page: https://www.traditionaldreamfactory.com/token
[^bc]: OASA glossary, bonding curve: https://oasa.earth/glossary/bonding-curve/
[^netx]: *Tokenomics $NETX v2 | NetX State* (Juan Zaninetti, 2025), reviewed in [[11 - Review of $NETX v2 tokenomics (2025)]].
[^narrative]: `../NS_platform/Documentation/07 - Investor Narrative (Argentina).md`, "Honesty rules".
