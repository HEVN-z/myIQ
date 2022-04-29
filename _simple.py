from datetime import datetime
import threading
from iqoptionapi.stable_api import IQ_Option
import time
import json
import os
# from numba import jit, cuda


from dotenv import load_dotenv
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

bot = IQ_Option(email,password)
bot.connect()
while True:
    if bot.check_connect():
        print("Connected")
        break
    else:
        print("Not Connected")
        break

# Variables

isBuy = False
target_time = 30
Action = "hold"
rate1 = 50
rate2 = 40
rate3 = 20

balance = bot.get_balance()
print("Your balance is",balance,"\n What you want to play")

Money = input("Money amount : ")
if Money == "" or Money == None:
    Money = 1
    print("Default money =",Money)
else:
    Money = float(Money)
    print("Your money is",Money)

Active = input("Currency pair : ")
if Active == "" or Active == None:
    Active = "EURJPY"
    Active = Active.upper()
    print("Default currency pair =",Active)
else:
    Active = Active.upper()
    print("Your currency pair is",Active)

expirations_mode = input("Expired mode : ")
if expirations_mode == "" or expirations_mode == None:
    expirations_mode = 1
    print("Default expired mode =",expirations_mode)
else:
    expirations_mode = int(expirations_mode)
    print("Your expired mode is",expirations_mode)

# indicator function
def ind():
    indicator = bot.get_technical_indicators(Active)

    #OSC 1 minute
    one_minute_OSC = [x for x in indicator if x["candle_size"] == 60 and x["group"] == "OSCILLATORS"]
    one_minute_OSC_buy = sum(item["action"] == "buy" for item in one_minute_OSC)
    one_minute_OSC_hold = sum(item["action"] == "hold" for item in one_minute_OSC)
    one_minute_OSC_sell = sum(item["action"] == "sell" for item in one_minute_OSC)
    max = one_minute_OSC_buy + one_minute_OSC_hold + one_minute_OSC_sell
    diff = one_minute_OSC_buy - one_minute_OSC_sell
    osc_one_min = diff / max * 100

    #MOV 1 minute
    one_minute_MOV = [x for x in indicator if x["candle_size"] == 60 and x["group"] == "MOVING AVERAGES"]
    one_minute_MOV_buy = sum(item["action"] == "buy" for item in one_minute_MOV)
    one_minute_MOV_hold = sum(item["action"] == "hold" for item in one_minute_MOV)
    one_minute_MOV_sell = sum(item["action"] == "sell" for item in one_minute_MOV)
    max = one_minute_MOV_buy + one_minute_MOV_hold + one_minute_MOV_sell
    diff = one_minute_MOV_buy - one_minute_MOV_sell
    mov_one_min = diff / max * 100

    average_one = (osc_one_min+mov_one_min)/2

    '''print("OSC 1 minute:", osc_one_min)
    print("MOV 1 minute:", mov_one_min)
    print("Average 1 minute:", average_one)'''

    #OSC 5 minutess
    five_minutes_OSC = [x for x in indicator if x["candle_size"] == 300 and x["group"] == "OSCILLATORS"]
    five_minutes_OSC_buy = sum(item["action"] == "buy" for item in five_minutes_OSC)
    five_minutes_OSC_hold = sum(item["action"] == "hold" for item in five_minutes_OSC)
    five_minutes_OSC_sell = sum(item["action"] == "sell" for item in five_minutes_OSC)
    max = five_minutes_OSC_buy + five_minutes_OSC_hold + five_minutes_OSC_sell
    diff = five_minutes_OSC_buy - five_minutes_OSC_sell
    osc_five_min = diff / max * 100

    #MOV 5 minutess
    five_minutes_MOV = [x for x in indicator if x["candle_size"] == 300 and x["group"] == "MOVING AVERAGES"]
    five_minutes_MOV_buy = sum(item["action"] == "buy" for item in five_minutes_MOV)
    five_minutes_MOV_hold = sum(item["action"] == "hold" for item in five_minutes_MOV)
    five_minutes_MOV_sell = sum(item["action"] == "sell" for item in five_minutes_MOV)
    max = five_minutes_MOV_buy + five_minutes_MOV_hold + five_minutes_MOV_sell
    diff = five_minutes_MOV_buy - five_minutes_MOV_sell
    mov_five_min = diff / max * 100

    average_five = (osc_five_min+mov_five_min)/2

    '''print("OSC 5 minutes:", osc_five_min)
    print("MOV 5 minutes:", mov_five_min)
    print("Average 5 minutes:", average_five)'''

    #OSC 15 minutess
    fifty_minutes_OSC = [x for x in indicator if x["candle_size"] == 900 and x["group"] == "OSCILLATORS"]
    fifty_minutes_OSC_buy = sum(item["action"] == "buy" for item in fifty_minutes_OSC)
    fifty_minutes_OSC_hold = sum(item["action"] == "hold" for item in fifty_minutes_OSC)
    fifty_minutes_OSC_sell = sum(item["action"] == "sell" for item in fifty_minutes_OSC)
    max = fifty_minutes_OSC_buy + fifty_minutes_OSC_hold + fifty_minutes_OSC_sell
    diff = fifty_minutes_OSC_buy - fifty_minutes_OSC_sell
    osc_fifty_min = diff / max * 100

    #MOV 15 minutess
    fifty_minutes_MOV = [x for x in indicator if x["candle_size"] == 900 and x["group"] == "MOVING AVERAGES"]
    fifty_minutes_MOV_buy = sum(item["action"] == "buy" for item in fifty_minutes_MOV)
    fifty_minutes_MOV_hold = sum(item["action"] == "hold" for item in fifty_minutes_MOV)
    fifty_minutes_MOV_sell = sum(item["action"] == "sell" for item in fifty_minutes_MOV)
    max = fifty_minutes_MOV_buy + fifty_minutes_MOV_hold + fifty_minutes_MOV_sell
    diff = fifty_minutes_MOV_buy - fifty_minutes_MOV_sell
    mov_fifty_min = diff / max * 100

    average_fifty = (osc_fifty_min+mov_fifty_min)/2

    '''print("OSC 15 minutes:", osc_fifty_min)
    print("MOV 15 minutes:", mov_fifty_min)
    print("Average 15 minutes:", average_fifty)'''

    return osc_one_min, osc_five_min, osc_fifty_min, mov_one_min, mov_five_min, mov_fifty_min, average_one, average_five, average_fifty
indicator = bot.get_technical_indicators(Active)
'''
def ind_one():
    #indicator = bot.get_technical_indicators(Active)
    #OSC 1 minute
    one_minute_OSC = [x for x in indicator if x["candle_size"] == 60 and x["group"] == "OSCILLATORS"]
    one_minute_OSC_buy = sum(item["action"] == "buy" for item in one_minute_OSC)
    one_minute_OSC_hold = sum(item["action"] == "hold" for item in one_minute_OSC)
    one_minute_OSC_sell = sum(item["action"] == "sell" for item in one_minute_OSC)
    max = one_minute_OSC_buy + one_minute_OSC_hold + one_minute_OSC_sell
    diff = one_minute_OSC_buy - one_minute_OSC_sell
    osc_one_min = diff / max * 100

    #MOV 1 minute
    one_minute_MOV = [x for x in indicator if x["candle_size"] == 60 and x["group"] == "MOVING AVERAGES"]
    one_minute_MOV_buy = sum(item["action"] == "buy" for item in one_minute_MOV)
    one_minute_MOV_hold = sum(item["action"] == "hold" for item in one_minute_MOV)
    one_minute_MOV_sell = sum(item["action"] == "sell" for item in one_minute_MOV)
    max = one_minute_MOV_buy + one_minute_MOV_hold + one_minute_MOV_sell
    diff = one_minute_MOV_buy - one_minute_MOV_sell
    mov_one_min = diff / max * 100

    average_one = (osc_one_min+mov_one_min)/2

    return average_one

def ind_five():
    indicator = bot.get_technical_indicators(Active)

    #OSC 5 minutess
    five_minutes_OSC = [x for x in indicator if x["candle_size"] == 300 and x["group"] == "OSCILLATORS"]
    five_minutes_OSC_buy = sum(item["action"] == "buy" for item in five_minutes_OSC)
    five_minutes_OSC_hold = sum(item["action"] == "hold" for item in five_minutes_OSC)
    five_minutes_OSC_sell = sum(item["action"] == "sell" for item in five_minutes_OSC)
    max = five_minutes_OSC_buy + five_minutes_OSC_hold + five_minutes_OSC_sell
    diff = five_minutes_OSC_buy - five_minutes_OSC_sell
    osc_five_min = diff / max * 100

    #MOV 5 minutess
    five_minutes_MOV = [x for x in indicator if x["candle_size"] == 300 and x["group"] == "MOVING AVERAGES"]
    five_minutes_MOV_buy = sum(item["action"] == "buy" for item in five_minutes_MOV)
    five_minutes_MOV_hold = sum(item["action"] == "hold" for item in five_minutes_MOV)
    five_minutes_MOV_sell = sum(item["action"] == "sell" for item in five_minutes_MOV)
    max = five_minutes_MOV_buy + five_minutes_MOV_hold + five_minutes_MOV_sell
    diff = five_minutes_MOV_buy - five_minutes_MOV_sell
    mov_five_min = diff / max * 100

    average_five = (osc_five_min+mov_five_min)/2

    return average_five

def ind_fifty():
    indicator = bot.get_technical_indicators(Active)
    
    #OSC 15 minutess
    fifty_minutes_OSC = [x for x in indicator if x["candle_size"] == 900 and x["group"] == "OSCILLATORS"]
    fifty_minutes_OSC_buy = sum(item["action"] == "buy" for item in fifty_minutes_OSC)
    fifty_minutes_OSC_hold = sum(item["action"] == "hold" for item in fifty_minutes_OSC)
    fifty_minutes_OSC_sell = sum(item["action"] == "sell" for item in fifty_minutes_OSC)
    max = fifty_minutes_OSC_buy + fifty_minutes_OSC_hold + fifty_minutes_OSC_sell
    diff = fifty_minutes_OSC_buy - fifty_minutes_OSC_sell
    osc_fifty_min = diff / max * 100

    #MOV 15 minutess
    fifty_minutes_MOV = [x for x in indicator if x["candle_size"] == 900 and x["group"] == "MOVING AVERAGES"]
    fifty_minutes_MOV_buy = sum(item["action"] == "buy" for item in fifty_minutes_MOV)
    fifty_minutes_MOV_hold = sum(item["action"] == "hold" for item in fifty_minutes_MOV)
    fifty_minutes_MOV_sell = sum(item["action"] == "sell" for item in fifty_minutes_MOV)
    max = fifty_minutes_MOV_buy + fifty_minutes_MOV_hold + fifty_minutes_MOV_sell
    diff = fifty_minutes_MOV_buy - fifty_minutes_MOV_sell
    mov_fifty_min = diff / max * 100

    average_fifty = (osc_fifty_min+mov_fifty_min)/2

    return average_fifty
'''

def check_buy(average1, average5, average15):
    if average1 > rate1 and average5 > rate2 and average15 > rate3:
        return "call"
    elif average1 < (rate1*-1) and average5 < (rate2*-1) and average15 < (rate3*-1):
        return "put"
    else:
        return "hold"

now = datetime.now()
dt_object = datetime.timestamp(now)
date_stamp = datetime.fromtimestamp(dt_object)
purchase_time = None
time_count = None
# สร้างตัวแปรก่อนเข้า loop เพื่อป้องกัน memory leak ลองรันทิ้งไว้สัก 3-4 ชั่วโมงแล้วกลับมาดูผลอีกที
# ผล = เหมือนเดิม
# ตอนนี้รู้แล้วว่า มัน Leak มาจาก osc_one_min, osc_five_min, osc_fifty_min, mov_one_min, mov_five_min, mov_fifty_min, average_one, average_five, average_fifty = ind()

def check_win(id):
    print("\t\t \"### ",bot.check_win_v4(id)[0],"you got",round(bot.check_win_v4(id)[1],2),"###\"")
osc_one_min, osc_five_min, osc_fifty_min, mov_one_min, mov_five_min, mov_fifty_min, average_one, average_five, average_fifty = ind()

#Buy Loop
while True:
    dt_object = datetime.timestamp(now)
    date_stamp = datetime.fromtimestamp(dt_object)


    purchase_time = bot.get_remaning(expirations_mode)-1-target_time
    time_count = bot.get_remaning(expirations_mode)-target_time
    time.sleep(.2)
    #Slower timer print out
    if purchase_time < 32 and purchase_time > 30:
        osc_one_min, osc_five_min, osc_fifty_min, mov_one_min, mov_five_min, mov_fifty_min, average_one, average_five, average_fifty = ind()
    #print(ind_one())
    #print(ind_five())
    #print(ind_fifty())

    #Buy conditions
    
    if average_one.__floor__() > rate1 and average_five.__floor__() > rate2 and average_fifty.__floor__() > rate3:
        Action = "call"
    elif average_one.__floor__() < (rate1*-1) and average_five.__floor__() < (rate2*-1) and average_fifty.__floor__() < (rate3*-1):
        Action = "put"
    else:
        Action = "hold"
        
    print(Active,time_count,bot.get_remaning(expirations_mode),target_time," ===== ",rate1,"%" , average_one.__floor__(),"% ==== ",rate2,"%" , average_five.__floor__(),"% ===== ",rate3,"%" , average_fifty.__floor__(),"%")
    print("___________________________________________________________________")

    #Buy   
    if purchase_time==target_time and isBuy == False and Action != "hold":
        check, id = bot.buy(Money,Active,Action,expirations_mode)
        isBuy = True
        if check:
            print("!buy!",Action,Active)
            print("time stamp =", date_stamp)
            threading.Thread(target = check_win, args = (id,)).start()
        else:
            print("time stamp =", date_stamp)
            print("buy fail")

    if purchase_time<target_time -5:
        isBuy = False