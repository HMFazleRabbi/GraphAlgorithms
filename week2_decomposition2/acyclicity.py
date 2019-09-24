# Uses python3

import sys


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
    # diGraph.print()

    # Reverse Graph
    revDiGraph = Graph(n, m, radj)
    DiGraph_DFS(revDiGraph)
    # revDiGraph.print()

    # # Vertices
    # V = [x for x in range(n)]

    # # Pre-post variable
    # clock = 0
    # preVisit = [0 for x in range(n)]
    # postVisit = [0 for x in range(n)]

    # print("Edge List\t\t", edges)
    # print("Adj List\t\t", adj)
    # print("Vertices\t\t", V)
    # print("Visited \t\t", visited)

    print("Acyclic:\t\t", "True " if acyclic(diGraph) else "False")
