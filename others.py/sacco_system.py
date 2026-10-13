"""
SACCO loan tracker - version 2 (with Rima loan products).

Loan products
  school       18% reducing balance, up to 12 months
  development  12% reducing balance, up to 24 months
               (both): upfront deductions = 2% processing + 2.5% risk + KES 500 legal fee
  instant      up to KES 5,000, 10% interest deducted upfront, KES 100 form fee, due in 1 month
  vuka         Vuka na Rima, up to KES 20,000, 10% interest deducted upfront,
               KES 100 form fee, due in 1 month
  (instant & vuka): if unpaid after the due date, 10% penalty on the remaining balance

Run:  python sacco_loans.py demo
      python sacco_loans.py quote school 50000 12
      python sacco_loans.py alerts          (run daily, e.g. Windows Task Scheduler)
"""
import sqlite3
import sys
from datetime import date, timedelta
from calendar import monthrange

DB = "sacco.db"
REMIND_DAYS_BEFORE = 3       # warn this many days before the due date
GRACE_DAYS = 0               # days after due date before it counts as missed / penalty applies

PRODUCTS = {
    "school": dict(label="School loan", rate=18, max_months=12, max_amount=None,
                   upfront_interest=False, processing_pct=2, risk_pct=2.5,
                   legal_fee=500, form_fee=0, penalty_pct=0),
    "development": dict(label="Development loan", rate=12, max_months=24, max_amount=None,
                        upfront_interest=False, processing_pct=2, risk_pct=2.5,
                        legal_fee=500, form_fee=0, penalty_pct=0),
    "instant": dict(label="Instant loan", rate=10, max_months=1, max_amount=5000,
                    upfront_interest=True, processing_pct=0, risk_pct=0,
                    legal_fee=0, form_fee=100, penalty_pct=10),
    "vuka": dict(label="Vuka na Rima", rate=10, max_months=1, max_amount=20000,
                 upfront_interest=True, processing_pct=0, risk_pct=0,
                 legal_fee=0, form_fee=100, penalty_pct=10),
}


# ---------- database ----------
def connect():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.executescript("""
    CREATE TABLE IF NOT EXISTS members(
        id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT);
    CREATE TABLE IF NOT EXISTS loans(
        id INTEGER PRIMARY KEY, member_id INTEGER, product TEXT, principal REAL,
        annual_rate REAL, months INTEGER, start_date TEXT, instalment REAL,
        processing_fee REAL, risk_fee REAL, legal_fee REAL, form_fee REAL,
        upfront_interest REAL, net_disbursed REAL);
    CREATE TABLE IF NOT EXISTS schedule(
        id INTEGER PRIMARY KEY, loan_id INTEGER, no INTEGER, due_date TEXT,
        principal_part REAL, interest_part REAL, amount_due REAL,
        amount_paid REAL DEFAULT 0, penalty REAL DEFAULT 0, last_alert TEXT);
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY, loan_id INTEGER, paid_on TEXT,
        amount REAL, reference TEXT);
    """)
    cols = [r["name"] for r in con.execute("PRAGMA table_info(loans)")]
    if "product" not in cols:
        raise SystemExit("Old sacco.db found from version 1. Delete sacco.db and run again.")
    return con


# ---------- calculations ----------
def add_months(d, n):
    m = d.month - 1 + n
    y, m = d.year + m // 12, m % 12 + 1
    return date(y, m, min(d.day, monthrange(y, m)[1]))


def reducing_instalment(principal, annual_rate, months):
    r = annual_rate / 100 / 12
    if r == 0:
        return round(principal / months, 2)
    return round(principal * r / (1 - (1 + r) ** -months), 2)


def quote(product, principal, months=None):
    """Work out fees, net cash paid out and instalment, without touching the database."""
    if product not in PRODUCTS:
        raise ValueError(f"Unknown product '{product}'. Choose from: {', '.join(PRODUCTS)}")
    p = PRODUCTS[product]
    if principal <= 0:
        raise ValueError("Loan amount must be more than zero.")
    if p["max_amount"] and principal > p["max_amount"]:
        raise ValueError(f"{p['label']} maximum is KES {p['max_amount']:,}.")
    months = months or p["max_months"]
    if months < 1 or months > p["max_months"]:
        raise ValueError(f"{p['label']} can run for 1 to {p['max_months']} month(s).")

    processing = round(principal * p["processing_pct"] / 100, 2)
    risk = round(principal * p["risk_pct"] / 100, 2)
    legal, form = p["legal_fee"], p["form_fee"]
    up_interest = round(principal * p["rate"] / 100, 2) if p["upfront_interest"] else 0.0
    net = round(principal - processing - risk - legal - form - up_interest, 2)
    if net <= 0:
        raise ValueError("Deductions are more than the loan amount.")

    if p["upfront_interest"]:
        instalment = principal                    # interest already deducted upfront
    else:
        instalment = reducing_instalment(principal, p["rate"], months)
    return dict(product=product, label=p["label"], principal=principal, months=months,
                rate=p["rate"], processing_fee=processing, risk_fee=risk, legal_fee=legal,
                form_fee=form, upfront_interest=up_interest, net_disbursed=net,
                instalment=instalment)


def print_quote(q):
    print(f"\n{q['label']}: KES {q['principal']:,.2f} over {q['months']} month(s) at {q['rate']}%")
    for key, name in [("processing_fee", "Processing fee"), ("risk_fee", "Risk fee"),
                      ("legal_fee", "Legal fee"), ("form_fee", "Loan form fee"),
                      ("upfront_interest", "Interest (deducted upfront)")]:
        if q[key]:
            print(f"  - {name:<28} {q[key]:>12,.2f}")
    print(f"  = Cash to member             {q['net_disbursed']:>12,.2f}")
    print(f"  Monthly instalment           {q['instalment']:>12,.2f}")


def create_loan(con, member_id, product, principal, months=None, start=None):
    q = quote(product, principal, months)
    start = start or date.today()
    cur = con.execute(
        "INSERT INTO loans(member_id,product,principal,annual_rate,months,start_date,instalment,"
        "processing_fee,risk_fee,legal_fee,form_fee,upfront_interest,net_disbursed)"
        " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (member_id, product, principal, q["rate"], q["months"], start.isoformat(),
         q["instalment"], q["processing_fee"], q["risk_fee"], q["legal_fee"], q["form_fee"],
         q["upfront_interest"], q["net_disbursed"]))
    loan_id = cur.lastrowid

    if PRODUCTS[product]["upfront_interest"]:
        # one payment of the principal, due in a month
        rows = [(1, add_months(start, 1), principal, 0.0, principal)]
    else:
        rows, balance = [], principal
        r, inst = q["rate"] / 100 / 12, q["instalment"]
        for i in range(1, q["months"] + 1):
            interest = round(balance * r, 2)
            princ = round(inst - interest, 2)
            due = inst
            if i == q["months"]:                  # clear rounding on the last one
                princ = round(balance, 2)
                due = round(princ + interest, 2)
            balance = round(balance - princ, 2)
            rows.append((i, add_months(start, i), princ, interest, due))
    for no, due_date, princ, interest, due in rows:
        con.execute(
            "INSERT INTO schedule(loan_id,no,due_date,principal_part,interest_part,amount_due)"
            " VALUES(?,?,?,?,?,?)", (loan_id, no, due_date.isoformat(), princ, interest, due))
    con.commit()
    return loan_id


# ---------- payments ----------
def record_payment(con, loan_id, amount, paid_on=None, reference=""):
    paid_on = paid_on or date.today()
    con.execute("INSERT INTO payments(loan_id,paid_on,amount,reference) VALUES(?,?,?,?)",
                (loan_id, paid_on.isoformat(), amount, reference))
    left = amount
    rows = con.execute(
        "SELECT * FROM schedule WHERE loan_id=? AND amount_paid<amount_due ORDER BY no",
        (loan_id,)).fetchall()
    for row in rows:
        if left <= 0:
            break
        take = min(left, row["amount_due"] - row["amount_paid"])
        con.execute("UPDATE schedule SET amount_paid=amount_paid+? WHERE id=?",
                    (round(take, 2), row["id"]))
        left -= take
    con.commit()
    return round(left, 2)    # anything left over = overpayment


def history(con, loan_id):
    return con.execute("SELECT * FROM payments WHERE loan_id=? ORDER BY paid_on",
                       (loan_id,)).fetchall()


def outstanding(con, loan_id):
    """Total still owed on the loan (instalments + any penalty, less what was paid)."""
    r = con.execute("SELECT SUM(amount_due-amount_paid) t FROM schedule WHERE loan_id=?",
                    (loan_id,)).fetchone()
    return round(r["t"] or 0, 2)


# ---------- penalties ----------
def apply_penalties(con, today=None):
    """Instant and Vuka na Rima: 10% of the unpaid balance, charged once when overdue."""
    today = today or date.today()
    rows = con.execute("""
        SELECT s.*, l.product FROM schedule s JOIN loans l ON l.id=s.loan_id
        WHERE s.amount_paid < s.amount_due AND s.penalty = 0""").fetchall()
    applied = 0
    for s in rows:
        pct = PRODUCTS[s["product"]]["penalty_pct"]
        if not pct:
            continue
        if date.fromisoformat(s["due_date"]) < today - timedelta(days=GRACE_DAYS):
            pen = round((s["amount_due"] - s["amount_paid"]) * pct / 100, 2)
            con.execute("UPDATE schedule SET penalty=?, amount_due=amount_due+? WHERE id=?",
                        (pen, pen, s["id"]))
            applied += 1
    con.commit()
    return applied


# ---------- alerts ----------
def send_alert(member, message):
    """Swap this body for a real SMS (Africa's Talking) or email (smtplib) call."""
    print(f"[ALERT -> {member['name']} {member['phone']}] {message}")


def run_alerts(con, today=None):
    today = today or date.today()
    apply_penalties(con, today)
    rows = con.execute("""
        SELECT s.*, l.product, m.name, m.phone, m.email FROM schedule s
        JOIN loans l ON l.id=s.loan_id JOIN members m ON m.id=l.member_id
        WHERE s.amount_paid < s.amount_due""").fetchall()
    sent = 0
    for s in rows:
        due = date.fromisoformat(s["due_date"])
        owed = s["amount_due"] - s["amount_paid"]
        label = PRODUCTS[s["product"]]["label"]
        if s["last_alert"] == today.isoformat():
            continue                          # already alerted today
        if due < today - timedelta(days=GRACE_DAYS):
            days = (today - due).days
            msg = (f"MISSED: {label} instalment {s['no']} was due {due:%d %b %Y} "
                   f"({days} days late). ")
            if s["penalty"]:
                msg += f"A penalty of KES {s['penalty']:,.2f} has been added. "
            msg += f"Amount owing: KES {owed:,.2f}. Please pay or contact the SACCO."
        elif due <= today + timedelta(days=REMIND_DAYS_BEFORE):
            msg = (f"REMINDER: {label} instalment {s['no']} of KES {owed:,.2f} "
                   f"is due on {due:%d %b %Y}.")
        else:
            continue
        send_alert(s, msg)
        con.execute("UPDATE schedule SET last_alert=? WHERE id=?",
                    (today.isoformat(), s["id"]))
        sent += 1
    con.commit()
    return sent


# ---------- demo ----------
def demo():
    con = connect()
    mid = con.execute("INSERT INTO members(name,phone,email) VALUES(?,?,?)",
                      ("Jane Wanjiru", "+254700000000", "jane@example.com")).lastrowid

    print("=== Loan quotes ===")
    for product, amount, months in [("school", 50000, 12), ("development", 100000, 24),
                                    ("instant", 5000, 1), ("vuka", 20000, 1)]:
        print_quote(quote(product, amount, months))

    print("\n=== Rule checks ===")
    for args in [("instant", 6000), ("vuka", 25000), ("school", 50000, 13),
                 ("development", 50000, 25)]:
        try:
            quote(*args)
        except ValueError as e:
            print("Rejected:", e)

    print("\n=== School loan: pay first instalment ===")
    start = date.today() - timedelta(days=40)
    school = create_loan(con, mid, "school", 50000, 12, start)
    record_payment(con, school, 4584.00, start + timedelta(days=30), "MPESA-ABC123")
    print("Still owed on school loan:", outstanding(con, school))

    print("\n=== Instant loan: part paid, then overdue -> 10% penalty ===")
    instant = create_loan(con, mid, "instant", 5000, start=start)    # due 10 days ago
    record_payment(con, instant, 3000, reference="MPESA-XYZ789")
    print("Alerts sent:", run_alerts(con))
    print("Owed on instant loan after penalty:", outstanding(con, instant))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "demo"
    if cmd == "demo":
        demo()
    elif cmd == "quote":
        prod, amt = sys.argv[2], float(sys.argv[3])
        mths = int(sys.argv[4]) if len(sys.argv) > 4 else None
        print_quote(quote(prod, amt, mths))
    elif cmd == "alerts":
        print("Alerts sent:", run_alerts(connect()))