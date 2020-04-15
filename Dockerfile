FROM python:3.7-alpine
MAINTAINER One Eleven Ltd.

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc \
    libc-dev \
    linux-headers \
    postgresql-dev \
    musl-dev \
    zlib \
    zlib-dev

RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir /recipe_app
WORKDIR /recipe_app
COPY ./main /recipe_app

RUN mkdir -p /volume/web/media
RUN mkdir -p /volume/web/static

RUN adduser -D superuser
RUN chown -R superuser:superuser /volume/
RUN chmod -R 755 /volume/web
USER superuser

ENTRYPOINT []
CMD []