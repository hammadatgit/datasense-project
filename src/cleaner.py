import pandas as pd
import logging

def clean_sales(df):
    initial_rows = df.shape[0]

    # Remove duplicates
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - df.shape[0]
    if duplicates_removed > 0:
        logging.info(f"Removed {duplicates_removed} duplicate rows")

    # Fix date column
    df["date"] = pd.to_datetime(df["date"])

    # Fill missing quantities
    df["quantity"] = df["quantity"].fillna(1)
    logging.info("Missing quantities filled")

    return df