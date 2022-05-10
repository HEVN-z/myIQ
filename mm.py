from datetime import datetime
from genericpath import getsize
from threading import Thread
from iqoptionapi.stable_api import IQ_Option
import time
import psutil
import gc

from matplotlib.pyplot import get
# import TI_multi as TI
import mmjs as mm
import os
# from numba import jit, cuda
gc.enable()
T = Thread
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
rate1 = mm.get_rate1()
rate5 = mm.get_rate5()
rate15 = mm.get_rate15()
rate60 = mm.get_rate60()

balance = bot.get_balance()
print("Your balance is",balance,"\n What market you want to auto trade")

Money = input("Money amount : ")
if Money == "" or Money == None:
    Money = 1
    print("Default money =",Money)
else:
    Money = float(Money)
    print("Your money is",Money)
mm.set_base_amount(Money)
mm.set_order_amount(Money)

reset = input("Reset (Y/N): ")
if reset.upper == "Y":
    mm.set_today_profit(0)
    mm.set_martingale_level(0)
    print("Reset!")
else:
    print("no reset")

Active = input("Currency pair : ")
if Active == "" or Active == None:
    Active = mm.get_Active()
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

Balance_mode = input("Balance Mode : ")
if Balance_mode == "" or Balance_mode == None:
    Balance_mode = "PRACTICE"
    Balance_mode = Balance_mode.upper()
    print("Default Balance Mode =",Balance_mode)
else:
    Balance_mode = Balance_mode.upper()
    print("Your Balance Mode is",Balance_mode)

# indicator function


def check_buy(average1, average5, average15):
    if average1 > rate1 and average5 > rate5 and average15 > rate15:
        return "call"
    elif average1 < (rate1*-1) and average5 < (rate5*-1) and average15 < (rate15*-1):
        return "put"
    else:
        return "hold"

# สร้างตัวแปรก่อนเข้า loop เพื่อป้องกัน memory leak ลองรันทิ้งไว้สัก 3-4 ชั่วโมงแล้วกลับมาดูผลอีกที
# ผล = เหมือนเดิม
# ตอนนี้รู้แล้วว่า มัน Leak มาจาก osc_one_min, osc_five_min, osc_fifty_min, mov_one_min, mov_five_min, mov_fifty_min, average_one, average_five, average_fifty = ind()

def get_tech_ind_percentage(indicator, expire_time, type):
    items = [x for x in indicator if x["candle_size"] == expire_time and x["group"] == type]
    item_buy = sum(i["action"] == "buy" for i in items)
    item_hold = sum(i["action"] == "hold" for i in items)
    item_sell = sum(i["action"] == "sell" for i in items)
    total = item_buy + item_hold + item_sell
    return (item_buy - item_sell) / total * 100
indicator = None
def get_tech_i(active):
    global indicator
    indicator = bot.get_technical_indicators(active)
    osc1 = get_tech_ind_percentage(indicator, 60, "OSCILLATORS")
    osc5 = get_tech_ind_percentage(indicator, 300, "OSCILLATORS")
    osc15 = get_tech_ind_percentage(indicator, 900, "OSCILLATORS")
    osc60 = get_tech_ind_percentage(indicator, 3600, "OSCILLATORS")

    ma1 = get_tech_ind_percentage(indicator, 60, "MOVING AVERAGES")
    ma5 = get_tech_ind_percentage(indicator, 300, "MOVING AVERAGES")
    ma15 = get_tech_ind_percentage(indicator, 900, "MOVING AVERAGES")
    ma60 = get_tech_ind_percentage(indicator, 3600, "MOVING AVERAGES")

    av1 = (osc1 + ma1) / 2
    av5 = (osc5 + ma5) / 2
    av15 = (osc15 + ma15) / 2
    av60 = (osc60 + ma60) / 2
    # return round(av1,2), round(av5,2), round(av15,2), round(av60,2)
    global average1,average5,average15,average60
    average1,average5,average15,average60 = round(av1,2), round(av5,2), round(av15,2), round(av60,2)
    indicator = None
    gc.collect()


def check_win(id):
    # try:
        print("\t\t \"### ",bot.check_win_v4(id)[0],"you got",round(bot.check_win_v4(id)[1],2),"###\"")
        percent = percent = bot.get_all_profit()[Active]['turbo']
        w = bot.check_win_v4(id)[0].lower()
        if w == "win"   or w == "won":
            print("\t\t \"### You win",percent,"% ###\"")
            thisProfit = round(mm.get_order_amount()*percent,2)
            print('thisProfit =',thisProfit)
            mm.set_total_amount(mm.get_total_amount()+thisProfit)
            print('set_total_amount from WIN',mm.get_total_amount())
            mm.set_today_profit(mm.get_today_profit()+thisProfit)
            print('set_today_profit from WIN',mm.get_today_profit())
            mm.set_martingale_level(mm.get_martingale_level()+1)
            print('set_martingale_level from WIN',mm.get_martingale_level())

            if mm.get_martingale_level() < 0: # Reset martingale level
                print("\t\t\t\t+++++++++                        Reset martingale level from minus")
                mm.set_order_amount(round(mm.get_base_amount()))
                mm.set_martingale_level(0)
                mm.set_total_amount(0)
            elif mm.get_martingale_level() > mm.get_martingale_max_level():
                print("\t\t\t\t+++++++++                        Max martingale level Higher than max")
                mm.set_order_amount(round(mm.get_base_amount()))
                mm.set_martingale_level(0)
                mm.set_total_amount(0)
            elif mm.get_martingale_level() == 0 or mm.get_martingale_level() == 1:
                mm.set_order_amount(round(mm.get_base_amount()))
                mm.set_total_amount(0)
            
            
            elif False:
                print("+++++++++                        Plan A : Step by step")
                m = mm.get_base_amount()
                mm.set_order_amount(m)
            elif True and mm.get_martingale_level() <= mm.get_martingale_max_level():
                print("\t\t\t\t+++++++++                        Plan B : Push up")
                mm.set_order_amount(round(mm.get_order_amount()*mm.get_anti_martingale_multiplier(),2))
            elif False and mm.get_martingale_level() < mm.get_martingale_max_level():
                print("+++++++++                        Plan C : All in")
                mm.set_order_amount(mm.get_total_amount())
            elif False:
                print("Plan D")
            print(mm.get_order_amount())

        elif w == "lose" or w == "lost" or w == "loose":
            print("\t\t \"### You lose ###\"")
            thisLoss = round(mm.get_order_amount(),2)
            print('thisLoss',thisLoss)
            mm.set_total_amount(round(mm.get_total_amount()-thisLoss,2))
            print('set_total_amount from LOOSE',mm.get_total_amount())
            mm.set_today_profit(round(mm.get_today_profit()-thisLoss,2))
            print('set_today_profit from LOOSE',mm.get_today_profit())
            mm.set_martingale_level(mm.get_martingale_level()-1)
            print('set_martingale_level from LOOSE',mm.get_martingale_level())

            if mm.get_martingale_level() > 0: # Reset martingale level
                print("\t\t\t\t+++++++++                        Plan E : Reset martingale level from plus")
                mm.set_order_amount(round(mm.get_base_amount(),2))
                mm.set_martingale_level(0)
                mm.set_total_amount(0)
            elif mm.get_martingale_level() <= mm.get_martingale_min_level():
                print("\t\t\t\t+++++++++                        Plan F : Reset martingale level Lower than min")
                mm.set_order_amount(round(mm.get_base_amount(),2))
                mm.set_martingale_level(0)
                mm.set_total_amount(0)
            # elif mm.get_martingale_level() == 0:
            #     mm.set_order_amount(mm.get_base_amount())
            #     mm.set_total_amount(0)
                
            
            
            elif False:
                print("+++++++++                        Plan A : Step by step")
                mm.set_order_amount(mm.get_base_amount())
            elif False and mm.get_martingale_level() > mm.get_martingale_min_level():
                print("+++++++++                        Plan B : Classic Martingale")
                mm.set_order_amount(round(mm.get_base_amount()*mm.get_martingale_multiplier()*(mm.get_martingale_level()*-1),2))
            elif True and mm.get_martingale_level() > mm.get_martingale_min_level():
                # if mm.get_martingale_level() == 0:
                #     mm.set_total_amount(-mm.get_base_amount())
                print("\t\t\t\t+++++++++                        Plan C : Adaptive Martingale to profit target")
                base_profit = (mm.get_base_amount()*mm.get_profit_target())
                print('base profit = ',base_profit)
                target = (-1*mm.get_total_amount()) + base_profit
                print('get total amount in positive',(-1*mm.get_total_amount()))
                print('target profit =' ,target)
                mm.set_order_amount(round(target/percent,2))
                print('set_order_amount = ',mm.get_order_amount())
            elif False and mm.get_martingale_level() > mm.get_martingale_min_level():
                print("+++++++++                        Plan D : Adaptive Martingale to ZERO target")
                mm.set_order_amount(round((-1*mm.get_total_amount())/percent,2))

        else:
            print("\t\t \"### You tied ###\"")

        print('Total Amount update now = ',mm.get_total_amount())
        print('Today Profit update now = ',mm.get_today_profit())
    # except Exception as e:
    #     print("error:",e)

        global isBuy
        isBuy = False


#Buy Loop
while True:
    date_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    purchase_time = bot.get_remaning(expirations_mode)-1-target_time
    time_count = bot.get_remaning(expirations_mode)-target_time

    #Buy conditions
    if time_count == 32:
        T = Thread(target = lambda:get_tech_i(Active))
        T.start()
        T.join()
    
    # if average1 > rate1 and average5 > rate2 and average15 > rate3:
    #     Action = "call"
    # elif average1 < (rate1*-1) and average5 < (rate2*-1) and average15 < (rate3*-1):
    #     Action = "put"
    # else:
    #     Action = "hold"

    Action = check_buy()
    # print(Action, Active,time_count,purchase_time,target_time," ===== ",rate1,"%" , average1,"% ==== ",rate2,"%" , average5,"% ===== ",rate3,"%" , average15,"%")
    
    #Buy   
    if purchase_time==target_time and isBuy == False and Action != "hold":
        check, id = bot.buy(mm.get_order_amount(),Active,Action,expirations_mode)
        isBuy = True
        if check:
            print('\n\n\n\n\n')
            print("++++++++++++++++++++++++++++++++++++++   ++++ ORDER =",mm.get_order_amount())
            print("!buy!",Action,Active)
            print("time stamp =", date_stamp)
            print(Active,time_count,bot.get_remaning(expirations_mode),target_time," ===== ",rate1,"%" , average1,"% ==== ",rate5,"%" , average5,"% ===== ",rate15,"%" , average15,"%")
            print("___________________________________________________________________\t\t\t\t",psutil.cpu_percent(),"%")
            print("___________________________________________________________________\t\t\t\t",psutil.virtual_memory().percent,"%")
            Thread(target = check_win, args = (id,)).start()
        else:
            print("time stamp =", date_stamp)
            print("buy fail")
            print(Active,time_count,bot.get_remaning(expirations_mode),target_time," ===== ",rate1,"%" , average1,"% ==== ",rate5,"%" , average5,"% ===== ",rate15,"%" , average15,"%")
            

    # if purchase_time<target_time -5:
    #     isBuy = False