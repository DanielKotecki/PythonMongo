import pymongo
import json
import codecs
from pymongo import MongoClient
nameDb=""
nameCol=""
sciezka=""
print("1.Podłącz sie do bazy danych")
print("2.Utwórz bazę.")
wybor=input("Podaj:")
if wybor=="1":
        nameDb=input("nazwaBazy:")
        nameCol=input("nazwaKolekcji:")
        
elif wybor=="2":
    nameDb=input("nazwaBazy:")
    nameCol=input("nazwaKolekcji:")
    sciezka=input("podaj ścieżkę do pliku:")
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[nameDb]
mycol = mydb[nameCol]
if not sciezka=="":
    
    with open(sciezka,"r",encoding='utf8') as f:
        file_data = json.load(f)
    mycol.insert_many(file_data) 

while True:
    print("1.Wyświetl cała zawartość bazy danych.")
    print("2.Wyświetl z bazy danych tylko to miasto które podam.")
    print("3.Podaj nazwę zabytku")
    print("4.Wyświetl kategorie i ilość która znajduje sie w bazie")
    print("5.Podaj zabytek do usunięcia.")
    print("6.Miasto do usunięcia")
    print("7.Opcja szukająca w Położeniu miasta danego słowa i wyświetla miasto")
    print("9.Wyjście")
    wybor=int(input("podaj:"))  
    if wybor==1:
        for x in mycol.find():
                  
                    
                    print(x)
                    
                       
    elif wybor==2:
        nazwa=input("Podaj nazwę miasta z Wielkiej litery aby wyszukać zabytki:")
        ## dokument = mycol.find({"miasto":nazwa},{"_id":0,})
        dokument = mycol.find({"miasto":nazwa},{"_id":0})
        for x in dokument:
            print(x)
        
    elif wybor==9:
        print("3")
        break
    elif wybor==3:
         nazwa=input("Zabytek:")
         dokument = mycol.find({"zabytki":{ "$elemMatch": { "nazwa": nazwa}}},{"zabytki.$":1,"miasto":1,"_id":0})
         for x in dokument:
                print(x)
    elif wybor==4:
        dokument = mycol.aggregate([{"$unwind" : "$zabytki" },
            {"$group":{"_id":"$zabytki.typ_zabytku","ilość":{"$sum":1}}}])
        for x in dokument:
             print(x)
    elif wybor==5:
        usun=input("Podaj zabytek do usunięcia:")
        mycol.update_one({},{"$pull":{"zabytki":{"nazwa":usun}}})

        
    elif wybor==6:
        usun=input("Podaj nazwę miasta do usunięcia:")
        mycol.delete_one({"miasto":usun})
    elif wybor==7:
      szukane=input("Podaj co szukać w tekście:")
      dk= mycol.create_index([('Położenie',"text")],  default_language='english')
      cursor = mycol.find({'$text': {'$search':szukane}})
      for x in cursor:
            print(x)
    elif wybor==8:
        zaZabytku=""
        miasto=""
        miasto=input("Podaj miasto do którego dodać zabytek")
        zaZabytku=input("Podaj ścieżkę do pliku JSON zawierającego jeden zabytek:")
        with open(zaZabytku,"r",encoding='utf8') as f:
            file_data = json.load(f)
        mycol.update_one({"miasto":miasto},{"$push":{"zabytki":file_data}}) 


