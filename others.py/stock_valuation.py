"""
Share viability calculator (NSE-style, KSh)

How to use
1. Edit the STOCKS list at the bottom (or run with --interactive to type figures in).
2. Run:  python stock_viability.py
3. Each stock gets its ratios, a score out of 100 and a plain verdict.

All money figures should be in the same unit (e.g. KSh millions) EXCEPT price,
EPS and DPS, which are per share in KSh. Shares outstanding is in millions
if your money figures are in millions.

Use TTM (trailing twelve month) profit where you can: last full-year profit
+ latest interim profit - same interim period of the prior year.
"""

from dataclasses import dataclass, field
import sys


# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------
@dataclass
class StockInput:
    name: str
    price: float                    # current share price, KSh
    shares_outstanding: float       # in millions (match your money unit)
    net_profit: float               # TTM profit attributable to shareholders
    shareholders_equity: float      # latest book equity
    total_assets: float
    total_debt: float = 0.0         # interest-bearing borrowings
    cash: float = 0.0
    revenue: float = 0.0
    dividend_per_share: float = 0.0  # last 12 months, KSh
    prior_net_profit: float = 0.0   # profit for the previous comparable period (for growth)
    prior_equity: float = 0.0       # opening equity, if you want ROE on average equity
    sector: str = "general"         # "general", "bank", "utility", "retail", ...


# Your own hurdle rates. Change to suit you.
HURDLE = {
    "earnings_yield": 0.12,   # want at least this (Kenya T-bill/bond yields set the floor)
    "roe": 0.15,
    "roi": 0.10,              # return on invested capital
    "pe_max": 10.0,
    "pb_max": 1.5,
    "dividend_yield": 0.05,
    "debt_to_equity_max": 1.0,
}


# ---------------------------------------------------------------------------
# Calculations
# ---------------------------------------------------------------------------
def safe_div(a, b):
    return a / b if b not in (0, None) else None


def calculate(s: StockInput) -> dict:
    market_cap = s.price * s.shares_outstanding
    eps = safe_div(s.net_profit, s.shares_outstanding)
    pe = safe_div(s.price, eps) if eps and eps > 0 else None
    earnings_yield = safe_div(s.net_profit, market_cap)
    book_value_ps = safe_div(s.shareholders_equity, s.shares_outstanding)
    pb = safe_div(s.price, book_value_ps) if book_value_ps and book_value_ps > 0 else None

    avg_equity = (
        (s.shareholders_equity + s.prior_equity) / 2 if s.prior_equity else s.shareholders_equity
    )
    roe = safe_div(s.net_profit, avg_equity)
    roa = safe_div(s.net_profit, s.total_assets)

    invested_capital = s.shareholders_equity + s.total_debt - s.cash
    roi = safe_div(s.net_profit, invested_capital)  # return on invested capital

    dividend_yield = safe_div(s.dividend_per_share, s.price)
    payout = safe_div(s.dividend_per_share, eps) if eps and eps > 0 else None
    net_margin = safe_div(s.net_profit, s.revenue) if s.revenue else None
    debt_to_equity = safe_div(s.total_debt, s.shareholders_equity)
    profit_growth = (
        safe_div(s.net_profit - s.prior_net_profit, abs(s.prior_net_profit))
        if s.prior_net_profit else None
    )
    peg = (
        safe_div(pe, profit_growth * 100)
        if pe and profit_growth and profit_growth > 0 else None
    )
    # Graham-style cross-check: price vs sqrt(22.5 * EPS * BVPS)
    graham = (
        (22.5 * eps * book_value_ps) ** 0.5
        if eps and book_value_ps and eps > 0 and book_value_ps > 0 else None
    )

    return {
        "market_cap": market_cap,
        "eps": eps,
        "pe": pe,
        "earnings_yield": earnings_yield,
        "book_value_ps": book_value_ps,
        "pb": pb,
        "roe": roe,
        "roa": roa,
        "roi": roi,
        "dividend_yield": dividend_yield,
        "payout": payout,
        "net_margin": net_margin,
        "debt_to_equity": debt_to_equity,
        "profit_growth": profit_growth,
        "peg": peg,
        "graham_value": graham,
    }


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------
def score(s: StockInput, r: dict):
    """Returns (score out of 100, list of notes). Simple, transparent weights."""
    pts, notes = 0, []
    h = HURDLE

    def check(label, value, passed, weight, fmt):
        nonlocal pts
        if value is None:
            notes.append(f"  ? {label}: not available")
            return
        if passed:
            pts += weight
        mark = "+" if passed else "-"
        notes.append(f"  {mark} {label}: {fmt(value)}")

    pct = lambda v: f"{v * 100:.1f}%"
    num = lambda v: f"{v:.2f}"

    check("Earnings yield (>= %.0f%%)" % (h["earnings_yield"] * 100), r["earnings_yield"],
          r["earnings_yield"] is not None and r["earnings_yield"] >= h["earnings_yield"], 25, pct)
    check("ROE (>= %.0f%%)" % (h["roe"] * 100), r["roe"],
          r["roe"] is not None and r["roe"] >= h["roe"], 15, pct)
    check("ROI / return on invested capital (>= %.0f%%)" % (h["roi"] * 100), r["roi"],
          r["roi"] is not None and r["roi"] >= h["roi"], 10, pct)
    check("P/E (<= %.0f)" % h["pe_max"], r["pe"],
          r["pe"] is not None and r["pe"] <= h["pe_max"], 15, num)
    check("P/B (<= %.1f)" % h["pb_max"], r["pb"],
          r["pb"] is not None and r["pb"] <= h["pb_max"], 10, num)
    check("Dividend yield (>= %.0f%%)" % (h["dividend_yield"] * 100), r["dividend_yield"],
          r["dividend_yield"] is not None and r["dividend_yield"] >= h["dividend_yield"], 10, pct)
    # Debt matters less for banks (deposits are not "debt" in this sense)
    if s.sector != "bank":
        check("Debt/equity (<= %.1f)" % h["debt_to_equity_max"], r["debt_to_equity"],
              r["debt_to_equity"] is not None and r["debt_to_equity"] <= h["debt_to_equity_max"],
              10, num)
    else:
        pts += 10
        notes.append("  ~ Debt/equity skipped for banks")
    check("Profit growth (> 0)", r["profit_growth"],
          r["profit_growth"] is not None and r["profit_growth"] > 0, 5, pct)

    return pts, notes


def verdict(pts):
    if pts >= 75:
        return "STRONG - passes most of your tests"
    if pts >= 55:
        return "DECENT - worth a closer look, check the failed tests"
    if pts >= 35:
        return "WEAK - several tests failed, needs a clear reason to buy"
    return "AVOID for now - fails most tests"


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def fmt(v, kind="num"):
    if v is None:
        return "n/a"
    if kind == "pct":
        return f"{v * 100:.1f}%"
    if kind == "money":
        return f"{v:,.0f}"
    return f"{v:,.2f}"


def report(s: StockInput):
    r = calculate(s)
    pts, notes = score(s, r)
    print("=" * 62)
    print(f"{s.name}   (price KSh {s.price:,.2f}, sector: {s.sector})")
    print("=" * 62)
    print(f"Market cap          : {fmt(r['market_cap'], 'money')}")
    print(f"EPS                 : {fmt(r['eps'])}")
    print(f"P/E                 : {fmt(r['pe'])}")
    print(f"Earnings yield      : {fmt(r['earnings_yield'], 'pct')}")
    print(f"Book value / share  : {fmt(r['book_value_ps'])}")
    print(f"P/B                 : {fmt(r['pb'])}")
    print(f"ROE                 : {fmt(r['roe'], 'pct')}")
    print(f"ROA                 : {fmt(r['roa'], 'pct')}")
    print(f"ROI (invested cap.) : {fmt(r['roi'], 'pct')}")
    print(f"Dividend yield      : {fmt(r['dividend_yield'], 'pct')}")
    print(f"Payout ratio        : {fmt(r['payout'], 'pct')}")
    print(f"Net margin          : {fmt(r['net_margin'], 'pct')}")
    print(f"Debt / equity       : {fmt(r['debt_to_equity'])}")
    print(f"Profit growth       : {fmt(r['profit_growth'], 'pct')}")
    print(f"PEG                 : {fmt(r['peg'])}")
    print(f"Graham value (KSh)  : {fmt(r['graham_value'])}"
          + (f"  (price is {'below' if s.price < r['graham_value'] else 'above'} it)"
             if r["graham_value"] else ""))
    print("-" * 62)
    print("Tests:")
    print("\n".join(notes))
    print("-" * 62)
    print(f"Score: {pts}/100 -> {verdict(pts)}")
    if s.sector == "bank":
        print("Note: for banks, lean on earnings yield, ROE, P/B and NPLs. ROA/ROI look low by design.")
    if s.sector in ("utility", "energy"):
        print("Note: utilities carry heavy debt and big asset bases; "
              "check debt cover and tariff/regulatory risk, and expect lower ROE.")
    print()
    return r, pts


def compare(stocks):
    results = [(s, *report(s)) for s in stocks]
    if len(results) > 1:
        print("=" * 62)
        print("SIDE BY SIDE")
        print("=" * 62)
        header = f"{'Stock':<14}{'Yield':>8}{'P/E':>7}{'P/B':>7}{'ROE':>8}{'ROI':>8}{'Div':>7}{'Score':>7}"
        print(header)
        for s, r, pts in sorted(results, key=lambda x: -x[2]):
            print(
                f"{s.name[:13]:<14}"
                f"{fmt(r['earnings_yield'], 'pct'):>8}"
                f"{fmt(r['pe']):>7}"
                f"{fmt(r['pb']):>7}"
                f"{fmt(r['roe'], 'pct'):>8}"
                f"{fmt(r['roi'], 'pct'):>8}"
                f"{fmt(r['dividend_yield'], 'pct'):>7}"
                f"{pts:>7}"
            )
        print()


# ---------------------------------------------------------------------------
# Interactive entry
# ---------------------------------------------------------------------------
def ask(prompt, default=0.0, cast=float):
    raw = input(f"{prompt} [{default}]: ").strip()
    return cast(raw) if raw else default


def interactive():
    stocks = []
    while True:
        name = input("Stock name (blank to finish): ").strip()
        if not name:
            break
        stocks.append(StockInput(
            name=name,
            price=ask("Share price (KSh)"),
            shares_outstanding=ask("Shares outstanding (millions)"),
            net_profit=ask("TTM net profit"),
            shareholders_equity=ask("Shareholders' equity"),
            total_assets=ask("Total assets"),
            total_debt=ask("Total interest-bearing debt"),
            cash=ask("Cash"),
            revenue=ask("Revenue (TTM)"),
            dividend_per_share=ask("Dividend per share, last 12m (KSh)"),
            prior_net_profit=ask("Prior comparable period net profit"),
            prior_equity=ask("Opening/prior equity (0 to skip)"),
            sector=ask("Sector (general/bank/utility/retail)", "general", str),
        ))
    return stocks


# ---------------------------------------------------------------------------
# EDIT THESE: replace the placeholder numbers with your own figures.
# The numbers below are DUMMY values just to show the layout. They are not
# real Quick Mart or KenGen financials.
# ---------------------------------------------------------------------------
STOCKS = [
    StockInput(
        name="KenGen (EDIT ME)",
        sector="utility",
        price=10.0,
        shares_outstanding=6600,       # millions
        net_profit=12000,              # KSh millions, TTM
        shareholders_equity=190000,
        total_assets=400000,
        total_debt=120000,
        cash=10000,
        revenue=40000,
        dividend_per_share=0.3,
        prior_net_profit=9000,
        prior_equity=180000,
    ),
    StockInput(
        name="Quick Mart (EDIT ME)",
        sector="retail",
        price=7.5,
        shares_outstanding=400000000000,
        net_profit=1500000000,
        shareholders_equity=6000,
        total_assets=15000,
        total_debt=2000,
        cash=800,
        revenue=40000,
        dividend_per_share=0.5,
        prior_net_profit=1000,
        prior_equity=5500,
    ),
]


if __name__ == "__main__":
    data = interactive() if "--interactive" in sys.argv else STOCKS
    if not data:
        print("No stocks entered.")
    else:
        compare(data)