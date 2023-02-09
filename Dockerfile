FROM ubuntu:22.04

WORKDIR /api/

EXPOSE 8000

COPY . .

RUN apt-get update && apt-get --no-install-recommends --no-upgrade -y install libpq-dev python3-dev build-essential python3-pip
RUN pip install -r requirements.txt

CMD flask db upgrade && python3 main.py
