import json
import time
import requests
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
url= (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=52.52&longitude=13.41"
    "&hourly=temperature_2m,relative_humidity_2m,"
    "pressure_msl"
)

While True:
    response = requests.get(url)
    data = response.json()
    producer.send('weather_data', data)
    time.sleep(60)