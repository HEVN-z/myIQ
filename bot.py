from iqoptionapi.api import IQOptionAPI
from iqoptionapi.stable_api import IQ_Option
import logging
import time
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

error_password = """{code":"invalid_credentials","message":"You entered the wrong credential, Please check that login/password is correct."}"""
Iq = IQ_Option('e-exe-e@live.com','myHeavenz13')

"""
check,reason = Iq.connect()

if check:
    print("Start your robot")
    while True:
        if Iq.check_connect() == False:
            print("Reconnecting")
            check, reason = Iq.connect()
            if check:
                print("Reconnect success!")
            else:
                if reason==error_password:
                    print("Wrong password")
                else:
                    print("No Network")
else:
    if reason=="Error: [Errno -2] Name or service not known":
        print("No Network")
"""

print("API Version = ",IQ_Option.__version__)
print("Connecting = ",Iq.check_connect())
balance_type="PRACTICE"
