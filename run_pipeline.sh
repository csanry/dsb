#!/bin/bash

source activate dsb

pip install -e . 

python3 src/ingest/make_dataset.py &&\
python3 src/interim/make_transactions_data.py &&\
python3 src/interim/make_orders_data.py &&\ 
python3 src/interim/make_customers_data.py &&\ 
python3 src/interim/make_category_data.py &&\
python3 src/interim/make_rfm_data.py 
