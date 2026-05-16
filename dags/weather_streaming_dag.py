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

with DAG(
    dag_id='weather_streaming_dag',
    default_args=default_args,
    schedule_interval='*/5 * * * *',
    catchup=False
) as dag:
    producer_task = PythonOperator(
        task_id=send_weather_dag_to_kafka,
        python_callable=run_producer
    )
