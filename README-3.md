# Retail Business Performance & Profitability Analysis

**Internship project 1 | Tools:** SQL, Python (Pandas, NumPy), Tableau

## Objective
Analyse retail transaction data to identify profitable categories, regional and seasonal performance, and products that may need a slow-moving stock review.

## Dataset
`retail_transactions.csv` contains 600 illustrative sample transactions for calendar year 2025. It is synthetic and is not real company/customer data.

## Files
- `retail_transactions.csv` — source dataset for SQL, Python and Tableau.
- `retail_analysis_queries.sql` — table definition and SQL analysis queries.
- `retail_analysis.py` — cleaning, KPI calculations and export of analysis tables.
- `category_profitability.csv` — category-level output.
- `regional_performance.csv` — region-level output.
- `seasonal_performance.csv` — season-level output.
- `product_performance.csv` — product sales-volume review.
- `TABLEAU_DASHBOARD_GUIDE.md` — dashboard construction steps.
- `Retail_Project_Report.pdf` — two-page project report.

## Run using Python
Install dependencies:
```bash
pip install pandas numpy
```
Keep `retail_analysis.py` and `retail_transactions.csv` in the same folder, then run:
```bash
python retail_analysis.py
```

## SQL
Create a database table using the schema at the top of `retail_analysis_queries.sql`, import the CSV, and run the queries. The SQL uses SQLite-compatible syntax.

## Important limitation
Only transaction-level sales data is provided. Inventory days and stock turnover require inventory-on-hand and replenishment data. Low unit sales are used only as a proxy for identifying products for review.

## Author
Add your name, college, and internship organisation here before submission.
