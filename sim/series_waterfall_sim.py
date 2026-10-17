"""
Series waterfall model — Regeneration Trust Program (legal redesign, docs 25 and 28)
NS_Tokenomics / sim — v0.1, 2026-10-17

ALL INPUTS ARE ILLUSTRATIVE ASSUMPTIONS, to be re-tuned by Gus and Vagner (doc 28 §7 lists them).
This is a "what must be true" model, not a forecast and not an offer. Nothing here may be shown to
prospective investors as a promise of return.

What it does
  * One "series" = one project with its own money and its own investors (doc 28 §2).
  * Each year: revenue -> operating costs -> ground rent + regeneration royalty to the Foundation
    -> NetX management fee -> senior Green Notes (debt service) -> Regeneration Units (up to their
    CAP) -> First-loss units (junior, up to their target) -> residual: split between the commons
    (Foundation) and the units (upside share).
  * Caps are tracked with "hurdle accounts": each class has a balance that grows at its target or
    cap rate and shrinks with every distribution; when it reaches zero, the class is "full".
  * Scenario A: a 10 ha vineyard (wine sold from year 4). Scenario B: a 5 MW agrivoltaic plant.
  * Year H adds an exit value (exit_multiple x last year's operating cash).
  * Then: what USD 1,000 in units returns (cash or wine), and the "invest today, live here in
    10 years" journey.

Run: python3 sim/series_waterfall_sim.py > sim/RESULTS_series_waterfall.md   (stdlib only)
"""


def irr(cfs, lo=-0.99, hi=1.0):
    def npv(r):
        return sum(cf / (1 + r) ** t for t, cf in enumerate(cfs))
    if npv(lo) * npv(hi) > 0:
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def annuity(principal, rate, years):
    if years <= 0:
        return 0.0
    if rate == 0:
        return principal / years
    return principal * rate / (1 - (1 + rate) ** -years)


def run_series(p):
    """Return per-year rows and per-class cash flows (year 0 = investment)."""
    H = p["horizon"]
    raise_total = p["capex"]
    notes = raise_total * p["share_notes"]
    first_loss = raise_total * p["share_first_loss"]
    units = raise_total - notes - first_loss

    reserve = p.get("reserve", 0.0)   # part of the raise kept as cash for the years before revenue
    deficit = 0.0                     # unpaid shortfall once the reserve is used up
    un_acc = units                    # hurdle accounts
    fl_acc = first_loss
    note_bal = notes
    debt_service = annuity(notes, p["note_rate"], p["note_tenor"] - p["note_grace"])

    cf = dict(notes=[-notes], first_loss=[-first_loss], units=[-units], commons=[0.0], netx=[0.0])
    rows = []
    for t in range(1, H + 1):
        rev = p["revenue"](t)
        opex = p["opex"](t)
        to_foundation = p["ground_rent"] + p["royalty"] * rev
        fee = p["mgmt_fee"] * raise_total
        cash = rev - opex - to_foundation - fee
        exit_value = 0.0
        if t == H:
            cash += reserve       # what is left of the reserve is released at the end
            reserve = 0.0
            # exit: the remaining years of the series' surface right and project are sold to new
            # investors (or to the Mother Series) at a multiple of the last year's operating cash
            exit_value = p.get("exit_multiple", 0) * max(0.0, rev - opex - to_foundation - fee)
            cash += exit_value

        # Green Notes: interest-only during the grace years, then an annuity
        due = 0.0
        if note_bal > 1e-6:
            due = note_bal * p["note_rate"] if t <= p["note_grace"] else min(debt_service, note_bal * (1 + p["note_rate"]))
        cash -= due
        if t > p["note_grace"] and note_bal > 1e-6:
            note_bal = max(0.0, note_bal * (1 + p["note_rate"]) - due)

        # shortfalls: first the reserve, then a deficit that later years must repay
        if cash < 0:
            draw = min(reserve, -cash)
            reserve -= draw
            cash += draw
            deficit += -cash
            cash = 0.0
        else:
            refill = min(deficit, cash)
            deficit -= refill
            cash -= refill

        # Regeneration Units: senior equity, paid up to their CAP
        un_acc *= 1 + p["unit_cap"]
        pay_un = min(cash, un_acc)
        un_acc -= pay_un
        cash -= pay_un
        # First-loss: junior, paid after the units, up to its target
        fl_acc *= 1 + p["fl_target"]
        pay_fl = min(cash, fl_acc)
        fl_acc -= pay_fl
        cash -= pay_fl
        # Residual above both caps: mostly to the commons, a share to the units as an incentive
        up_units = cash * p["upside_share_units"]
        resid_commons = cash - up_units
        pay_un += up_units

        for k, v in (("notes", due), ("first_loss", pay_fl), ("units", pay_un),
                     ("commons", to_foundation + resid_commons), ("netx", fee)):
            cf[k].append(v)
        rows.append((t, rev, opex, to_foundation, fee, due, pay_un, pay_fl, resid_commons))
    cf["raise_total"] = raise_total
    cf["units_capital"] = units
    return rows, cf


# ------------------------------------------------------------------ Scenario A: vineyard
HA_VINE = 10
YIELD_T_HA = {1: 0, 2: 0, 3: 2, 4: 4, 5: 6}            # tonnes per ha; 7 from year 6
BOTTLES_PER_T = 750
PRICE_NET = 6.0          # USD per bottle received by the series (wholesale, ex-cellar)
VAR_COST = 2.5           # USD per bottle: custom winemaking, bottle, cork, label, freight
VINE_OPEX_HA = 6000      # USD per ha per year from year 1
RETAIL_VALUE = 14.0      # USD: what a bottle is worth to the investor who drinks it


def vine_tonnes(t):
    return YIELD_T_HA.get(t, 7) * HA_VINE


def vine_bottles_sold(t):
    # each vintage is sold the year after harvest (one year in barrel/bottle)
    return vine_tonnes(t - 1) * BOTTLES_PER_T if t >= 2 else 0


VINE = dict(
    name="A · Vineyard, 10 ha (wine from year 4)",
    horizon=15,
    capex=30000 * HA_VINE + 220000 + 50000,  # planting+irrigation+frost; working capital; permits/design
    reserve=220000,                          # covers the years before the first wine is sold
    exit_multiple=6,                         # vines keep producing for decades (surface right ≤50 y for plantations)
    revenue=lambda t: vine_bottles_sold(t) * PRICE_NET,
    opex=lambda t: VINE_OPEX_HA * HA_VINE + vine_bottles_sold(t) * VAR_COST,
    ground_rent=100 * HA_VINE,
    royalty=0.05,
    mgmt_fee=0.015,
    share_notes=0.0,          # a young vineyard can't carry debt
    share_first_loss=0.15,
    note_rate=0.0, note_tenor=0, note_grace=0,
    fl_target=0.04,
    unit_cap=0.09,
    upside_share_units=0.20,
)

# ------------------------------------------------------------------ Scenario B: agrivoltaics
MW = 5
SOLAR = dict(
    name="B · Agrivoltaics, 5 MW (power sold under a PPA)",
    horizon=20,
    capex=800000 * MW,
    revenue=lambda t: MW * 1900 * 60 * (0.995 ** (t - 1)),   # MWh/MW/yr x USD/MWh, 0.5%/yr degradation
    opex=lambda t: 15000 * MW + 10000,                        # O&M + vegetation care under panels
    ground_rent=100 * 12,                                     # ~12 ha
    royalty=0.05,
    mgmt_fee=0.01,
    share_notes=0.60,
    share_first_loss=0.10,
    note_rate=0.07, note_tenor=12, note_grace=1,
    fl_target=0.05,
    unit_cap=0.10,
    exit_multiple=3,          # ~5 more years of useful life after year 20
    upside_share_units=0.20,
)


def fmt(x):
    return f"{x:,.0f}"


def report(p):
    rows, cf = run_series(p)
    print(f"\n## {p['name']}\n")
    rt = cf["raise_total"]
    print(f"Raise: USD {fmt(rt)} = Green Notes {fmt(-cf['notes'][0])} + First-loss {fmt(-cf['first_loss'][0])}"
          f" + Regeneration Units {fmt(-cf['units'][0])}\n")
    print("| Year | Revenue | Op. costs | To Foundation (rent+royalty) | NetX fee | Notes | Units | First-loss | Residual to commons |")
    print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in rows:
        print("| " + " | ".join([str(r[0])] + [fmt(v) for v in r[1:]]) + " |")
    print()
    print("| Class | Paid in | Received | Multiple | IRR |")
    print("|---|---:|---:|---:|---:|")
    for k, label in [("notes", "Green Notes"), ("first_loss", "First-loss"), ("units", "Regeneration Units")]:
        c = cf[k]
        if c[0] == 0:
            continue
        got = sum(c[1:])
        print(f"| {label} | {fmt(-c[0])} | {fmt(got)} | {got / -c[0]:.2f}x | {irr(c):.1%} |")
    print(f"| **Foundation (commons)** | 0 | {fmt(sum(cf['commons']))} | — | — |")
    print(f"| NetX (fees) | 0 | {fmt(sum(cf['netx']))} | — | — |")
    return cf


def per_1000(cf, label):
    scale = 1000 / cf["units_capital"]
    flows = [v * scale for v in cf["units"]]
    print(f"\n### USD 1,000 in Regeneration Units of {label}\n")
    print("| Year | Cash to you (USD) |")
    print("|---:|---:|")
    for t, v in enumerate(flows):
        if t == 0:
            print(f"| 0 | {v:,.0f} (you invest) |")
        elif v > 0.5:
            print(f"| {t} | {v:,.0f} |")
    tot = sum(flows[1:])
    print(f"\nTotal received: **USD {tot:,.0f}** ({tot / 1000:.2f}x), IRR **{irr(flows):.1%}**.")
    return flows


def wine_path(flows):
    yearly = flows[1:-1]                  # years 1..14: distributions taken as bottles
    bottles = sum(yearly) / PRICE_NET
    final_cash = flows[-1]
    print("\n**Wine path** (you take years 1–14 of distributions as bottles at the series' price, "
          f"USD {PRICE_NET:.0f}, and year 15, including the exit, in cash): about **{bottles:,.0f} bottles**, "
          f"worth ~USD {bottles * RETAIL_VALUE:,.0f} at a retail value of USD {RETAIL_VALUE:.0f}, "
          f"plus USD {final_cash:,.0f} in year 15. Yield in kind is worth more to whoever drinks it "
          "than the same cash would be.")


def journey_live_here():
    print("\n## Journey: invest today, live here in 10 years\n")
    print("Accumulating units of the Mother Series (distributions reinvested). The net return is a "
          "parameter (blend of all series), not a forecast. The NAV in year 10 can pay the entry "
          "premium of a home surface right, on the same terms as anyone else, once housing is "
          "approved (no priority before approval: Ord. 173).\n")
    print("| Invested today | Net return | NAV in year 10 | Stay credits used meanwhile |")
    print("|---:|---:|---:|---|")
    for inv in (10000, 30000):
        for r in (0.03, 0.06, 0.09):
            print(f"| {inv:,} | {r:.0%} | {inv * (1 + r) ** 10:,.0f} | optional: part of the yield taken as stays |")


if __name__ == "__main__":
    print("# RESULTS — series waterfall (illustrative, not a forecast)\n")
    print("Generated by `sim/series_waterfall_sim.py`. Inputs are assumptions listed in doc 28 §7; "
          "re-tune them and re-run. Not an offer of securities.")
    cf_a = report(VINE)
    flows = per_1000(cf_a, "the vineyard series")
    wine_path(flows)
    cf_b = report(SOLAR)
    per_1000(cf_b, "the agrivoltaic series")
    journey_live_here()
