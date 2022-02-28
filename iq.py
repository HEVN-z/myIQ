from iqoptionapi.stable_api import IQ_Option
import logging
import random
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
email = "e-exe-e@live.com"
password = "meHeavenz13"
Iq=IQ_Option(email,password)
Iq.connect()#connect to iqoption
ALL_Asset=Iq.get_all_open_time()
#check if open or not
print(ALL_Asset["forex"]["EURUSD"]["open"])