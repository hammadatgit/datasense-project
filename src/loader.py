import pandas as pd
import yaml
import logging

def load_config():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)
    logging.info("Configuration loaded")
    return config

def load_datasets(config):
    sales = pd.read_csv(config["data_paths"]["sales"])
    customers = pd.read_csv(config["data_paths"]["customers"])
    products = pd.read_csv(config["data_paths"]["products"])
    logging.info("Datasets loaded")
    return sales, customers, products