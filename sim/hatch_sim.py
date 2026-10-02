"""
Hatch simulation — Lighthouse Founding Pass (RAIZ v0)
NS_Tokenomics / sim — v0.1, 2026-10-02

Purpose (Zargham/McConaghy lens): make the trade-off between what we RAISE and what we PROMISE explicit
before any number goes into a deck. All figures are ILLUSTRATIVE ASSUMPTIONS, not a forecast.

Model (deliberately simple, stdlib only, deterministic + a small Monte Carlo on uptake):
- Passes are sold in three tiers. Each pass returns a share of its price as Commons Credits
  (credit_ratio), spread over `credit_years`, redeemable for community goods/services.
- Honouring a credit costs the Commons Fund `cash_cost_per_credit` (communities must be paid partly
  in cash for inputs/labour; the rest is absorbed as their in-kind commitment to the pool).
- Of what's left after the credit liability is provisioned, the raise is split into buckets.
- Checks: I2 (credits <= k * pool capacity) and I3 (reserve >= 3 months commons opex).

Run:  python3 hatch_sim.py   -> prints markdown tables (copied into RESULTS.md)
"""
import random

TIERS = {           # price USD, scenario counts (low, base, high)
    "Seed":     (300,  (60, 150, 300)),
    "Steward":  (1500, (25, 60, 120)),
    "Guardian": (5000, (5, 15, 30)),
}
SCENARIOS = ("low", "base", "high")

PARAMS = dict(
    credit_ratio=0.30,          # 30% of price comes back as Commons Credits
    credit_years=3,
    redemption_rate=0.75,       # share of issued credits actually redeemed
    cash_cost_per_credit=0.50,  # Commons Fund pays 50c cash per 1 credit redeemed
    platform_and_legal_setup=25_000,  # USD one-off: association setup, counsel, KYC, audit (assumption)
    commons_opex_month=6_000,   # USD/month: stewarding, admin, insurance, MRV (assumption)
    pool_capacity_year=40_000,  # USD/yr of goods/services communities commit to the pool in yr 1 (assumption)
    k_backing=0.8,
    buckets={  # split of NET commons capital
        "Commons bootstrap (water, nursery, seed bank, kitchen)": 0.50,
        "Community incubation grants (allocation rounds)": 0.20,
        "Reserve (I3)": 0.20,
        "Stewardship ops runway": 0.10,
    },
)


def run(counts, p):
    gross = sum(price * n for (price, _), n in zip(TIERS.values(), counts))
    credits_issued = gross * p["credit_ratio"]
    credits_per_year = credits_issued / p["credit_years"]
    expected_cash_cost = credits_issued * p["redemption_rate"] * p["cash_cost_per_credit"]
    net = gross - expected_cash_cost - p["platform_and_legal_setup"]
    buckets = {k: net * v for k, v in p["buckets"].items()}
    reserve = buckets["Reserve (I3)"]
    months_reserve = reserve / p["commons_opex_month"]
    i2_ok = credits_per_year <= p["k_backing"] * p["pool_capacity_year"]
    i3_ok = months_reserve >= 3
    return dict(gross=gross, credits_issued=credits_issued, credits_per_year=credits_per_year,
                cash_cost=expected_cash_cost, net=net, buckets=buckets, months_reserve=months_reserve,
                i2_ok=i2_ok, i3_ok=i3_ok, holders=sum(counts))


def usd(x):
    return f"{x:,.0f}"


def main():
    p = PARAMS
    print("## 1. Scenarios (credit_ratio = 30%)\n")
    print("| Scenario | Holders | Gross raise | Credits issued | Credits/yr | Expected cash cost of credits | Net commons capital | Reserve months | I2 backing | I3 reserve |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|:-:|:-:|")
    for i, s in enumerate(SCENARIOS):
        counts = [v[1][i] for v in TIERS.values()]
        r = run(counts, p)
        print(f"| {s} | {r['holders']} | {usd(r['gross'])} | {usd(r['credits_issued'])} | {usd(r['credits_per_year'])} | "
              f"{usd(r['cash_cost'])} | {usd(r['net'])} | {r['months_reserve']:.1f} | {'✅' if r['i2_ok'] else '❌'} | {'✅' if r['i3_ok'] else '❌'} |")

    print("\n## 2. Base scenario — use of net commons capital\n")
    base = run([v[1][1] for v in TIERS.values()], p)
    print("| Bucket | USD | % |")
    print("|---|---:|---:|")
    for k, v in base["buckets"].items():
        print(f"| {k} | {usd(v)} | {p['buckets'][k]*100:.0f}% |")

    print("\n## 3. Sweep — how generous can credits be? (base uptake)\n")
    print("| Credit ratio | Credits/yr | Pool capacity needed for I2 (USD/yr) | Net commons capital | I2 with 40k/yr pool |")
    print("|---:|---:|---:|---:|:-:|")
    for cr in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        q = dict(p, credit_ratio=cr)
        r = run([v[1][1] for v in TIERS.values()], q)
        need = r["credits_per_year"] / p["k_backing"]
        print(f"| {cr*100:.0f}% | {usd(r['credits_per_year'])} | {usd(need)} | {usd(r['net'])} | {'✅' if r['i2_ok'] else '❌'} |")

    print("\n## 4. Monte Carlo on uptake (2,000 runs, each tier ~ uniform between low and high)\n")
    random.seed(7)
    nets, fails_i2, fails_i3 = [], 0, 0
    for _ in range(2000):
        counts = [random.randint(v[1][0], v[1][2]) for v in TIERS.values()]
        r = run(counts, p)
        nets.append(r["net"])
        fails_i2 += not r["i2_ok"]
        fails_i3 += not r["i3_ok"]
    nets.sort()
    pct = lambda q: nets[int(q * (len(nets) - 1))]
    print("| Metric | Value |")
    print("|---|---:|")
    print(f"| Net commons capital P10 | {usd(pct(0.10))} |")
    print(f"| Net commons capital P50 | {usd(pct(0.50))} |")
    print(f"| Net commons capital P90 | {usd(pct(0.90))} |")
    print(f"| Runs breaking I2 (credits > 80% of pool capacity) | {fails_i2/20:.1f}% |")
    print(f"| Runs breaking I3 (reserve < 3 months opex) | {fails_i3/20:.1f}% |")


if __name__ == "__main__":
    main()
