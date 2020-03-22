FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
