from DB import DB
import Graph


generalizzazione = dict()
generalizzazione['zipcode'] = 2
generalizzazione['sesso'] = 1
generalizzazione['data'] = 2
numeroQuasiIdentifier = 3
listOfQuasiIdentifier = ['zipcode', 'sesso', 'data']


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
    testDB = DB("./database.sqlite")
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if not node.marked:
            # add node to list of checked nodes
            if node.isRoot:
                frequencySet = testDB.emulateFrequencySetComputation(len(node.quasiIdentifier))
            else:
                frequencySet = testDB.emulateFrequencySetComputation(len(node.quasiIdentifier))
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

    kAnonimity = 3
    totalGraphDict = dict()
    # costruzione grafo con nodi contenenti un solo quasi identifier
    tmp = []
    for qi in listOfQuasiIdentifier:
        g = Graph.SingleNodeGraph(qi)
        tmp.append(g)
    totalGraphDict['1'] = tmp

    # costruzione grafo con nodi contenenti due quasi identifier
    combinationsOfQi = generateCombinationsOfQuasiIdentifier()
    tmp =[]
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


if __name__ == "__main__":
    main()







