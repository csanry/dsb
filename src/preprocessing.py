import datetime as dt
import logging
import os

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from src import config


class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):

        df = X.copy()

        # transformations
        df["order_total_price"] = df["price"] + df["freight_value"]
        df["shipping_cost_perc"] = df["freight_value"] / df["order_total_price"]
        df["purchase_dow"] = df["order_purchase_timestamp"].dt.dayofweek
        df["late_delivery"] = (
            df["order_estimated_delivery_date"] < df["order_delivered_customer_date"]
        )
        df["delivery_days"] = (
            df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
        ).dt.days
        df["days_late"] = (
            (
                df["order_estimated_delivery_date"]
                - df["order_delivered_customer_date"]
            ).dt.days
        ).apply(lambda x: max(x, 0))
        df["product_size"] = (
            df["product_length_cm"] * df["product_height_cm"] * df["product_width_cm"]
        )

        return df


def preprocessing():

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    logger = logging.getLogger()

    logger.info("Engineering features")
    df = pd.read_parquet(config.INT_FILE_PATH / "transactions_raw.parquet")
    feature_engineering = FeatureEngineering()

    df = feature_engineering.transform(df)

    df.to_parquet(config.INT_FILE_PATH / "transactions.parquet")
    logger.info("Done")


def main():
    preprocessing()


if __name__ == "__main__":
    main()
