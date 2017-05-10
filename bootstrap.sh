#!/bin/bash

# things I need
sudo yum install -y python35-pip python35-devel
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install boto boto3 pandas websocket-client numpy pyyaml spark-sklearn requests Flask jupyter matplotlib scipy kafka-python -U
# sudo python3 -m pip install geoplotlib pyglet -U
# testing connection
# telnet localhost 2181

wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_2.10/2.1.0/spark-streaming-kafka-0-8-assembly_2.10-2.1.0.jar
# make directory
mkdir -p ~/Downloads && cd ~/Downloads

# download kafka
wget http://mirrors.gigenet.com/apache/kafka/0.10.2.1/kafka_2.12-0.10.2.1.tgz

mkdir -p ~/kafka && cd ~/kafka

tar -xvzf ~/Downloads/kafka_2.12-0.10.2.1.tgz --strip 1

# start kafka
nohup bin/kafka-server-start.sh config/server.properties &
