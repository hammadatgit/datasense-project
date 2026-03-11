# main.py
from src.logger import setup_logger
from src.loader import load_config, load_datasets
from src.validator import validate_sales
from src.cleaner import clean_sales
from src.merger import merge_data
from src.analyzer import sales_by_region, monthly_sales
from src.visualization import plot_sales_by_region, plot_monthly_sales, price_boxplot
from src.insights import generate_insights
from src.quality import calculate_quality

# --- Setup logging ---
setup_logger()

# --- Load configuration and datasets ---
config = load_config()
sales, customers, products = load_datasets(config)

# --- Validate and clean ---
validate_sales(sales)
sales = clean_sales(sales)

# --- Merge datasets ---
df = merge_data(sales, customers, products)

# --- Print first few rows ---
print(df.head())

# --- Analysis ---
region_table = sales_by_region(df)
monthly_table = monthly_sales(df)

# --- Data Quality ---
score = calculate_quality(df)

# --- Generate automated insights ---
insights = generate_insights(region_table, monthly_table)

# --- Visualization ---
plot_sales_by_region(region_table)
plot_monthly_sales(monthly_table)
price_boxplot(df)

# --- Print summary ---
print(f"\nDATA QUALITY SCORE: {score}")
for insight in insights:
    print(insight)