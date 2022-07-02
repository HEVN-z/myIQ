############################################################################################
## Import packages
############################################################################################

import json

############################################################################################
## Load files
############################################################################################

file = "TI_multi.json"
json_file = json.load(open(file))

###############################################################################################
## Function
###############################################################################################

def get_enable(active):
    json_file = json.load(open(file,'r'))
    return json_file[active]['enable']

def get_data(active,time):
    json_file = json.load(open(file,'r'))
    return json_file[active]['data'][time]

def get_percent(active):
    json_file = json.load(open(file,'r'))
    return json_file[active]['data']['percent']

############################################################################################
## Write files
############################################################################################

def set_update_enable(active,new_enable):
    json_file[active] = new_enable
    json.dump(json_file, open(file, "w"),indent=4)

def set_data(active,one,five,fifteen,sixty):
    json_file[active]['data']['one'] = one
    json_file[active]['data']['five'] = five
    json_file[active]['data']['fifteen'] = fifteen
    json_file[active]['data']['hour'] = sixty
    json.dump(json_file, open(file, "w"),indent=4)

def set_percent(active,percent):
    json_file[active]['data']['percent'] = percent
    json.dump(json_file, open(file, "w"),indent=4)

