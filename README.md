# Data Engineering Final Project

1. Realtime map plotting MeetUp RSVP with Venues location.
2. Presenting a static table with the number of event counts in major cities in the US

## Technologies Used and Architecture Diagram

![alt text](https://github.com/derekliu7/DE-Final-Project/blob/master/Architecture.png)

## Data

1. Data retrieved from MeetUp RSVP saved as PARQUET files in S3
2. Only Venues has been used for this project due to time restriction.
3. Other DataFrames will be stored and used for statical analysis in the future

## The Five S's(Stream, Store, Structure, Synthesize, Show)

### Stream
- EC2, Kafka producer/spark consumer

### Store
- S3, WebSocket

### Structure
- S3, Parquet, Pandas DataFrame, png(geoplotlib)

### Synthesize
- EMR, Spark Streaming Kafka, Spark-submit, Spark SKlearn(KMeans)

### Show
- S3, html, Flask
