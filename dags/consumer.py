from airflow import DAG, Dataset
from airflow.operators.python_operator import PythonOperator

from datetime import timedelta, datetime

my_file = Dataset("/tmp/my_file.txt")

def read_my_file(outlets=[my_file]):
        with open(my_file.uri, "r") as f:
            print(f.read())

with DAG(
    dag_id='consumer',
    start_date=datetime(2024, 4, 30),
    schedule=[my_file], 
    catchup=False
)as dag:
    task = PythonOperator(
        task_id= 'read_my_file',
        python_callable= read_my_file
    )

        
            
