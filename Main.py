from Nodo import Nodo


generalizzazione = dict()
generalizzazione['zipcode'] = 5
generalizzazione['sesso'] = 2
generalizzazione['data'] = 3
numeroQuasiIdentifier = 3


def stampo(root):
    i = 0
    while(len(root.nextNode) > 0):
        node = root.nextNode.pop()
        print("Nodo successivo esistente !!!!" + str(i) + " ")
        print(node)
        i += 1

'''
Esegue la query e inserisce tutti gli zipcode (etc...) all'interno del primo nodo
'''

def costruisciGrafoRicorsivo(nodo, i, quasiIdIndex):

    a = nodo.levelOfGeneralizations[nodo.quasiIdentifier[quasiIdIndex]]
    b = generalizzazione[nodo.quasiIdentifier[quasiIdIndex]]
    print("valore di a -> " + str(a))
    print("valore di b -> " + str(b))
    if(a == b):
        return
    nodo.levelOfGeneralizations[nodo.quasiIdentifier[quasiIdIndex]] = i
    nodoSucc = Nodo(nodo.quasiIdentifier, False)
    nodo.nextNode.append(nodoSucc)
    costruisciGrafoRicorsivo(nodoSucc, i+1, quasiIdIndex)

def costruisciGrafo(root, quasiIdentifiers, quasiIdIndex):
    root.isRoot = True
    root.quasiIdentifier = quasiIdentifiers

    root.levelOfGeneralizations[quasiIdentifiers[quasiIdIndex]] = 0
    nodo = Nodo(quasiIdentifiers, False)
    print(nodo.quasiIdentifier[quasiIdIndex])
    root.nextNode.append(nodo)
    costruisciGrafoRicorsivo(nodo, 1, quasiIdIndex)
    return root


quasiIdentifier = []
quasiIdentifier.append("zipcode")
quasiIdentifier.append("sesso")
quasiIdentifier.append("data")

# generiamo tutte le coppi di quasiIdenifier
quasiIdentifierCouple = []
for qi in range(0, len(quasiIdentifier)):
    for i in range(qi, len(quasiIdentifier)):
        if(qi != i):
            tupla = (quasiIdentifier[qi], quasiIdentifier[i])
            quasiIdentifierCouple.append(tupla)

for i in quasiIdentifierCouple:
    print(i)

for i in range (0, 3):
    root = Nodo(quasiIdentifier, False)
    root = costruisciGrafo(root, quasiIdentifier, i)
    stampo(root)






