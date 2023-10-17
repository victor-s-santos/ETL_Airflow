from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id="hello_world_test", start_date=datetime(2023, 1, 1), schedule_interval="0 0 * * *", catchup=False) as dag:
    hello_world = BashOperator(task_id="hello_world", bash_command="echo Hello world!")

    @task()
    def run_task():
        print("Hello world, its working!")

    
    hello_world >> run_task()