############################################################################################
## Import packages
############################################################################################

import json


############################################################################################
## Load files
############################################################################################

json_file = json.load(open("mmjs.json"))

###############################################################################################
## Function
###############################################################################################

def get_base_amount():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['amount']['base_amount']

def get_order_amount():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['amount']['order_amount']

def get_total_amount():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['amount']['total_amount']

def get_today_profit():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['profit']['today_total_profit']

def get_profit_target():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['profit']['profit_target']

def get_martingale_level():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['martingale']['level']
    
def get_martingale_max_level():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['martingale']['max_level']

def get_martingale_min_level():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['martingale']['min_level']


def get_martingale_multiplier():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['martingale']['multiplier']

def get_anti_martingale_multiplier():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['martingale']['anti_multiplier']

def get_target_goal():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['target_goal']

def get_target_loss():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['target_loss']

def get_Active():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['Active']

def get_email():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['email']

def get_password():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['password']

def get_rate1():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['rate1']

def get_rate5():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['rate5']

def get_rate15():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['rate15']

def get_rate60():
    json_file = json.load(open("mmjs.json",'r'))
    return json_file['rate60']

############################################################################################
## Write files
############################################################################################

def set_base_amount(new_base_amount):
    json_file['amount']['base_amount'] = new_base_amount
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_order_amount(new_order_amount):
    if new_order_amount < 1:
        new_order_amount = 1
    json_file['amount']['order_amount'] = new_order_amount
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_total_amount(new_total_amount):
    json_file['amount']['total_amount'] = new_total_amount
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_today_profit(new_today_profit):
    json_file['profit']['today_total_profit'] = new_today_profit
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_profit_target(new_profit_target):
    json_file['profit']['profit_target'] = new_profit_target
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_martingale_level(new_martingale_level):
    json_file['martingale']['level'] = new_martingale_level
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_martingale_max_level(new_martingale_max_level):
    json_file['martingale']['max_level'] = new_martingale_max_level
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_martingale_min_level(new_martingale_min_level):
    json_file['martingale']['min_level'] = new_martingale_min_level
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_martingale_multiplier(new_martingale_multiplier):
    json_file['martingale']['multiplier'] = new_martingale_multiplier
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_anti_martingale_multiplier(new_anti_martingale_multiplier):
    json_file['martingale']['anti_multiplier'] = new_anti_martingale_multiplier
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_target_goal(new_target_goal):
    json_file['target_goal'] = new_target_goal
    json.dump(json_file, open("mmjs.json", "w"),indent=4)

def set_target_loss(new_target_loss):
    json_file['target_loss'] = new_target_loss
    json.dump(json_file, open("mmjs.json", "w"),indent=4)