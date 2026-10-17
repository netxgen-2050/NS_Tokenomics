"""
Monte Carlo pass over the series waterfall — design B (docs 28 and 29)
NS_Tokenomics / sim — v0.1, 2026-10-17

ALL INPUTS ARE ILLUSTRATIVE ASSUMPTIONS. "What must be true" exploration, not a forecast, not an offer.

The deterministic model (series_waterfall_sim.py) shows ONE path. Here each series is run N times with
uncertain inputs, to see the spread of outcomes and how often something breaks:
  * Vineyard: frost years (a share of the crop lost), price and cost uncertainty, a permit delay that
    shifts the first planting by 0-2 years.
  * Agrivoltaics: PPA price, output, capex overrun, a grid-connection delay of 0-2 years.
Outputs: P10 / P50 / P90 of the Units' IRR and of the money the Foundation receives; the probability
that Units lose money, that they reach their cap, and that First-loss capital is not fully repaid.

Run: python3 sim/series_montecarlo_sim.py > sim/RESULTS_series_montecarlo.md   (stdlib only)
"""
import math
import random

from series_waterfall_sim import run_series, irr

N = 2000
SEED = 7


def pct(xs, q):
    xs = sorted(x for x in xs if not math.isnan(x))
    if not xs:
        return float("nan")
    k = (len(xs) - 1) * q
    f, c = math.floor(k), math.ceil(k)
    return xs[f] if f == c else xs[f] + (xs[c] - xs[f]) * (k - f)


# ------------------------------------------------------------------ vineyard draw
def vineyard_draw(rng):
    ha = 10
    delay = rng.choice([0, 0, 1, 1, 2])                 # permits / water rights
    price = 6.0 * math.exp(rng.gauss(0, 0.20))          # net USD per bottle
    var_cost = 2.5 * math.exp(rng.gauss(0, 0.15))
    opex_ha = 6000 * math.exp(rng.gauss(0, 0.15))
    mature_t = 7 * math.exp(rng.gauss(0, 0.15))         # t/ha at maturity
    frost = {t: (0.4 if rng.random() < 0.15 else 1.0) for t in range(0, 20)}  # 15% of years: frost

    def tonnes(t):
        age = t - delay
        if age <= 0:
            return 0.0
        base = {1: 0, 2: 0, 3: 2, 4: 4, 5: 6}.get(age, mature_t)
        return base * ha * frost[t]

    def sold(t):
        return tonnes(t - 1) * 750 if t >= 2 else 0.0

    return dict(
        horizon=15,
        capex=30000 * ha + 220000 + 50000,
        reserve=220000,
        exit_multiple=6,
        revenue=lambda t: sold(t) * price,
        opex=lambda t: (opex_ha * ha if t > delay else 15000) + sold(t) * var_cost,
        ground_rent=100 * ha,
        royalty=0.05,
        mgmt_fee=0.015,
        share_notes=0.0,
        share_first_loss=0.15,
        note_rate=0.0, note_tenor=0, note_grace=0,
        fl_target=0.04,
        unit_cap=0.09,
        upside_share_units=0.20,
    )


# ------------------------------------------------------------------ agrivoltaic draw
def solar_draw(rng):
    mw = 5
    ppa = 60 * math.exp(rng.gauss(0, 0.25))
    output = 1900 * math.exp(rng.gauss(0, 0.05))
    overrun = 1 + max(0.0, rng.gauss(0.05, 0.10))
    delay = rng.choice([0, 0, 0, 1, 2])                  # grid connection

    def rev(t):
        age = t - delay
        return 0.0 if age <= 0 else mw * output * ppa * (0.995 ** (age - 1))

    return dict(
        horizon=20,
        capex=800000 * mw * overrun,
        reserve=0.0,
        exit_multiple=3,
        revenue=rev,
        opex=lambda t: 15000 * mw + 10000,
        ground_rent=100 * 12,
        royalty=0.05,
        mgmt_fee=0.01,
        share_notes=0.60,
        share_first_loss=0.10,
        note_rate=0.07, note_tenor=12, note_grace=1,
        fl_target=0.05,
        unit_cap=0.10,
        upside_share_units=0.20,
    )


def explore(name, draw, rng):
    u_irr, commons, fl_mult, notes_short = [], [], [], 0
    cap = None
    for _ in range(N):
        p = draw(rng)
        cap = p["unit_cap"]
        _, cf = run_series(p)
        u_irr.append(irr(cf["units"]))
        commons.append(sum(cf["commons"]))
        if cf["first_loss"][0] != 0:
            fl_mult.append(sum(cf["first_loss"][1:]) / -cf["first_loss"][0])
        if cf["notes"][0] != 0:
            # notes are "short" if they received less than principal + 1 year of coupon
            if sum(cf["notes"][1:]) < -cf["notes"][0] * (1 + p["note_rate"]):
                notes_short += 1
    valid = [x for x in u_irr if not math.isnan(x)]
    loss = sum(1 for x in u_irr if math.isnan(x) or x < 0) / N
    at_cap = sum(1 for x in valid if x >= cap - 0.002) / N
    fl_short = sum(1 for m in fl_mult if m < 1.0) / max(1, len(fl_mult))
    print(f"\n## {name}  (N = {N})\n")
    print("| Output | P10 | P50 | P90 |")
    print("|---|---:|---:|---:|")
    print(f"| Regeneration Units IRR | {pct(u_irr, .1):.1%} | {pct(u_irr, .5):.1%} | {pct(u_irr, .9):.1%} |")
    print(f"| Foundation receives (USD) | {pct(commons, .1):,.0f} | {pct(commons, .5):,.0f} | {pct(commons, .9):,.0f} |")
    if fl_mult:
        print(f"| First-loss multiple | {pct(fl_mult, .1):.2f}x | {pct(fl_mult, .5):.2f}x | {pct(fl_mult, .9):.2f}x |")
    print()
    print(f"- Probability the Units **lose money**: **{loss:.0%}**")
    print(f"- Probability the Units **reach their cap** ({cap:.0%}): **{at_cap:.0%}**")
    print(f"- Probability First-loss is **not fully repaid**: **{fl_short:.0%}**")
    if notes_short:
        print(f"- Probability the Green Notes are **short**: **{notes_short / N:.0%}**")


if __name__ == "__main__":
    rng = random.Random(SEED)
    print("# RESULTS — Monte Carlo over the series waterfall (illustrative, not a forecast)\n")
    print("Generated by `sim/series_montecarlo_sim.py` (seed 7). Uncertainty ranges are assumptions "
          "listed in doc 29 §5; re-tune and re-run. Not an offer of securities.")
    explore("A · Vineyard, 10 ha", vineyard_draw, rng)
    explore("B · Agrivoltaics, 5 MW", solar_draw, rng)
