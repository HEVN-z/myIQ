# import api

import time
from iqoptionapi.stable_api import IQ_Option

# import class

from indic_psar import PSAR
from mm import MoneyManager

# Stand-in

indic_psar = PSAR()
mm = MoneyManager()

# login connection

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

# Asset Management

ALL_Asset= bot.get_all_open_time()
#print("ALL_Asset:", ALL_Asset)
#print("ALL_Asset[0]:", ALL_Asset[0])
#print(ALL_Asset["binary"]["EURUSD"]["open"])

goal = "EURUSD"
#print("get candles")
#candles = bot.get_candles(goal, 60,3, time.time())
#print("candles:", candles)
#indicator = bot.get_technical_indicators(goal)
#print("\"indicator:\" = ", indicator)

print(mm.MoneySplit(bot.get_balance())[0])

balance_type = "PRACTICE"
bot.change_balance(balance_type)
print("Balance: ",bot.get_balance())
amount = float(input("amount: "))

# Signal Command

while True:
    signal = input("Command: ")
    if signal == "buy":
        check, id = bot.buy(amount,"EURUSD","call",1)
        if check:
            print("!buy!")
            print(bot.check_win_v4(id)[0],"You got",round(bot.check_win_v4(id)[1],2))
        else:
            print("buy fail")
        #bot.buy_digital_spot("EURUSD",amount,"call",1)
    elif signal == "sell":
        check, id = bot.buy(amount,"EURUSD","put",1)
        if check:
            print("!sell!")
            print(bot.check_win_v4(id)[0],"You got",round(bot.check_win_v4(id)[1],2))
        else:
            print("sell fail")
        #bot.buy_digital_spot("EURUSD",amount,"put",1)
    elif signal == "stop":
        break
    else:
        pass
print("End process")