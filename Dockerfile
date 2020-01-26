FROM python:3.8-alpine

# Install dependencies required for psycopg2
RUN apk update && apk add libpq && \
    apk update && apk add --virtual .build-deps gcc \
                                                libxml2-dev \
                                                libxslt-dev \
                                                python3-dev \
                                                musl-dev \
                                                postgresql-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./main ./main
COPY .env .env
COPY manage.py manage.py

# Remove dependencies only required for psycopg2 build
RUN apk del .build-deps

EXPOSE 18000

CMD ["gunicorn", "-b", "0.0.0.0:18000", "--reload", "--workers", "6", "main.wsgi", "--timeout", "300"]
