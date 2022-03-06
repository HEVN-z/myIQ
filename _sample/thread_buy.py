from iqoptionapi.stable_api import IQ_Option 
import threading
class buyThread (threading.Thread):
    def __init__(self, account,price,ACTIVES,ACTION,expirations):
        threading.Thread.__init__(self)
        self.account=account
        self.price=price
        self.ACTIVES=ACTIVES
        self.ACTION=ACTION
        self.expirations=expirations
    def run(self):
         
        ans=self.account.buy(self.price, self.ACTIVES, self.ACTION, self.expirations)
        print(ans)

#account1=IQ_Option("dummy.esper@gmail.com","12651265exe")
#account1.connect()
#d = account1.get_binary_option_detail()
#print(d["EURUSD"]["turbo"])

#print(d["USDJPY-OTC"]["turbo"] != {})


'''thread1 = buyThread(account1,1, "EURUSD-OTC", "put",1)
thread2 = buyThread(account1,5, "EURUSD-OTC", "call",1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()'''