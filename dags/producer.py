from airflow import DAG, Dataset
from airflow.operators.python_operator import PythonOperator

from datetime import timedelta, datetime

my_file = Dataset("/tmp/my_file.txt")

def update_my_file(outlets=[my_file]):
        with open(my_file.uri, "+a") as f:
            f.write("producer update")

with DAG(
    dag_id='producer',
    start_date=datetime(2024, 4, 30),
    schedule_interval='@daily', 
    catchup=False
):
    
    task1 = PythonOperator(
              task_id= 'update_my_file',
        python_callable= update_my_file
    )