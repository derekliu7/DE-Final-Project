#!/bin/bash

sudo apt-get update -y
sudo apt install python3-pip -y
sudo python3 -m pip install pip boto3 websocket-client -U
