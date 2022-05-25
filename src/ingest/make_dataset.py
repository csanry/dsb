import logging
import os
import zipfile

from src import config
from src.helpers import setup_credentials


def make_dataset():

    setup_credentials()
    from kaggle.api.kaggle_api_extended import KaggleApi

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    logger = logging.getLogger()

    api = KaggleApi()
    api.authenticate()

    file_names = [
        "olist_customers_dataset.csv",
        "olist_geolocation_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_order_payments_dataset.csv",
        "olist_order_reviews_dataset.csv",
        "olist_orders_dataset.csv",
        "olist_products_dataset.csv",
        "olist_sellers_dataset.csv",
        "product_category_name_translation.csv",
    ]

    logger.info("Downloading files")
    for file in file_names:
        api.dataset_download_file(
            dataset="olistbr/brazilian-ecommerce",
            file_name=file,
            path=config.RAW_FILE_PATH,
        )

    logger.info("Extracting zip files")
    for file in os.listdir(config.RAW_FILE_PATH):
        if file.endswith(".zip"):
            with zipfile.ZipFile(config.RAW_FILE_PATH / file, "r") as zipref:
                zipref.extractall(path=config.RAW_FILE_PATH)
                os.remove(config.RAW_FILE_PATH / file)

    logger.info("\n".join(os.listdir(config.RAW_FILE_PATH)))

    logger.info("Done")


def main():
    make_dataset()


if __name__ == "__main__":
    main()
