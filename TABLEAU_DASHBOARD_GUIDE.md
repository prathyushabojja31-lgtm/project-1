# Tableau Dashboard Guide

## Dashboard title
Retail Business Performance & Profitability Analysis

## Connect data
1. Open Tableau Public or Tableau Desktop.
2. Choose **Text file** and select `retail_transactions.csv`.
3. Confirm `Order_Date` is a Date field; `Sales`, `Profit`, and `Quantity` are numeric.

## Recommended dashboard layout
- KPI cards: Total Sales, Total Profit, Profit Margin %, Transactions.
- Bar chart: Profit by Product_Category (sort descending).
- Horizontal bar chart: Sales by Region.
- Line chart: Monthly Sales and Profit (use MONTH(Order_Date)).
- Heat map: Season by Product_Category, coloured by Sales or Profit.
- Detail table: Product, Units Sold, Sales, Profit, Profit Margin %.

## Filters
Add Region, Product_Category, Season, and Order_Date filters. Apply filters to all relevant worksheets.

## Calculated fields (if needed)
- Profit: `SUM([Sales]) - SUM([Total_Cost])`
- Profit Margin %: `SUM([Profit]) / SUM([Sales])`
- Month: `DATETRUNC('month', [Order_Date])`

## Inventory limitation
The sample dataset contains sales transactions, not stock-on-hand snapshots or replenishment records. Therefore it cannot calculate true inventory turnover or days of inventory. Use low units sold as a **slow-moving product review proxy**, not as proof of excess stock. For a real inventory analysis, add Opening Stock, Closing Stock, Purchase Quantity, and Stock Age fields.

## Deliverable
Save the workbook as `Retail_Business_Dashboard.twbx` after building the dashboard in Tableau.
