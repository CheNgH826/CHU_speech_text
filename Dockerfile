FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y apt-transport-https \
&& apt-get update \
&& apt-get install -y tzdata \
&& apt-get install -y python3-pip python3-dev \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip \
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 \
&& echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list \
&& apt-get update \
&& apt-get install -y mongodb-org \
&& apt install sqlite3 \
&& apt-get install -y alsa-base alsa-utils \
&& apt-get install -y portaudio19-dev

COPY ./setup/requirements.txt /opt/app/requirements.txt
COPY ./setup/db_init.py /opt/app/db_init.py

RUN cd /opt/app/ \
&& pip install -r requirements.txt \
&& python db_init.py

ENTRYPOINT mongod --dbpath dock/database/mongodb