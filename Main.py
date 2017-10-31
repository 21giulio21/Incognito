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


# visits all the nodes of a graph (connected component) using BFS
def bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            print graph
            node.description()
            if neighbours is not None:
                # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
    return explored

def main():
    # costruzione grafo con nodi contenenti un solo quasi identifier
    for qi in listOfQuasiIdentifier:
        g = Graph.SingleNodeGraph(qi)
        #g.printGraph()

    # costruzione grafo con nodi contenenti due quasi identifier

    combinationsOfQi = generateCombinationsOfQuasiIdentifier()

    for couple in combinationsOfQi:
        l = couple.split(",")
        g = Graph.DoubleNodeGraph(l[0], l[1])
        #g.printGraph()
        graph = g.getGraph()
        visited = bfs(graph, g.getRoot())
        print("RISULTATO BFS:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print visited
    # costruzione grafo con nodi contenenti tre quasi identifier
    g = Graph.TripleNodeGraph(listOfQuasiIdentifier[0],
                                 listOfQuasiIdentifier[1],
                                 listOfQuasiIdentifier[2])
    #g.printGraph()


if __name__ == "__main__":
    main()







