import os
import json
from time import sleep
from kafka import KafkaProducer
from kafka import KafkaConsumer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
LEGIT_TOPIC = os.environ.get('LEGIT_TOPIC')
FRAUD_TOPIC = os.environ.get('FRAUD_TOPIC')

# check whether a transaction is fraud or not
def is_fraud_transaction(transaction):
    return transaction['amount'] >= 2000

if __name__ == "__main__":
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    for message in consumer:
        transaction: dict = message.value
        if is_fraud_transaction(transaction):
            topic = FRAUD_TOPIC
        else:
            topic = LEGIT_TOPIC
        producer.send(topic, value=transaction)
        print(topic, transaction)
