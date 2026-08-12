"""
RIMA SACCO - SCHOOL LOAN CALCULATOR
------------------------------------
Product: School Loan
Interest basis: 18% per annum, REDUCING BALANCE
Repayment: Equal monthly instalments (amortizing / annuity method)

This follows the same layout as the "SCHOOL LOAN MOVEMENT SCHEDULE"
tab in MOVEMENT_SCHEDULE.xlsx:
    MONTH | INSTALMENT | INTEREST | PRINCIPAL | BALANCE

On a reducing balance loan, interest each month is charged only on the
OUTSTANDING BALANCE (not the original amount), so the interest portion
of each instalment shrinks over time while the principal portion grows,
even though the total instalment stays the same every month.
"""

from dataclasses import dataclass


@dataclass
class LoanTerms:
    principal: float          # Amount disbursed to the member
    annual_rate: float        # Annual interest rate, e.g. 0.18 for 18%
    term_months: int          # Repayment period in months


def monthly_installment(loan: LoanTerms) -> float:
    """
    Standard reducing-balance (amortizing) instalment formula:

        I = P * r * (1 + r)^n / ((1 + r)^n - 1)

    where:
        P = principal
        r = monthly interest rate (annual_rate / 12)
        n = number of monthly instalments
    """
    r = loan.annual_rate / 12
    n = loan.term_months
    if r == 0:
        return loan.principal / n
    factor = (1 + r) ** n
    return loan.principal * r * factor / (factor - 1)


def build_movement_schedule(loan: LoanTerms):
    """
    Builds the month-by-month movement schedule.
    Returns a list of dicts, one row per month, mirroring the
    MONTH | INSTALMENT | INTEREST | PRINCIPAL | BALANCE columns.
    Instalment is rounded to 2 dp; the final instalment absorbs any
    rounding difference so the balance closes exactly to zero.
    """
    r = loan.annual_rate / 12
    installment = round(monthly_installment(loan), 2)

    schedule = []
    balance = loan.principal

    # Month 0 row - disbursement, matches the template's "Principal Amount" row
    schedule.append({
        "month": 0,
        "instalment": None,
        "interest": None,
        "principal": None,
        "balance": round(balance, 2),
    })

    for month in range(1, loan.term_months + 1):
        interest = round(balance * r, 2)
        principal_portion = installment - interest

        # On the last month, force balance to exactly 0 (absorbs rounding)
        if month == loan.term_months:
            principal_portion = balance
            installment_this_month = round(interest + principal_portion, 2)
        else:
            installment_this_month = installment

        balance = round(balance - principal_portion, 2)

        schedule.append({
            "month": month,
            "instalment": round(installment_this_month, 2),
            "interest": interest,
            "principal": round(principal_portion, 2),
            "balance": balance,
        })

    return schedule


def print_schedule(schedule):
    header = f"{'MONTH':>5} | {'INSTALMENT':>12} | {'INTEREST':>10} | {'PRINCIPAL':>12} | {'BALANCE':>14}"
    print(header)
    print("-" * len(header))
    for row in schedule:
        if row["month"] == 0:
            print(f"{row['month']:>5} | {'Principal Amount':>12} | {'':>10} | {'':>12} | {row['balance']:>14,.2f}")
        else:
            print(f"{row['month']:>5} | {row['instalment']:>12,.2f} | {row['interest']:>10,.2f} | "
                  f"{row['principal']:>12,.2f} | {row['balance']:>14,.2f}")


def summarize(loan: LoanTerms, schedule):
    total_paid = sum(r["instalment"] for r in schedule if r["month"] != 0)
    total_interest = total_paid - loan.principal
    print("\nSUMMARY")
    print("-" * 40)
    print(f"Loan amount (principal)   : {loan.principal:>14,.2f}")
    print(f"Interest rate             : {loan.annual_rate*100:>13.1f}% p.a. (reducing balance)")
    print(f"Loan term                 : {loan.term_months:>14} months")
    print(f"Monthly instalment        : {monthly_installment(loan):>14,.2f}")
    print(f"Total amount to be repaid : {total_paid:>14,.2f}")
    print(f"Total interest payable    : {total_interest:>14,.2f}")


if __name__ == "__main__":
    # Member's loan application: 40,000, 12 months, 18% p.a. reducing balance
    member_loan = LoanTerms(principal=100000, annual_rate=0.18, term_months=12)

    schedule = build_movement_schedule(member_loan)
    print_schedule(schedule)
    summarize(member_loan, schedule)