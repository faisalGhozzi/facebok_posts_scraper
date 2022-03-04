from typing import Collection
from pymongo import MongoClient

try:
    con = MongoClient()
    print("connected!")
except:
    print('could not connect')

db = con.database

collection = db.facebook_scraped