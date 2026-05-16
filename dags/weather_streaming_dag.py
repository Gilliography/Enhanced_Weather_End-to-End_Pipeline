from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
}

def run_producer():
    subprocess.run(
        ['python', "/opt/airflow/dags/producer.py"]
        check=True
    )