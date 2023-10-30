# ETL_Airflow

# How to run
 * 1. __Clone the repo:__
    - `git clone https://github.com/victor-s-santos/ETL_Airflow`

 * 2. __Config your env file:__
    - `AIRFLOW_IMAGE_NAME=apache/airflow:2.7.1`
      `AIRFLOW_UID=50000`

 * 3. __Build the image:__
    - `docker compose up airflow-init`
    - `docker compose up`
 
 * 4. __Check airflow UI:__
    - `Access the following: http://0.0.0.0:8080/`
    - `And get in by the following credentials: user: airflow; password: airflow`

# Project Schema
## Dag: processing_fast_food
### `The dag have necessaries task to download a dataset, send dataset values to mongodb, sanitize the mongo values and finally send the sanitized values to a postgres database. The processing_fast_food dag have the following tasks:`
   - get_dataset_from_kaggle;
   - send_values_to_mongo;
   - sanitize_data;
   - send_to_postgres;
   - generate_report;
   - send_to_postgres;