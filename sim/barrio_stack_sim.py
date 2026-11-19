"""
Barrio stack model — one neighbourhood trust with three instruments:
  Token Tierra   = a lot paid in instalments (Juanpi, call 2026-11-16)
  Token Inversor = money lent to the neighbourhood trust for infrastructure, paid back with a premium (Juanpi, same call)
  FARO           = the commons membership; it receives a toll on every payment and yearly dues (Gus, slides 2026-11-09)
NS_Tokenomics / sim — v0.1, 2026-11-19

ALL INPUTS ARE PLACEHOLDERS. "What must be true" model, not a forecast, an offer or a price list.
Context, the proposal and the rules it touches: docs 32 and 34.

The question: can the lots of ONE neighbourhood pay back the people who financed its infrastructure,
and what does the commons receive on the way?

Reused from sim/lot_sale_sim.py (all [criterio] or [NC] there): lot price, infrastructure per lot,
owner's share, broker, NetX contract, commons contribution, yearly dues.
New here, all [criterio] unless noted: number of lots (21, slides of 2026-11-09), contingency, set-up cost,
down payment, instalment lengths, sales pace, the 10% yearly premium (Juanpi's example in the call).

Run: python3 sim/barrio_stack_sim.py > sim/RESULTS_barrio_stack.md   (stdlib only)
"""

from lot_sale_sim import (CONTRIBUTION, DUES, INFRA_PER_LOT, LOT_HIGH, LOT_MID, NETX_FEE,
                          OWNER_SHARE, SELLING_COST)

VERSION = "0.1"
DATE = "2026-11-19"

LOTS = 21                 # northern sector, slides of 2026-11-09 [S]
CONTINGENCY = 0.10        # on infrastructure [criterio]
SETUP_COST = 40_000       # trust, fiduciary, legal, tokenisation rail, one-off [criterio]; no quote
PREMIUM = 0.10            # per year, simple, on the Token Inversor [Juanpi's example, call 2026-11-16]
DOWN_PAYMENT = 0.20       # share of the lot price paid when the plan starts [criterio]
PLANS = (0, 12, 24, 36)   # instalment months; 0 = paid in full at once [criterio]
PACES = (1, 2, 3, 5)      # lots sold per quarter [criterio]
MATURITIES = (12, 24, 36) # months until the Token Inversor is bought back [12 is Juanpi's example]
LOT_PRICES = (LOT_MID, LOT_HIGH, 60_000)  # 60k is a test value above the reported range [criterio]
BASE_PACE, BASE_PLAN = 2, 24
HORIZON = 72              # months simulated
NET_SHARE = 1 - OWNER_SHARE - SELLING_COST - NETX_FEE - CONTRIBUTION  # what the trust keeps of each USD paid


def raise_needed():
    return LOTS * INFRA_PER_LOT * (1 + CONTINGENCY) + SETUP_COST


def collections(pace, plan, price=LOT_MID):
    """USD paid by lot buyers in each month (index 0..HORIZON). Lots sell at the start of each quarter."""
    paid = [0.0] * (HORIZON + 1)
    sold = 0
    month = 0
    while sold < LOTS and month <= HORIZON:
        batch = min(pace, LOTS - sold)
        if plan == 0:
            paid[month] += batch * price
        else:
            paid[month] += batch * price * DOWN_PAYMENT
            instalment = price * (1 - DOWN_PAYMENT) / plan
            for m in range(month + 1, min(month + plan, HORIZON) + 1):
                paid[m] += batch * instalment
        sold += batch
        month += 3
    return paid


def coverage(pace, plan, maturity, price=LOT_MID):
    """Cash the trust has at maturity, divided by what it owes on a single buy-back date."""
    cash = sum(collections(pace, plan, price)[:maturity + 1]) * NET_SHARE
    due = raise_needed() * (1 + PREMIUM * maturity / 12)
    return cash / due


def pass_through(pace, plan, price=LOT_MID):
    """Pay investors as lot money arrives: premium on what is still owed first, then principal.
    Returns (month fully repaid or None, total paid, left in the trust at the end)."""
    owed = raise_needed()
    accrued = 0.0
    total = 0.0
    left = 0.0
    done = None
    for month, paid in enumerate(collections(pace, plan, price)):
        if done is None and month > 0:
            accrued += owed * PREMIUM / 12
        cash = paid * NET_SHARE
        if done is None:
            pay_premium = min(cash, accrued)
            accrued -= pay_premium
            cash -= pay_premium
            pay_principal = min(cash, owed)
            owed -= pay_principal
            cash -= pay_principal
            total += pay_premium + pay_principal
            if owed < 0.5 and accrued < 0.5:
                done = month
        left += cash
    return done, total, left


def commons_by_year(pace, plan, price=LOT_MID):
    """Toll on lot payments and dues from sold lots, per year, for 6 years."""
    paid = collections(pace, plan, price)
    rows = []
    for year in range(1, 7):
        start, end = (year - 1) * 12, year * 12
        toll = sum(paid[start + (1 if year > 1 else 0):end + 1]) * CONTRIBUTION
        sold = min(LOTS, pace * ((end // 3) + 1)) if end <= HORIZON else LOTS
        sold_mid = min(LOTS, pace * (((start + end) // 2) // 3 + 1))
        rows.append((year, toll, sold_mid * DUES, sold))
    return rows


def pct(x):
    return f"{x * 100:.0f}%"


def usd(x):
    return f"{x:,.0f}"


def main():
    need = raise_needed()
    print("# RESULTS — barrio stack model (placeholders, not a forecast or an offer)\n")
    print(f"Generated by `sim/barrio_stack_sim.py` v{VERSION}, {DATE}. Proposal and context: docs 32 and 34. "
          "Inputs reused from `sim/lot_sale_sim.py` are [criterio] or [NC] there; the 10% premium is "
          "Juanpi's example in the call of 2026-11-16; everything else is a placeholder [criterio].\n")

    print("## 1. The neighbourhood in numbers\n")
    print("| Item | Value |")
    print("|---|---:|")
    print(f"| Lots | {LOTS} |")
    print(f"| Lot price, middle of the reported range (USD) | {usd(LOT_MID)} |")
    print(f"| Infrastructure per lot (USD) | {usd(INFRA_PER_LOT)} |")
    print(f"| Contingency on infrastructure | {pct(CONTINGENCY)} |")
    print(f"| Set-up cost of the trust and the rail (USD) | {usd(SETUP_COST)} |")
    print(f"| **Money the Token Inversor has to bring (USD)** | **{usd(need)}** |")
    print(f"| Of each USD a buyer pays: owner {pct(OWNER_SHARE)}, broker {pct(SELLING_COST)}, "
          f"NetX contract {pct(NETX_FEE)} [verify], commons {pct(CONTRIBUTION)} | trust keeps {pct(NET_SHARE)} |")
    print()

    print("## 2. Is there enough money at all? (every lot sold and fully paid)\n")
    print("What the trust keeps from all the lots, against what it owes if it buys the Token Inversor back "
          f"with {pct(PREMIUM)} a year.\n")
    print("| Lot price (USD) | Trust keeps, all lots (USD) | Owed at 12 months | Owed at 24 months | Owed at 36 months | Left after a 24-month buy-back (USD) |")
    print("|---:|---:|---:|---:|---:|---:|")
    for price in LOT_PRICES:
        keeps = LOTS * price * NET_SHARE
        dues = [need * (1 + PREMIUM * m / 12) for m in MATURITIES]
        print(f"| {usd(price)} | {usd(keeps)} | {usd(dues[0])} | {usd(dues[1])} | {usd(dues[2])} | {usd(keeps - dues[1])} |")
    breakeven = need * (1 + PREMIUM * 2) / (LOTS * NET_SHARE)
    print(f"\nLot price at which all the lots just cover a 24-month buy-back: USD {usd(breakeven)}. "
          "Houses are left out: each family pays for its own.\n")

    print("## 3. Is the money there on the buy-back date?\n")
    print("Cash in the trust on the date, divided by what it owes. 100% or more means it can pay. "
          f"Lots at USD {usd(LOT_MID)}, down payment {pct(DOWN_PAYMENT)}.\n")
    for maturity in MATURITIES:
        print(f"**Buy-back at {maturity} months**\n")
        print("| Lots sold per quarter | Paid at once | 12 instalments | 24 instalments | 36 instalments |")
        print("|---:|---:|---:|---:|---:|")
        for pace in PACES:
            cells = " | ".join(pct(coverage(pace, plan, maturity)) for plan in PLANS)
            print(f"| {pace} | {cells} |")
        print()

    print("## 4. The alternative: pay investors as the lot money arrives\n")
    print(f"No fixed buy-back date. Each month the trust pays the {pct(PREMIUM)} yearly premium on what it "
          "still owes, then principal. The table shows the month in which investors are fully paid.\n")
    for price in LOT_PRICES[:2]:
        print(f"**Lots at USD {usd(price)}**\n")
        print("| Lots sold per quarter | Paid at once | 12 instalments | 24 instalments | 36 instalments |")
        print("|---:|---:|---:|---:|---:|")
        for pace in PACES:
            cells = []
            for plan in PLANS:
                done, _total, _left = pass_through(pace, plan, price)
                cells.append("not in 6 years" if done is None else f"month {done}")
            print(f"| {pace} | {' | '.join(cells)} |")
        print()
    done, total, left = pass_through(BASE_PACE, BASE_PLAN)
    if done is None:
        print(f"Base case ({BASE_PACE} lots per quarter, {BASE_PLAN} instalments, USD {usd(LOT_MID)}): "
              f"investors receive USD {usd(total)} of the USD {usd(need)} they put in, plus nothing left "
              "for the trust: the lots don't cover it.\n")
    else:
        print(f"Base case ({BASE_PACE} lots per quarter, {BASE_PLAN} instalments, USD {usd(LOT_MID)}): "
              f"investors put in USD {usd(need)} and receive USD {usd(total)} by month {done}; "
              f"USD {usd(left)} is left in the trust.\n")

    print("## 5. What the commons receives on the way\n")
    print(f"Base case: {BASE_PACE} lots per quarter, {BASE_PLAN} instalments, lots at USD {usd(LOT_MID)}, "
          f"toll {pct(CONTRIBUTION)} of every payment, dues USD {usd(DUES)} per sold lot per year. "
          "Lots only: houses would add to the toll if it applies to them.\n")
    print("| Year | Toll on lot payments (USD) | Dues (USD) | Total (USD) | Lots sold by year end |")
    print("|---:|---:|---:|---:|---:|")
    for year, toll, dues, sold in commons_by_year(BASE_PACE, BASE_PLAN):
        print(f"| {year} | {usd(toll)} | {usd(dues)} | {usd(toll + dues)} | {sold} |")
    total_toll = LOTS * LOT_MID * CONTRIBUTION
    print(f"\nThe toll adds up to USD {usd(total_toll)} once; dues settle at USD {usd(LOTS * DUES)} a year. "
          "Against a commons budget of USD 72,000 a year (`sim/RESULTS.md`), lots alone cover about "
          f"{pct(LOTS * DUES / 72_000)} once the sale ends.\n")

    print("## 6. What must be true\n")
    print("1. The lot price, the owner's share or the infrastructure cost has to move: at the middle of the "
          "reported range the lots of the neighbourhood barely cover the money that built it.")
    print("2. A single buy-back date at 12 months doesn't fit lots sold in instalments: the trust owes the "
          "money before the buyers have paid it.")
    print("3. Paying investors as the lot money arrives removes the date risk; what is left is the sales risk.")
    print("4. The commons can't live on lots: the toll comes once and dues are small. It needs its own income "
          "(stays, kitchen, workshops, dues from more neighbourhoods).")


if __name__ == "__main__":
    main()
