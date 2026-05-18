from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

def run_producer():
    result = subprocess.run(
        ["python3", "/opt/airflow/kafka/producer.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        raise Exception(result.stderr)

with DAG(
    dag_id="weather_streaming_pipeline",
    default_args=default_args,
    schedule="*/5 * * * *",
    catchup=False
) as dag:

    producer_task = PythonOperator(
        task_id="send_weather_to_kafka",
        python_callable=run_producer
    )