# Kafka Elasticsearch Streaming Example

A simple real-time data streaming project demonstrating how to produce social media interaction events with **Apache Kafka**, consume them using Python, store them in **Elasticsearch**, and analyze them through **Kibana**.

## Overview

This project simulates a real-time social media data pipeline.

The producer generates random social media interaction events such as likes, comments, shares, views, hashtags, locations, and engagement rates. These events are published to an Apache Kafka topic.

The consumer listens to the Kafka topic, processes incoming events, and stores them in Elasticsearch. The indexed data can then be explored and visualized through Kibana.

## Architecture

```text
Python Producer
      |
      v
Apache Kafka
      |
      v
Python Consumer
      |
      v
Elasticsearch
      |
      v
Kibana
```

## Technologies

* Python
* Apache Kafka
* Apache ZooKeeper
* Elasticsearch
* Kibana
* Docker
* Docker Compose
* kafka-python
* Faker

## Project Structure

```text
kafka-elasticsearch-example/
├── consumer/
│   ├── consumer.py
│   └── requirements.txt
├── producer/
│   ├── producer.py
│   └── requirements.txt
├── docker-compose.yml
├── requirements.txt
├── start.sh
└── README.md
```

## How It Works

### Producer

The producer generates a new social media interaction event every two seconds and sends it to the following Kafka topic:

```text
social-media-stream
```

Each generated event contains fields such as:

```json
{
  "event_id": "7ba843fc-5f31-4fb6-b4d4-667268c458fa",
  "post_id": "post_12045",
  "user_id": "user_425",
  "content_type": "video",
  "likes": 1250,
  "comments": 110,
  "shares": 45,
  "views": 8750,
  "hashtags": [
    "technology",
    "software"
  ],
  "post_created_at": "2026-07-10T14:30:00",
  "interaction_timestamp": "2026-07-10T15:15:00",
  "engagement_rate": 16.06,
  "location": "İstanbul",
  "is_viral": false
}
```

The generated values are randomized using the Faker library and Python's random module.

### Consumer

The consumer subscribes to the `social-media-stream` Kafka topic using the following consumer group:

```text
social-media-consumer-group
```

Each received event is written to the following Elasticsearch index:

```text
social-media-events
```

The consumer automatically creates the Elasticsearch index and its mapping if the index does not already exist.

The index contains mappings for:

* Event and post identifiers
* User identifiers
* Content types
* Likes, comments, shares, and views
* Hashtags
* Creation and interaction timestamps
* Engagement rates
* Locations
* Viral content status

## Requirements

Before running the project, make sure the following tools are installed:

* Python 3.9 or later
* Docker
* Docker Compose
* Git

## Installation

Clone the repository:

```bash
git clone https://github.com/Elifakyol1020/kafka-elasticsearch-example.git
cd kafka-elasticsearch-example
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment.

On macOS or Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Infrastructure

Start Kafka, ZooKeeper, Elasticsearch, and Kibana:

```bash
docker compose up -d
```

Check the running containers:

```bash
docker compose ps
```

The following services will be available:

| Service       | Address                 |
| ------------- | ----------------------- |
| Kafka         | `localhost:9092`        |
| ZooKeeper     | `localhost:2181`        |
| Elasticsearch | `http://localhost:9200` |
| Kibana        | `http://localhost:5601` |

You can verify Elasticsearch by opening:

```text
http://localhost:9200
```

## Running the Application

### Option 1: Start Producer and Consumer Together

On macOS or Linux, make the startup script executable:

```bash
chmod +x start.sh
```

Run the script:

```bash
./start.sh
```

The script starts both the producer and consumer processes.

### Option 2: Start Them Manually

Open a terminal and run the producer:

```bash
python producer/producer.py
```

Open another terminal and run the consumer:

```bash
python consumer/consumer.py
```

The producer will continuously publish new events, while the consumer will read and store them in Elasticsearch.

## Exploring the Data in Kibana

Open Kibana:

```text
http://localhost:5601
```

To view the indexed events:

1. Open **Management**.
2. Go to **Stack Management**.
3. Select **Data Views**.
4. Create a new data view.
5. Enter the following index pattern:

```text
social-media-events*
```

6. Select `interaction_timestamp` or `post_created_at` as the timestamp field.
7. Open **Discover** to inspect the events.

You can create visualizations such as:

* Posts grouped by content type
* Average engagement rate
* Viral and non-viral post distribution
* Total likes, comments, shares, and views
* Most frequently used hashtags
* Events grouped by location
* Interaction activity over time

## Elasticsearch Queries

List all indices:

```bash
curl http://localhost:9200/_cat/indices?v
```

Retrieve indexed social media events:

```bash
curl "http://localhost:9200/social-media-events/_search?pretty"
```

Retrieve the total number of indexed documents:

```bash
curl "http://localhost:9200/social-media-events/_count?pretty"
```

Retrieve only viral posts:

```bash
curl -X GET "http://localhost:9200/social-media-events/_search?pretty" \
  -H "Content-Type: application/json" \
  -d '
{
  "query": {
    "term": {
      "is_viral": true
    }
  }
}'
```

## Stopping the Project

Stop the producer and consumer with:

```text
Ctrl + C
```

Stop the Docker services:

```bash
docker compose down
```

To stop the services and remove the Elasticsearch volume:

```bash
docker compose down -v
```

> Removing the volume permanently deletes the indexed Elasticsearch data.

## Main Configuration

The main configuration values are currently defined directly in the Python files.

```python
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "social-media-stream"
ELASTICSEARCH_HOST = "http://localhost:9200"
INDEX_NAME = "social-media-events"
```


## Purpose

This project was created as a practical example of:

* Event-driven architecture
* Producer-consumer communication
* Real-time data streaming
* Kafka consumer groups
* Elasticsearch indexing
* Data visualization with Kibana
* Docker-based local infrastructure

## Author

**Elif Akyol**

* GitHub: [@Elifakyol1020](https://github.com/Elifakyol1020)
