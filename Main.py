from Nodo import Nodo
import copy

generalizzazione = dict()
generalizzazione['zipcode'] = 3
generalizzazione['sesso'] = 2
generalizzazione['data'] = 3
numeroQuasiIdentifier = 3
listOfQuasiIdentifier = ['zipcode', 'sesso', 'data']

def nearNodes(node):
    nodes = []
    qi = copy.copy(node.quasiIdentifier)
    for key in node.levelOfGeneralizations:
        levels = node.levelOfGeneralizations.copy()
        if(generalizzazione[key] > levels[key]):
            levels[key] += 1
            nodes.append(Nodo(qi, False, levels))
    return nodes

def printGraph(graph):
    count = 0
    for k in graph:
        count += 1
        print("counter -> " + str(count))
        k.description()
        for i in graph[k]:
            print("nodo vicino:")
            i.description()

def doubleNodeGraphGenerator(qiString1, qiString2):
    # numero di nodi = (generalizzazione[qiString1]+1)*(generalizzazione[qiString]+1)
    listOfNode = []
    qi = [qiString1, qiString2]

    for i in range(0, generalizzazione[qiString2] + 1):
        for j in range(0, generalizzazione[qiString1] + 1):
            levelOfGeneralizations = dict()
            levelOfGeneralizations[qiString2] = i
            levelOfGeneralizations[qiString1] = j
            node = Nodo(qi, False, levelOfGeneralizations)
            listOfNode.append(node)
    graph = dict()
    for node in listOfNode:
        graph[node] = nearNodes(node)
    return graph

def singleNodeGraphGenerator(qiString):
    graph = dict()
    listOfNode = []
    qi = [qiString]
    for i in range(0, generalizzazione[qiString] + 1):
        levelOfGeneralizations = dict()
        levelOfGeneralizations[qiString] = i
        node = Nodo(qi, False, levelOfGeneralizations)
        listOfNode.append(node)
    for node in listOfNode:
        graph[node] = nearNodes(node)
    return graph

def tripleNodeGraphGenerator(qiStr1, qiStr2, qiStr3):
    # numero di nodi = qi1*qi2*qi3
    listOfNode = []
    qi = [qiStr1, qiStr2, qiStr3]

    for i in range(0, generalizzazione[qiStr2] + 1):
        for j in range(0, generalizzazione[qiStr1] + 1):
            for k in range(0, generalizzazione[qiStr3] + 1):
                levelOfGeneralizations = dict()
                levelOfGeneralizations[qiStr3] = k
                levelOfGeneralizations[qiStr2] = i
                levelOfGeneralizations[qiStr1] = j
                node = Nodo(qi, False, levelOfGeneralizations)
                listOfNode.append(node)

    graph = dict()
    for node in listOfNode:
        graph[node] = nearNodes(node)
    return graph

# costruzione grafo con nodi contenenti un solo quasi identifier
for qi in listOfQuasiIdentifier:
    print("+++++++++nuovo grafo++++++++++++++++++++++++++++")
    g = singleNodeGraphGenerator(qi)
    printGraph(g)
    print("\n\n\n\n\n++++++++++++++++++++++++++\n\n\n\n\n\n")


# costruzione grafo con nodi contenenti due quasi identifier
combinationsOfQi = []
for qi1 in listOfQuasiIdentifier:
    for qi2 in listOfQuasiIdentifier:
        if(qi1 != qi2 and not(combinationsOfQi.__contains__(qi1 + "," + qi2)
                           or combinationsOfQi.__contains__(qi2 + "," + qi1))):
            combinationsOfQi.append(qi1 + "," + qi2)


for couple in combinationsOfQi:
    print("+++++++++nuovo grafo++++++++++++++++++++++++++++")
    l = couple.split(",")
    g = doubleNodeGraphGenerator(l[0], l[1])
    printGraph(g)
    print("\n\n\n\n\n++++++++++++++++++++++++++\n\n\n\n\n\n")

# costruzione grafo con nodi contenenti tre quasi identifier
print("-------------nuovo grafo----------------------------")
g = tripleNodeGraphGenerator(listOfQuasiIdentifier[0],
                             listOfQuasiIdentifier[1],
                             listOfQuasiIdentifier[2])
printGraph(g)
print("\n\n\n\n\n-------------------------------\n\n\n\n\n\n")








