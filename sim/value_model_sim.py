"""
Investor value model — RAIZ (utility) vs Lighthouse fideicomiso units (real-estate) vs benchmarks
NS_Tokenomics / sim — v0.1, 2026-10-02

ALL INPUTS ARE ILLUSTRATIVE ASSUMPTIONS (sources/logic listed in 09 - Investor Value Model.md).
This is a "what must be true" model, not a forecast and not an offer. Nothing here may be shown to
prospective buyers as a promise of return (see 06 - Legal Friction Map, L2/L19).

Part A — RAIZ as a TDF-style, capacity-backed utility token
  * Each RAIZ (phase-3 form) entitles 1 stay-night/year (+ utility fee) and a share of community
    product "airdrops" (vouchers committed to the Commons Pool). Supply capped by built capacity.
  * Price follows a rational bonding curve (OASA/TDF style): p(s) = pmax - (pmax - p0) / (1 + s/k)
  * We compute (1) in-kind "consumption yield" for a holder who uses the entitlement,
    (2) curve price path as capacity is built (what a later buyer pays),
    (3) an "economic IRR" for a holder who uses X% of the entitlement and (if legal rails exist)
        exits at curve price in year 10.

Part B — Lighthouse fideicomiso units (land never sold; income from licences/tariffs)
  * Investors fund infrastructure; BioPueblo contributes the DRS in kind; income from community
    licences (derecho de uso / canon), productive leases, infra tariffs and hospitality share.
  * Exit by cession of units at year 15 at NAV = net distributable income / cap rate.

Run: python3 value_model_sim.py   (stdlib only)
"""
import math

# ---------------------------------------------------------------- helpers
def irr(cfs, lo=-0.99, hi=1.5):
    def npv(r):
        return sum(cf / (1 + r) ** t for t, cf in enumerate(cfs))
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if f_lo * f_mid <= 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def pct(x):
    return "n/a" if x != x else f"{x*100:.1f}%"


def usd(x):
    return f"{x:,.0f}"


# ---------------------------------------------------------------- Part A: RAIZ
RAIZ = {
    "conservative": dict(p0=250, pmax=420, night_value=60, night_growth=0.02, utility_fee=18,
                         airdrop_y1=5, airdrop_growth=0.10, beds_2035=120, use_rate=0.35, start_year=3),
    "base":         dict(p0=250, pmax=500, night_value=80, night_growth=0.03, utility_fee=15,
                         airdrop_y1=10, airdrop_growth=0.15, beds_2035=250, use_rate=0.50, start_year=2),
    "upside":       dict(p0=250, pmax=650, night_value=110, night_growth=0.04, utility_fee=15,
                         airdrop_y1=15, airdrop_growth=0.20, beds_2035=400, use_rate=0.65, start_year=2),
}
YEARS = 10


def curve_price(s, p0, pmax, k):
    return pmax - (pmax - p0) / (1 + s / k)


def run_raiz(p):
    cap = p["beds_2035"] * 365            # supply cap = bed-nights/yr at full build (TDF logic)
    k = cap / 3                            # curve steepness (price ~ midpoint at 1/3 of cap)
    rows, cfs = [], [-p["p0"]]             # one RAIZ bought at hatch price p0 (year 0)
    for t in range(1, YEARS + 1):
        built_share = min(1.0, t / YEARS)  # capacity built linearly to year 10
        supply_sold = cap * built_share * 0.9
        price_t = curve_price(supply_sold, p["p0"], p["pmax"], k)
        night = p["night_value"] * (1 + p["night_growth"]) ** t
        airdrop = p["airdrop_y1"] * (1 + p["airdrop_growth"]) ** (t - 1)
        stay_value = max(0.0, night - p["utility_fee"]) if t >= p["start_year"] else 0.0
        full_value = stay_value + airdrop
        realised = stay_value * p["use_rate"] + airdrop
        cf = realised + (price_t if t == YEARS else 0)
        cfs.append(cf)
        rows.append((t, price_t, full_value, full_value / p["p0"], realised))
    return rows, cfs, irr(cfs), irr([-p["p0"]] + [r[4] for r in rows])  # with exit, use-only


# ---------------------------------------------------------------- Part B: fideicomiso units
FIDEI = {
    "conservative": dict(cash_invest=6_000_000, land_inkind=4_000_000, settle_ha=70, settle_canon=8_000,
                         prod_ha=530, prod_canon=100, residents=700, tariff_margin=150, hosp=50_000,
                         opex_ratio=0.40, ramp_years=10, cap_rate=0.09, entry_uplift=0.0),
    "base":         dict(cash_invest=6_000_000, land_inkind=4_000_000, settle_ha=70, settle_canon=12_000,
                         prod_ha=530, prod_canon=150, residents=1000, tariff_margin=250, hosp=100_000,
                         opex_ratio=0.35, ramp_years=8, cap_rate=0.08, entry_uplift=0.0),
    "upside":       dict(cash_invest=6_000_000, land_inkind=4_000_000, settle_ha=70, settle_canon=18_000,
                         prod_ha=530, prod_canon=200, residents=1200, tariff_margin=350, hosp=200_000,
                         opex_ratio=0.30, ramp_years=7, cap_rate=0.07, entry_uplift=0.0),
}
EXIT_YEAR = 15


def run_fidei(p, with_uplift=None):
    investor_share = p["cash_invest"] / (p["cash_invest"] + p["land_inkind"])
    cfs = [-p["cash_invest"]]
    income_mature = 0
    for t in range(1, EXIT_YEAR + 1):
        ramp = min(1.0, t / p["ramp_years"])
        gross = (p["settle_ha"] * p["settle_canon"] + p["prod_ha"] * p["prod_canon"]
                 + p["residents"] * p["tariff_margin"] + p["hosp"]) * ramp
        net = gross * (1 - p["opex_ratio"])
        dist = net * investor_share
        income_mature = net
        cf = dist
        if t == EXIT_YEAR:
            nav_total = net / p["cap_rate"]
            cf += nav_total * investor_share
        cfs.append(cf)
    return income_mature, investor_share, irr(cfs)


def main():
    print("## Part A — RAIZ (TDF-style utility, phase-3 form)\n")
    print("Per 1 RAIZ bought at the hatch price. 'Full in-kind value' = market value of the yearly night minus utility fee, plus community airdrops.\n")
    print("| Scenario | Yr-5 full in-kind value | Yr-5 consumption yield on hatch price | Yr-10 curve price | Use-only IRR (realised use) | IRR use + exit at curve (yr 10) |")
    print("|---|---:|---:|---:|---:|---:|")
    for name, p in RAIZ.items():
        rows, cfs, irr_exit, irr_use = run_raiz(p)
        y5 = rows[4]
        y10 = rows[9]
        print(f"| {name} | {usd(y5[2])} | {pct(y5[3])} | {usd(y10[1])} | {pct(irr_use)} | {pct(irr_exit)} |")

    print("\n### Base scenario, year by year (1 RAIZ)\n")
    rows, *_ = run_raiz(RAIZ["base"])
    print("| Year | Curve price (what a new buyer pays) | Full in-kind value | Consumption yield on hatch price | Realised value at 50% use |")
    print("|---:|---:|---:|---:|---:|")
    for t, price, full, cy, real in rows:
        print(f"| {t} | {usd(price)} | {usd(full)} | {pct(cy)} | {usd(real)} |")

    print("\n## Part B — Lighthouse fideicomiso units (land never sold)\n")
    print(f"Investors put cash for infrastructure; BioPueblo contributes the DRS in kind; exit by cession of units in year {EXIT_YEAR} at NAV = net income / cap rate.\n")
    print("| Scenario | Net income at maturity (USD/yr, whole trust) | Investor share | Investor IRR (15y, exit at NAV) |")
    print("|---|---:|---:|---:|")
    for name, p in FIDEI.items():
        inc, share, r = run_fidei(p)
        print(f"| {name} | {usd(inc)} | {pct(share)} | {pct(r)} |")

    print("\n### What must be true to reach a family-office hurdle? (base scenario, vary settlement canon & cap rate)\n")
    print("| Settlement licence canon (USD/ha/yr) | Exit cap rate 9% | 8% | 7% |")
    print("|---:|---:|---:|---:|")
    for canon in (8_000, 12_000, 18_000, 25_000, 35_000):
        cells = []
        for cr in (0.09, 0.08, 0.07):
            p = dict(FIDEI["base"], settle_canon=canon, cap_rate=cr)
            cells.append(pct(run_fidei(p)[2]))
        print(f"| {usd(canon)} | " + " | ".join(cells) + " |")

    print("\n### Lever: entry below value (approval uplift) — investors' cash buys units at a discount to post-approval NAV\n")
    print("| Discount at entry vs. post-approval value | Base investor IRR |")
    print("|---:|---:|")
    for disc in (0.0, 0.15, 0.30, 0.45):
        p = dict(FIDEI["base"], cash_invest=FIDEI["base"]["cash_invest"] * (1 - disc))
        # same economic share as before (the discount is the early-entry reward)
        base_share = FIDEI["base"]["cash_invest"] / (FIDEI["base"]["cash_invest"] + FIDEI["base"]["land_inkind"])
        cfs = [-p["cash_invest"]]
        for t in range(1, EXIT_YEAR + 1):
            ramp = min(1.0, t / p["ramp_years"])
            gross = (p["settle_ha"] * p["settle_canon"] + p["prod_ha"] * p["prod_canon"]
                     + p["residents"] * p["tariff_margin"] + p["hosp"]) * ramp
            net = gross * (1 - p["opex_ratio"])
            cf = net * base_share + ((net / p["cap_rate"]) * base_share if t == EXIT_YEAR else 0)
            cfs.append(cf)
        print(f"| {disc*100:.0f}% | {pct(irr(cfs))} |")


if __name__ == "__main__":
    main()
