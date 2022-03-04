import time
from iqoptionapi.stable_api import IQ_Option

from indic_psar import PSAR


email = "dummy.esper@gmail.com"
password = "12651265exe"

bot = IQ_Option(email,password)
bot.connect()
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
indic_psar = PSAR()

while True:
    if bot.check_connect():
        print("Connected")
        break
    else:
        print("Not Connected")
        break

balance_type = "PRACTICE"
bot.change_balance(balance_type)
print("Balance: ",bot.get_balance())
amount = float(input("amount: "))

while True:
    signal = input("Command: ")
    if signal == "buy":
        check, id = bot.buy(amount,"EURUSD","call",1)
        if check:
            print("!buy!")
        else:
            print("buy fail")
        #bot.buy_digital_spot("EURUSD",amount,"call",1)
    elif signal == "sell":
        check, id = bot.buy(amount,"EURUSD","put",1)
        if check:
            print("!sell!")
        else:
            print("sell fail")
        #bot.buy_digital_spot("EURUSD",amount,"put",1)
    elif signal == "stop":
        break
    else:
        pass
print("End process")
