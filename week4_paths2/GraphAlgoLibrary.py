#Uses python3

import sys
import queue, heapq

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

    def __init__(self, n=0, m=0, adjList=[], weight=[]):
        self.n = n
        self.m = m
        self.adj = adjList
        self.w = weight

    # Vertices
        self.V = [x for x in range(n)]

    # Pre-post variable
        self.clock = 0
        self.preVisit = [0 for x in range(self.n)]
        self.postVisit = [0 for x in range(self.n)]
    # Connected Components counter
        self.ccompCount = 0

    def EdgeWeight(self, u, v):
    	uIdx=u
    	vIdx=self.adj[u].index(v)
    	return self.w[uIdx][vIdx]

    def resetPrePost(self):
        self.clock=0
        self.preVisit = [0 for x in range(self.n)]
        self.postVisit = [0 for x in range(self.n)]

    def print(self):
        
        print("n m: %d %d" % (self.n, self.m))
        print("Adj List\t\t", self.adj)
        print("Weight List\t\t", self.w)
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


def relax (u, v, G, dist):
    
    uIdx=u
    vIdx=G.adj[u].index(v)

    if (dist[v] > (dist[u]+G.w[uIdx][vIdx]) or dist[v]==-1):
        dist[v]=dist[u]+G.w[uIdx][vIdx]
        return True
    return False


def DiGraph_DFS(G):
    visited = [False for _ in range(G.n)]

    for v in G.V:
        if not visited[v]:
            Explore(G, v, visited)
            G.ccompCount = G.ccompCount + 1

def reachall(G, s):
    # write your code here
    visited = [False for _ in range(G.n)]
    Explore(G, s, visited)
    return visited

def reach(G, s, t):
    # write your code here
    visited = reach(G, s)
    return int(visited[t])

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
    visited = [False for _ in range(revG.n)]
    result = 0
    #write your code here
    order=toposort(revG)
    ccList=[]
    
    # Iterate
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
            ccList.append(connected_component)
            
    return result, ccList


def LoadGraphFromFile(fname):
    # Read inputs
    adjList = readAdjList(fname)
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

    # DiGraph
    diGraph = Graph(n, m, adj)
    DiGraph_DFS(diGraph)
    # diGraph.print()

    # DiReverse Graph
    revDiGraph = Graph(n, m, radj)
    DiGraph_DFS(revDiGraph)
    # revDiGraph.print()

    return n, m, adj, diGraph, revDiGraph

def LoadWeightedGraphFromFile(fname):
    # Read inputs
    adjList = readAdjList(fname)
    n, m = list(map(int, adjList[0].split()))
    edges = []
    for iEdge in adjList[1:]:
        edges.append(list(map(int, iEdge.split())))

    # Adj list
    adj = [[] for _ in range(n)]
    weight = [[] for _ in range(n)]
    for (a, b, w) in edges:
        adj[a - 1].append(b - 1)
        weight[a - 1].append(w)

    # Reverse Adj List
    radj = [[] for _ in range(n)]
    rweight = [[] for _ in range(n)]
    for (a, b, w) in edges:
        radj[b - 1].append(a - 1)
        rweight[a - 1].append(w)


    # DiGraph
    diGraph = Graph(n=n, m=m, adjList=adj, weight=weight) 
    DiGraph_DFS(diGraph)
    # diGraph.print()

    # DiReverse Graph
    revDiGraph = Graph(n=n, m=m, adjList=radj, weight=weight) 
    DiGraph_DFS(revDiGraph)
    # revDiGraph.print()

    return n, m, adj, weight, diGraph, revDiGraph


def ConvertToUndirectedAdjList(adj):
    edges=[]
    for u in range(len(adj)):
        for v in adj[u]:
            edges.append([u,v])
            edges.append([v,u])

    # Adj list
    newAdjList = [[] for _ in range(len(adj))]
    for (a, b) in edges:
        newAdjList[a].append(b)

    return newAdjList



if __name__ == '__main__':

    # Read inputs
    fname="Graph.txt"
    n, m, adj, G, revG = LoadGraphFromFile(fname)

    # SCC
    result, ccList = number_of_strongly_connected_components(G, revG)
    print("Total CC: %d"%(result), "::",ccList)

