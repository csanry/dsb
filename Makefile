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

pipe:
	python3 $(PROJECT_DIR)/src/make_dataset.py
	python3 $(PROJECT_DIR)/src/make_transactions_data.py
	python3 $(PROJECT_DIR)/src/preprocessing.py