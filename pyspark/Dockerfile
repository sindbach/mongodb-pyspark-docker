FROM ubuntu:14.04

# See https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update -y \
    && apt-get install -y wget python-dev openjdk-7-jre-headless python-pip nano\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

RUN pip install pymongo

RUN useradd --create-home --shell /bin/bash ubuntu 

ENV HOME /home/ubuntu
ENV SPARK_VERSION 1.6.2
ENV HADOOP_VERSION 2.6
ENV MONGO_SPARK_VERSION 1.0.0
ENV SCALA_VERSION 2.10

WORKDIR ${HOME}

ENV SPARK_HOME ${HOME}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}

ENV PATH $PATH:${SPARK_HOME}/bin

COPY files/times.json /home/ubuntu/times.json
COPY files/readme.txt /home/ubuntu/readme.txt
COPY files/examples.py /home/ubuntu/examples.py
COPY files/initDocuments.py /home/ubuntu/initDocuments.py

RUN chown -R ubuntu:ubuntu /home/ubuntu/* 

USER ubuntu 

# get spark 
RUN wget http://apache.mirror.digitalpacific.com.au/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
tar xvf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

RUN rm -fv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
