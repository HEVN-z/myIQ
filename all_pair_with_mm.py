from iqoptionapi.stable_api import IQOptionAPI as iq

uid_file = open('uid.txt', 'r')
uid = uid_file.read()
u = uid.split('\n')
uid_file.close()

print(u)
