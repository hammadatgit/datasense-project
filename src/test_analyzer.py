# test_analyzer.py

from src.loader import load_config, load_datasets
from src.cleaner import clean_sales
from src.merger import merge_data
from src.analyzer import sales_by_region, top_products, monthly_sales, pivot_sales

config = load_config()
sales, customers, products = load_datasets(config)
sales = clean_sales(sales)
df = merge_data(sales, customers, products)

print("Sales by Region:\n", sales_by_region(df))
print("\nTop Products:\n", top_products(df))
print("\nMonthly Sales:\n", monthly_sales(df))
print("\nPivot Table:\n", pivot_sales(df))