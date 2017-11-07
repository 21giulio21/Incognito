'''
    Questa classe ha il solo scopo di illustrare il funzionamento del
    modulo DB.py e di costruire il database andando a riempire le tre tabelle.
    Non verrà dunque invocata nell'esecuzione del programma, ma solo nella
    fase di setup (la prima volta).
'''
from DB import DB

'''
Le tabella sono costruite in questo modo: 

TABELLA_1: ID, ZIPCODE, NOME
TABELLA_2: ID, ZIPCODE, SESSO, NOME
TABELLA_3: ID, ZIPCODE, SESSO, DATA_NASCITA, NOME



'''
db = DB('/home/giulio/Scrivania/AonzoVenduto.sqlite')
dizionario = dict()
dizionario["SESSO"] = 0
dizionario["ZIPCODE"] = 5
dizionario["DATA_NASCITA"] = 1
db.anonimizzazione("TABELLA_3",dizionario)


#db.insertIntoTable2()


#db.insertIntoTable1()
#db.svuotaTabella("TABELLA_1")
#db.stampaTabella1()
#v = db.selectAllFromTable1()

#db.insertIntoTable3()

#print db.selectCountFromQuasiIdentifierTabella2()


'''
#Print del count
print db.selectCountFromQuasiIdentifier("NOME","TABELLA").fetchall()
'''