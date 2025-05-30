import time
import random
import json
from kafka import KafkaProducer
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8')
)

def generate_temperature_data():
    return {
        'sensor_id': str(random.randint(1, 50)),
        'temperature': round(random.uniform(-10.0, 40.0), 2),
        'timestamp': fake.date_time().isoformat()
    }

if __name__ == "__main__":
    topic = 'test-topic'

    while True:
        data = generate_temperature_data()
        print(f"Producing: {data}")
        key = data['sensor_id']
        producer.send(topic, key=key, value=data)
        time.sleep(1)  # Simulate a delay between messages