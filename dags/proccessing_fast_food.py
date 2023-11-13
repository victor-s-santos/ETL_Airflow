from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from tasks.task_sample import run_task
from tasks.kaggle.export_csv import download_csv
from tasks.send_csv_to_mongo.main import get_csvs
import os


with DAG(dag_id="hello_world_test", start_date=datetime(2023, 1, 1), schedule_interval="0 0 * * *", catchup=False) as dag:
    dict_credentials = {"username": os.getenv("KAGGLE_USER"), "key": os.getenv("KAGGLE_KEY")}
    full_dict = {
        "credentials": dict_credentials,
        "dataset_owner": "joebeachcapital",
        "dataset_name": "fast-food",
    }

    hello_world = BashOperator(task_id="hello_world", bash_command="echo Hello world!")
    
    python_hello_world = PythonOperator(
        task_id="python_hello_world",
        python_callable=run_task,
        op_args=[dict_credentials["username"], dict_credentials["key"]],
        dag=dag
    )
    
    task_download_csv = PythonOperator(
        task_id="download_csv",
        python_callable=download_csv,
        op_args=[full_dict["credentials"], full_dict["dataset_owner"], full_dict["dataset_name"]],
        dag=dag
    )

    task_get_csv = PythonOperator(
        task_id="send_csv_to_mongo",
        python_callable=get_csvs,
        dag=dag
    )
    # hello_world >> python_hello_world
    hello_world >> python_hello_world >> task_download_csv >> task_get_csv
