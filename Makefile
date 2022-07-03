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

## Launch the project 
project-up: 
	docker compose -f container/docker-compose.yaml up

## Teardown the project
project-down: 
	docker compose -f container/docker-compose.yaml down --rmi all
	 
## Run pipe 
pipe:
	bash run_pipeline.sh

## Push updates to docker container
docker_push: 
	docker build -t csanry/dsb:latest container/.
	docker login 
	docker push csanry/dsb:latest

## Clean environment 
clean:
	pre-commit run --all-files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ipynb_checkpoints" -delete

