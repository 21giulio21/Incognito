import sqlite3
from random import randint

class DB:

    #Passo il path nel costruttore
    def __init__(self,pathDatabase):
        self.conn = sqlite3.connect(pathDatabase)
        self.cursore = self.conn.cursor()

        # TORNA UN ARRay associativo in cui in posizione ARRAY[0] conTiene la prima tupla e
        # ARRAY[0][0] CONTIENE L'ID DELLA TUPLA 0 E ARRAY[0][1] torna lo zipcode della
        # prima tupla E ARRAY[0][2] TORNA IL NOME
    def selectAllFromTable1(self):
        query = "SELECT * FROM TABELLA_1";
        return self.cursore.execute(query).fetchall();
    def selectAllFromTable2(self):
        query = "SELECT * FROM TABELLA_2";
        return self.cursore.execute(query).fetchall();
    def selectAllFromTable3(self):
        query = "SELECT * FROM TABELLA_3";
        return self.cursore.execute(query).fetchall();

    def svuotaTabella(self,tabella):
        query = "DELETE FROM "+tabella+" WHERE 1=1;"
        self.cursore.execute(query)




    def insertIntoTable1(self):

        nomi = ["Sofia","Aurora","Giulia","Emma","Gianni","Giulio","Alessandro","Alessio","Simone"]
        cap =  ["16121","16120","16132","16321","12121","26121","36121","16336",
               "16231", "16430", "26132", "36622", "52151", "45141", "36611", "19306",
               "19834", "12234", "12345", "14451", "15126", "26178", "76728", "18906",
               "48394", "85745", "59658", "56743", "15126", "23445", "12111", "23433",
               "47385", "49835", "57483", "43215", "15126", "98745", "23432", "23244",
               "37489", "28390", "48392", "34321", "34567", "43456", "32433", "43232"]

        for i in range(0,400):
            nome = nomi[randint(0, len(nomi)-1)]
            capSingolo = cap[randint(0, len(cap)-1)]
            if capSingolo<1000:
                return

            query = "INSERT INTO TABELLA_1 VALUES (NULL,'" + capSingolo +"','"+nome + "')"
            self.cursore.execute(query)
            self.conn.commit()

    def insertIntoTable3(self):

        nomi = ["Sofia", "Aurora", "Giulia", "Emma", "Francesco", "Giulio", "Alessandro", "Alessio"]
        cap = ["16121", "16120", "16132", "16321", "12121", "26121", "36121", "16336",
               "16231", "16430", "26132", "36622", "52151", "45141", "36611", "19306",
               "19834", "12234", "12345", "14451", "15126", "26178", "76728", "18906",
               "48394", "85745", "59658", "56743", "15126", "23445", "12111", "23433",
               "47385", "49835", "57483", "43215", "15126", "98745", "23432", "23244",
               "37489", "28390", "48392", "34321", "34567", "43456", "32433", "43232"]

        for i in range(0, 400):
            nome = nomi[randint(0, len(nomi) - 1)]
            capSingolo = cap[randint(0, len(cap) - 1)]
            giornoNascita = randint(1, 30)
            meseNascita = randint(1, 12)
            annoNascita = randint(1932,2000)
            stringaDataNascita = str(giornoNascita) + "-" + str(meseNascita) + "-" + str(annoNascita)
            if nome[len(nome) - 1] == "o":
                sesso = "M"
            else:
                sesso = "F"
            if capSingolo < 1000:
                return

            query = "INSERT INTO TABELLA_3 VALUES (NULL,'" + capSingolo + "', '" + sesso + "'  ,'" + stringaDataNascita +"' ,'" + nome + "')"
            self.cursore.execute(query)
            self.conn.commit()

    def insertIntoTable2(self):

        nomi = ["Sofia", "Aurora", "Giulia", "Emma", "Francesco", "Giulio", "Alessandro", "Alessio"]
        cap = ["16121", "16120", "16132", "16321", "12121", "26121", "36121", "16336",
               "16231", "16430", "26132", "36622", "52151", "45141", "36611", "19306",
               "19834", "12234", "12345", "14451", "15126", "26178", "76728", "18906",
                "48394", "85745", "59658", "56743", "15126", "23445", "12111", "23433",
               "47385", "49835", "57483", "43215", "15126", "98745", "23432", "23244",
               "37489", "28390", "48392", "34321", "34567", "43456", "32433", "43232"]

        for i in range(0, 400):
            nome = nomi[randint(0, len(nomi) - 1)]
            capSingolo = cap[randint(0, len(cap) - 1)]
            if nome[len(nome)-1] == "o":
                sesso = "M"
            else:
                sesso = "F"
            if capSingolo < 1000:
                return

            query = "INSERT INTO TABELLA_2 VALUES (NULL,'" + capSingolo + "', '"+ sesso +"'  , '" + nome + "')"
            self.cursore.execute(query)
            self.conn.commit()

    # In questa funzione deve esserci: Select COUNT(*) FROM TABELLA GROUP BY Q1,Q2
    # TORNA UN ARRay associativo in cui in posizione ARRAY[0] conviene la prima tupla e
    # ARRAY[0][0] CONTIENE L'ID DELLA TUPLA 0 E ARRAY[0][1] torna lo zipcode della
    # prima tupla, ovviamente i qi vanno datiin questo modo: q1,q2
    def selectCountFromQuasiIdentifierTabella1(self,qi):
        query = "Select Count(*),"+qi+" from TABELLA_1 GROUP BY " + qi
        return self.cursore.execute(query).fetchall();

     # In questa funzione deve esserci: Select COUNT(*) FROM TABELLA GROUP BY Q1,Q2
    # TORNA UN ARRay associativo in cui in posizione ARRAY[0] conviene la prima tupla e
    #  ARRAY[0][0] CONTIENE L'ID DELLA TUPLA 0 E ARRAY[0][1] torna lo zipcode della
    # prima tupla e ARRAY[0][2] contiene il sesso, ovviamente i qi vanno datiin questo modo: q1,q2
    def selectCountFromQuasiIdentifierTabella2(self,qi):
        query = "Select Count(*),"+qi+" from TABELLA_2 GROUP BY " + qi
        return self.cursore.execute(query).fetchall();

    # In questa funzione deve esserci: Select COUNT(*) FROM TABELLA GROUP BY Q1,Q2
    # TORNA UN ARRay associativo in cui in posizione ARRAY[0] conviene la prima tupla e
    #  ARRAY[0][0] CONTIENE L'ID DELLA TUPLA 0 E ARRAY[0][1] torna lo zipcode della
    # prima tupla e ARRAY[0][2] contiene il sesso,ovviamente i qi vanno datiin questo modo: q1,q2
    def selectCountFromQuasiIdentifierTabella3(self,qi):
        query = "Select Count(*),"+qi+" from TABELLA_3 GROUP BY " + qi
        return self.cursore.execute(query).fetchall();


    def stampaTabella2(self):
        valoriTornati = self.selectAllFromTable2()
        for i in valoriTornati:
            id, zipcode,sesso, nome = i
            print " ID -> " + str(id)
            print " NOME ->" + nome
            print " CAP ->" + zipcode
            print " SESSO ->" + sesso
            print "\n"

    def stampaTabella3(self):
        valoriTornati = self.selectAllFromTable3()
        for i in valoriTornati:
            id, zipcode,sesso, data, nome = i
            print " ID -> " + str(id)
            print " NOME ->" + nome
            print " CAP ->" + zipcode
            print " SESSO ->" + sesso
            print " data ->" + data
            print "\n"



    def stampaTabella1(self):
        valoriTornati = self.selectAllFromTable1()
        for i in valoriTornati:
            id, zipcode, nome = i
            print " ID -> " + str(id)
            print " NOME ->" + nome
            print " CAP ->" + zipcode
            print "\n"

    # Quando chiamo la funzione anonumizzazione ricreo il database che deve essere modificato
    # in questo modo anonimizzo  questo database temporaneo.
    # Questa funzione viene chiamata pero da un DB db2 = DB(pathDatabase da modificare)
    def anonimizzazione(self,tabella,dizionario):

        #Riempio prima di tutto il database nuovo dopo averlo svuotato
        self.svuotaTabella(tabella)

        #Inserisco le tuple nella tabella che devo utilizzare per anonimizzare
        if tabella == "TABELLA_1":
            self.insertIntoTable1()
        elif tabella == "TABELLA_2":
            self.insertIntoTable2()
        elif tabella == "TABELLA_3":
            self.insertIntoTable3()

        #dizionario  fa

        if qi == "SESSO":
            for i in range(0,400):
                query = "UPDATE "+tabella+" SET SESSO = '*' WHERE ID=" + str(i)
