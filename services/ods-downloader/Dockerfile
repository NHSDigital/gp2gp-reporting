FROM python:3.14-slim

COPY . /prmods

ARG IMAGE_TAG
ENV BUILD_TAG=${IMAGE_TAG}

RUN pip install --upgrade pip && \
    pip install setuptools && \
    cd /prmods && \
    python setup.py install

ENTRYPOINT ["python", "-m", "prmods.pipeline.main"]
