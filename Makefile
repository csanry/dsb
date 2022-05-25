#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python3


ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

#################################################################################
# COMMANDS             	                                                        #
#################################################################################

## Setup packages
pkg: 
	pip install -e .
    
## Run pipe 
pipe:
	pip install -e .
	python3 $(PROJECT_DIR)/src/ingest/make_dataset.py
	python3 $(PROJECT_DIR)/src/interim/make_transactions_data.py
	python3 $(PROJECT_DIR)/src/interim/make_orders_data.py
	python3 $(PROJECT_DIR)/src/interim/make_customers_data.py
	python3 $(PROJECT_DIR)/src/interim/make_category_data.py
	python3 $(PROJECT_DIR)/src/interim/make_rfm_data.py
	

# Push updates to docker container
docker_push: 
	docker build -t csanry/dsb:latest .
	docker login 
	docker push csanry/dsb:latest

## Clean environment 
clean:
	pre-commit run --all-files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ipynb_checkpoints" -delete
