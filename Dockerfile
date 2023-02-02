FROM python:3.10.9-alpine

WORKDIR /api/

EXPOSE 8000

COPY . .

RUN pip install -r requirements.txt

CMD python3 api.py
