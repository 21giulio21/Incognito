import sqlite3

class DB:

    #Passo il path nel costruttore
    def __init__(self,pathDatabase):
        self.conn = sqlite3.connect(pathDatabase)
        self.cursore = self.conn.cursor()

    def selectAllFromTable(self,tabella):
        query = "SELECT * FROM " + tabella;
        #query = "SHOW DATABASES;"
        return self.cursore.execute(query);

    def insertIntoTable(self,tabella):
        query = "INSERT INTO " + tabella + " Values (NULL,'H')"
        self.cursore.execute(query)
        self.conn.commit()

    #In questa funzione deve esserci: Select COUNT(*) FROM TABELLA GROUP BY Q1,Q2
    def selectCountFromQuasiIdentifier(self,qid,tabella):
        query = "Select Count(*) from "+tabella + " GROUP BY " + qid
        return self.cursore.execute(query);

