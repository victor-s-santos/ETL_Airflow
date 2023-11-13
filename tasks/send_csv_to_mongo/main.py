from csv import DictReader
from tasks.utils.mongo_connection.main import Mongo 
import os
import logging

def get_csvs()-> list:
    """Create a list of all csv files in current directory

    Returns:
        list: List of csv files names
    """
    csv_files_list = []
    for file in os.listdir():
        if file.endswith(".csv"):
            csv_files_list.append(file)
    logging.info(f"The list of csv files: {csv_files_list}")
    return csv_files_list

def send_to_mongo():
    logging.info("Initializing send_to_mongo")
    list_of_csv_files = get_csvs()
    mongo_credentials = {
        "user": os.getenv("MONGOUSER"),
        "password": os.getenv("MONGOPASSWORD"),
        "host": os.getenv("MONGOHOST"),
        "port": os.getenv("MONGOPORT"),
        "db_name": os.getenv("MONGODBNAME"),
    }
    mongo_obj = Mongo(credentials=mongo_credentials)
    mongo_obj.connect_to_mongo()
    my_db = mongo_obj.get_connection()
    logging.info("Connected successfully!")
    
    n = 0
    for csv_file in list_of_csv_files:
        my_collection = my_db[csv_file]
        with open(csv_file, "r") as file:
            dict_objs = DictReader(file)
            for dicio in dict_objs:
                n += 1
                my_collection.insert_one(dict(dicio))
    logging.info(f"The total inserted records is: {n}")