import pymongo
import time
import os
import dotenv
dotenv.load_dotenv()

start = time.time()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
signal_db = client.signal
user_db = client.user
mm_db = client.mm
history_db = client.history
