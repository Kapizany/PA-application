FROM ubuntu:22.04

WORKDIR /api/

EXPOSE 8000

COPY . .

RUN chmod +x ./start.sh

RUN apt-get update && apt-get --no-install-recommends --no-upgrade -y install libpq-dev python3-dev build-essential python3-pip
RUN pip install -r requirements.txt

CMD ./start.sh
