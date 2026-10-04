import pandas as pd
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_FILE = Path("data/raw/transactions_raw.csv")
OUTPUT_FILE = Path("data/processed/transactions_clean.csv")


# ============================================================
# LOAD DATA
# ============================================================

def load_data():
    print("Loading raw dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Raw records loaded: {len(df)}")

    return df


# ============================================================
# DATA CLEANING
# ============================================================

def clean_data(df):

    print("\nStarting data cleaning...")

    # --------------------------------------------------------
    # 1. Convert Date column
    # --------------------------------------------------------

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # --------------------------------------------------------
    # 2. Convert Amount to numeric
    # --------------------------------------------------------

    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # --------------------------------------------------------
    # 3. Remove duplicate Transaction IDs
    # --------------------------------------------------------

    duplicate_count = df["Transaction_ID"].duplicated().sum()

    print(f"Duplicate transactions found: {duplicate_count}")

    df = df.drop_duplicates(
        subset=["Transaction_ID"],
        keep="first"
    )

    # --------------------------------------------------------
    # 4. Remove rows with critical missing values
    # --------------------------------------------------------

    critical_columns = [
        "Transaction_ID",
        "Date",
        "Category",
        "Type",
        "Amount"
    ]

    missing_before = df[critical_columns].isnull().sum().sum()

    print(f"Missing critical values found: {missing_before}")

    df = df.dropna(subset=critical_columns)

    # --------------------------------------------------------
    # 5. Remove invalid amounts
    # --------------------------------------------------------

    invalid_amounts = (df["Amount"] <= 0).sum()

    print(f"Invalid amounts found: {invalid_amounts}")

    df = df[df["Amount"] > 0]

    # --------------------------------------------------------
    # 6. Validate transaction type
    # --------------------------------------------------------

    valid_types = ["Income", "Expense"]

    df = df[df["Type"].isin(valid_types)]

    # --------------------------------------------------------
    # 7. Create date-based features
    # --------------------------------------------------------

    df["Year"] = df["Date"].dt.year

    df["Month"] = df["Date"].dt.month

    df["Month_Name"] = df["Date"].dt.strftime("%B")

    df["Year_Month"] = df["Date"].dt.strftime("%Y-%m")

    df["Day"] = df["Date"].dt.day

    df["Day_Name"] = df["Date"].dt.strftime("%A")

    # --------------------------------------------------------
    # 8. Create Income and Expense amount columns
    # --------------------------------------------------------

    df["Income_Amount"] = df["Amount"].where(
        df["Type"] == "Income",
        0
    )

    df["Expense_Amount"] = df["Amount"].where(
        df["Type"] == "Expense",
        0
    )

    # --------------------------------------------------------
    # 9. Sort by date
    # --------------------------------------------------------

    df = df.sort_values(
        by=["Date", "Transaction_ID"]
    ).reset_index(drop=True)

    return df


# ============================================================
# VALIDATION
# ============================================================

def validate_clean_data(df):

    print("\n" + "=" * 60)
    print("CLEAN DATA VALIDATION")
    print("=" * 60)

    print(f"Total records       : {len(df)}")
    print(f"Total columns       : {len(df.columns)}")

    print(
        f"Missing values      : {df.isnull().sum().sum()}"
    )

    print(
        f"Duplicate IDs       : "
        f"{df['Transaction_ID'].duplicated().sum()}"
    )

    print(
        f"Invalid amounts     : "
        f"{(df['Amount'] <= 0).sum()}"
    )

    print(
        f"Income records      : "
        f"{(df['Type'] == 'Income').sum()}"
    )

    print(
        f"Expense records     : "
        f"{(df['Type'] == 'Expense').sum()}"
    )

    print("\nColumns:")

    for column in df.columns:
        print(f" - {column}")


# ============================================================
# SAVE DATA
# ============================================================

def save_data(df):

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\nClean dataset saved to: {OUTPUT_FILE}"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    df = load_data()

    df = clean_data(df)

    validate_clean_data(df)

    save_data(df)

    print("\nData cleaning completed successfully! ✅")