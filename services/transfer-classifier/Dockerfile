FROM python:3.14-slim

# Update the package list and upgrade all installed system packages
RUN apt-get update && apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /prmdata
COPY ./src ./src
COPY setup.py .

ARG IMAGE_TAG
ENV BUILD_TAG=${IMAGE_TAG}

RUN pip install --upgrade pip setuptools wheel && \
    pip install .

ENTRYPOINT ["python", "-m", "prmdata.pipeline.main"]
