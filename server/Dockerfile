FROM python:3-alpine
MAINTAINER Raseel Bhagat <raseelbhagat@gmail.com>

COPY live-location-tracker /live-location-tracker
COPY entrypoint.sh /entrypoint.sh
WORKDIR /live-location-tracker
RUN apk update && apk add gcc libc-dev linux-headers mariadb-dev python3-dev mysql-client && pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
