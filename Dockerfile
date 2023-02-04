FROM ubuntu:22.04

WORKDIR /api/

EXPOSE 8000

COPY . .

RUN apt-get install libpq-dev python3-dev build-essential
RUN pip install -r requirements.txt

CMD python3 main.py
