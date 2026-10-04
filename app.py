import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Finance Insights",
    page_icon="",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

DATA_FILE = Path(
    "data/processed/transactions_clean.csv"
)


@st.cache_data
def load_data():

    df = pd.read_csv(DATA_FILE)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


df = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("Smart Finance Insights")

st.markdown(
    "### Personal Financial Analytics Dashboard"
)

st.divider()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Filters")


# Year filter

years = sorted(df["Year"].unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)


# Category filter

categories = sorted(
    df["Category"].unique()
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)


# Transaction type

transaction_types = sorted(
    df["Type"].unique()
)

selected_types = st.sidebar.multiselect(
    "Transaction Type",
    transaction_types,
    default=transaction_types
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["Year"].isin(selected_years)) &
    (df["Category"].isin(selected_categories)) &
    (df["Type"].isin(selected_types))
]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_income = filtered_df[
    "Income_Amount"
].sum()

total_expense = filtered_df[
    "Expense_Amount"
].sum()

net_savings = (
    total_income - total_expense
)

savings_rate = (
    (net_savings / total_income) * 100
    if total_income > 0
    else 0
)


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Income",
        f"₹{total_income:,.0f}"
    )


with col2:

    st.metric(
        "Total Expense",
        f"₹{total_expense:,.0f}"
    )


with col3:

    st.metric(
        "Net Savings",
        f"₹{net_savings:,.0f}"
    )


with col4:

    st.metric(
        "Savings Rate",
        f"{savings_rate:.2f}%"
    )


st.divider()


# ============================================================
# MONTHLY ANALYSIS
# ============================================================

monthly = (
    filtered_df
    .groupby("Year_Month")
    .agg(
        Income=("Income_Amount", "sum"),
        Expense=("Expense_Amount", "sum")
    )
    .reset_index()
)

monthly["Savings"] = (
    monthly["Income"] -
    monthly["Expense"]
)


st.subheader("Monthly Financial Trend")


fig_monthly = px.line(
    monthly,
    x="Year_Month",
    y=["Income", "Expense", "Savings"],
    markers=True,
    title="Income, Expense and Savings"
)

fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Amount (₹)",
    legend_title="Metric"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)


# ============================================================
# EXPENSE CATEGORY ANALYSIS
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("Expense by Category")

    category_expense = (
        filtered_df[
            filtered_df["Type"] == "Expense"
        ]
        .groupby("Category")["Amount"]
        .sum()
        .reset_index()
        .sort_values(
            "Amount",
            ascending=False
        )
    )

    fig_category = px.bar(
        category_expense,
        x="Category",
        y="Amount",
        title="Total Spending by Category"
    )

    fig_category.update_layout(
        xaxis_title="Category",
        yaxis_title="Amount (₹)"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )


# ============================================================
# PAYMENT METHOD ANALYSIS
# ============================================================

with col2:

    st.subheader("Payment Method")

    payment_data = (
        filtered_df[
            filtered_df["Type"] == "Expense"
        ]
        .groupby("Payment_Method")["Amount"]
        .sum()
        .reset_index()
        .sort_values(
            "Amount",
            ascending=False
        )
    )

    fig_payment = px.pie(
        payment_data,
        names="Payment_Method",
        values="Amount",
        title="Expense Distribution by Payment Method"
    )

    st.plotly_chart(
        fig_payment,
        use_container_width=True
    )


# ============================================================
# ACCOUNT ANALYSIS
# ============================================================

st.subheader("Spending by Account")


account_data = (
    filtered_df[
        filtered_df["Type"] == "Expense"
    ]
    .groupby("Account")["Amount"]
    .sum()
    .reset_index()
    .sort_values(
        "Amount",
        ascending=False
    )
)


fig_account = px.bar(
    account_data,
    x="Account",
    y="Amount",
    title="Expense by Account"
)

st.plotly_chart(
    fig_account,
    use_container_width=True
)


# ============================================================
# FINANCIAL INSIGHTS
# ============================================================

st.subheader("🧠 Financial Insights")

# Top expense category
if not category_expense.empty:

    top_category = category_expense.iloc[0]["Category"]

    top_category_amount = category_expense.iloc[0]["Amount"]

    st.info(
        f"🔝 Your highest spending category is "
        f"**{top_category}**, with spending of "
        f"**₹{top_category_amount:,.0f}**."
    )


# Savings insight
if savings_rate >= 20:

    st.success(
        f"✅ Your current savings rate is "
        f"**{savings_rate:.2f}%**, indicating a healthy "
        f"savings level."
    )

elif savings_rate >= 10:

    st.warning(
        f"💡 Your savings rate is "
        f"**{savings_rate:.2f}%**. "
        f"There may be opportunities to increase savings."
    )

else:

    st.error(
        f"⚠️ Your savings rate is only "
        f"**{savings_rate:.2f}%**. "
        f"Consider reviewing discretionary expenses."
    )


# Highest spending month
if not monthly.empty:

    highest_month = monthly.loc[
        monthly["Expense"].idxmax()
    ]

    st.info(
        f"📅 Your highest spending month was "
        f"**{highest_month['Year_Month']}**, "
        f"with expenses of "
        f"**₹{highest_month['Expense']:,.0f}**."
    )


# ============================================================
# TRANSACTION TABLE
# ============================================================

st.subheader("Transaction Details")


display_columns = [
    "Date",
    "Description",
    "Category",
    "Type",
    "Amount",
    "Payment_Method",
    "Account"
]


st.dataframe(
    filtered_df[
        display_columns
    ].sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Smart Finance Insights | By Rutik Bane | "
    "Python • Pandas • Streamlit • Plotly"
)