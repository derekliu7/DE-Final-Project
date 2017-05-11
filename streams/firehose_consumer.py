#!/usr/bin/env python3
from kafka import KafkaConsumer
import json
import os
import yaml
import boto3


if __name__ == '__main__':

    # get aws credentials
    credentials = yaml.load(open(os.path.expanduser('~/.ssh/api_cred.yml')))

    # connect to kinesis firehose
    client = boto3.client('firehose',
                          region_name='us-east-1',
                          **credentials['aws'])

    consumer = KafkaConsumer('meetup',
                             group_id='rsvp',
                             bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    # deliver to S3
    for message in consumer:
        # print(message)
        data = str(message.value)
        client.put_record(DeliveryStreamName='de-final',
                          Record={'Data': data})
