
FROM python:3.8-slim-buster

WORKDIR /delivery-api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/app.py"]