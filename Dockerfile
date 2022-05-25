FROM ubuntu:18.04

SHELL ["bin/bash", "-c"]

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update &&\
    apt install -y python3-dev wget build-essential nano &&\
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
    mkdir root/.conda &&\
    sh Miniconda3-latest-Linux-x86_64.sh -b &&\
    rm -f Miniconda3-latest-Linux-x86_64.sh &&\
    mkdir project

COPY . project/

RUN conda env create -f project/environment.yaml