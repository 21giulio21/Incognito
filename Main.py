from DB import DB
import Graph
import timeit


generalizzazione = dict()
generalizzazione['zipcode'] = 5
generalizzazione['sesso'] = 1
generalizzazione['data'] = 3
numeroQuasiIdentifier = 3
listOfQuasiIdentifier = ['zipcode', 'sesso', 'data']

def incognitoTable1(kAnonimity):
    # applico Incognito alla prima tabella che contiene solo zipcode
    g = Graph.SingleNodeGraph("zipcode")
    bfs(g.getGraph(), g.getRoot(), kAnonimity)
    print "Nodo marked"
    for n in g.getGraph():
        if n.marked:
            print "RAGGIUNTA K-ANONIMITY NELLA TABELLA1 AL NODO:"
            n.description()
            return


def incognitoTable2(kAnonimity):
    # applico Incognito alla prima tabella che contiene zipcode
    localListOfQi = ["zipcode", "sesso"]
    localGraphList = []
    localGraphDict = dict()

    for qi in localListOfQi:
        g = Graph.SingleNodeGraph(qi)
        localGraphList.append(g)
    localGraphDict['1'] = localGraphList

    g = Graph.DoubleNodeGraph("zipcode", "sesso")
    localGraph2List = []
    localGraph2List.append(g)

    localGraphDict['2'] = localGraph2List

    bfsIncognito(localGraphDict, kAnonimity)

    for i in localGraphDict:
        for g in localGraphDict[i]:
            for n in g.getGraph():
                if n.marked:
                    print "RAGGIUNTA K-ANONIMITY NELLA TABELLA2 AL NODO:"
                    n.description()
                    return


def incognitoTable3(kAnonimity):
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
    bfsIncognito(totalGraphDict, kAnonimity)

    for i in totalGraphDict:
        for g in totalGraphDict[i]:
            for n in g.getGraph():
                if n.marked:
                    print "RAGGIUNTA K-ANONIMITY NELLA TABELLA2 AL NODO:"
                    n.description()
                    return


def generateCombinationsOfQuasiIdentifier():
    combinationsOfQi = []
    for qi1 in listOfQuasiIdentifier:
        for qi2 in listOfQuasiIdentifier:
            if(qi1 != qi2 and not(combinationsOfQi.__contains__(qi1 + "," + qi2)
                               or combinationsOfQi.__contains__(qi2 + "," + qi1))):
                combinationsOfQi.append(qi1 + "," + qi2)
    return combinationsOfQi


# visits all the nodes of a graph (connected component) using BFS
def bfs(graph, start, kAnonimity):
    # keep track of nodes to be checked
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
                    frequencySet = testDB.selectCountFromQuasiIdentifierTabella1(
                        node.quasiIdentifier[0].upper()
                    )
                elif len(node.quasiIdentifier) == 2:
                    frequencySet = testDB.selectCountFromQuasiIdentifierTabella2(
                        node.quasiIdentifier[0].upper(),
                        node.quasiIdentifier[1].upper()
                    )
                else:
                    frequencySet = testDB.selectCountFromQuasiIdentifierTabella3(
                        node.quasiIdentifier[0].upper(),
                        node.quasiIdentifier[1].upper(),
                        node.quasiIdentifier[2].upper()
                    )
            else:
                if len(node.quasiIdentifier) == 1:
                    # anonimizza il database sulla base del nodo in cui sei
                    frequencySet = testDB.selectCountFromQuasiIdentifierTabella1(
                        node.quasiIdentifier[0].upper()
                    )
                elif len(node.quasiIdentifier) == 2:
                    # anonimizza il database sulla base del nodo in cui sei
                    frequencySet = testDB.selectCountFromQuasiIdentifierTabella2(
                        node.quasiIdentifier[0].upper(),
                        node.quasiIdentifier[1].upper()
                    )
                else:
                    frequencySet = testDB.selectCountFromQuasiIdentifierTabella3(
                        node.quasiIdentifier[0].upper(),
                        node.quasiIdentifier[1].upper(),
                        node.quasiIdentifier[2].upper()
                    )
            print frequencySet
            if min(frequencySet) == kAnonimity:
                node.marked = True
                print "trovato nodo con k anonimity"
                for n in graph[node]:
                    nodeToMark = getKeyByDictionary(n.levelOfGeneralizations, graph)
                    nodeToMark.marked = True
            else:
                neighbours = graph[node]
                if neighbours is not None:
                    # add neighbours of node to queue
                    for neighbour in neighbours:
                        nodeToAdd = getKeyByDictionary(neighbour.levelOfGeneralizations, graph)
                        queue.append(nodeToAdd)


def bfsIncognito(totalGraph, kAnonimity):
    for k in totalGraph:
        for g in totalGraph[k]:
            bfs(g.getGraph(), g.getRoot(), kAnonimity)



def getKeyByDictionary(levels, graph):
    for k in graph:
        if k.levelOfGeneralizations == levels:
            return k
    return None


def main():

    kAnonimity = raw_input("Insert desired k-anonymity level:")

    print str(kAnonimity) + "anonymize table containing 1 quasiIdentifier..."
    start = timeit.timeit()
    incognitoTable1(kAnonimity)
    end = timeit.timeit()
    print "Elapsed time to " + str(kAnonimity) + \
          "-anonymize a table containing 1 quasiIdentifier: " + str(end - start)

    print str(kAnonimity) + "anonymize table containing 2 quasiIdentifier..."
    start = timeit.timeit()
    incognitoTable2(kAnonimity)
    end = timeit.timeit()
    print "Elapsed time to " + str(kAnonimity) + \
          "-anonymize a table containing 2 quasiIdentifier: " + str(end - start)

    print str(kAnonimity) + "anonymize table containing 3 quasiIdentifier..."
    start = timeit.timeit()
    incognitoTable3(kAnonimity)
    end = timeit.timeit()
    print "Elapsed time to " + str(kAnonimity) + \
          "-anonymize a table containing 3 quasiIdentifier: " + str(end - start)


if __name__ == "__main__":
    main()







