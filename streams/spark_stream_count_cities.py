import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def countUpdate(newCount, oldCount):
    if oldCount is None:
        oldCount = 0
    return sum(newCount) + oldCount


if __name__ == '__main__':
    sc = SparkContext(appName='CityCount')
    sc.setLogLevel('ERROR')
    ssc = StreamingContext(sc, 5)

    zkQuorum, topic = 'localhost:2181', 'meetup'
    k = KafkaUtils.createStream(ssc, zkQuorum, 'rsvp', {topic: 1})
    r = k.map(lambda x: x[1])
    r_json = r.map(lambda x: json.loads(x))
    r_us = r_json.filter(lambda x: x['group']['group_country'] == 'us')
    r_cityPair = r_us.map(lambda x: (x['group']['group_city'], 1))
    r_stateCount = r_cityPair.updateStateByKey(countUpdate)

    # producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'),
    #                          bootstrap_servers=['localhost:9092'])
    r_stateCount.pprint()
    # k.pprint()
    ssc.checkpoint('checkpoint')
    ssc.start()
    ssc.awaitTermination()
