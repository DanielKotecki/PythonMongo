import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
#name=input("Podaj imie:")
#mydict = { "name": name, "address": "Highway 37","other":{"age":23} }

#x = mycol.insert_one(mydict)

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

myquery = { "name":"Daniel" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

  with open('currencies.json') as f:
    file_data = json.load(f)

# use collection_currency.insert(file_data) if pymongo version < 3.0
mycol.insert_one(file_data) 