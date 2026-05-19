import json
import requests
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time

url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=52.52&longitude=13.41"
    "&hourly=temperature_2m"
)

for i in range(10):

    try:

        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        response = requests.get(url)

        data = response.json()

        producer.send("weather-events", data)

        producer.flush()

        print("Weather event sent successfully")

        break

    except NoBrokersAvailable:

        print("Kafka not ready yet... retrying")

        time.sleep(5)