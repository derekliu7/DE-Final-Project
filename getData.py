import websocket
import yaml
import os
import boto3


def on_message(ws, message):
    client.put_record(DeliveryStreamName='de-final',
                      Record={'Data': message})


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def connect_aws():
    credentials = yaml.load(
        open(os.path.expanduser('~/.ssh/aws_cred.yml')))
    client = boto3.client('firehose',
                          region_name='us-east-1', **credentials['aws'])
    return client


if __name__ == "__main__":
    client = connect_aws()
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://stream.meetup.com/2/rsvps",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
