import sqlite3
from DB import DB

#c = conn.cursor()
# Insert a row of data
#c.execute("INSERT INTO TABELLA VALUES (NULL,'M')")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()

db = DB('./database.sqlite')
db.insertIntoTable("TABELLA")
valoriTornati =  db.selectAllFromTable("TABELLA")

for i in valoriTornati.fetchall():
    id , nome = i
    print " ID -> " + str(id)
    print " NOME ->" +  nome

#Print del count
print db.selectCountFromQuasiIdentifier("NOME","TABELLA").fetchall()