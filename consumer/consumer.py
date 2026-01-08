import json
import time
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from datetime import datetime

KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'social-media-stream'
GROUP_ID = 'social-media-consumer-group'

ELASTICSEARCH_HOST = 'http://localhost:9200'
INDEX_NAME = 'social-media-events'

es = Elasticsearch(
    [ELASTICSEARCH_HOST],
    request_timeout=30
)

def create_index_mapping():
    mapping = {
        "mappings": {
            "properties": {
                "event_id": {"type": "keyword"},
                "post_id": {"type": "keyword"},
                "user_id": {"type": "keyword"},
                "content_type": {"type": "keyword"},
                "likes": {"type": "integer"},
                "comments": {"type": "integer"},
                "shares": {"type": "integer"},
                "views": {"type": "integer"},
                "hashtags": {"type": "keyword"},
                "post_created_at": {"type": "date"},
                "interaction_timestamp": {"type": "date"},
                "engagement_rate": {"type": "float"},
                "location": {"type": "keyword"},
                "is_viral": {"type": "boolean"}
            }
        },
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    }
    
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body=mapping)
        print(f"Elasticsearch index olusturuldu: {INDEX_NAME}")
    else:
        print(f"Elasticsearch index zaten mevcut: {INDEX_NAME}")


def create_consumer():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=[KAFKA_BROKER],
        group_id=GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        auto_commit_interval_ms=1000
    )
    return consumer


def index_to_elasticsearch(event):
    try:
        response = es.index(
            index=INDEX_NAME,
            id=event['event_id'],
            document=event
        )
        return response
    except Exception as e:
        print(f"Elasticsearch'e yazma hatasi: {e}")
        return None


def main():
    print(f"Kafka Consumer baslatiliyor...")
    print(f"Kafka Broker: {KAFKA_BROKER}")
    print(f"Topic: {TOPIC_NAME}")
    print(f"Elasticsearch: {ELASTICSEARCH_HOST}")
    print(f"Index: {INDEX_NAME}")
    print("-" * 60)
    
    create_index_mapping()
    
    consumer = create_consumer()
    
    print(f"Consumer hazir. Veri bekleniyor...\n")
    
    processed_count = 0
    error_count = 0
    
    try:
        for message in consumer:
            event = message.value
            processed_count += 1
            
            result = index_to_elasticsearch(event)
            
            if result:
                print(f"[{processed_count}] Islendi: Post {event['post_id']} | "
                      f"Begeni: {event['likes']} | "
                      f"ES ID: {result['_id']}")
            else:
                error_count += 1
                print(f"[{processed_count}] Hata: Post {event['post_id']} islenemedi")
            
            if processed_count % 10 == 0:
                print(f"\nIstatistik: {processed_count} islendi, {error_count} hata\n")
            
    except KeyboardInterrupt:
        print("\n\nConsumer durduruldu.")
        print(f"Toplam {processed_count} adet veri islendi.")
        print(f"Toplam {error_count} adet hata olustu.")
    except Exception as e:
        print(f"\nHata olustu: {e}")
    finally:
        consumer.close()
        print("Kafka consumer kapatildi.")


if __name__ == '__main__':
    main()
