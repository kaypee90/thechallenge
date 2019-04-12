FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /config

ADD /config/requirements.txt /config/

RUN pip install -r /config/requirements.txt

RUN mkdir /src && cd src && mkdir /take_home;

WORKDIR /src/take_home
