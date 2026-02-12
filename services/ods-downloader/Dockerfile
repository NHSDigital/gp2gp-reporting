FROM python:3.14-slim

WORKDIR /prmods
COPY . .

ARG IMAGE_TAG
ENV BUILD_TAG=${IMAGE_TAG}

RUN pip install --upgrade pip setuptools wheel && \
    pip install .

ENTRYPOINT ["python", "-m", "prmods.pipeline.main"]
