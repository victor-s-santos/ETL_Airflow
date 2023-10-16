# ETL_Airflow

# How to run
 * 1. __Clone the repo:__
    - `git clone https://github.com/victor-s-santos/ETL_Airflow`

 * 2. __Config your env file:__
    - `AIRFLOW_IMAGE_NAME=apache/airflow:2.7.1`
      `AIRFLOW_UID=50000`

 * 3. __Build the image:__
    - `docker compose up --build`
 
 * 4. __Check airflow UI:__
    - `Access the following: http://0.0.0.0:8080/`
    - `And get in by the following credentials: user: airflow; password: airflow`