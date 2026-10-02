---
title: Hatch simulation — results v0.1
created: 2026-10-02
generated_by: sim/hatch_sim.py (re-run after changing PARAMS; paste output below)
status: ILLUSTRATIVE — every input is an assumption, not a forecast or an offer
---

# Hatch simulation — results v0.1

Back to [[../00 - README]] · Design: [[../04 - MVP February 2027 (The Hatch)]]

## 🌱 What this tells us in plain words

1. With the assumed tiers (USD 300 / 1,500 / 5,000) and a **base of ~225 founders**, the Hatch raises **~USD 210k gross** and leaves **~USD 160k of net commons capital** after setting aside the real cost of honouring credits and legal setup. That's a meaningful start (seed bank, nursery, first water works, 3–5 community micro-grants), **not** enough to build 1,000 ha of infrastructure. The real-estate money comes through the fideicomiso, separately.
2. **Success is a risk too.** In the high scenario we sell more passes than the communities can honour in goods and services: credits outrun pool capacity (I2 ❌). Fix: **cap the number of passes per cohort** to pool capacity, or make the credit ratio **fall as more passes are sold** (a soft "bonding curve" on generosity rather than on price).
3. **Failure is mostly a reserve problem.** In the low scenario we can't hold 3 months of commons opex (I3 ❌). Fix: a **minimum threshold** (e.g. USD 75k net). If not reached by a deadline, the Hatch converts into pure memberships and the Commons Fund doesn't open (all-or-nothing, like a crowdfunding threshold).
4. **Credits are a promise we must be able to keep.** Up to ~40% of price returned as credits is safe *if* communities commit ~USD 40k/yr of goods/services in year 1. Beyond that we're printing promises. ❓ So the single most important number to research is **what the first 2–3 communities can actually commit to the pool in 2027**.

## Assumptions (edit in `PARAMS` / `TIERS`)

| Input | Value | Why / to validate |
|---|---|---|
| Tiers | Seed 300 · Steward 1,500 · Guardian 5,000 | Founding membership USD 2–5k for ~15 people was discussed (Legal brief §0.a); added a low tier for breadth |
| Uptake low/base/high | 90 / 225 / 450 holders | ❓ Validate with the commitment registry (Phase 0) |
| Credit ratio | 30% of price, over 3 years | Lever: attractiveness vs capital |
| Redemption | 75% | Breakage is real, but don't design to profit from it |
| Cash cost per credit | 0.50 | Communities need cash for inputs; rest is their in-kind commitment |
| Setup | USD 25k | Association setup, counsel, KYC, audit ❓ |
| Commons opex | USD 6k/month | ❓ |
| Pool capacity yr 1 | USD 40k of goods/services | ❓ the key unknown |

## Output (v0.1 run)

## 1. Scenarios (credit_ratio = 30%)

| Scenario | Holders | Gross raise | Credits issued | Credits/yr | Expected cash cost of credits | Net commons capital | Reserve months | I2 backing | I3 reserve |
|---|---:|---:|---:|---:|---:|---:|---:|:-:|:-:|
| low | 90 | 80,500 | 24,150 | 8,050 | 9,056 | 46,444 | 1.5 | ✅ | ❌ |
| base | 225 | 210,000 | 63,000 | 21,000 | 23,625 | 161,375 | 5.4 | ✅ | ✅ |
| high | 450 | 420,000 | 126,000 | 42,000 | 47,250 | 347,750 | 11.6 | ❌ | ✅ |

## 2. Base scenario — use of net commons capital

| Bucket | USD | % |
|---|---:|---:|
| Commons bootstrap (water, nursery, seed bank, kitchen) | 80,688 | 50% |
| Community incubation grants (allocation rounds) | 32,275 | 20% |
| Reserve (I3) | 32,275 | 20% |
| Stewardship ops runway | 16,138 | 10% |

## 3. Sweep — how generous can credits be? (base uptake)

| Credit ratio | Credits/yr | Pool capacity needed for I2 (USD/yr) | Net commons capital | I2 with 40k/yr pool |
|---:|---:|---:|---:|:-:|
| 0% | 0 | 0 | 185,000 | ✅ |
| 10% | 7,000 | 8,750 | 177,125 | ✅ |
| 20% | 14,000 | 17,500 | 169,250 | ✅ |
| 30% | 21,000 | 26,250 | 161,375 | ✅ |
| 40% | 28,000 | 35,000 | 153,500 | ✅ |
| 50% | 35,000 | 43,750 | 145,625 | ❌ |
| 60% | 42,000 | 52,500 | 137,750 | ❌ |

## 4. Monte Carlo on uptake (2,000 runs, each tier ~ uniform between low and high)

| Metric | Value |
|---|---:|
| Net commons capital P10 | 124,366 |
| Net commons capital P50 | 196,520 |
| Net commons capital P90 | 265,656 |
| Runs breaking I2 (credits > 80% of pool capacity) | 12.6% |
| Runs breaking I3 (reserve < 3 months opex) | 2.0% |

## Next iterations of the model

- Replace fixed tiers with a **cohort step curve** (price per cohort rises 10–15%) and a **falling credit ratio** per cohort, and test I2 again.
- Add **fideicomiso inflows** (Ledger A) as a separate track so nobody confuses the two doors.
- Add **recurring flows** (tariffs, pool fees, tributes) to model the post-land-sale steady state (brief Challenge 5).
- Port to cadCAD / radCAD if we go to the Augmented Bonding Curve in Phase 3.
