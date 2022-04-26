from multiprocessing import Process
from iqoptionapi.stable_api import IQ_Option
import time

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

def getEURUSD():
    while True:
        bot.get_technical_indicators("EURUSD")
        print("EURUSD \t 1")
def getAUDUSD():
    while True:
        bot.get_technical_indicators("AUDUSD")
        print("AUDUSD \t\t 2")
def getEURJPY():
    while True:
        bot.get_technical_indicators("EURJPY")
        print("EURJPY \t\t\t 3")

def timer():
    while True:
        time.sleep(1)
        print("\t\t\t\t\t\t",time.time())
'''if __name__ == "__main__":
    p1,p2,p3 = Process(target=getEURUSD),Process(target=getAUDUSD),Process(target=getEURJPY)
    p1.start()
    p2.start()
    p3.start()'''
if __name__ == "__main__":
    p1 = Process(target=getEURUSD, args=())
    p2 = Process(target=getAUDUSD, args=())
    p3 = Process(target=getEURJPY, args=())
    ptime = Process(target=timer, args=())
    p1.start()
    p2.start()
    p3.start()
    ptime.start()
    p1.join()
    p2.join()
    p3.join()
    ptime.join()
