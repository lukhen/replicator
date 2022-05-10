FROM python:3.10.2-alpine

RUN apk update && \
    apk add --no-cache postgresql-dev; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    rust \
    && pip install --upgrade pip \
    && pip install mysql-replication==0.26 \
    && pip install pg_chameleon \
    && pip install --upgrade pip \
    && pip install cryptography \
    && apk del --no-cache .build-deps

RUN apk add netcat-openbsd

RUN adduser pg -D
USER pg
WORKDIR /home/pg

COPY . /home/pg
HEALTHCHECK CMD chameleon show_status --config default --source mysql | grep -Eq ^.*mysql.*running.*$
CMD ["sh", "./wait-for.sh", "-t", "90", "mysqldb:3306", "--", "sh", "start-script.sh"]
