FROM python:3.12-alpine

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
ADD . .

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt

EXPOSE 5000