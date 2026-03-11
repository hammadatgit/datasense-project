import pandas as pd

sales = pd.read_csv("data/sales.csv")
products = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")

print(sales.head())
print(products.head())
print(customers.head())