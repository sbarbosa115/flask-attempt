FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-virtualenv python-dev build-essential supervisor

COPY . /root/analytics
WORKDIR /root/analytics/
COPY Docker/conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN pip install -r /root/analytics/requirements.txt

EXPOSE 5000