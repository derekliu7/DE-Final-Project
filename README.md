# Data Engineering Final Project
-- Use everything I've learned in this course. That's right!

  __Current__:
- Geographically plotting clusters of events based on location
- Spark streaming numbers of event for cities in the U.S.

## Technology and Architecture Diagram

![alt text](https://github.com/derekliu7/DE-Final-Project/blob/master/Architecture.png)

## Data

- Data retrieved from MeetUp RSVP saved as __parquet__ files in S3
- Only __Venues__ table has been used for this project due to time restriction
- Other DataFrames will be stored and used for statical analysis in the future

## The Five S's(Stream, Store, Structure, Synthesize, Show)

### Stream
- EC2, WebSocket, Request

### Store
- S3, Firehose, Spark

### Structure
- S3, Parquet, Pandas DataFrame, png(Geoplotlib)

### Synthesize
- EMR, Spark Streaming Kafka, Spark-submit, Spark SKlearn(KMeans)

### Show
- S3, html, Flask


## The Eight properties

![alt text](https://www.cinemaz.com/images/stories/immagini_2016/the-hateful-eight/the-hateful-eight-copia-pirata.jpg)

### Robustness and fault tolerance
- Data are stored in AWS
- Divided and stored in multiple folders in S3

### Low latency reads and updates
- spark-submit script(reads parquet, divides and stores, plot and save, push to s3) daily
- spark streaming

### Scalability
- huh?

### Generalization
- code can be worked on all other tables

### Extensibility
- the ML model will need to take all historical data
- spark streaming city counts can be reset(maybe daily?)

### Ad hoc queries
- huh?

### Minimal maintenance
- batch - spin a cluster and run the spark-submit script, shut it off
- spark streaming will take place on EC2.

### Debuggability
- Avoid running Kafka server locally (Extremely difficult to debug)
- Make a new Instance

## Obstacles

- Difficult to set up spark streaming Kafka

- Extremely messy descriptions of the MeetUp events made categorization difficult

## Visionary

- Cluster event descriptions using deep learning processing(eg: word2vec)

- Update the current map: Label and categorize major cities based on the cluster of descriptions(eg: San Francisco: Tech, Los Angeles: Entertainment, Tokyo: Anime Expo...)

- Make a Realtime event counting table(JavaScript!!! Dam!!!)

https://s3.amazonaws.com/clustermapbucket/geohtml
