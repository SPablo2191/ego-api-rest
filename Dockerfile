# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements/dev.txt /code/requirements/
RUN pip install -r requirements/dev.txt
COPY . /code/
