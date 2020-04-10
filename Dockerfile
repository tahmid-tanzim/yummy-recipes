FROM python:3.7-alpine
MAINTAINER One Eleven Ltd.

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /recipe_app
WORKDIR /recipe_app
COPY ./main /recipe_app

RUN adduser -D superuser
USER superuser

ENTRYPOINT []
CMD []