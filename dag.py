from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owners': 'airflow',
    'start_date': datetime.today() - timedelta(days=1)

def etl_tasks():
    with DAG('extract_dag', start_date=datetime(2022, 1, 1),
             schedule_interval='@once',
             catchup=False,
             default_args=default_args) as dag:

        extract_tasks = [PythonOperator(
            task_id=f'api_{types}_request.py',
            python_callable = etl_tasks,
            op_kawrgs={'api': types }
        ) for types in ['cover', 'game', 'gamemode', 'genre', 'platform']]


# for api [extract tasks] >> [create_db, initial import] >>
# [gamemode, genre, platform] >> transform >> add tables >> load