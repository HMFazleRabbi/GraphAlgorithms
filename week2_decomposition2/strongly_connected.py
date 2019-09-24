#Uses python3

import sys

sys.setrecursionlimit(200000)


def PreVisit(G, v):
    G.preVisit[v] = G.clock
    G.clock = G.clock + 1


def PostVisit(G, v):
    G.postVisit[v] = G.clock
    G.clock = G.clock + 1

# Graph Class


class Graph():
    """docstring for Graph"""

    def __init__(self, n, m, adjList):
        self.n = n
        self.m = m
        self.adj = adjList
    # Vertices
        self.V = [x for x in range(n)]

    # Pre-post variable
        self.clock = 0
        self.preVisit = [0 for x in range(n)]
        self.postVisit = [0 for x in range(n)]
    # Connected Components counter
        self.ccompCount = 0

    def resetPrePost(self):
        self.clock=0
        self.preVisit = [0 for x in range(n)]
        self.postVisit = [0 for x in range(n)]

    def print(self):
        print("Adj List\t\t", self.adj)
        print("Vertices\t\t", self.V)
        print("preVisit\t\t", self.preVisit)
        print("postVisit\t\t", self.postVisit)
        print("CC counter\t\t", self.ccompCount)


def Explore(G, v, visited):
    visited[v] = True
    PreVisit(G, v)
    for u in G.adj[v]:
        if not visited[u]:
            Explore(G, u, visited)
    PostVisit(G, v)


def DiGraph_DFS(G):
    visited = [False for _ in range(len(G.V))]

    for v in G.V:
        if not visited[v]:
            Explore(G, v, visited)
            G.ccompCount = G.ccompCount + 1


def reach(G, x, y):
    # write your code here
    visited = [False for _ in range(len(G.V))]
    Explore(G, x, visited)
    return int(visited[y])


def acyclic(G):
    cyclic = 0
    G.print()
    for v in G.V:
        for u in G.adj[v]:
            print(u)
            if (reach(G, u, v)):
                return 1
    return 0


def readAdjList(fpath):
    fileObj = open(fpath)
    adjList = []
    for line in fileObj.readlines():
        adjList.append(line.strip())
    return adjList


def toposort(G):
    order = []

    #write your code here
    order=sorted(range(len(G.postVisit)), key=lambda k: G.postVisit[k], reverse=True) 
    return order

def number_of_strongly_connected_components(G, revG):
	visited = [False for _ in range(len(revG.V))]
	result = 0
	#write your code here
	order=toposort(revG)
	print("order: ",order)
	for v in order:
		if not visited[v]:
			result=result+1
			G.resetPrePost()
			Explore(G, v, visited)

			# Record CC path
			ccPath=[]
			for u in G.V:
				if (G.postVisit[u]>0): ccPath.append(u)
			connected_component=sorted(ccPath, key=lambda k: G.postVisit[k], reverse=True) 
			print("connected_component[%d]:\t"%(result),connected_component)
	return result


if __name__ == '__main__':
    # Read inputs
    adjList = readAdjList("Graph.txt")
    n, m = list(map(int, adjList[0].split()))
    edges = []
    for iEdge in adjList[1:]:
        edges.append(list(map(int, iEdge.split())))

    # Adj list
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    # Reverse Adj List
    radj = [[] for _ in range(n)]
    for (a, b) in edges:
        radj[b - 1].append(a - 1)

    # Graph
    diGraph = Graph(n, m, adj)
    DiGraph_DFS(diGraph)
    diGraph.print()

    # Reverse Graph
    revDiGraph = Graph(n, m, radj)
    DiGraph_DFS(revDiGraph)


    # SCC
    number_of_strongly_connected_components(diGraph, revDiGraph)

