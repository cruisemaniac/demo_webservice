FROM python:3.7.3-alpine3.8
MAINTAINER mail@cruisemaniac.com
RUN apk add --no-cache mariadb-dev build-base
ADD requirements.txt /
RUN pip install -r /requirements.txt

COPY ./ /code
WORKDIR /code

CMD [ "python", "app.py" ]