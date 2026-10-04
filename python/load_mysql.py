import pandas as pd
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "transactions_clean.csv"
ENV_FILE = BASE_DIR / ".env"


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv(ENV_FILE)

print("Environment configuration loaded.")
print("MYSQL_HOST:", os.getenv("MYSQL_HOST"))
print("MYSQL_USER:", os.getenv("MYSQL_USER"))
print("MYSQL_DATABASE:", os.getenv("MYSQL_DATABASE"))
print(
    "MYSQL_PASSWORD loaded:",
    bool(os.getenv("MYSQL_PASSWORD"))
)


# ============================================================
# LOAD CSV
# ============================================================

print("\nLoading cleaned dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Records loaded from CSV: {len(df)}")


# ============================================================
# MYSQL CONNECTION
# ============================================================

print("\nConnecting to MySQL...")

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()

print("Connected to MySQL successfully.")


# ============================================================
# INSERT QUERY
# ============================================================

insert_query = """
INSERT IGNORE INTO transactions (
    `Transaction_ID`,
    `Date`,
    `Description`,
    `Category`,
    `Subcategory`,
    `Type`,
    `Amount`,
    `Payment_Method`,
    `Account`,
    `Merchant`,
    `Location`,
    `Year`,
    `Month`,
    `Month_Name`,
    `Year_Month`,
    `Day`,
    `Day_Name`,
    `Income_Amount`,
    `Expense_Amount`
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""


# ============================================================
# PREPARE DATA
# ============================================================

data = []

for _, row in df.iterrows():

    data.append((
        row["Transaction_ID"],
        row["Date"],
        row["Description"],
        row["Category"],
        row["Subcategory"],
        row["Type"],
        row["Amount"],
        row["Payment_Method"],
        row["Account"],
        row["Merchant"],
        row["Location"],
        row["Year"],
        row["Month"],
        row["Month_Name"],
        row["Year_Month"],
        row["Day"],
        row["Day_Name"],
        row["Income_Amount"],
        row["Expense_Amount"]
    ))


# ============================================================
# INSERT DATA
# ============================================================

print("\nInserting transactions into MySQL...")

cursor.executemany(
    insert_query,
    data
)

connection.commit()


print(
    f"Rows inserted/processed: {cursor.rowcount}"
)


# ============================================================
# VERIFY RECORD COUNT
# ============================================================

cursor.execute(
    "SELECT COUNT(*) FROM transactions"
)

total_records = cursor.fetchone()[0]

print(
    f"Total records currently in MySQL: {total_records}"
)


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
connection.close()

print("\nMySQL connection closed.")
print("Data loading completed successfully!")