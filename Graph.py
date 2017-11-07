# from Main import nearNodes
from DB import DB
from Nodo import Nodo
import copy


generalizzazione = dict()
generalizzazione['ZIPCODE'] = 5
generalizzazione['SESSO'] = 1
generalizzazione['DATA_NASCITA'] = 3

def nearNodes(node):
    nodes = []
    qi = copy.copy(node.quasiIdentifier)
    for key in node.levelOfGeneralizations:
        levels = node.levelOfGeneralizations.copy()
        if(generalizzazione[key] > levels[key]):
            levels[key] += 1
            nodes.append(Nodo(qi, False, levels))
    return nodes

class SingleNodeGraph:
    def __init__(self, qiString):
        self.graph = dict()
        listOfNode = []
        qi = [qiString]
        self.quasiId = copy.copy(qi)
        for i in range(0, generalizzazione[qiString] + 1):
            levelOfGeneralizations = dict()
            levelOfGeneralizations[qiString] = i
            node = Nodo(qi, False, levelOfGeneralizations)
            if i == 0:
                node.isRoot = True
            listOfNode.append(node)
        for node in listOfNode:
            self.graph[node] = nearNodes(node)

    def printGraph(self):
        count = 0
        print("+++++++++nuovo grafo++++++++++++++++++++++++++++")
        for k in self.graph:
            count += 1
            print("counter -> " + str(count))
            k.description()
            for i in self.graph[k]:
                print("nodo vicino:")
                i.description()
        print("---------fine grafo----------------------------\n\n\n\n\n\n")

    def getGraph(self):
        return self.graph

    def getRoot(self):
        for k in self.graph:
            if k.isRoot:
                return k
        return None


class DoubleNodeGraph:
    def __init__(self, qiString1, qiString2):
        # numero di nodi = (generalizzazione[qiString1]+1)*(generalizzazione[qiString]+1)
        listOfNode = []
        qi = [qiString1, qiString2]
        self.quasiId = copy.copy(qi)
        for i in range(0, generalizzazione[qiString2] + 1):
            for j in range(0, generalizzazione[qiString1] + 1):
                levelOfGeneralizations = dict()
                levelOfGeneralizations[qiString2] = i
                levelOfGeneralizations[qiString1] = j
                node = Nodo(qi, False, levelOfGeneralizations)
                if i == 0 and j == 0:
                    node.isRoot = True
                listOfNode.append(node)
        self.graph = dict()
        for node in listOfNode:
            self.graph[node] = nearNodes(node)


    def printGraph(self):
        count = 0
        print("+++++++++nuovo grafo++++++++++++++++++++++++++++")
        for k in self.graph:
            count += 1
            print("counter -> " + str(count))
            k.description()
            for i in self.graph[k]:
                print("nodo vicino:")
                i.description()
        print("---------fine grafo----------------------------\n\n\n\n\n\n")

    def getGraph(self):
        return self.graph

    def getRoot(self):
        for k in self.graph:
            if k.isRoot:
                return k
        return None



class TripleNodeGraph:
    def __init__(self, qiStr1, qiStr2, qiStr3):
        # numero di nodi = qi1*qi2*qi3
        listOfNode = []
        qi = [qiStr1, qiStr2, qiStr3]
        self.quasiId = copy.copy(qi)
        for i in range(0, generalizzazione[qiStr2] + 1):
            for j in range(0, generalizzazione[qiStr1] + 1):
                for k in range(0, generalizzazione[qiStr3] + 1):
                    levelOfGeneralizations = dict()
                    levelOfGeneralizations[qiStr3] = k
                    levelOfGeneralizations[qiStr2] = i
                    levelOfGeneralizations[qiStr1] = j
                    node = Nodo(qi, False, levelOfGeneralizations)
                    if i == 0 and j == 0 and k == 0:
                        node.isRoot = True
                    listOfNode.append(node)

        self.graph = dict()
        for node in listOfNode:
            self.graph[node] = nearNodes(node)


    def printGraph(self):
        count = 0
        print("+++++++++nuovo grafo++++++++++++++++++++++++++++")
        for k in self.graph:
            count += 1
            print("counter -> " + str(count))
            k.description()
            for i in self.graph[k]:
                print("nodo vicino:")
                i.description()
        print("---------fine grafo----------------------------\n\n\n\n\n\n")

    def getGraph(self):
        return self.graph

    def getRoot(self):
        for k in self.graph:
            if k.isRoot:
                return k
        return None

