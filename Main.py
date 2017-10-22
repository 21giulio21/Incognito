import Nodo
import sys
import math

def stampo(grafo):
    for i in grafo:
        print i.descrizione()

quasiIdentifier = []
for i in range(1,len(sys.argv)):
    g = 0
    g = raw_input("inserire il grado di anonimizzazione: ")
    tupla = (sys.argv[i],str(g))
    quasiIdentifier.append(tupla)


numeroQuasiIdentifier = len(quasiIdentifier)



for i in range(1,numeroQuasiIdentifier):
    numeroGrafi = math.factorial(numeroQuasiIdentifier) / (math.factorial(i) * math.factorial(numeroQuasiIdentifier-i))

    #Grafi che vanno a costruirsi dal numero di grafi dell'iterazione
    serieDiGrafi = []
    for i in range(0,numeroGrafi):
        grafo = []
        for i in range(0,len(quasiIdentifier)):
            grafo.append(Nodo.Nodo(quasiIdentifier[i][0],False))

        '''
        Costruisco tutti i grafi
        '''
# esco da tutti i for

#for........False
    '''
    Ricerca in ampieza
    '''





