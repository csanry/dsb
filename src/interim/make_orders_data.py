import logging
import os

import pandas as pd
from src import config
from src.interim import make_transactions_data


def make_orders_data():

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()

    logger.info("Loading file")

    if not os.path.exists(config.INT_FILE_PATH / "transactions.parquet"):
        make_transactions_data()

    df = pd.read_parquet(config.INT_FILE_PATH / "transactions.parquet")

    logger.info("Processing")
    orders_agg = (
        df.groupby(
            ["order_id", "customer_unique_id", "customer_city", "customer_state"]
        )
        .agg(
            {
                "product_id": "nunique",
                "product_category_name": lambda x: set(x),
                "order_total_price": "sum",
                "order_delivered_customer_date": "max",
                "order_estimated_delivery_date": "max",
                "order_delivered_carrier_date": "max",
                "price": "sum",
                "freight_value": "sum",
                "delivery_days": "mean",
                "seller_id": "nunique",
                "order_item_id": "count",
                "late_delivery": "max",
            }
        )
        .reset_index(drop=False)
    )

    orders_agg.rename(
        columns={
            "product_id": "unique_products",
            "seller_id": "n_sellers",
            "order_item_id": "basket_size",
        },
        inplace=True,
    )

    orders_agg["shipping_cost_perc"] = (
        orders_agg["freight_value"] / orders_agg["order_total_price"]
    )

    orders_agg.to_parquet(config.INT_FILE_PATH / "orders_agg.parquet")
    logger.info("Done")


def main():
    make_orders_data()


if __name__ == "__main__":
    main()
