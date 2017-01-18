#!/usr/bin/python
#!-*- coding: utf -8 -*-
import time
import json

#{"active": 0, "adspotid": "10000148", "bids": 2, "carrier": "46999", "city": "-", "clicks": 1, "connectType": "2", "costs": 0.008574, "creativeid": "100000434", "make": "others", "model": "0", "os": "Android", "osv": "5.0", "province": "23", "time": "2016110817", "wins": 2}
last_hour = time.timestrf("%Y%m%d%H",time.localtime(time.time()-3600))
path = '/Users/haoshun/LOG/Logger/result.'+last_hour+'.log'
for line in open(path):
    jsonStr = line.rsplit("\r\n")
    jsonObj = json.loads(jsonStr)
    actives = jsonObj['active']
    bids = jsonObj['bids'] 
carrier = jsonObj   
adspotid = jsobObj['adspotid']
    
