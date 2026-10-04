-- ============================================================
-- SMART FINANCE INSIGHTS
-- SQL Analysis Queries
-- ============================================================

USE smart_finance;


-- ============================================================
-- 1. Total Number of Transactions
-- ============================================================

SELECT COUNT(*) AS total_transactions
FROM transactions;


-- ============================================================
-- 2. Total Income
-- ============================================================

SELECT
    SUM(Income_Amount) AS total_income
FROM transactions;


-- ============================================================
-- 3. Total Expense
-- ============================================================

SELECT
    SUM(Expense_Amount) AS total_expense
FROM transactions;


-- ============================================================
-- 4. Net Savings
-- ============================================================

SELECT
    SUM(Income_Amount) - SUM(Expense_Amount) AS net_savings
FROM transactions;


-- ============================================================
-- 5. Savings Rate
-- ============================================================

SELECT
    ROUND(
        (
            (SUM(Income_Amount) - SUM(Expense_Amount))
            / SUM(Income_Amount)
        ) * 100,
        2
    ) AS savings_rate
FROM transactions;


-- ============================================================
-- 6. Income vs Expense by Transaction Type
-- ============================================================

SELECT
    Type,
    COUNT(*) AS transaction_count,
    SUM(Amount) AS total_amount
FROM transactions
GROUP BY Type;


-- ============================================================
-- 7. Expense by Category
-- ============================================================

SELECT
    Category,
    SUM(Expense_Amount) AS total_expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category
ORDER BY total_expense DESC;


-- ============================================================
-- 8. Monthly Income and Expense
-- ============================================================

SELECT
    Year_Month,
    SUM(Income_Amount) AS total_income,
    SUM(Expense_Amount) AS total_expense
FROM transactions
GROUP BY Year_Month
ORDER BY Year_Month;


-- ============================================================
-- 9. Expense by Payment Method
-- ============================================================

SELECT
    Payment_Method,
    SUM(Expense_Amount) AS total_expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Payment_Method
ORDER BY total_expense DESC;


-- ============================================================
-- 10. Expense by Account
-- ============================================================

SELECT
    Account,
    SUM(Expense_Amount) AS total_expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Account
ORDER BY total_expense DESC;


-- ============================================================
-- 11. Top 10 Expense Transactions
-- ============================================================

SELECT
    Transaction_ID,
    Date,
    Category,
    Description,
    Amount
FROM transactions
WHERE Type = 'Expense'
ORDER BY Amount DESC
LIMIT 10;


-- ============================================================
-- 12. Yearly Financial Summary
-- ============================================================

SELECT
    Year,
    SUM(Income_Amount) AS total_income,
    SUM(Expense_Amount) AS total_expense,
    SUM(Income_Amount) - SUM(Expense_Amount) AS net_savings
FROM transactions
GROUP BY Year
ORDER BY Year;


-- ============================================================
-- 13. Category and Subcategory Analysis
-- ============================================================

SELECT
    Category,
    Subcategory,
    SUM(Expense_Amount) AS total_expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category, Subcategory
ORDER BY total_expense DESC;


-- ============================================================
-- 14. Monthly Savings
-- ============================================================

SELECT
    Year_Month,
    SUM(Income_Amount) AS income,
    SUM(Expense_Amount) AS expense,
    SUM(Income_Amount) - SUM(Expense_Amount) AS savings
FROM transactions
GROUP BY Year_Month
ORDER BY Year_Month;


-- ============================================================
-- 15. Highest Spending Category
-- ============================================================

SELECT
    Category,
    SUM(Expense_Amount) AS total_expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category
ORDER BY total_expense DESC
LIMIT 1;