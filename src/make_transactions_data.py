import datetime as dt
import logging

import pandas as pd

from src import config, make_dataset


def make_transactions_data():

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    logger = logging.getLogger()

    logger.info("Reading necessary files")
    try:
        customers = pd.read_csv(config.RAW_FILE_PATH / "olist_customers_dataset.csv")
        orders = pd.read_csv(config.RAW_FILE_PATH / "olist_orders_dataset.csv")
        order_items = pd.read_csv(
            config.RAW_FILE_PATH / "olist_order_items_dataset.csv"
        )
        products = pd.read_csv(config.RAW_FILE_PATH / "olist_products_dataset.csv")
        sellers = pd.read_csv(config.RAW_FILE_PATH / "olist_sellers_dataset.csv")
        translations = pd.read_csv(
            config.RAW_FILE_PATH / "product_category_name_translation.csv"
        )
    except FileNotFoundError:
        make_dataset()
        customers = pd.read_csv(config.RAW_FILE_PATH / "olist_customers_dataset.csv")
        orders = pd.read_csv(config.RAW_FILE_PATH / "olist_orders_dataset.csv")
        order_items = pd.read_csv(
            config.RAW_FILE_PATH / "olist_order_items_dataset.csv"
        )
        products = pd.read_csv(config.RAW_FILE_PATH / "olist_products_dataset.csv")
        sellers = pd.read_csv(config.RAW_FILE_PATH / "olist_sellers_dataset.csv")
        translations = pd.read_csv(
            config.RAW_FILE_PATH / "product_category_name_translation.csv"
        )

    df = (
        customers.merge(orders, on="customer_id", how="left")
        .merge(order_items, on="order_id", how="left")
        .merge(products, on="product_id", how="left")
        .merge(sellers, on="seller_id", how="left")
        .merge(translations, on="product_category_name", how="left")
    )

    format = "%Y-%m-%d %H:%M:%S"

    datetime_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], format=format)

    df.drop(columns=["product_category_name"], inplace=True)

    df.rename(
        columns={
            "product_name_lenght": "product_name_length",
            "product_description_lenght": "product_description_length",
            "product_category_name_english": "product_category_name",
        },
        inplace=True,
    )

    df.to_parquet(config.INT_FILE_PATH / "transactions.parquet")
    logger.info("Done")


def main():
    make_transactions_data()


if __name__ == "__main__":
    main()
