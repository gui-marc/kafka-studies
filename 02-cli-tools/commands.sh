# In one terminal, access the container:
docker exec -it kafka /bin/bash
# Then run the following commands to create a topic and produce/consume messages.
# Create a topic named 'test-topic'
/opt/kafka/bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092
# List all topics
/opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
# Produce messages to 'test-topic'
/opt/kafka/bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
# Consume messages from 'test-topic'
/opt/kafka/bin/kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092
# To exit the producer or consumer, use Ctrl+C
