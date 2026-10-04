# Smart Finance Insights

Smart Finance Insights is a personal financial analytics project that analyzes income, expenses, savings, spending patterns, and financial behavior using Python, MySQL, Streamlit, and Power BI.

The project follows a complete data analytics workflow from dataset generation and data cleaning to database storage, analysis, visualization, and rule-based financial recommendations.


## 📌 Project Overview

Managing personal finances becomes difficult when transactions are spread across different categories, payment methods, accounts, and time periods.

Smart Finance Insights provides a centralized analytical solution to:

\- Track income and expenses

\- Analyze monthly financial trends

\- Identify major spending categories

\- Analyze payment methods and accounts

\- Calculate savings and savings rate

\- Identify unusual or large transactions

\- Generate rule-based financial recommendations

\- Present insights through interactive dashboards


## 🎯 Objectives

The main objectives of this project are:
1\. Generate a realistic financial transaction dataset.

2\. Clean and prepare the data using Python and Pandas.

3\. Perform exploratory data analysis.

4\. Store structured transaction data in MySQL.

5\. Perform financial analysis using Python and SQL.

6\. Build an interactive Streamlit dashboard.

7\. Build a Power BI financial analytics dashboard.

8\. Generate meaningful financial insights and recommendations.


## 🛠️ Technology Stack

| Technology | Purpose |

| Python | Data generation, cleaning and analysis |

| Pandas | Data manipulation and preprocessing |

| Plotly | Interactive visualizations |

| Streamlit | Interactive web dashboard |

| MySQL | Structured data storage and SQL analysis |

| Power BI | Business intelligence and visualization |

| DAX | Power BI financial measures |

| Git \& GitHub | Version control and project hosting |

| python-dotenv | Secure environment variable management |


## 🏗️ Project Architecture

Python Dataset Generator

         ↓

    Raw CSV Dataset

         ↓

Python Data Cleaning

         ↓

   Clean CSV Dataset

         ↓

        MySQL

      ↙       ↘

SQL Analysis   Power BI

      ↘       ↙

  Financial Insights

         ↓

Recommendations

         ↓

Streamlit Dashboard


## 📂 Project Structure
SmartFinanceInsights/

│

├── app.py

├── requirements.txt

├── .gitignore

│

├── data/

│   ├── raw/

│   │   └── transactions\_raw.csv

│   │

│   └── processed/

│       └── transactions\_clean.csv

│

├── python/

│   ├── generate\_dataset.py

│   ├── clean\_data.py

│   ├── eda.py

│   ├── insights.py

│   └── load\_mysql.py

│

└── powerbi/

   └── SFI.pbix


## 🔄 Data Analytics Workflow
## 1. Dataset Generation
The project generates a realistic synthetic financial transaction dataset containing:

\- Income transactions

\- Expense transactions

\- Categories and subcategories

\- Payment methods

\- Accounts

\- Merchants

\- Locations

\- Dates and time-related attributes


The generated dataset contains:

\- 1,710 transactions

\- 54 income transactions

\- 1,656 expense transactions


### 2. Data Cleaning \& Preparation

The raw dataset is processed using Pandas.

The cleaning process includes:

\- Missing value validation

\- Duplicate transaction checking

\- Data type validation

\- Date conversion

\- Transaction amount validation

\- Feature engineering



Additional analytical columns include:

\- Year

\- Month

\- Month Name

\- Year-Month

\- Day

\- Day Name

\- Income Amount

\- Expense Amount


Output:

data/processed/transactions\_clean.csv


### 3. Exploratory Data Analysis

The EDA process analyzes:
\- Total income

\- Total expenses

\- Net savings

\- Savings rate

\- Monthly income and expenses

\- Expense categories

\- Income categories

\- Payment methods

\- Accounts

\- Top expense transactions

\- Yearly financial performance


### 4. MySQL Database

The cleaned transaction data is stored in a MySQL database.

Database:



```text

smart\_finance

```



Main table:



```text

transactions

```



The database provides a structured layer for storing and querying financial transaction data.


### 5. Streamlit Dashboard

The Streamlit application provides an interactive interface for exploring the financial dataset.

The dashboard includes:

\- Financial KPI cards

\- Monthly income and expense trends

\- Expense category analysis

\- Payment method analysis

\- Account analysis

\- Transaction-level data

\- Interactive filters



Run the dashboard using:

```bash

streamlit run app.py

```

### 6. Power BI Dashboard

Power BI is used as the business intelligence layer of the project.

The dashboard contains:

\- Total Income

\- Total Expense

\- Net Savings

\- Savings Rate

\- Monthly Income vs Expense

\- Expense by Category

\- Expense by Payment Method

\- Year filters

\- Category filters

\- Transaction Type filters



Example DAX measures:



```DAX

Total Income =

SUM(transactions\[Income\_Amount])

```



```DAX

Total Expense =

SUM(transactions\[Expense\_Amount])

```



```DAX

Net Savings =

\[Total Income] - \[Total Expense]

```



```DAX

Savings Rate =

DIVIDE(

   \[Net Savings],

   \[Total Income],

   0

)


\## 📊 Key Financial Results

Based on the generated dataset:

| Metric | Value |

|---|---:|

| Total Transactions | 1,710 |

| Total Income | ₹1,525,713.65 |

| Total Expense | ₹1,218,446.86 |

| Net Savings | ₹307,266.79 |

| Savings Rate | 20.14% |


## 💡 Financial Insights



The project generates financial insights by analyzing:

\- Highest spending categories

\- Monthly spending behavior

\- Monthly savings performance

\- Payment method usage

\- Account-level spending

\- Large transactions

\- Overall savings rate


## 🤖 Rule-Based Recommendations

The recommendation system uses financial rules to generate suggestions based on the analyzed data.

Examples include:

\- Improving savings when the savings rate is low

\- Reducing spending in high-expense categories

\- Reviewing unusually large transactions

\- Monitoring frequently used payment methods

The recommendations are generated using Python-based rule logic rather than a machine learning model.


\## 🔐 Security

Sensitive database credentials are stored using environment variables.

The `.env` file is excluded from Git using `.gitignore`.

Example:


```env

MYSQL\_HOST=localhost

MYSQL\_USER=root

MYSQL\_PASSWORD=your\_password

MYSQL\_DATABASE=smart\_finance


Do not commit actual database passwords or other secrets to GitHub.


\## 🚀 How to Run the Project



\### 1. Clone the repository

```bash

git clone https://github.com/rutikbane2404/SmartFinanceInsights.git

cd SmartFinanceInsights

```

\### 2. Create a virtual environment


```bash

python -m venv .venv

```

\### 3. Activate the virtual environment

Windows:

```bash

.venv\\Scripts\\activate

```
\### 4. Install dependencies


```bash

pip install -r requirements.txt

```

\### 5. Configure MySQL

Create the database:


```sql

CREATE DATABASE smart\_finance;

```

Configure the `.env` file with your local MySQL credentials.


\### 6. Run the Streamlit dashboard


```bash

streamlit run app.py

```
\---



\## 📈 Project Highlights

\- End-to-end data analytics workflow

\- Synthetic financial dataset generation

\- Data cleaning and feature engineering

\- Exploratory data analysis

\- MySQL database integration

\- SQL-based data storage and analysis

\- Interactive Streamlit dashboard

\- Power BI business intelligence dashboard

\- DAX-based financial KPIs

\- Rule-based financial recommendations

\- Secure environment variable handling

\- Git and GitHub version control

\---

## 🔮 Future Scope

Possible future improvements include:

\- Machine learning-based expense prediction

\- Automated anomaly detection

\- Financial forecasting

\- Personalized budgeting

\- Advanced recommendation systems

\- Cloud database integration

\- Automated data ingestion from financial sources

\---

## 👨‍💻 Author
Rutik Bane
MCA Student | Data Analytics | Python | MySQL | Power BI | Web Development


## 📄 License

This project is created for educational and portfolio purposes.