#Uses python3

import sys
import queue
from GraphAlgoLibrary import *

def bfs(adj, s, t = 0):

    # Init Nodes
    # Note: Possible to init all nodes because this is a UNDIRECTED graph hence
    # no difference between source and sink
    dist=[-1 for _ in range(len(adj))]

    # Init Queue
    q = queue.Queue()
    q.put(s)
    dist[s]=0
    print(dist)
    # Assign distance 
    while not q.empty():
        # Deque - Processed
        u = q.get()

        # Enqeque - discover
        for v in adj[u]:
            if dist[v]==-1:
                q.put(v)
                dist[v]=dist[u]+1
                print(dist)

        # Exit if reached target
        if dist[t] > 0:
            return dist


    return dist

def distance(adj, s, t):
    #write your code here
    dist=bfs(adj,s,t)
    return dist[t]

if __name__ == '__main__':
    # Read inputs
    fname="Graph.txt"
    n, m, adj, _, _ = LoadGraphFromFile(fname)
    undirectedAdj = ConvertToUndirectedAdjList(adj)
    print(undirectedAdj)
    s=2
    t=4
    print("BFS shortest distance: %d"%(distance(undirectedAdj, s, t)))
    
