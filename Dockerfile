FROM python:3.12-alpine

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
ADD . .

RUN apk update
RUN apk add --no-cache gcc musl-dev linux-headers openssh-client iproute2
RUN pip install -r requirements.txt


# RUN ip route add 172.17.254.45 via $(ip route | grep default | awk '{print $3}')

EXPOSE 5000