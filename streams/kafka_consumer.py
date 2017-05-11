from kafka import KafkaConsumer
import json

if __name__ == '__main__':

    consumer = KafkaConsumer('meetup',
                             group_id='1',
                             bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    for message in consumer:
        # print(message)
        data = str(message.value)
        print(data)
