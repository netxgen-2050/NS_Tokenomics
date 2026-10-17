---
title: Impact on tokenomics
created: 2026-10-17
status: v0.1 — what the proposed design changes in RAIZ, the pots and the repo's rules; decisions for Gus and the team
---

# 26 · Impact on tokenomics

Back to [[00 - README]] · Legal redesign: [[25 - Legal design v0.1 (Land Foundation + Regeneration Trust Program)]] · Design: [[25 - Legal design v0.1 (Land Foundation + Regeneration Trust Program)]]

## 🌱 In one breath

Yield and the commons can work together if they live in **two different instruments that talk to each other**:
- **RAIZ** stays the membership and voice of the commons. Its yield is **in kind**: stays, food, courses, a say in where the Commons Fund goes.
- **Regeneration Units** (tokenised trust units of each series) carry the **cash yield**, on regulated rails. Their yield is capped, and part of it is tied to verified regeneration.

Merging both into one token is possible, but then RAIZ becomes a security: KYC for everyone, a regulated issuer, fewer people able to join. Keeping them separate lets anyone join the commons and lets investors earn. Most of the repo's design survives; four rules need amending.

## 1. The instruments after the redesign

| Instrument | Holder | What it gives | Yield | Legal nature | Where it lives |
|---|---|---|---|---|---|
| **RAIZ membership** (today's Founding Pass, v0) | Anyone, any nationality | Membership of the commons; stay credits; community products; voice on the Commons Fund | **In kind** (stays, food, courses) | Membership + service contract with the Foundation (or a members' association) | Foundation |
| **Regeneration Units** (participation units of a series, tokenised later) | Investors, KYC | A share of the series' cash flows, capped | **Cash**, variable, capped; a **regeneration-linked** part | Security: private placement first, then CNV public offering and tokenisation | Each series of the Program |
| **Green Notes** (senior debt of a series) | Investors, KYC, including foreign funds | A fixed coupon | **Cash**, fixed | Security (debt securities of a financial trust) | Each series |
| **First-loss units** | Catalytic investors (foundations, climate funds) | Lower in the waterfall, impact reporting | Cash after the notes, possibly lower | Security (private) | Each series |
| **NetX equity** (SAFE today) | Venture investors; the landowner | The upside of the manager and platform | Venture | Shares of the holding | NetX holding |
| **Community instruments** | Residents, clusters | Homes on sub-surface rights; cooperative shares | Housing; limited interest on cooperative shares | Surface right; cooperative law | Communities |

## 2. How RAIZ and the Units talk to each other (the link, without merging)

Options, from safest to boldest [criterio; each needs counsel]:

1. **Regeneration-linked yield** ✅: part of each Unit's return depends on verified regeneration KPIs (cover, soil organic matter, water infiltration) measured in the yearly ecological ledger. This is how sustainability-linked bonds work [S]. Investors are paid more when the land is doing better.
2. **Yield in kind for unit holders** ✅: unit holders can take part of their distribution as RAIZ stay credits. The cash goes to the Foundation, which delivers the service.
3. **Commons share of every flow, visible on-chain** ✅: the royalty and the residual above the cap are shown live on the platform. That is RAIZ's "treasury" made transparent.
4. **RAIZ members get first access to Unit issuances** ⚠️: a priority right to invest. It could make RAIZ look like a gateway to a security [verify].
5. **RAIZ itself pays cash from the royalty** ❌ for now: that turns RAIZ into a security, with KYC and a regulated issuer, and the commons into an investment pool. Possible later (RAIZ v2, regulated), but it changes what the commons is.

## 3. The pots, redrawn

| Before (main) | After (legal redesign) | Change |
|---|---|---|
| **Company** pot: SAFE in the holding | NetX holding: SAFE and equity; earns fees and licences | Same; now with a clear business: manager + platform (answers `07` H-14) |
| **Commons** pot: Guardian association, RAIZ | **Foundation**: land + Commons Fund; RAIZ memberships, ground rents, royalty, residual, grants, value capture | Bigger: the commons gets the land **and** a share of every flow |
| **Land** pot: fideicomiso units over the land | **Program series**: notes and units over **projects on surface rights**, not over the land | The investors' object changes: projects, not land |
| — | Easement holder | New, independent |

## 4. Rules of the main repo this would amend

| Rule in `AGENTS.md` | Proposed amendment | Why |
|---|---|---|
| 1 · Diode: nothing may encumber the land | **Keep for the land; allow surface rights and project assets to be pledged or mortgaged** | Project finance (solar, hub) needs collateral; the land stays untouched (CCyC 2120) |
| 2 · Three pots | **Commons money is never company or investor money; investors hold series, NetX holds fees** | Same spirit, more vehicles |
| 3 · RAIZ is a utility; no yield language | **RAIZ stays a utility with in-kind yield; cash yield lives in Regeneration Units and Green Notes, and can be described plainly there** | The rule already allowed returns in trust units; this makes yield explicit and links it to regeneration |
| 6 · One person, one vote | Unchanged for residents; investors vote only in their series | — |
| — (new) | **Capped investor returns; residual to the commons** | Steward-ownership applied to finance |
| — (new) | **The regeneration royalty is paid before investors** | The commons gets paid in bad years too |

Docs that would change if this is adopted: `00 - README.md` (60-second answer), `03`, `04` (who receives the Pass money: the Foundation), `09` (stakeholders table), `12` (round inputs: series 0), `20` (land structure) and `sim/value_model_sim.py` (add the waterfall with royalty and cap).

## 5. Questions for the team

1. Separate instruments (RAIZ + Units) or one token? Recommendation: separate now, revisit for RAIZ v2.
2. Royalty rate *r* and return cap: Vagner to model ranges per engine.
3. Which regeneration KPIs drive the linked yield, and who certifies them (the Council of Regeneration plus an external verifier)?
4. Does the Feb 2027 Founding Pass go to the Foundation (if it exists) or to a fiscal host?

---

## Sources & logic used

- Sustainability-linked instruments: ICMA Sustainability-Linked Bond Principles (coupon tied to KPIs) [S]; CNV guidelines for social, green and sustainable securities [S] [verify current resolution].
- Securities line: Ley 26.831 art. 2; Ley 27.739 (PSAV) [C]; CNV tokenisation regime and sandbox [S] [verify].
- Current tokenomics: `03 - Long-Term Vision.md`, `04 - MVP February 2027 (The Hatch).md`, `09 - Investor Value Model (win-win-win).md`, `AGENTS.md` (read as inputs, not as rules here).
- Amendments and recommendations: our judgement [criterio].
