from datetime import datetime
#para conseguir importar
import sys
sys.path.insert(0, '/tasks/task_sample.py')
#fim
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from tasks.task_sample import run_task

with DAG(dag_id="hello_world_test", start_date=datetime(2023, 1, 1), schedule_interval="0 0 * * *", catchup=False) as dag:
    hello_world = BashOperator(task_id="hello_world", bash_command="echo Hello world!")
    python_hello_world = PythonOperator(
        task_id="python_hello_world",
        python_callable=run_task,
        dag=dag
    )
    

    
    hello_world >> python_hello_world