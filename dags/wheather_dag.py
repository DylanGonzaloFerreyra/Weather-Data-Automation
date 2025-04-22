from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from fetch_weather import fetch_and_store_weather


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 1), 
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "weather_data_pipeline", 
    default_args=default_args,
    description="Pipeline para obtener y almacenar datos meteorológicos",
    schedule_interval="0 * * * *", 
)

fetch_weather_task = PythonOperator(
    task_id="fetch_weather",  
    python_callable=fetch_and_store_weather, 
    dag=dag,
)