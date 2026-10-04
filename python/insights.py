import pandas as pd
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_FILE = Path(
    "data/processed/transactions_clean.csv"
)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(INPUT_FILE)

df["Date"] = pd.to_datetime(df["Date"])


# ============================================================
# BASIC FINANCIAL METRICS
# ============================================================

total_income = df["Income_Amount"].sum()

total_expense = df["Expense_Amount"].sum()

net_savings = total_income - total_expense

savings_rate = (
    net_savings / total_income * 100
    if total_income > 0
    else 0
)


# ============================================================
# 1. TOP EXPENSE CATEGORY
# ============================================================

expense_df = df[
    df["Type"] == "Expense"
]

category_expense = (
    expense_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_category = category_expense.index[0]

top_category_amount = category_expense.iloc[0]


# ============================================================
# 2. HIGHEST SPENDING MONTH
# ============================================================

monthly_expense = (
    expense_df
    .groupby("Year_Month")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

highest_expense_month = monthly_expense.index[0]

highest_expense_month_amount = (
    monthly_expense.iloc[0]
)


# ============================================================
# 3. LOWEST SPENDING MONTH
# ============================================================

lowest_expense_month = monthly_expense.index[-1]

lowest_expense_month_amount = (
    monthly_expense.iloc[-1]
)


# ============================================================
# 4. BEST SAVINGS MONTH
# ============================================================

monthly_finance = (
    df
    .groupby("Year_Month")
    .agg(
        Income=("Income_Amount", "sum"),
        Expense=("Expense_Amount", "sum")
    )
)

monthly_finance["Savings"] = (
    monthly_finance["Income"] -
    monthly_finance["Expense"]
)

best_savings_month = (
    monthly_finance["Savings"]
    .idxmax()
)

best_savings_amount = (
    monthly_finance["Savings"]
    .max()
)


# ============================================================
# 5. WORST SAVINGS MONTH
# ============================================================

worst_savings_month = (
    monthly_finance["Savings"]
    .idxmin()
)

worst_savings_amount = (
    monthly_finance["Savings"]
    .min()
)


# ============================================================
# 6. MOST USED PAYMENT METHOD
# ============================================================

payment_method = (
    expense_df
    .groupby("Payment_Method")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_payment_method = payment_method.index[0]

top_payment_amount = payment_method.iloc[0]


# ============================================================
# 7. HIGHEST SPENDING ACCOUNT
# ============================================================

account_expense = (
    expense_df
    .groupby("Account")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_account = account_expense.index[0]

top_account_amount = account_expense.iloc[0]


# ============================================================
# 8. LARGE TRANSACTION ANALYSIS
# ============================================================

expense_mean = expense_df["Amount"].mean()

expense_std = expense_df["Amount"].std()

large_transaction_threshold = (
    expense_mean + 2 * expense_std
)

large_transactions = expense_df[
    expense_df["Amount"] >
    large_transaction_threshold
]


# ============================================================
# DISPLAY INSIGHTS
# ============================================================

print("=" * 60)
print("SMART FINANCE INSIGHTS")
print("=" * 60)


print("\nOVERALL FINANCIAL POSITION")

print(
    f"Total Income       : ₹{total_income:,.2f}"
)

print(
    f"Total Expense      : ₹{total_expense:,.2f}"
)

print(
    f"Net Savings        : ₹{net_savings:,.2f}"
)

print(
    f"Savings Rate       : {savings_rate:.2f}%"
)


print("\nTOP EXPENSE CATEGORY")

print(
    f"{top_category}: "
    f"₹{top_category_amount:,.2f}"
)


print("\nHIGHEST SPENDING MONTH")

print(
    f"{highest_expense_month}: "
    f"₹{highest_expense_month_amount:,.2f}"
)


print("\nLOWEST SPENDING MONTH")

print(
    f"{lowest_expense_month}: "
    f"₹{lowest_expense_month_amount:,.2f}"
)


print("\nBEST SAVINGS MONTH")

print(
    f"{best_savings_month}: "
    f"₹{best_savings_amount:,.2f}"
)


print("\nWORST SAVINGS MONTH")

print(
    f"{worst_savings_month}: "
    f"₹{worst_savings_amount:,.2f}"
)


print("\nTOP PAYMENT METHOD")

print(
    f"{top_payment_method}: "
    f"₹{top_payment_amount:,.2f}"
)


print("\nHIGHEST SPENDING ACCOUNT")

print(
    f"{top_account}: "
    f"₹{top_account_amount:,.2f}"
)


print("\nLARGE TRANSACTIONS")

print(
    f"Threshold: "
    f"₹{large_transaction_threshold:,.2f}"
)

print(
    f"Large transactions found: "
    f"{len(large_transactions)}"
)


# ============================================================
# AUTOMATED RECOMMENDATIONS
# ============================================================

print("\n" + "=" * 60)
print("FINANCIAL RECOMMENDATIONS")
print("=" * 60)


# Recommendation 1

if savings_rate < 10:

    print(
        "Savings rate is low. "
        "Consider reducing discretionary expenses."
    )

elif savings_rate < 20:

    print(
        "Savings rate is moderate. "
        "Try increasing monthly savings gradually."
    )

else:

    print(
        "Savings rate is healthy. "
        "Continue maintaining disciplined spending."
    )


# Recommendation 2

print(
    f"Monitor your highest spending category: "
    f"{top_category}."
)


# Recommendation 3

if len(large_transactions) > 0:

    print(
        f"Review {len(large_transactions)} "
        f"unusually large expense transactions."
    )

else:

    print(
        "No unusually large expense transactions detected."
    )


# Recommendation 4

print(
    f"Your highest expense payment method is "
    f"{top_payment_method}. "
    f"Review spending through this method regularly."
)


print("\n" + "=" * 60)
print("INSIGHT ANALYSIS COMPLETED ")
print("=" * 60)