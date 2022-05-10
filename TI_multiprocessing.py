import time
from multiprocessing import Process
from threading import Thread
from iqoptionapi.stable_api import IQ_Option
from TI_multi import *
from dotenv import load_dotenv
import os
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print("Starting...")

bot = IQ_Option(email, password)
bot.connect()

expirations_mode = 1#input("Expired mode : ")
# if expirations_mode == "" or expirations_mode == None:
#     expirations_mode = 1
#     print("Default expired mode =",expirations_mode)
# else:
#     expirations_mode = int(expirations_mode)
#     print("Your expired mode is",expirations_mode)
offset = 30

while True:
    if bot.connect():
        print("Connected")
        break
    else:
        print("Failed to connect")

print("I am Online!")

def get_tech_ind_percentage(indicator, expire_time, type):
    items = [x for x in indicator if x["candle_size"] == expire_time and x["group"] == type]
    item_buy = sum(i["action"] == "buy" for i in items)
    item_hold = sum(i["action"] == "hold" for i in items)
    item_sell = sum(i["action"] == "sell" for i in items)
    total = item_buy + item_hold + item_sell
    return (item_buy - item_sell) / total * 100

def get_tech_i(active):
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
    return round(av1,2), round(av5,2), round(av15,2), round(av60,2)

def get_tech_i_percentage(active):
    run = bot.get_all_open_time()['turbo'][active]['open']
    while True:
        timer = bot.get_remaning(expirations_mode)
        if bot.get_remaning(15) == (15*60)-10:
            run = bot.get_all_open_time()['turbo'][active]['open']
        if run and timer == (expirations_mode*60)-10:
            percent = bot.get_all_profit()[active]['turbo']
            set_percent(active,percent)
        if run and timer > (expirations_mode*60)+2 and timer < (expirations_mode*60)+5:
            one, five, fifteen, sixty = get_tech_i(active)
            print(active, one, five, fifteen, sixty,timer,(expirations_mode*60))
            set_data(active, one, five, fifteen, sixty)
            print(time.strftime('%H:%M:%S', time.localtime(time.time())))
        # print(bot.get_remaning(15)-30,(15*60)-30)
        time.sleep(.2)

if __name__ == "__main__":
    Thread(target=get_tech_i_percentage, args=("GBPUSD",)).start()
    Thread(target=get_tech_i_percentage, args=("EURJPY",)).start()
    Thread(target=get_tech_i_percentage, args=("EURUSD",)).start()
    Thread(target=get_tech_i_percentage, args=("NZDUSD",)).start()
    Thread(target=get_tech_i_percentage, args=("AUDUSD",)).start()
    Thread(target=get_tech_i_percentage, args=("EURCHF",)).start()
    Thread(target=get_tech_i_percentage, args=("GBPJPY",)).start()
    Thread(target=get_tech_i_percentage, args=("AUDNZD",)).start()
