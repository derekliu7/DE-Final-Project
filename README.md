# Data Engineering Final Project
-- __Intention__: Use every technology I've learned in this course. 

  __Current__:
- Geographically plotting clusters of events based on location
- Spark streaming numbers of event for cities in the U.S.

## Technology and Architecture Diagram

<img src="https://github.com/derekliu7/DE-Final-Project/blob/master/Architecture.png" width="800" height="500" />

## Data

![](https://github.com/derekliu7/DE-Final-Project/blob/master/Table%20Diagram.png)

- Data retrieved from MeetUp RSVP saved as __parquet__ files in S3
- Only __Venues__ table has been used for this project due to time restriction
- Other DataFrames will be stored and used for statical analysis in the future

## The Five S's(Stream, Store, Structure, Synthesize, Show)

### Stream
- __WebSocket__: pull data from MeetUp API
- __Kafka__: producer sends data into 'meetup' topic

### Store
- __Kinesis__: raw data stored in S3 using Kinesis Firehose
- __Boto3__: image of the graph

### Structure
- __Spark__: Parquet, Pandas DataFrame, png(Geoplotlib)

### Synthesize
- __EMR__: Spark Streaming Kafka, Spark-submit, Spark SKlearn(KMeans)

### Show
- __S3__, html static webpage
- __Geoplotlib__: map plot


## The Eight properties

![](https://www.cinemaz.com/images/stories/immagini_2016/the-hateful-eight/the-hateful-eight-copia-pirata.jpg)

### Robustness and fault tolerance
- HIGHLY rely on the stability of AWS(S3, EC2 single instance, EMR cluster)
- Kafka sever running on one single instance

### Low latency reads and updates
- spark-submit script(reads parquet, divides and stores, plot and save, push to s3) daily
- spark streaming(mini batches)

### Scalability
- Replace html with Flask(including multiple plots with plotly)

### Generalization
- code can be worked on all other tables

### Extensibility
- the ML model will need to take all historical data
- spark streaming city counts can be reset(maybe daily?)

### Ad hoc queries
- batch script needs to be manually ran once a daily
- real-time streaming data frame is not showing ATM

### Minimal maintenance
- batch - spin a cluster and run the spark-submit script, shut it off
- spark streaming will take place on EC2.

### Debuggability
- Avoid running Kafka server locally (Extremely difficult to debug)
- can be improved by having an alert script, warning when EC2 is down

# Obstacles

- Difficult to set up spark streaming Kafka

- Extremely messy descriptions of the MeetUp events made categorization difficult

# Visionary

- Cluster event descriptions using deep learning processing(eg: word2vec)

- Update the current map: Label and categorize major cities based on the cluster of descriptions(eg: San Francisco: Tech, Los Angeles: Entertainment, Tokyo: Anime Expo...)

- Make a real-time event counting table

https://s3.amazonaws.com/clustermapbucket/geohtml
