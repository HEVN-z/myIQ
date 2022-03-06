import asyncio
from iqoptionapi.stable_api import IQ_Option
from _sample.thread_buy import buyThread as thread_buy
email = "dummy.esper@gmail.com"
password = "12651265exe"
Iq=IQ_Option(email,password)
Iq.connect()#connect to iqoption
Money=1
ACTIVES="EURUSD-OTC"
ACTION="call"#or "put"
expirations_mode=1
buy1 = thread_buy(Iq,Money,ACTIVES,ACTION,expirations_mode)
'''
async def buy():
    Iq.buy(Money,ACTIVES,ACTION,expirations_mode)
    print("buy")
    await asyncio.sleep(2)
'''
isBuy = False
target_time = 30
looper = False
#while True:
#    remaning_time=Iq.get_remaning(expirations_mode)-1
#    purchase_time=remaning_time-target_time
#    print(purchase_time)
#    if purchase_time==target_time and isBuy == False:
#        buy()
#        isBuy = True
#    if purchase_time<target_time -1:
#        isBuy = False
#    if True:
#        break

while True:
    remaning_time=Iq.get_remaning(expirations_mode)-1
    purchase_time=remaning_time-target_time
    print(purchase_time)
    if purchase_time == target_time and isBuy == False:
        buy1.run().start()
        looper = True
        #asyncio.run(buy())
    elif purchase_time == target_time+1 and looper:
        isBuy = True