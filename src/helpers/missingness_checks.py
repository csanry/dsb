import logging

import matplotlib.pyplot as plt
import missingno as msno


def missingness_checks(df):

    log_fmt = "%(asctime)s:%(name)s:%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()

    logger.info(f"Number of missing columns: {df.isna().sum().sum()}")
    logger.info(
        f"Missing columns (0: No missing values, 1: Missing values) {df.isna().sum()}"
    )
    logger.info(f"Missingness through the data")

    msno.matrix(df)
    plt.show()

    logger.info("Missingness correlations")
    msno.heatmap(df)
    plt.show()
