"""
Retail Business Performance & Profitability Analysis
Run: python retail_analysis.py
Input: retail_transactions.csv in the same folder
Outputs: category_profitability.csv, regional_performance.csv,
         seasonal_performance.csv, product_performance.csv
"""
import pandas as pd
from pathlib import Path

DATA = Path(__file__).with_name("retail_transactions.csv")
df = pd.read_csv(DATA, parse_dates=["Order_Date"])

# Data quality checks and cleaning
df.columns = df.columns.str.strip()
for col in ["Region", "Product_Category", "Sub_Category", "Product", "Season"]:
    df[col] = df[col].astype("string").str.strip()
df = df.drop_duplicates(subset=["Order_ID"])
df = df.dropna(subset=["Order_ID", "Order_Date", "Product_Category", "Quantity"])
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df = df.dropna(subset=["Quantity", "Sales", "Profit"])
df = df[(df["Quantity"] > 0) & (df["Sales"] >= 0)]

# Recalculate metrics to ensure consistency
df["Sales"] = (df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])).round(2)
df["Total_Cost"] = (df["Quantity"] * df["Unit_Cost"]).round(2)
df["Profit"] = (df["Sales"] - df["Total_Cost"]).round(2)
df["Profit_Margin_Pct"] = (df["Profit"] / df["Sales"].replace(0, pd.NA) * 100).round(2)

print("RETAIL BUSINESS SUMMARY")
print("Transactions:", len(df))
print("Total sales:", round(df["Sales"].sum(), 2))
print("Total profit:", round(df["Profit"].sum(), 2))
print("Overall profit margin (%):", round(df["Profit"].sum()/df["Sales"].sum()*100, 2))

category = df.groupby("Product_Category", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum"), Units_Sold=("Quantity", "sum"))
category["Profit_Margin_Pct"] = (category["Profit"] / category["Sales"] * 100).round(2)
category.sort_values("Profit", ascending=False).to_csv("category_profitability.csv", index=False)

region = df.groupby("Region", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
region.to_csv("regional_performance.csv", index=False)

season = df.groupby("Season", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum"), Units_Sold=("Quantity", "sum"))
season.to_csv("seasonal_performance.csv", index=False)

product = df.groupby(["Product", "Product_Category"], as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum"), Units_Sold=("Quantity", "sum"))
# Sales-volume proxy only: actual inventory-on-hand/stock-age data is not included.
product["Movement_Flag"] = product["Units_Sold"].apply(
    lambda x: "Review - lower sales volume" if x <= product["Units_Sold"].quantile(0.25) else "Regular")
product.sort_values("Units_Sold").to_csv("product_performance.csv", index=False)

print("\\nAnalysis files created successfully.")
