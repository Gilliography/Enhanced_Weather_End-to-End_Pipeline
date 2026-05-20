import json
import requests
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=52.52&longitude=13.41"
    "&hourly=temperature_2m,relative_humidity_2m,pressure_msl"
)

response = requests.get(url)

data = response.json()

hourly = data["hourly"]

for i in range(len(hourly["time"])):

    record = {
        "time": hourly["time"][i],
        "temperature_2m": hourly["temperature_2m"][i],
        "relative_humidity_2m": hourly["relative_humidity_2m"][i],
        "pressure_msl": hourly["pressure_msl"][i]
    }

    producer.send("weather-events", record)

producer.flush()

print("Weather rows sent to Kafka")