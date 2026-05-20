import json
import pandas as pd
from kafka import KafkaConsumer
from sqlalchemy import create_engine

consumer = KafkaConsumer(
    'weather-events',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

print("Consumer started...")

for message in consumer:

    data = message.value

    df = pd.DataFrame([data])

    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",
        index=False
    )

    print("Inserted row into PostgreSQL")