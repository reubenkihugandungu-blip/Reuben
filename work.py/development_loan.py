"""
Development Loan - Movement Schedule Generator
Rima Sacco Limited

Reducing balance method.
Single input point: change `principal=` in the LoanTerms(...) call at the bottom.
"""

from dataclasses import dataclass


@dataclass
class LoanTerms:
    principal: float
    annual_rate_pct: float   # annual interest rate, percent
    term_months: int
    loan_name: str = "Development Loan"


def generate_movement_schedule(terms: LoanTerms):
    """
    Reducing balance amortization.
    Equal monthly installment (annuity-style), interest charged on
    outstanding balance each month, principal portion reduces balance.
    """
    monthly_rate = (terms.annual_rate_pct / 100) / 12
    n = terms.term_months
    p = terms.principal

    if monthly_rate == 0:
        installment = p / n
    else:
        installment = p * (monthly_rate * (1 + monthly_rate) ** n) / \
                      ((1 + monthly_rate) ** n - 1)

    schedule = []
    balance = p
    total_interest = 0.0
    total_principal = 0.0

    for month in range(1, n + 1):
        interest = balance * monthly_rate
        principal_paid = installment - interest

        if month == n:
            principal_paid = balance
            installment_this_month = principal_paid + interest
        else:
            installment_this_month = installment

        closing_balance = balance - principal_paid

        schedule.append({
            "Month": month,
            "Opening Balance": round(balance, 2),
            "Installment": round(installment_this_month, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal_paid, 2),
            "Closing Balance": round(max(closing_balance, 0), 2),
        })

        total_interest += interest
        total_principal += principal_paid
        balance = closing_balance

    return schedule, {
        "loan_name": terms.loan_name,
        "principal": p,
        "annual_rate_pct": terms.annual_rate_pct,
        "term_months": n,
        "monthly_installment": round(installment, 2),
        "total_interest": round(total_interest, 2),
        "total_repayment": round(total_principal + total_interest, 2),
    }


def print_schedule(schedule, summary):
    print(f"\n{summary['loan_name']} - Movement Schedule")
    print(f"Principal: Ksh {summary['principal']:,.2f}  |  "
          f"Rate: {summary['annual_rate_pct']}% p.a. (reducing balance)  |  "
          f"Term: {summary['term_months']} months")
    print("-" * 90)
    print(f"{'Mth':<5}{'Opening Bal':>15}{'Installment':>15}"
          f"{'Interest':>13}{'Principal':>13}{'Closing Bal':>15}")
    print("-" * 90)
    for row in schedule:
        print(f"{row['Month']:<5}{row['Opening Balance']:>15,.2f}"
              f"{row['Installment']:>15,.2f}{row['Interest']:>13,.2f}"
              f"{row['Principal']:>13,.2f}{row['Closing Balance']:>15,.2f}")
    print("-" * 90)
    print(f"Total Interest: Ksh {summary['total_interest']:,.2f}   "
          f"Total Repayment: Ksh {summary['total_repayment']:,.2f}\n")


if __name__ == "__main__":
    # -----------------------------------------------------------
    # SINGLE INPUT POINT: change principal here (100,000 - 1,000,000)
    # -----------------------------------------------------------
    terms = LoanTerms(
        principal=325000,
        annual_rate_pct=12,
        term_months=24,
        loan_name="Development Loan",
    )

    schedule, summary = generate_movement_schedule(terms)
    print_schedule(schedule, summary)