from turtle import color
import matplotlib.pyplot as plt
from iqoptionapi.stable_api import IQ_Option
from matplotlib.animation import FuncAnimation
import numpy as np

from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

iq_bot = IQ_Option(email,password)

iq_bot.connect()
goal="EURUSD-OTC"
size=60#size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
timeperiod=10
maxdict=20
iq_bot.start_candles_stream(goal,size,maxdict)

#create figure
plt.figure()

#define width of candlestick elements
width = 1
width2 = .5
ax = plt.subplot()
#define up and down prices
def animation(gg):
    ax.clear()  
    candles = iq_bot.get_realtime_candles(goal,size)
    inputs = {
        'index': np.array([]),
        'time': np.array([]),
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }
    try:
        for timestamp in candles:
            # print(timestamp)
            # print(candles[timestamp]['from'])
            # print(candles[timestamp]['to'])
            inputs['time'] = np.append(inputs['time'], timestamp)
            # inputs['index'] = np.append(inputs['time'], candles[timestamp]['from'].index(timestamp))
            inputs["open"]=np.append(inputs["open"],candles[timestamp]["open"] )
            inputs["high"]=np.append(inputs["high"],candles[timestamp]["max"] )
            inputs["low"]=np.append(inputs["low"],candles[timestamp]["min"] )
            inputs["close"]=np.append(inputs["close"],candles[timestamp]["close"] )
            inputs["volume"]=np.append(inputs["volume"],candles[timestamp]["volume"] )
    except Exception as e:
        print(e)
    for i in range(len(inputs['time'])):
        inputs['index'] = np.append(inputs['index'], i)

    print(inputs['index'])

    #define width of candlestick elements
    width = .4
    width2 = .05

    #define up and down prices
    up = inputs["close"]>inputs["open"]
    up_candle = {
        'index': inputs['index'][up],
        'time': np.array([]),
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }
    try:
        up_candle['open'] = np.append(up_candle['open'],inputs['open'][up])
        up_candle['high'] = np.append(up_candle['high'],inputs['high'][up])
        up_candle['low'] = np.append(up_candle['low'],inputs['low'][up])
        up_candle['close'] = np.append(up_candle['close'],inputs['close'][up])
        up_candle['volume'] = np.append(up_candle['volume'],inputs['volume'][up])
        up_candle['time'] = np.append(up_candle['time'],inputs['time'][up])
    except Exception as e:
        print(e)
        
    down = inputs["close"]<inputs["open"]
    down_candle = {
        'index': inputs['index'][down],
        'time': np.array([]),
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }
    try:
        down_candle['open'] = np.append(down_candle['open'],inputs['open'][down])
        down_candle['high'] = np.append(down_candle['high'],inputs['high'][down])
        down_candle['low'] = np.append(down_candle['low'],inputs['low'][down])
        down_candle['close'] = np.append(down_candle['close'],inputs['close'][down])
        down_candle['volume'] = np.append(down_candle['volume'],inputs['volume'][down])
        down_candle['time'] = np.append(down_candle['time'],inputs['time'][down])
        
    except Exception as e:
        print(e)
    # print(up)
    # print(up_candle)
    # print(down)
    # print(down_candle)
    # print(inputs['open'])
        
    #define colors to use
    col1 = 'green'
    col2 = 'red'

    #plot up prices
    ax.bar(up_candle['index'],up_candle['close']-up_candle['open'],width,bottom=up_candle['open'],color=col1)
    ax.bar(up_candle['index'],up_candle['high']-up_candle['close'],width2,bottom=up_candle['close'],color=col1)
    ax.bar(up_candle['index'],up_candle['low']-up_candle['open'],width2,bottom=up_candle['open'],color=col1)

    #plot down prices
    ax.bar(down_candle['index'],down_candle['close']-down_candle['open'],width,bottom=down_candle['open'],color=col2)
    ax.bar(down_candle['index'],down_candle['high']-down_candle['open'],width2,bottom=down_candle['open'],color=col2)
    ax.bar(down_candle['index'],down_candle['low']-down_candle['close'],width2,bottom=down_candle['close'],color=col2)

    ax.plot(inputs['index'],inputs['close'],color='black')

    # plt.cla()
    
ani = FuncAnimation(plt.gcf(),animation,interval=250)
#rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

plt.tight_layout()

#display candlestick chart
plt.show()