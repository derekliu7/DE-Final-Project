#!/usr/bin/env python3
import websocket
import json
from kafka import KafkaProducer


def on_message(ws, message):
    producer.send('meetup', message)
    producer.flush()


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


if __name__ == "__main__":

    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                             bootstrap_servers=['localhost:9092'])

    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://stream.meetup.com/2/rsvps",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
