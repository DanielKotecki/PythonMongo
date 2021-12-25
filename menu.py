a=3

while True:
    print("1.Wyświetl cała zawartość bazy danych.")
    wybor=int(input("podaj:"))  
    if wybor==1:
        print("1")
    elif wybor==2:
        print("2")
    elif wybor==3:
        print("3")
        
           
       
    print("1.Utwórz bazę.")
    print("2.Podłącz sie do bazy danych")
    wybor=input("Podaj:")
    if wybor=="1":
        nameDb=input("nazwaBazy:")
        nameCol=input("nazwaKolekcji:")
        
    elif wybor=="2":
        nameDb=input("nazwaBazy:")
        nameCol=input("nazwaKolekcji:")
        sciezka=input("podaj ścieżkę do pliku:")
        with open(sciezka,"r",encoding='utf8') as f:
        file_data = json.load(f)
        mycol.insert_many(file_data) 
