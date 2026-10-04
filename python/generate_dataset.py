import numpy as np
import pandas as pd
from pathlib import Path


# PROJECT CONFIGURATION

RANDOM_SEED = 42

START_DATE = "2025-01-01"
END_DATE = "2026-12-31"

OUTPUT_FILE = Path("data/raw/transactions_raw.csv")


# FINANCIAL CATEGORIES

EXPENSE_CATEGORIES = {

    "Food": [
        "Groceries",
        "Restaurant",
        "Canteen",
        "Food Delivery"
    ],

    "Travel": [
        "Bus",
        "Train",
        "Taxi",
        "Fuel"
    ],

    "Shopping": [
        "Clothing",
        "Electronics",
        "Accessories"
    ],

    "Rent": [
        "Monthly Rent"
    ],

    "Utilities": [
        "Electricity",
        "Internet",
        "Mobile",
        "Gas"
    ],

    "Education": [
        "Books",
        "Course",
        "Exam Fees"
    ],

    "Healthcare": [
        "Medicine",
        "Doctor",
        "Lab"
    ],

    "Entertainment": [
        "Movies",
        "Gaming",
        "Events"
    ],

    "Subscriptions": [
        "Netflix",
        "Spotify",
        "Cloud Storage"
    ],

    "Personal Care": [
        "Salon",
        "Grooming",
        "Cosmetics"
    ],

    "Others": [
        "Miscellaneous"
    ]
}


INCOME_CATEGORIES = {

    "Salary": [
        "Monthly Salary"
    ],

    "Freelance": [
        "Web Project",
        "Design Project"
    ],

    "Investment": [
        "Dividend",
        "Interest"
    ],

    "Business": [
        "Business Income"
    ],

    "Other Income": [
        "Other"
    ]
}



# PAYMENT METHODS

PAYMENT_METHODS = [
    "UPI",
    "Cash",
    "Debit Card",
    "Credit Card",
    "Net Banking"
]


# ACCOUNTS

ACCOUNTS = [
    "Main Bank",
    "Savings Account",
    "Cash",
    "Credit Card"
]



# TRANSACTION TYPES

TRANSACTION_TYPES = [
    "Income",
    "Expense"
]



# RANDOM SEED

np.random.seed(RANDOM_SEED)


print("Smart Finance Insights - Dataset Generator")
print("Configuration loaded successfully.")



# RANDOM DATE GENERATION

def generate_random_date():
    """
    Generate a random transaction date between START_DATE
    and END_DATE.
    """

    start = pd.Timestamp(START_DATE)
    end = pd.Timestamp(END_DATE)

    days_difference = (end - start).days

    random_days = np.random.randint(
        0,
        days_difference + 1
    )

    return start + pd.Timedelta(
        days=int(random_days)
    )



# MONTHLY SALARY GENERATION

def generate_salary_transaction(transaction_id, date):
    """
    Generate one monthly salary transaction.
    """

    amount = np.random.normal(
        55000,
        5000
    )

    amount = round(
        max(amount, 40000),
        2
    )

    return {
        "Transaction_ID": transaction_id,
        "Date": date,
        "Description": "Monthly Salary",
        "Category": "Salary",
        "Subcategory": "Monthly Salary",
        "Type": "Income",
        "Amount": amount,
        "Payment_Method": "Net Banking",
        "Account": "Main Bank",
        "Merchant": "Employer",
        "Location": "India"
    }



# OTHER INCOME TRANSACTION GENERATION

def generate_income_transaction(
    transaction_id,
    date
):
    """
    Generate one irregular income transaction.

    Salary is handled separately because it occurs
    once every month.
    """

    income_type = np.random.choice(
        [
            "Freelance",
            "Investment",
            "Business",
            "Other Income"
        ],
        p=[
            0.50,
            0.25,
            0.15,
            0.10
        ]
    )

    subcategory = np.random.choice(
        INCOME_CATEGORIES[income_type]
    )

    if income_type == "Freelance":

        amount = np.random.uniform(
            3000,
            15000
        )

        description = subcategory

        merchant = "Freelance Client"

    elif income_type == "Investment":

        amount = np.random.uniform(
            500,
            5000
        )

        description = subcategory

        merchant = "Investment Source"

    elif income_type == "Business":

        amount = np.random.uniform(
            5000,
            20000
        )

        description = "Business Income"

        merchant = "Business"

    else:

        amount = np.random.uniform(
            500,
            4000
        )

        description = "Other Income"

        merchant = "Other Source"

    amount = round(
        max(amount, 100),
        2
    )

    payment_method = np.random.choice(
        PAYMENT_METHODS,
        p=[
            0.45,
            0.10,
            0.10,
            0.05,
            0.30
        ]
    )

    account = np.random.choice(
        [
            "Main Bank",
            "Savings Account"
        ],
        p=[
            0.75,
            0.25
        ]
    )

    return {
        "Transaction_ID": transaction_id,
        "Date": date,
        "Description": description,
        "Category": income_type,
        "Subcategory": subcategory,
        "Type": "Income",
        "Amount": amount,
        "Payment_Method": payment_method,
        "Account": account,
        "Merchant": merchant,
        "Location": "India"
    }



# EXPENSE TRANSACTION GENERATION


def generate_expense_transaction(
    transaction_id,
    date,
    category=None
):
    """
    Generate one realistic expense transaction.

    If category is provided, that category is used.
    Otherwise a category is selected automatically.
    """

    if category is None:

        category = np.random.choice(
            [
                "Food",
                "Travel",
                "Shopping",
                "Education",
                "Healthcare",
                "Entertainment",
                "Subscriptions",
                "Personal Care",
                "Others"
            ],
            p=[
                0.30,
                0.15,
                0.12,
                0.07,
                0.05,
                0.10,
                0.06,
                0.08,
                0.07
            ]
        )

    subcategory = np.random.choice(
        EXPENSE_CATEGORIES[category]
    )


    
    # REALISTIC TRANSACTION AMOUNTS

    if category == "Food":

        amount = np.random.uniform(
            50,
            800
        )

    elif category == "Travel":

        amount = np.random.uniform(
            30,
            800
        )

    elif category == "Shopping":

        amount = np.random.uniform(
            300,
            5000
        )

    elif category == "Education":

        amount = np.random.uniform(
            500,
            5000
        )

    elif category == "Healthcare":

        amount = np.random.uniform(
            200,
            5000
        )

    elif category == "Entertainment":

        amount = np.random.uniform(
            200,
            2500
        )

    elif category == "Subscriptions":

        amount = np.random.uniform(
            100,
            1000
        )

    elif category == "Personal Care":

        amount = np.random.uniform(
            200,
            2000
        )

    else:

        amount = np.random.uniform(
            100,
            2000
        )

    amount = round(
        max(amount, 10),
        2
    )


    payment_method = np.random.choice(
        PAYMENT_METHODS,
        p=[
            0.45,
            0.10,
            0.10,
            0.05,
            0.30
        ]
    )


    account = np.random.choice(
        [
            "Main Bank",
            "Savings Account",
            "Cash",
            "Credit Card"
        ],
        p=[
            0.65,
            0.15,
            0.10,
            0.10
        ]
    )


    return {
        "Transaction_ID": transaction_id,
        "Date": date,
        "Description": subcategory,
        "Category": category,
        "Subcategory": subcategory,
        "Type": "Expense",
        "Amount": amount,
        "Payment_Method": payment_method,
        "Account": account,
        "Merchant": "Local Merchant",
        "Location": "India"
    }



# MONTHLY RENT


def generate_rent_transaction(
    transaction_id,
    date
):
    """
    Generate one monthly rent transaction.
    """

    amount = round(
        np.random.uniform(
            12000,
            20000
        ),
        2
    )

    return {
        "Transaction_ID": transaction_id,
        "Date": date,
        "Description": "Monthly Rent",
        "Category": "Rent",
        "Subcategory": "Monthly Rent",
        "Type": "Expense",
        "Amount": amount,
        "Payment_Method": "Net Banking",
        "Account": "Main Bank",
        "Merchant": "Landlord",
        "Location": "India"
    }



# MONTHLY UTILITY / BILL

def generate_utility_transaction(
    transaction_id,
    date
):
    """
    Generate one monthly utility transaction.
    """

    category = "Utilities"

    subcategory = np.random.choice(
        EXPENSE_CATEGORIES[category]
    )

    amount = round(
        np.random.uniform(
            500,
            3000
        ),
        2
    )

    return {
        "Transaction_ID": transaction_id,
        "Date": date,
        "Description": subcategory,
        "Category": category,
        "Subcategory": subcategory,
        "Type": "Expense",
        "Amount": amount,
        "Payment_Method": np.random.choice(
            PAYMENT_METHODS,
            p=[
                0.45,
                0.05,
                0.10,
                0.05,
                0.35
            ]
        ),
        "Account": "Main Bank",
        "Merchant": "Service Provider",
        "Location": "India"
    }



# COMPLETE DATASET GENERATION

def generate_dataset():
    """
    Generate a realistic personal-finance dataset.

    Recurring:
        Salary       -> monthly
        Rent         -> monthly
        Utilities    -> monthly

    Frequent:
        Food         -> daily
        Travel       -> frequent

    Occasional:
        Shopping
        Education
        Healthcare
        Entertainment
        Subscriptions
        Personal Care
        Others

    Irregular income:
        Freelance
        Investment
        Business
        Other Income
    """

    transactions = []

    transaction_id = 1

    current_date = pd.Timestamp(
        START_DATE
    )

    end_date = pd.Timestamp(
        END_DATE
    )


    while current_date <= end_date:

        month_key = (
            current_date.year,
            current_date.month
        )



        # 1. MONTHLY SALARY         

        if current_date.day == 1:

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_salary_transaction(
                    transaction_id_str,
                    current_date
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


         
        # 2. MONTHLY RENT

        if current_date.day == 2:

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_rent_transaction(
                    transaction_id_str,
                    current_date
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


         
        # 3. MONTHLY UTILITIES

        if current_date.day == 5:

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_utility_transaction(
                    transaction_id_str,
                    current_date
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


         
        # 4. DAILY FOOD
        
        food_transactions = np.random.randint(
            1,
            3
        )

        for _ in range(
            food_transactions
        ):

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_expense_transaction(
                    transaction_id_str,
                    current_date,
                    category="Food"
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


         
        # 5. FREQUENT TRAVEL / TRANSPORT
         
        if np.random.random() < 0.60:

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_expense_transaction(
                    transaction_id_str,
                    current_date,
                    category="Travel"
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


         
        # 6. OCCASIONAL EXPENSES

        if np.random.random() < 0.08:

            occasional_categories = [
                "Shopping",
                "Education",
                "Healthcare",
                "Entertainment",
                "Subscriptions",
                "Personal Care",
                "Others"
            ]

            category = np.random.choice(
                occasional_categories,
                p=[
                    0.25,
                    0.10,
                    0.10,
                    0.20,
                    0.15,
                    0.10,
                    0.10
                ]
            )

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_expense_transaction(
                    transaction_id_str,
                    current_date,
                    category=category
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


         
        # 7. OCCASIONAL IRREGULAR INCOME
         
        if np.random.random() < 0.04:

            transaction_id_str = (
                f"TXN{transaction_id:06d}"
            )

            transaction = (
                generate_income_transaction(
                    transaction_id_str,
                    current_date
                )
            )

            transactions.append(
                transaction
            )

            transaction_id += 1


        # NEXT DAY         

        current_date += pd.Timedelta(
            days=1
        )


    return transactions



# CREATE DATAFRAME

def create_dataframe(
    transactions
):
    """
    Convert transactions into a Pandas DataFrame.
    """

    df = pd.DataFrame(
        transactions
    )

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    df = (
        df
        .sort_values(
            [
                "Date",
                "Transaction_ID"
            ]
        )
        .reset_index(
            drop=True
        )
    )

    return df


# DATA QUALITY VALIDATION

def validate_dataset(
    df
):
    """
    Validate the generated financial dataset.
    """

    print("\n" + "=" * 60)
    print("DATA QUALITY VALIDATION")
    print("=" * 60)


    # Missing values
    missing_values = (
        df.isnull()
        .sum()
        .sum()
    )

    print(
        f"Missing values: {missing_values}"
    )


    # Duplicate IDs
    duplicate_ids = (
        df["Transaction_ID"]
        .duplicated()
        .sum()
    )

    print(
        f"Duplicate Transaction IDs: "
        f"{duplicate_ids}"
    )


    # Invalid amounts
    invalid_amounts = (
        df["Amount"] <= 0
    ).sum()

    print(
        f"Invalid amounts: "
        f"{invalid_amounts}"
    )


    # Invalid transaction types
    invalid_types = (
        ~df["Type"].isin(
            TRANSACTION_TYPES
        )
    ).sum()

    print(
        f"Invalid transaction types: "
        f"{invalid_types}"
    )


    # Invalid dates
    invalid_dates = (
        df["Date"].isna()
    ).sum()

    print(
        f"Invalid dates: "
        f"{invalid_dates}"
    )


    # Invalid categories
    valid_categories = set(
        EXPENSE_CATEGORIES.keys()
    ) | set(
        INCOME_CATEGORIES.keys()
    )

    invalid_categories = (
        ~df["Category"].isin(
            valid_categories
        )
    ).sum()

    print(
        f"Invalid categories: "
        f"{invalid_categories}"
    )


    # Dataset shape
    print("\nDataset shape:")

    print(
        f"Rows: {df.shape[0]}"
    )

    print(
        f"Columns: {df.shape[1]}"
    )


    # Transaction distribution
    print(
        "\nTransaction distribution:"
    )

    print(
        df["Type"].value_counts()
    )


    # Validation status
    if (
        missing_values == 0
        and duplicate_ids == 0
        and invalid_amounts == 0
        and invalid_types == 0
        and invalid_dates == 0
        and invalid_categories == 0
    ):

        print(
            "\nValidation Status: PASSED"
        )

    else:

        print(
            "\nValidation Status: FAILED"
        )


    print("=" * 60)



# SAVE DATASET


def save_dataset(
    df
):
    """
    Save the generated dataset.
    """

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        "\nDataset saved successfully!"
    )

    print(
        f"File: {OUTPUT_FILE}"
    )



# BASIC FINANCIAL ANALYSIS


def analyze_dataset(
    df
):
    """
    Perform basic financial analysis.
    """

    total_income = (
        df.loc[
            df["Type"] == "Income",
            "Amount"
        ].sum()
    )

    total_expense = (
        df.loc[
            df["Type"] == "Expense",
            "Amount"
        ].sum()
    )

    net_savings = (
        total_income -
        total_expense
    )

    total_transactions = len(df)

    income_transactions = (
        df["Type"] == "Income"
    ).sum()

    expense_transactions = (
        df["Type"] == "Expense"
    ).sum()


    if total_income > 0:

        savings_rate = (
            net_savings /
            total_income
        ) * 100

    else:

        savings_rate = 0


    print("\n" + "=" * 60)
    print("BASIC FINANCIAL ANALYSIS")
    print("=" * 60)

    print(
        f"Total Transactions : "
        f"{total_transactions:,}"
    )

    print(
        f"Income Transactions: "
        f"{income_transactions:,}"
    )

    print(
        f"Expense Transactions: "
        f"{expense_transactions:,}"
    )

    print(
        f"\nTotal Income   : "
        f"₹{total_income:,.2f}"
    )

    print(
        f"Total Expense  : "
        f"₹{total_expense:,.2f}"
    )

    print(
        f"Net Savings    : "
        f"₹{net_savings:,.2f}"
    )

    print(
        f"Savings Rate   : "
        f"{savings_rate:.2f}%"
    )


    print(
        "\nIncome by Category:"
    )

    income_categories = (
        df[
            df["Type"] == "Income"
        ]
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    print(
        income_categories
    )


    print(
        "\nTop Expense Categories:"
    )

    expense_categories = (
        df[
            df["Type"] == "Expense"
        ]
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    print(
        expense_categories
    )

    print("=" * 60)



# MAIN PROGRAM
  

if __name__ == "__main__":

    # Generate transactions
    transactions = generate_dataset()

    # Create DataFrame
    df = create_dataframe(
        transactions
    )


    print(
        "\nDataset generated successfully!"
    )

    print(
        f"Total transactions: "
        f"{len(df):,}"
    )


    print(
        "\nFirst 5 transactions:"
    )

    print(
        df.head()
    )


    print(
        "\nTransaction types:"
    )

    print(
        df["Type"].value_counts()
    )


    print(
        "\nDataset columns:"
    )

    print(
        df.columns.tolist()
    )


    # Validate
    validate_dataset(
        df
    )


    # Save
    save_dataset(
        df
    )


    # Analyze
    analyze_dataset(
        df
    )