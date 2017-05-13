from pyspark import SparkContext
from pyspark.sql import SparkSession
import datetime

time_tuple = str(datetime.date.today())
month = time_tuple[5: 7]
day = time_tuple[8:]
path = 's3a://definal/2017/{}/{}/*/*'.format(month, day)


def readData():
    sc = SparkContext('local[*]')
    spark = SparkSession(sc)
    raw_data = spark.read.json(path)
    filtered_data = raw_data.filter('rsvp_id IS NOT NULL')
    filtered_data.cache()
    return None


def makeRsvp(filtered_data):
    rsvp_df = filtered_data.selectExpr('rsvp_id',
                                       'event.event_id',
                                       'group.group_id',
                                       'member.member_id',
                                       'venue.venue_id',
                                       'guests',
                                       'mtime',
                                       'visibility')
    return rsvp_df


def makeEvent(filtered_data):
    event_df = filtered_data.selectExpr('event.event_id',
                                        'event.event_name',
                                        'event.event_url',
                                        'event.time').filter('event.event_id IS NOT NULL')
    return event_df


def makeGroup(filtered_data):
    group_df = filtered_data.selectExpr('group.group_id',
                                        'group.group_name',
                                        'group.group_topics',
                                        'group.group_city',
                                        'group.group_state',
                                        'group.group_country').filter('group.group_id IS NOT NULL')
    return group_df


def makeMember(filtered_data):
    member_df = filtered_data.selectExpr('member.member_id',
                                         'member.member_name').filter('member.member_id IS NOT NULL')
    return member_df


def makeVenue(filtered_data):
    venue_df = filtered_data.selectExpr('venue.venue_id',
                                        'venue.venue_name',
                                        'venue.lat',
                                        'venue.lon').filter('venue.venue_id IS NOT NULL')
    return venue_df


if __name__ == '__main__':
    filtered_data = readData()
    rsvp_df = makeRsvp(filtered_data)
    event_df = makeEvent(filtered_data)
    group_df = makeGroup(filtered_data)
    member_df = makeMember(filtered_data)
    venue_df = makeVenue(filtered_data)

    title1 = '{}{}'.format('rsvp_df', str(time_tuple))
    title2 = '{}{}'.format('event_df', str(time_tuple))
    title3 = '{}{}'.format('group_df', str(time_tuple))
    title4 = '{}{}'.format('member_df', str(time_tuple))
    title5 = '{}{}'.format('venue_df', str(time_tuple))

    rsvp_df.write.parquet('{}{}'.format('s3a://definal2/rsvp/', title1))
    event_df.write.parquet('{}{}'.format('s3a://definal2/event/', title2))
    group_df.write.parquet('{}{}'.format('s3a://definal2/group/', title3))
    member_df.write.parquet('{}{}'.format('s3a://definal2/member/', title4))
    venue_df.write.parquet('{}{}'.format('s3a://definal2/venueCSV/', title5))
