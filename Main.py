from Nodo import Nodo


generalizzazione = dict()
generalizzazione['zipcode'] = 3
generalizzazione['sesso'] = 2
generalizzazione['data'] = 3
numeroQuasiIdentifier = 3


def stampo(root):
    i = 0
    print(root)
    while(len(root.nextNode) > 0):
        node = root.nextNode.pop()
        print("Nodo successivo esistente !!!!" + str(i) + " ")
        print(node)
        i += 1

'''
Esegue la query e inserisce tutti gli zipcode (etc...) all'interno del primo nodo
'''

def costruisciGrafoRicorsivo(nodo, generValue, quasiIdIndex):

    for i in range(0, len(nodo.quasiIdentifier)):
        livelloDiGeneralizzazioneCorrente = nodo.levelOfGeneralizations[nodo.quasiIdentifier[quasiIdIndex]]
        livelloDiGeneralizzazioneMax = generalizzazione[nodo.quasiIdentifier[quasiIdIndex]]
        print("valore di a -> " + str(livelloDiGeneralizzazioneCorrente))
        print("valore di b -> " + str(livelloDiGeneralizzazioneMax))
        if(livelloDiGeneralizzazioneCorrente < livelloDiGeneralizzazioneMax):
            nodo.levelOfGeneralizations[nodo.quasiIdentifier[quasiIdIndex]] = generValue
            nodoSucc = Nodo(nodo.quasiIdentifier, False)
            nodo.nextNode.append(nodoSucc)
            costruisciGrafoRicorsivo(nodoSucc, generValue + 1, quasiIdIndex)
        elif(livelloDiGeneralizzazioneCorrente == livelloDiGeneralizzazioneMax and i < len(nodo.quasiIdentifier)):
            continue
        else:
            return


def costruisciGrafo(root, quasiIdentifiers, quasiIdIndex):
    root.isRoot = True
    root.quasiIdentifier = quasiIdentifiers

    for i in range(0, len(quasiIdentifiers)):
        root.levelOfGeneralizations[quasiIdentifiers[i]] = 0
        nodo = Nodo(quasiIdentifiers, False)
        print(nodo.quasiIdentifier[quasiIdIndex])
        root.nextNode.append(nodo)
        costruisciGrafoRicorsivo(nodo, 1, quasiIdIndex)
    return root


quasiIdentifier = []
quasiIdentifier.append("zipcode")
quasiIdentifier.append("sesso")


# generiamo tutte le coppi di quasiIdenifier
quasiIdentifierCouple = []
for qi in range(0, len(quasiIdentifier)):
    for i in range(qi, len(quasiIdentifier)):
        if(qi != i):
            tupla = (quasiIdentifier[qi], quasiIdentifier[i])
            quasiIdentifierCouple.append(tupla)

for i in quasiIdentifierCouple:
    print(i)


root = Nodo(quasiIdentifier, False)
root = costruisciGrafo(root, quasiIdentifier, 0)
stampo(root)






