from iqoptionapi.stable_api import IQ_Option as iq

uid_file = open('uid.txt', 'r')
uid = uid_file.read()
uid = uid.split('\n')
email = uid[0]
email = email.split('=')[1].strip()
password = uid[1]
password = password.split('=')[1].strip()
uid_file.close()

print(email)
print(password)
bot = iq(email, password)
bot.connect()
print(bot.check_connect())
