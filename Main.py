import copy
from DB import DB
import Graph
import time

delta = 5

generalizzazione = dict()
generalizzazione['ZIPCODE'] = 5
generalizzazione['SESSO'] = 1
generalizzazione['DATA_NASCITA'] = 3
numeroQuasiIdentifier = 3
listOfQuasiIdentifier = ['ZIPCODE', 'SESSO', 'DATA_NASCITA']

def suppression(frequencySet):
    toRet = []
    for i in frequencySet:
        if i > delta:
            toRet.append(i)
    return toRet


def setUpDB(db):
    db.svuotaTabella("TABELLA_1")
    db.svuotaTabella("TABELLA_2")
    db.svuotaTabella("TABELLA_3")
    db.conn.close()
    return DB("./TEMP.sqlite")


def incognitoTable1(kAnonimity, flag):
    # applico Incognito alla prima tabella che contiene solo ZIPCODE
    g = Graph.SingleNodeGraph("ZIPCODE")
    bfs(g.getGraph(), g.getRoot(), kAnonimity, "TABELLA_1", flag)
    print "Nodo marked"
    for n in g.getGraph():
        if n.marked:
            print "RAGGIUNTA K-ANONIMITY NELLA TABELLA1 AL NODO:"
            n.description()
            return



def incognitoTable2(kAnonimity, flag):
    # applico Incognito alla prima tabella che contiene ZIPCODE
    localListOfQi = ["ZIPCODE", "SESSO"]
    localGraphList = []
    localGraphDict = dict()

    for qi in localListOfQi:
        g = Graph.SingleNodeGraph(qi)
        localGraphList.append(g)
    localGraphDict['1'] = localGraphList

    g = Graph.DoubleNodeGraph("ZIPCODE", "SESSO")
    localGraph2List = []
    localGraph2List.append(g)

    localGraphDict['2'] = localGraph2List

    bfsIncognito(localGraphDict, kAnonimity, "TABELLA_2", flag)

    for i in localGraphDict:
        for g in localGraphDict[i]:
            for n in g.getGraph():
                if n.marked:
                    print "RAGGIUNTA K-ANONIMITY NELLA TABELLA2 AL NODO:"
                    n.description()
                    break



def incognitoTable3(kAnonimity, flag):
    totalGraphDict = dict()
    # costruzione grafo con nodi contenenti un solo quasi identifier
    tmp = []
    for qi in listOfQuasiIdentifier:
        g = Graph.SingleNodeGraph(qi)
        tmp.append(g)
    totalGraphDict['1'] = tmp

    # costruzione grafo con nodi contenenti due quasi identifier
    combinationsOfQi = generateCombinationsOfQuasiIdentifier()
    tmp = []
    for couple in combinationsOfQi:
        l = couple.split(",")
        g = Graph.DoubleNodeGraph(l[0], l[1])
        tmp.append(g)
    totalGraphDict['2'] = tmp

    # costruzione grafo con nodi contenenti tre quasi identifier
    tmp = []
    g = Graph.TripleNodeGraph(listOfQuasiIdentifier[0],
                              listOfQuasiIdentifier[1],
                              listOfQuasiIdentifier[2])
    tmp.append(g)
    totalGraphDict['3'] = tmp
    bfsIncognito(totalGraphDict, kAnonimity, "TABELLA_3", flag)

    for i in totalGraphDict:
        for g in totalGraphDict[i]:
            for n in g.getGraph():
                if n.marked:
                    print "RAGGIUNTA K-ANONIMITY NELLA TABELLA2 AL NODO:"
                    n.description()
                    break


def generateCombinationsOfQuasiIdentifier():
    combinationsOfQi = []
    for qi1 in listOfQuasiIdentifier:
        for qi2 in listOfQuasiIdentifier:
            if(qi1 != qi2 and not(combinationsOfQi.__contains__(qi1 + "," + qi2)
                               or combinationsOfQi.__contains__(qi2 + "," + qi1))):
                combinationsOfQi.append(qi1 + "," + qi2)
    return combinationsOfQi


# visits all the nodes of a graph (connected component) using BFS
def bfs(graph, start, kAnonimity, tabella, flag):
    print "grafo con qi:"
    print start.quasiIdentifier
    print "dimensione grafo: " + str(len(graph))
    testDB = DB("./PROVA.sqlite")
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if not node.marked:
            # add node to list of checked nodes
            if node.isRoot:
                if len(node.quasiIdentifier) == 1:
                    resultQuery = testDB.selectCountFromQuasiIdentifierTabella(
                        node.quasiIdentifier[0].upper(), tabella
                    )
                elif len(node.quasiIdentifier) == 2:
                    q = node.quasiIdentifier[0].upper() + "," + node.quasiIdentifier[1].upper()
                    resultQuery = testDB.selectCountFromQuasiIdentifierTabella(q, tabella)
                else:
                    q = node.quasiIdentifier[0].upper() + "," \
                        + node.quasiIdentifier[1].upper() + "," \
                        + node.quasiIdentifier[2].upper()
                    resultQuery = testDB.selectCountFromQuasiIdentifierTabella(q, tabella)

            else:
                newTestDB = DB("./TEMP.sqlite")
                if len(node.quasiIdentifier) == 1:
                    db = setUpDB(newTestDB)
                    db.anonimizzazione(tabella, node.levelOfGeneralizations)
                    resultQuery = db.selectCountFromQuasiIdentifierTabella(
                        node.quasiIdentifier[0].upper(), tabella
                    )
                    db.conn.close()

                elif len(node.quasiIdentifier) == 2:
                    db = setUpDB(newTestDB)
                    db.anonimizzazione(tabella, node.levelOfGeneralizations)
                    q = node.quasiIdentifier[0].upper() + "," + node.quasiIdentifier[1].upper()
                    resultQuery = db.selectCountFromQuasiIdentifierTabella(q, tabella)
                    db.conn.close()


                else:
                    db = setUpDB(newTestDB)
                    db.anonimizzazione(tabella, node.levelOfGeneralizations)
                    q = node.quasiIdentifier[0].upper() + "," \
                        + node.quasiIdentifier[1].upper() + "," \
                        + node.quasiIdentifier[2].upper()
                    resultQuery = db.selectCountFromQuasiIdentifierTabella(q, tabella)
                    db.conn.close()


            frequencySet = []
            count = 0
            for i in resultQuery:
                count += 1
                print i
                if count > 5:
                    break


                frequencySet.append(i[0])
            backup = copy.copy(frequencySet)
            if flag == True and max(frequencySet) > delta:
                frequencySet = suppression(backup)
            minimum = min(frequencySet)
            print frequencySet
            if minimum >= kAnonimity:
                node.description()
                node.marked = True
                print "trovato nodo con k anonimity"
                for n in graph[node]:
                    nodeToMark = getKeyByDictionary(n.levelOfGeneralizations, graph)
                    nodeToMark.marked = True
            else:
                print "non ancora raggiunta la k anonimity"
                neighbours = graph[node]
                if neighbours is not None:
                    # add neighbours of node to queue
                    for neighbour in neighbours:
                        nodeToAdd = getKeyByDictionary(neighbour.levelOfGeneralizations, graph)
                        queue.append(nodeToAdd)


def bfsIncognito(totalGraph, kAnonimity, tabella, flag):
    for k in totalGraph:
        for g in totalGraph[k]:
            bfs(g.getGraph(), g.getRoot(), kAnonimity, tabella, flag)



def getKeyByDictionary(levels, graph):
    for k in graph:
        if k.levelOfGeneralizations == levels:
            return k
    return None


def main():

    kString = raw_input("Insert desired k-anonymity level:")
    kAnonimity = int(kString)

    answer = raw_input("Do you want suppress in case of unreachble k-anonymity? (y/n)")
    flag = False
    if answer == 'y':
        flag = True
    else:
        flag = False


    print str(kAnonimity) + "-anonymizing table containing 1 quasiIdentifier..."
    start = time.time()
    incognitoTable1(kAnonimity, flag)
    end = time.time()
    print "Elapsed time to " + str(kAnonimity) + \
          "-anonymize a table containing 1 quasiIdentifier: " + str(end - start)
    
    print "\n\n" + str(kAnonimity) + "-anonymizing table containing 2 quasiIdentifier..."
    start = time.time()
    incognitoTable2(kAnonimity, flag)
    end = time.time()
    print "Elapsed time to " + str(kAnonimity) + \
          "-anonymize a table containing 2 quasiIdentifier: " + str(end - start)
    

    print "\n\n" + str(kAnonimity) + "-anonymizing table containing 3 quasiIdentifier..."
    start = time.time()
    incognitoTable3(kAnonimity, flag)
    end = time.time()
    print "Elapsed time to " + str(kAnonimity) + \
          "-anonymize a table containing 3 quasiIdentifier: " + str(end - start)


if __name__ == "__main__":
    main()







