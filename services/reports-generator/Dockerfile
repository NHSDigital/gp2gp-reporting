FROM python:3.14-slim

COPY . /prmreportsgenerator

ARG IMAGE_TAG
ENV BUILD_TAG=${IMAGE_TAG}

RUN pip install setuptools && \
    cd /prmexporter && \
    python setup.py install

ENTRYPOINT ["python", "-m", "prmreportsgenerator.main"]
