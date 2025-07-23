from pymongo import MongoClient
from dotenv import load_dotenv
import os
 
load_dotenv()
 
client = None
db = None
 
def init_db():
    global client, db
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client.get_database()
    return db
