import sqlite3
import random

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
        groupByString = ""
        for i in range(0, len(qid)):
            if i == len(qid) - 1:
                groupByString += qid[i] + ";"
            else:
                groupByString += qid[i] + ", "
        query = "Select Count(*) from " + tabella + " GROUP BY " + qid
        return self.cursore.execute(query)

    def emulateFrequencySetComputation(self, level):
        frequencySet = []
        if level == 1:
            maximum = 2
            minimum = 1
        elif level == 2:
            maximum = 4
            minimum = 2
        else:
            maximum = 6
            minimum = 3
        for i in range(0, 10):
            frequencySet.append(random.randint(minimum, maximum))
        return frequencySet

