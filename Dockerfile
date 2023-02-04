FROM python:3.10.9-alpine

WORKDIR /api/

EXPOSE 8000

COPY . .

RUN apk add --update libpq-dev python3-dev build-essential
RUN pip install -r requirements.txt

CMD python3 main.py
