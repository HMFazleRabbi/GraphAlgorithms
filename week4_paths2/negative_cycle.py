#Uses python3

import sys
from  GraphAlgoLibrary import *


def negative_cycle(G):
    dist=[-1 for _ in range(len(adj))]

    # Init distance and path
    dist=[-1 for _ in range(G.n)]
    prev=[-1 for _ in range(G.n)]
    state=True
    iteration=0
    relaxedEdge = [-1,-1]

    
    # Edhe list
    while state:
        state=False
        relaxedEdge=[]

        for u in G.V:
            for v in G.adj[u]:
                if (relax (u, v, G, dist)):
                    prev[v]=u       #To tracce path for infinite arbitrage 
                    state=True      
                    relaxedEdge.append([u,v]) # Nodes affected by infinite arbitrage

        # Check -ve cycle
        if (iteration == G.n and state):
            print("Negative cycle detected")
            return prev, relaxedEdge, True
            break
        iteration=iteration+1

    return [], [], False 


if __name__ == '__main__':
        # Read inputs
    fname="Graph.txt"
    n, m, adj, weight, G, rG = LoadWeightedGraphFromFile(fname)
    
    
    # Shortest path
    # shortest_path=dijkstra(s=0, t=3, G=G)
    node, relax_edge, present =negative_cycle(G=G)
    print("Node's source: ",node)
    print("Relaxed edge: ", relax_edge)
    print("Negati cycle preset: ", present)