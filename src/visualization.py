import matplotlib.pyplot as plt
import seaborn as sns

# --- Sales by Region ---
def plot_sales_by_region(df):
    """
    Bar plot of revenue by region
    """
    sns.barplot(data=df, x="region", y="revenue")
    plt.title("Revenue by Region")
    plt.ylabel("Revenue")
    plt.xlabel("Region")
    plt.tight_layout()
    plt.savefig("reports/plots/sales/revenue_by_region.png")
    plt.clf()

# --- Monthly Sales Trend ---
def plot_monthly_sales(df):
    """
    Line plot of monthly sales revenue
    """
    df.plot(kind="line", marker='o')
    plt.title("Monthly Sales Trend")
    plt.ylabel("Revenue")
    plt.xlabel("Month")
    plt.tight_layout()
    plt.savefig("reports/plots/sales/monthly_sales.png")
    plt.clf()

# --- Product Price Distribution ---
def price_boxplot(df):
    """
    Boxplot of product prices by category
    """
    sns.boxplot(data=df, x="category", y="price")
    plt.title("Product Price Distribution by Category")
    plt.ylabel("Price")
    plt.xlabel("Category")
    plt.tight_layout()
    plt.savefig("reports/plots/products/price_boxplot.png")
    plt.clf()