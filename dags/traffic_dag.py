from datetime import timedelta, datetime

from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from scripts.dataloader import DataLoader
from scripts.db_connection import Connection


default_args = {
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def read_data():
    """csv data reading
    """
    dl = DataLoader()
    headers, rows = dl.read_csv('../data/traffic.csv')
    vehicles, trajectories = dl.data_to_dataframe(headers, rows)
    vehicles.to_csv('../data/vehicles.csv', index=False)
    trajectories.to_csv('../data/trajectories.csv',index=False)

def create_table():
    con = Connection()
    con.create_table()

def insert_data_to_db():
    """Insert data to db"""
    con = Connection()
    vehicles = pd.read_csv('../data/vehicles.csv')
    trajectories = pd.read_csv('../data/trajectories.csv')
    con.df_to_sql('vehicles', vehicles)
    con.df_to_sql('trajectories', trajectories)

with DAG(
    default_args=default_args,
    dag_id='traffic_dag',
    description='Read csv, extract, and put to postgres',
    start_date=datetime(2024, 4, 30),
    schedule_interval='@daily'
) as dag:
    data_reader = PythonOperator(
        task_id= 'read_data',
        python_callable= read_data
    )
    table_creator = PythonOperator(
        task_id='table_creator',
        python_callable=create_table
    )
    insert_data = PythonOperator(
        task_id='insert_data_to_db',
        python_callable=insert_data_to_db
    )
    
data_reader>>table_creator>>insert_data    