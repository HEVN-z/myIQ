from multiprocessing.connection import answer_challenge
from textwrap import indent
from talib.abstract import EMA , SAR, CDL3INSIDE
from iqoptionapi.stable_api import IQ_Option
import time
import numpy as np
import sys
import statistics

email = "dummy.esper@gmail.com"
password = "12651265exe"
bot = IQ_Option(email,password)
bot.connect()
while True:
    if bot.check_connect():
        print("Connected")
        break
    else:
        print("Not Connected")
        break
'''
acceleration = .02
maximum = .2
while True:
    end_from_time=time.time()
    ANS=[]
    for i in range(1):
        data=bot.get_candles("EURUSD", 60, 3, end_from_time)
        ANS =data+ANS
        end_from_time=int(data[0]["from"])-1
    print(time.time())
    #print(ANS[0])
    #print(ANS[1])
    #print(ANS[2])
    high1 = ANS[0]["max"]
    low1 = ANS[0]["min"]
    high2 = ANS[1]["max"]
    low2 = ANS[1]["min"]
    high3 = ANS[2]["max"]
    low3 = ANS[2]["min"]
    print("high1",high1,"\t","low1",low1)
    print("high2",high2,"\t","low2",low2)
    print("high3",high3,"\t","low3",low3)
    SAR1 = SAR(high1,low1, acceleration, maximum)
    SAR2 = SAR(np.array([high2,low2]), acceleration, maximum)
    SAR3 = SAR(np.array([high3,low3]), acceleration, maximum)
    print("SAR1",SAR1[0],"\t","SAR2",SAR2[0],"\t","SAR3",SAR3[0])
'''
'''
while True:
    #print(time.time())
    #ap = np.array([([])])
    tech = bot.get_technical_indicators("EURUSD")
    #ap = np.append(bot.get_technical_indicators("EURUSD")[0])
    #print("\t1")
    #ap = np.append(bot.get_technical_indicators("AUDUSD")[0])
    #print("\t\t2")
    #ap = np.append(bot.get_technical_indicators("EURJPY")[0])
    #print("\t\t\t3")
    #print(ap)
    
    #Indi2 = Indi[0]
    #print(sys.getsizeof(Indi))
    #print(sys.getsizeof(Indi2))
    #print(sys.getsizeof(bot.get_technical_indicators("EURUSD")[0]))
'''

goal="EURUSD"
size=60#size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
timeperiod=3
maxdict=5
print("start stream...")
bot.start_candles_stream(goal,size,maxdict)
print("Start EMA Sample")
while True:
    candles=bot.get_realtime_candles(goal,size)

    inputs = {
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }
    for timestamp in candles:

        inputs["open"]=np.append(inputs["open"],candles[timestamp]["open"] )
        inputs["high"]=np.append(inputs["high"],candles[timestamp]["max"] )
        inputs["low"]=np.append(inputs["low"],candles[timestamp]["min"] )
        inputs["close"]=np.append(inputs["close"],candles[timestamp]["close"] )
        inputs["volume"]=np.append(inputs["volume"],candles[timestamp]["volume"] )


    print("Show SAR")
    #print(candles)
    #print("inputs")
    #print(inputs)
    #print(inputs["close"][len(inputs["close"])-1])
    #print(inputs["close"])
    #print(EMA(inputs, timeperiod=timeperiod))
    #print(SAR(inputs, acceleration=0.02, maximum=0.2))
    PSAR = list(SAR(inputs, acceleration=0.02, maximum=0.2))
    PPSAR = inputs["close"] - PSAR

    print(CDL3INSIDE(inputs))

    #print(PPSAR)
    #print(SAR(inputs["high"],inputs["low"], acceleration=0.02, maximum=0.2))
    #list_range = 14
    #stdlist = list(inputs["close"])
    #stdev = statistics.stdev(stdlist(range(len(inputs["close"])-14,len(inputs["close"]))))
    #print(stdev)
    print("\n")
    time.sleep(1)
bot.stop_candles_stream(goal,size)
