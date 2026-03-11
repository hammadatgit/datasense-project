# src/analyzer.py

def sales_by_region(df):
    """
    Group sales by region and sum revenue.
    Returns a DataFrame: region | revenue
    """
    table = df.groupby("region")["revenue"].sum().reset_index()
    return table


def top_products(df):
    """
    Group sales by product_name and sum revenue.
    Returns a Series sorted descending by revenue.
    """
    return df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)


def monthly_sales(df):
    """
    Convert date to month period and aggregate revenue.
    Returns a Series: month | revenue
    """
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["revenue"].sum()

def pivot_sales(df):
    """
    Create a pivot table: revenue by region and product category.
    """
    pivot = df.pivot_table(
        values="revenue",
        index="region",
        columns="category",
        aggfunc="sum"
    )
    return pivot