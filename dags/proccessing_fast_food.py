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
# from tasks.kaggle.export_csv import download_csv

with DAG(dag_id="hello_world_test", start_date=datetime(2023, 1, 1), schedule_interval="0 0 * * *", catchup=False) as dag:
    hello_world = BashOperator(task_id="hello_world", bash_command="echo Hello world!")
    
    python_hello_world = PythonOperator(
        task_id="python_hello_world",
        python_callable=run_task,
        dag=dag
    )
    
    # task_download_csv = PythonOperator(
    #     task_id="download_csv",
    #     python_callable=download_csv,
    #     dag=dag
    # )

    
    # hello_world >> python_hello_world >> task_download_csv

    hello_world >> python_hello_world

# TODO Arrumar o erro acusado na task_download_csv que é variável de ambiente