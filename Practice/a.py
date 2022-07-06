from iqoptionapi.stable_api import IQ_Option
from threading import Thread
import time
from dotenv import load_dotenv
import os
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
mongodb = os.getenv("MONGO_URI")

begin_time = time.time()
bot = IQ_Option(email, password)
bot.connect()
print(bot.get_balance())
end_time = time.time()
print("total time", end_time - begin_time)
