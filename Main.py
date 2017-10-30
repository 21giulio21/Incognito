from Nodo import Nodo
import Graph
import copy

generalizzazione = dict()
generalizzazione['zipcode'] = 3
generalizzazione['sesso'] = 2
generalizzazione['data'] = 3
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

def nearNodes(node):
    nodes = []
    qi = copy.copy(node.quasiIdentifier)
    for key in node.levelOfGeneralizations:
        levels = node.levelOfGeneralizations.copy()
        if(generalizzazione[key] > levels[key]):
            levels[key] += 1
            nodes.append(Nodo(qi, False, levels))
    return nodes

def bfs(graph, start):
    # to improve
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def main():
    # costruzione grafo con nodi contenenti un solo quasi identifier
    for qi in listOfQuasiIdentifier:
        g = Graph.SingleNodeGraph(qi)
        g.printGraph()

    # costruzione grafo con nodi contenenti due quasi identifier

    combinationsOfQi = generateCombinationsOfQuasiIdentifier()

    for couple in combinationsOfQi:
        l = couple.split(",")
        g = Graph.DoubleNodeGraph(l[0], l[1])
        g.printGraph()

    # costruzione grafo con nodi contenenti tre quasi identifier
    g = Graph.TripleNodeGraph(listOfQuasiIdentifier[0],
                                 listOfQuasiIdentifier[1],
                                 listOfQuasiIdentifier[2])
    g.printGraph()


if __name__ == "__main__":
    main()







