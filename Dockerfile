FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    ALLURE_VERSION=2.36.0\
    WORKDIR=/usr/workspace


RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl tar openjdk-21-jre-headless \
 && rm -rf /var/lib/apt/lists/*

RUN curl -fsSLo /tmp/allure.tgz "https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz" \
 && tar -xzf /tmp/allure.tgz -C /opt \
 && ln -sf /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure \
 && rm -f /tmp/allure.tgz \
 && allure --version

WORKDIR /usr/workspace

COPY requirements.txt /usr/workspace/requirements.txt

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir playwright \
 && playwright install --with-deps chromium

COPY . /usr/workspace
