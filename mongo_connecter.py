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

def get_signal_db_TIA(market):
    return signal_db.tech_indicator.find_one({'market':market})['signal']

def set_signal_db_TIA(market,signal):
    # TIA = Technical Indicator Analysis
    global signal_db
    tia = signal_db.tech_indicator
    if tia.find_one({"market":market}) is None:
        tia.insert_one({"market":market,"signal":signal})
    else:
        tia.update_one({"market":market},{"$set":{"signal":signal}})


set_signal_db_TIA('EURUSD','call')
print(get_signal_db_TIA('EURUSD'))