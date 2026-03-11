import logging

def merge_data(sales, customers, products):
    df = sales.merge(products, on="product_id", how="left")
    df = df.merge(customers, on="customer_id", how="left")
    df["revenue"] = df["price"] * df["quantity"]
    logging.info("Datasets merged successfully")
    return df