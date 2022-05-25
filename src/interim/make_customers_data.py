import logging
import os

import pandas as pd

from src import config, make_transactions_data


def make_customers_data():

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()

    logger.info("Loading file")

    if not os.path.exists(config.INT_FILE_PATH / "transactions.parquet"):
        make_transactions_data()

    df = pd.read_parquet(config.INT_FILE_PATH / "transactions.parquet")

    logger.info("Processing")
    cust_agg = (
        df.groupby(["customer_unique_id", "customer_city", "customer_state"])
        .agg(
            {
                "order_id": "count",
                "product_id": "nunique",
                "product_category_name": lambda x: set(x),
                "order_total_price": "sum",
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

    cust_agg.rename(
        columns={
            "product_id": "unique_products",
            "seller_id": "n_sellers",
            "order_item_id": "basket_size",
        },
        inplace=True,
    )

    cust_agg["shipping_cost_perc"] = (
        cust_agg["freight_value"] / cust_agg["order_total_price"]
    )

    cust_agg.to_parquet(config.INT_FILE_PATH / "cust_agg.parquet")
    logger.info("Done")


def main():
    make_customers_data()


if __name__ == "__main__":
    main()
