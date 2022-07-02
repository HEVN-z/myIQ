from signal import signal
import pymongo
import time
import os
import dotenv
dotenv.load_dotenv()

start = time.time()

client = pymongo.MongoClient(os.getenv('LOCAL_URI'))
signal_db = client.signal
user_db = client.user
mm_db = client.mm
history_db = client.history

# Trend Following

def get_signal_db_TIA(market):
    db = signal_db.tech_indicator
    signal = db.find_one({'market':market})['signal']
    time = db.find_one({'market':market})['time']
    return {'signal':signal, 'time':time}

def set_signal_db_TIA(market,signal,time):
    # TIA = Technical Indicator Analysis
    global signal_db
    db = signal_db.tech_indicator
    if db.find_one({'market':market}) is None:
        db.insert_one({'market':market,'signal':signal,'time':time})
    else:
        db.update_one({'market':market},{'$set':{'signal':signal,'time':time}})

# SAR Reversal

def get_signal_db_CCI(market):
    db = signal_db.cci_reversal
    signal = db.find_one({'market':market})['signal']
    time = db.find_one({'market':market})['time']
    return {'signal':signal, 'time':time}

def set_signal_db_CCI(market,signal,time):
    # CCI Reversal
    global signal_db
    db = signal_db.cci_reversal
    if db.find_one({'market':market}) is None:
        db.insert_one({'market':market,'signal':signal,'time':time})
    else:
        db.update_one({'market':market},{'$set':{'signal':signal,'time':time}})

# Test IO Signal

# set_signal_db_TIA('EURUSD','call',time.time())
print(get_signal_db_TIA('EURUSD'))
print(get_signal_db_TIA('EURUSD')['signal'])
print(get_signal_db_TIA('EURUSD')['time'])
# set_signal_db_CCI('EURUSD','call',time.time())
print(get_signal_db_CCI('EURUSD'))
print(get_signal_db_CCI('EURUSD')['signal'])
print(get_signal_db_CCI('EURUSD')['time'])
end = time.time()
print(end-start)