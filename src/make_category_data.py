import logging
import os

import pandas as pd

from src import config, make_transactions_data


def make_category_data():

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()

    logger.info("Loading file")

    if not os.path.exists(config.INT_FILE_PATH / "transactions.parquet"):
        make_transactions_data()

    df = pd.read_parquet(config.INT_FILE_PATH / "transactions.parquet")

    logger.info("Processing")
    category_agg = (
        df.groupby(["product_category_name"])
        .agg(
            {
                "customer_unique_id": "nunique",
                "order_id": "count",
                "product_id": "nunique",
                "order_total_price": "sum",
                "price": "sum",
                "freight_value": "sum",
                "delivery_days": "mean",
                "seller_id": "nunique",
                "order_item_id": "count",
                "late_delivery": "sum",
            }
        )
        .reset_index(drop=False)
    )

    category_agg.rename(
        columns={
            "customer_unique_id": "n_unique_cust",
            "order_id": "total_orders",
            "product_id": "unique_products",
            "seller_id": "n_sellers",
            "order_item_id": "quantity",
        },
        inplace=True,
    )

    category_agg["shipping_cost_perc"] = (
        category_agg["freight_value"] / category_agg["order_total_price"]
    )
    category_agg["avg_item_value"] = category_agg["price"] / category_agg["quantity"]
    category_agg["late_delivery_perc"] = (
        category_agg["late_delivery"] / category_agg["total_orders"]
    )

    category_agg.to_parquet(config.INT_FILE_PATH / "category_agg.parquet")
    logger.info("Done")


def main():
    make_category_data()


if __name__ == "__main__":
    main()
