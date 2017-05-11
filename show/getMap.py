import geoplotlib
from Kmeanslayer import KMeansLayer
from pyspark.sql import SparkSession
from pyspark import SparkContext
from boto.s3.connection import S3Connection


def getData():
    '''
    going over to S3 and converting all parquet files to Pandas dataframe
    '''
    sc = SparkContext('local[*]')
    spark = SparkSession(sc)

    parqfile = spark.read.parquet(
        's3a://definal2/venueCSV/*')
    data = parqfile.toPandas()
    return data


def makeMap(data):
    '''
    1. use Kmeans cluster lat and lon of each rsvp event
    2. plot them on a world map
    3. take a screenshot of the map and save
    '''
    geoplotlib.add_layer(KMeansLayer(data))
    geoplotlib.set_smoothing(True)
    geoplotlib.set_bbox(geoplotlib.utils.BoundingBox.WORLD)
    geoplotlib.savefig('clustermap')
    return None


def uploadToS3():
    '''
    1. upload the map to S3
    2. make a html that shows the map
    '''
    conn = S3Connection()
    bucket = conn.get_bucket('clustermapbucket')
    pic = bucket.new_key('clustermap')
    pic.content_type = 'image/png'
    pic.set_contents_from_filename('clustermap.png', policy='public-read')

    map_html = '''<!DOCTYPE html>
    <html>
      <body>
        <img src="clustermap">
      </body>
    </html>
    '''
    webpage = bucket.new_key('geohtml')
    webpage.content_type = 'html'
    webpage.set_contents_from_string(map_html, policy='public-read')
    return None


if __name__ == '__main__':
    data = getData()
    makeMap(data)
    uploadToS3()

# https://s3.amazonaws.com/clustermapbucket/geohtml
