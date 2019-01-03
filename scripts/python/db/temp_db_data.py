import time,datetime 
from tinydb import TinyDB, Query
db = TinyDB('db.json')
import json

temps = [float(item['temperature']) for item in db]

def min_temp():
    return min(temps)

def max_temp():
    return max(temps)

def mean_temp():
    return sum(temps)/len(temps)

def temp_items(start,end):
    temps = Query()
    return db.search((temps.timestamp >= start) & (temps.timestamp <= end))