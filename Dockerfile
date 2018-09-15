FROM python:3.6.4-alpine3.7

RUN apk update && apk add openrc postgresql-dev jpeg-dev zlib-dev gcc musl-dev libxml2-dev libxslt-dev nfs-utils
RUN rc-update add nfsmount default

RUN mkdir /base /join
WORKDIR /base

ENV PYTHONUSERBASE "/join/pythonuserbase"
EXPOSE 8000

VOLUME ["/join/pythonuserbase/", "/base/"]
