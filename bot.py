import asyncio
from iqoptionapi.stable_api import IQ_Option
email = "dummy.esper@gmail.com"
password = "12651265exe"
Iq=IQ_Option(email,password)
Iq.connect()#connect to iqoption
Money=1
ACTIVES="EURUSD"
ACTION="call"#or "put"
expirations_mode=1

async def buy():
    Iq.buy(Money,ACTIVES,ACTION,expirations_mode)
    print("buy")
    await asyncio.sleep(2)

isBuy = False
target_time = 30
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
    if purchase_time==30:
        asyncio.run(buy())
    if purchase_time==28:
        break