import datetime as dt
import logging

import pandas as pd
from src import config


def make_rfm_data():

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()

    logger.info("Reading in files")
    customers = pd.read_csv(config.RAW_FILE_PATH / "olist_customers_dataset.csv")
    orders = pd.read_csv(config.RAW_FILE_PATH / "olist_orders_dataset.csv")
    order_items = pd.read_csv(config.RAW_FILE_PATH / "olist_order_items_dataset.csv")

    logger.info("Processing")
    grouped_order_items = (
        order_items.groupby("order_id")
        .agg({"price": "sum", "freight_value": "sum", "shipping_limit_date": "max"})
        .reset_index()
    )

    rfm = customers.merge(orders, on="customer_id", how="inner").merge(
        grouped_order_items, on="order_id", how="inner"
    )

    rfm = rfm.loc[rfm["order_status"] == "delivered"]

    datetime_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    format = "%Y-%m-%d %H:%M:%S"

    rfm.dropna(axis=0, inplace=True)

    for col in datetime_cols:
        rfm[col] = pd.to_datetime(rfm[col], format=format)

    max_date = max(rfm["order_purchase_timestamp"]) + dt.timedelta(days=1)

    rfm = (
        rfm.groupby("customer_unique_id")
        .agg(
            {
                "order_purchase_timestamp": lambda x: (max_date - x.max()).days,
                "customer_id": "count",
                "price": "sum",
            }
        )
        .reset_index()
    )

    rfm.rename(
        columns={
            "order_purchase_timestamp": "recency",
            "customer_id": "frequency",
            "price": "monetary",
        },
        inplace=True,
    )

    logger.info("Extracting file")
    rfm.to_parquet(config.INT_FILE_PATH / "rfm.parquet")
    logger.info("Done")


def main():
    make_rfm_data()


if __name__ == "__main__":
    main()
