from pymongo import MongoClient
from dotenv import load_dotenv
import os
 
load_dotenv()
 
client = None
db = None
 
def init_db():
    global client, db
    try:
        client = MongoClient(os.getenv('MONGODB_URI'))
        db_name = os.getenv('MONGODB_URI').split('/')[-1].split('?')[0]
        db = client[db_name]
        print(f"Connected to database: {db_name}")
        return db
    except Exception as e:
        print(f"Database connection failed: {str(e)}")
        raise
