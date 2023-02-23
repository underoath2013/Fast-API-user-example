FROM python:3.11.0-alpine

WORKDIR /app

EXPOSE 8000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api .



