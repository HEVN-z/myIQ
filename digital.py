from iqoptionapi.stable_api import IQ_Option
import time
import numpy as np
import os
from dotenv import load_dotenv
from threading import Thread
load_dotenv()

isBuy = False

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
bot = IQ_Option(email,password)

def checkBuy(id):
    global isBuy
    print(bot.check_win_v4(id))
    isBuy = False

bot.connect()
print(bot.get_balance())
while True:
    if bot.get_remaning(1) == 60 and isBuy == False:
        check, id = bot.buy_digital_spot("EURUSD",1,'call',1)
        if check == True:
            isBuy = True
            Thread(checkBuy(id)).start()
            print('buy success')
        else:
            print('buy fail')
        print('buy')