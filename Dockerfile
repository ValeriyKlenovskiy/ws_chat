FROM python:3.9

RUN mkdir /chat

WORKDIR /chat

COPY req.txt .

RUN pip install -r req.txt

COPY . .