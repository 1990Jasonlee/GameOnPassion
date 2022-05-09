from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from api_cover_request import get_games_cover

default_args = {
    'owners': 'airflow',
    'start_date': datetime.today() - timedelta(days=1)
}

with DAG('extract_dag', start_date=datetime(2022, 5, 1),
         schedule_interval='@weekly',
         catchup=False,
         default_args=default_args) as dag:
    extract_tasks = PythonOperator(
        task_id='./extract_API_scripts/api_cover_request.py',
        python_callable=get_games_cover(),
        dag=dag)

# for api [extract tasks] >> [create_db, initial import] >>
# [gamemode, genre, platform] >> transform >> add tables >> load
