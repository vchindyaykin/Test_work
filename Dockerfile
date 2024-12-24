FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && apt-get clean

RUN apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean


ENV driver_type='docker'
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromium-driver

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "pytest tests/"]
