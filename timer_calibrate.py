from iqoptionapi.stable_api import IQ_Option
import time
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

bot = IQ_Option(email,password)
bot.connect()
print(bot.get_balance())

bot.start_candles_stream("EURUSD",60,1)
while True:
    candles = bot.get_realtime_candles("EURUSD",60)
    for timestamp in candles:
        print(timestamp)
        # print(candles[timestamp]['from'])
        s = int(candles[timestamp]['to'])
        print('\n\n')
        print(type(s))
        print(type(time.time()))
        print('time   : ',time.localtime(s).tm_min,time.localtime(s).tm_sec)
        print('real   : ',time.localtime(time.time()).tm_min,time.localtime(time.time()).tm_sec)
        print('remain : ',(bot.get_remaning(1) - 60) *-1)

        # print(candles[timestamp]['open'])
        # print(candles[timestamp]['max'])
        # print(candles[timestamp]['min'])
        # print(candles[timestamp]['close'])
        # print(candles[timestamp]['volume'])
    # print(candles)
    time.sleep(.5)
