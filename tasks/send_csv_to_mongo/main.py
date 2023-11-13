from csv import DictReader
from tasks.utils import mongo_connection
import os

def get_csvs():
    print(os.getcwd())
    print(os.listdir())
    return os.listdir()