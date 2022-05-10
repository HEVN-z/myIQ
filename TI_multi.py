############################################################################################
## Import packages
############################################################################################

import json


############################################################################################
## Load files
############################################################################################

json_file = json.load(open("TI_multi.json"))

###############################################################################################
## Function
###############################################################################################

def get_enable(active):
    json_file = json.load(open("TI_multi.json",'r'))
    return json_file[active]['enable']

def get_data(active,time):
    json_file = json.load(open("TI_multi.json",'r'))
    return json_file[active]['data'][time]

def get_percent(active):
    json_file = json.load(open("TI_multi.json",'r'))
    return json_file[active]['data']['percent']

############################################################################################
## Write files
############################################################################################

def set_update_enable(active,new_enable):
    json_file[active] = new_enable
    json.dump(json_file, open("TI_multi.json", "w"),indent=4)

def set_data(active,one,five,fifteen,sixty):
    json_file[active]['data']['one'] = one
    json_file[active]['data']['five'] = five
    json_file[active]['data']['fifteen'] = fifteen
    json_file[active]['data']['hour'] = sixty
    json.dump(json_file, open("TI_multi.json", "w"),indent=4)

def set_percent(active,percent):
    json_file[active]['data']['percent'] = percent
    json.dump(json_file, open("TI_multi.json", "w"),indent=4)
