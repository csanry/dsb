ISSS621 - Data Science for Business - Closed Loop Data Ecosystem
==============================

Table of Contents
------------

| S/NO | Section |
| --- | --- |
| 1. | [About this Project](#1) | 
| 2. | [Setup Environment](#2) | 
| 3. | [Teardown Environment](#3) | 
| 4. | [Download Data](#4) |
| 5. | [Run the MBA Analysis](#5) |
| 4. | [Project Organization](#4) | 
| 5. | [Workflow](#5) | 
| 6. | [Development Workflow](#6) | 
| 7. | [Pull Requests](#7) | 

About this Project <a name="1"></a>
------------

OList info and background here 


```text
template writeup
```


Setup Environment <a name="2"></a>
------------

### Prerequisties 

* Download and install [anaconda](https://www.anaconda.com/products/distribution) 

* Download [docker](https://www.docker.com/products/docker-desktop/) 

* Download [git](https://git-scm.com/downloads) 


In your terminal of choice, run the following terminal commands 

```bash
git clone https://github.com/csanry/dsb.git
cd dsb
```

Ensure that you are logged into docker hub. Then run the following command to set up the docker environment 

```bash
docker login
docker-compose up
```

The command launches an Ubuntu-based distro, and a Jupyter Lab environment for running the pipelines. Launch the Lab environment from the terminal by clicking on the generated URL

In the environment, run the following commands in an open terminal 

```bash
cd project
bash run_pipeline.sh
```

Check that the environment is properly set up using the following command

```bash
make test_environment
```

Project Organization <a name="3"></a>
------------

The repository is structured with the following hierarchy

```
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── fin
│   ├── int
│   │   ├── category_agg.parquet
│   │   ├── cust_agg.parquet
│   │   ├── orders_agg.parquet
│   │   ├── rfm.parquet
│   │   └── transactions.parquet
│   └── raw
│       ├── olist_customers_dataset.csv
│       ├── olist_geolocation_dataset.csv
│       ├── olist_order_items_dataset.csv
│       ├── olist_order_payments_dataset.csv
│       ├── olist_order_reviews_dataset.csv
│       ├── olist_orders_dataset.csv
│       ├── olist_products_dataset.csv
│       ├── olist_sellers_dataset.csv
│       └── product_category_name_translation.csv
├── docker-compose.yaml
├── environment.yaml
├── image
├── notebooks
│   ├── delivery.ipynb
│   ├── eda_customers.ipynb
│   ├── eda_products.ipynb
│   ├── geospacial.ipynb
│   ├── mba_analysis.ipynb
│   ├── missingness_transactions.ipynb
│   ├── recommender.ipynb
│   ├── rfm.ipynb
│   └── time_series.ipynb
├── run_pipeline.sh
├── setup.py
└── src
    ├── __init__.py
    ├── config.py
    ├── helpers
    │   ├── __init__.py
    │   ├── missingness_checks.py
    │   ├── quick_eda.py
    │   ├── setup_credentials.py
    │   └── standardize_cols.py
    ├── ingest
    │   ├── __init__.py
    │   └── make_dataset.py
    ├── interim
    │   ├── __init__.py
    │   ├── make_category_data.py
    │   ├── make_customers_data.py
    │   ├── make_orders_data.py
    │   ├── make_rfm_data.py
    │   └── make_transactions_data.py
    ├── make_transactions_data.py
    └── preprocessing.py
```