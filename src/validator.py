import logging

def validate_sales(df):
    required_columns = ["sale_id","product_id","customer_id","date","quantity"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    if (df["quantity"] < 0).any():
        logging.warning("Negative quantities detected")

    logging.info("Sales dataset validation passed")
    return True