from asyncio.windows_events import NULL
from concurrent.futures import thread
import time
from iqoptionapi.stable_api import IQ_Option

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

# Variables

isBuy = False
target_time = 30
timer = 0
Action = "hold"
rate1 = 45
rate2 = 40
rate3 = 40

balance = bot.get_balance()
print("Your balance is",balance,"\n What you want to play")

Money = input("Money amount : ")
if Money == "" or Money == NULL:
    Money = 1
float(Money)
print("Default money =",Money)

Active = input("Currency pair : ")
if Active == "" or Active == NULL:
    Active = "EURUSD"
Active.upper()
print("Default currency pair =",Active)

expirations_mode = input("Expired mode : ")
if expirations_mode == "" or expirations_mode == NULL:
    expirations_mode = 1
int(expirations_mode)
print("Default expired mode =",expirations_mode)

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

    return average_one, average_five, average_fifty

#Buy Loop

while True:
    average_one, average_five, average_fifty = ind()

    purchase_time = bot.get_remaning(expirations_mode)-1-target_time
    
    #Slower timer print out
    if timer != average_one.__floor__():
        print("Average 1 minute:", average_one.__floor__())
        print("Average 5 minutes:", average_five.__floor__())
        print("Average 15 minutes:", average_fifty.__floor__())
        print("Time update",purchase_time)
        timer = average_one.__floor__()

    #Buy conditions

    if average_one > rate1 and average_five > rate2 and average_fifty > rate3:
        Action = "call"
    elif average_one < (rate1*-1) and average_five < (rate2*-1) and average_fifty < (rate3*-1):
        Action = "put"
    else:
        Action = "hold"

    #Buy

    if purchase_time==target_time and isBuy == False and Action != "hold":
        check, id = bot.buy(Money,Active,Action,expirations_mode)
        isBuy = True
        if check:
            print("!buy!",Action)
            print(bot.check_win_v4(id)[0],"you got",round(bot.check_win_v4(id)[1],2))
        else:
            print("buy fail")
    if purchase_time<target_time -5:
        isBuy = False