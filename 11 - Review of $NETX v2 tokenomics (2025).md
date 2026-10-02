---
title: Review — "Tokenomics $NETX v2 | NetX State" (2025)
created: 2026-10-02
reviewed_doc: https://docs.google.com/document/d/1zFkzxH-YqFpWDtFPAblSf_SOsfKx50fkjo8TfvDxOQc (author Juan Zaninetti, created 2025-07-19, last edit 2025-08-10)
status: v0.1 critical reading — what to keep, adapt, drop
---

# 11 · Review of $NETX v2 tokenomics (2025)

Back to [[00 - README]]

## 🌱 In one breath

Last year's paper is a **classic DeFi network-token design**: 1 billion fixed supply, public sale on exchanges, staking, burns, collateral. It was written for a different strategy (NetX State as a "Regenerative Layer 2" of Próspera). Several ideas are worth keeping (time-locked voting, launchpool airdrops of community tokens, a regenerative impact fund, XP for contribution). The core financial architecture conflicts with **Argentine law as researched on 2026-09-29** and with **Gus's diode principle**, so it shouldn't be the base for RAIZ.

## 1. What the paper proposes (summary)

| Element | $NETX v2 |
|---|---|
| Supply | Fixed 1,000,000,000 |
| Allocation | Community & regenerative rewards 40% (10-y unlock) · Treasury 15% · Team & advisors 20% (1-y cliff, 3-y vest) · Private sale 7.5% @ USD 0.03 · Public sale 7.5% @ USD 0.06 · Initial liquidity 10% |
| Raise | ~USD 6.75M (private + public) |
| Use of funds | Tech 30% · Ops & growth 30% · Reserve 20% · Market making 4.44% · Liquidity 5.56% · Admin 10% |
| Utility | ve-locked governance (×1 at 1 y → ×6 at 5 y); currency for protocol fees; staking for node access/reputation with slashing; **collateral for lending**, performance bonds |
| Monetary policy | Aggressive **burns** (70% of fees, 80% of slashes, 50% of RWA/NFT fees…) → deflationary |
| Rewards | Lock-day airdrop; **launchpool**: stakers receive tokens of new ecosystem projects |
| Community plan | XP missions (Zealy/Galxe), referral airdrops, 10-y "regenerative impact" rewards via oracles |
| Framework | Members, ReGen nodes, investors, developers; BTC/RBTC/stablecoins; **FIR — Fondo de Impacto Regenerativo** governed by the community |

## 2. Keep / adapt / drop

| Idea | Verdict | Where it goes in our design | Why |
|---|---|---|---|
| **ve-lock** (longer lock → more voice) | ✅ Adapt (softened ×1…×2, capped, √) | [[10 - Governance Primitives (options)]] §2 | Rewards long-term commitment; reduces flash capture |
| **Launchpool airdrops** of new community tokens to stakers | ✅ Adapt as **utility airdrops** of community vouchers to RAIZ holders | [[03 - Long-Term Vision]] §3, [[09 - Investor Value Model (win-win-win)]] §4 | Matches Gus's "RAIZ holders receive airdrops from the 12 communities" [^call]; keep them redeemable goods/services, not financial tokens 🧨 |
| **FIR (regenerative impact fund)** governed by members | ✅ Keep the idea | = our **Commons Fund** | Same purpose; ours adds the principle gate and bicameral control |
| **XP / missions** for early community | ✅ Adapt as **non-transferable** Semillas/Genesis records | [[04 - MVP February 2027 (The Hatch)]] | Good for activation; must not convert into a sellable token 🧨 |
| **Stake-for-access with slashing** for nodes | 🟡 Adapt as **commitment deposits/bonds** in community agreements | [[05 - Community Token Templates]] §3 | Ostrom's graduated sanctions; but a slashable financial stake is a legal instrument to design with counsel |
| Team & advisors 20% / 10-y community unlock | 🟡 Informative | Holding cap table, not RAIZ | RAIZ shouldn't allocate tokens to the company team (I7: NetX doesn't extract from the commons) |
| **1B fixed supply + "scarcity drives value"** | ❌ Drop | RAIZ supply is **capacity-backed** (beds × nights + pool) | Scarcity narrative = expectation of profit → security 🧨 [^ley26831]; and an arbitrary 1B cap disconnects tokens from real capacity |
| **Public sale + CEX/DEX liquidity + market making** | ❌ Drop (for AR) | Possible only on regulated/offshore rails in phase 3 | Transferable token = activo virtual; platform = PSAV; public offering 🧨 [^drs] |
| **Burns / deflation** | ❌ Drop | — | Exists to raise price → investment-contract signal; no use-value logic |
| **Token as collateral for lending** | ❌ Drop | — | Violates the diode (financial leverage close to land); TDF mortgage lesson [^principles] |
| BTC/RBTC as network collateral | ❌ Drop for now | — | Adds currency risk and regulatory surface without serving the commons |
| Fees paid in $NETX | 🟡 Later | Commons Credits / vouchers inside the closed loop | Fine as internal credits; not as a traded currency in AR |

## 3. Numbers worth reusing (as reference, not targets)

- Use-of-funds split (Tech 30 / Ops 30 / Reserve 20 / Admin 10) is a useful **sanity check** for [[12 - Round Inputs (costs and use of funds)]].
- The 20% reserve matches our I3 invariant spirit.

## 4. What this means for the conversation with the team

The 2025 paper answers *"how do we make a token price go up?"*. The 2026 question is *"how do we fund the commons and give every stakeholder their kind of return, legally?"*. Juanpi's work on community activation (XP, airdrops, anti-sybil) is valuable and could be re-used in the platform's onboarding. ❓ Is he available to collaborate on the RAIZ activation plan?

## Sources & logic used

- Reviewed document: *Tokenomics $NETX v2 | NetX State* (Google Doc linked above), read on 2026-10-02.
- Legal lens: DRS/fideicomiso research 2026-09-29; logic: diode / layer separation; utility vs security (see [[06 - Legal Friction Map]]).

[^call]: Private call Gus–Gabriel, 2026-10-02 (private transcript).
[^ley26831]: Ley 26.831 art. 2, per `../NS_platform/Documentation/Investigacion — DRS, fideicomisos y tokenizacion (Lighthouse VRN) 2026-09-29.md` §6 D.1.
[^drs]: Same research, §6 D.2–D.4 (CNV tokenisation regime, PSAV, PFC).
[^principles]: Gus's layer-separation principle and TDF mortgage case, see [[00 - README]] "Ground rules".
