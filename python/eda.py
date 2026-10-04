import pandas as pd
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_FILE = Path("data/processed/transactions_clean.csv")


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(INPUT_FILE)

df["Date"] = pd.to_datetime(df["Date"])


# ============================================================
# BASIC INFORMATION
# ============================================================

print("=" * 60)
print("SMART FINANCE INSIGHTS - EDA")
print("=" * 60)

print(f"\nTotal Transactions : {len(df)}")

print(f"Income Transactions : {(df['Type'] == 'Income').sum()}")

print(f"Expense Transactions: {(df['Type'] == 'Expense').sum()}")


# ============================================================
# 1. FINANCIAL KPIs
# ============================================================

total_income = df["Income_Amount"].sum()
total_expense = df["Expense_Amount"].sum()

net_savings = total_income - total_expense

savings_rate = (
    (net_savings / total_income) * 100
    if total_income > 0
    else 0
)

average_expense = df.loc[
    df["Type"] == "Expense",
    "Amount"
].mean()

average_income = df.loc[
    df["Type"] == "Income",
    "Amount"
].mean()


print("\n" + "=" * 60)
print("FINANCIAL KPIs")
print("=" * 60)

print(f"Total Income       : ₹{total_income:,.2f}")
print(f"Total Expense      : ₹{total_expense:,.2f}")
print(f"Net Savings        : ₹{net_savings:,.2f}")
print(f"Savings Rate       : {savings_rate:.2f}%")
print(f"Average Income     : ₹{average_income:,.2f}")
print(f"Average Expense    : ₹{average_expense:,.2f}")


# ============================================================
# 2. MONTHLY ANALYSIS
# ============================================================

monthly = df.groupby("Year_Month").agg(
    Income=("Income_Amount", "sum"),
    Expense=("Expense_Amount", "sum")
).reset_index()

monthly["Savings"] = (
    monthly["Income"] - monthly["Expense"]
)

monthly["Savings_Rate"] = (
    monthly["Savings"] /
    monthly["Income"].replace(0, pd.NA)
) * 100


print("\n" + "=" * 60)
print("MONTHLY FINANCIAL ANALYSIS")
print("=" * 60)

print(monthly.to_string(index=False))


# ============================================================
# 3. EXPENSE BY CATEGORY
# ============================================================

expense_df = df[df["Type"] == "Expense"]

category_expense = (
    expense_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)


print("\n" + "=" * 60)
print("EXPENSE BY CATEGORY")
print("=" * 60)

for category, amount in category_expense.items():
    print(f"{category:<20} ₹{amount:,.2f}")


# ============================================================
# 4. INCOME BY CATEGORY
# ============================================================

income_df = df[df["Type"] == "Income"]

category_income = (
    income_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)


print("\n" + "=" * 60)
print("INCOME BY CATEGORY")
print("=" * 60)

for category, amount in category_income.items():
    print(f"{category:<20} ₹{amount:,.2f}")


# ============================================================
# 5. PAYMENT METHOD ANALYSIS
# ============================================================

payment_analysis = (
    expense_df
    .groupby("Payment_Method")["Amount"]
    .sum()
    .sort_values(ascending=False)
)


print("\n" + "=" * 60)
print("EXPENSE BY PAYMENT METHOD")
print("=" * 60)

for method, amount in payment_analysis.items():
    print(f"{method:<20} ₹{amount:,.2f}")


# ============================================================
# 6. ACCOUNT ANALYSIS
# ============================================================

account_analysis = (
    expense_df
    .groupby("Account")["Amount"]
    .sum()
    .sort_values(ascending=False)
)


print("\n" + "=" * 60)
print("EXPENSE BY ACCOUNT")
print("=" * 60)

for account, amount in account_analysis.items():
    print(f"{account:<20} ₹{amount:,.2f}")


# ============================================================
# 7. TOP 10 EXPENSE TRANSACTIONS
# ============================================================

top_expenses = (
    expense_df
    .sort_values("Amount", ascending=False)
    .head(10)
)


print("\n" + "=" * 60)
print("TOP 10 EXPENSE TRANSACTIONS")
print("=" * 60)

print(
    top_expenses[
        [
            "Date",
            "Description",
            "Category",
            "Amount"
        ]
    ].to_string(index=False)
)


# ============================================================
# 8. YEARLY ANALYSIS
# ============================================================

yearly = df.groupby("Year").agg(
    Income=("Income_Amount", "sum"),
    Expense=("Expense_Amount", "sum")
).reset_index()

yearly["Savings"] = (
    yearly["Income"] - yearly["Expense"]
)

yearly["Savings_Rate"] = (
    yearly["Savings"] /
    yearly["Income"].replace(0, pd.NA)
) * 100


print("\n" + "=" * 60)
print("YEARLY ANALYSIS")
print("=" * 60)

print(yearly.to_string(index=False))


# ============================================================
# 9. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY ✅")
print("=" * 60)