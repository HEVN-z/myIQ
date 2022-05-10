import time
import talib as ta
import numpy as np
from iqoptionapi.stable_api import IQ_Option
import os
from dotenv import load_dotenv
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

bot = IQ_Option(email,password)
bot . connect()

Active = 'EURUSD'
size = 60
maxdict = 20

bot . start_candles_stream(Active,size,maxdict)

while True:

    candles = bot . get_realtime_candles(Active,size)
    inputs = {
        'index': np.array([]),
        'time': np.array([]),
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }

    for timestamp in candles:
        inputs['time'] = np.append(inputs['time'], timestamp)
        inputs["open"]=np.append(inputs["open"],candles[timestamp]["open"] )
        inputs["high"]=np.append(inputs["high"],candles[timestamp]["max"] )
        inputs["low"]=np.append(inputs["low"],candles[timestamp]["min"] )
        inputs["close"]=np.append(inputs["close"],candles[timestamp]["close"] )
        inputs["volume"]=np.append(inputs["volume"],candles[timestamp]["volume"] )
    for i in range(len(inputs['time'])):
        inputs['index'] = np.append(inputs['index'], i)

    doji = ta.CDLDOJI(inputs['open'], inputs['high'], inputs['low'], inputs['close'])
    dojistar = ta.CDLDOJISTAR(inputs['open'], inputs['high'], inputs['low'], inputs['close'])
    dragonfly = ta.CDLDRAGONFLYDOJI (inputs['open'], inputs['high'], inputs['low'], inputs['close'])

    print('Doji = ',doji)
    print('Dojistar = ',dojistar)
    print('Dragondly = ',dragonfly)
    time.sleep(1)