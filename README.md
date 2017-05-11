# Data Engineering Final Project

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
- EC2, Kafka producer/spark consumer

### Store
- S3, WebSocket

### Structure
- S3, Parquet, Pandas DataFrame, png(Geoplotlib)

### Synthesize
- EMR, Spark Streaming Kafka, Spark-submit, Spark SKlearn(KMeans)

### Show
- S3, html, Flask

## Obstacles

- Difficult to set up spark streaming Kafka

- Extremely messy descriptions of the MeetUp events made categorization difficult

## Visionary

- Cluster event descriptions using deep learning processing(eg: word2vec)

- Update the current map: Label and categorize major cities based on the cluster of descriptions(eg: San Francisco: Tech, Los Angeles: Entertainment, Tokyo: Anime Expo...)

- Make a Realtime event counting table(JavaScript!!! Dam!!!)
