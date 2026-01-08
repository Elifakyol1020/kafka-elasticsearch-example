import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer
from faker import Faker

fake = Faker('tr_TR')

KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'social-media-stream'

CONTENT_TYPES = ['photo', 'video', 'text', 'story', 'reel']

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None
)


def generate_social_media_event():
    post_created_at = fake.date_time_between(start_date='-7d', end_date='now')
    interaction_time = fake.date_time_between(start_date=post_created_at, end_date='now')
    
    population = list(range(0, 10000))
    weights = [50] * 1000 + [30] * 2000 + [15] * 3000 + [4] * 3000 + [1] * 1000
    likes = random.choices(population, weights=weights)[0]
    
    comments = int(likes * random.uniform(0.05, 0.15))
    shares = int(likes * random.uniform(0.01, 0.05))
    views = likes * random.randint(3, 10)
    
    event = {
        'event_id': fake.uuid4(),
        'post_id': f"post_{random.randint(1000, 999999)}",
        'user_id': f"user_{random.randint(1, 50000)}",
        'content_type': random.choice(CONTENT_TYPES),
        'likes': likes,
        'comments': comments,
        'shares': shares,
        'views': views,
        'hashtags': [fake.word() for _ in range(random.randint(0, 5))],
        'post_created_at': post_created_at.isoformat(),
        'interaction_timestamp': interaction_time.isoformat(),
        'engagement_rate': round((likes + comments + shares) / max(views, 1) * 100, 2),
        'location': fake.city() if random.random() > 0.3 else None,
        'is_viral': True if likes > 5000 or shares > 200 else False
    }
    
    return event


def main():
    print(f"Sosyal Medya Veri Ureticisi baslatiliyor...")
    print(f"Kafka Broker: {KAFKA_BROKER}")
    print(f"Topic: {TOPIC_NAME}")
    print(f"Her 2 saniyede bir veri gonderilecek...")
    print("-" * 60)
    
    event_count = 0
    
    try:
        while True:
            event = generate_social_media_event()
            event_count += 1
            
            producer.send(
                TOPIC_NAME,
                key=event['post_id'],
                value=event
            )
            
            viral_status = "Viral" if event['is_viral'] else "Normal"
            print(f"[{event_count}] Gonderildi: Post {event['post_id']} | "
                  f"Tur: {event['content_type']} | "
                  f"Begeni: {event['likes']} | "
                  f"Yorum: {event['comments']} | "
                  f"Paylasim: {event['shares']} | "
                  f"Viral: {viral_status}")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\nVeri uretimi durduruldu.")
        print(f"Toplam {event_count} adet veri gonderildi.")
    except Exception as e:
        print(f"\nHata olustu: {e}")
    finally:
        producer.close()
        print("Kafka producer kapatildi.")


if __name__ == '__main__':
    main()
