from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start reading at the earliest message
    enable_auto_commit=True,  # Automatically commit offsets
    group_id='test-group',  # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # Deserialize message value
)

if __name__ == "__main__":
    print("Consumer started. Waiting for messages...")
    try:
        for message in consumer:
            # Each message is a ConsumerRecord object
            print(f"Received message: {message.value} from key: {message.key.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()  # Close the consumer connection