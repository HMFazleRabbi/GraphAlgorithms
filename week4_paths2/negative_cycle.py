#Uses python3

import sys
from  GraphAlgoLibrary import *

# /*************************************************************
# *   Author          : H M Fazle Rabbi
# *   Date Modified   : 20191008_1429
# *   Description     : Deteccting whether negative cycle exits
# *   by relaxing till G.n iteration as nodes that not part of 
# *   -ve cycle will stop relaxing before G.n iteration. The 
# *   output is list of parent for all  node, list of edges that
# *   relaxed on last iteration(wiil include atleast one edge), flag
# *   Expects  only 1 -ve cycle in graph.
# *   Copyright © 2000, MV Technology Ltd. All rights reserved.
# *************************************************************/
def negative_cycle(G):
    dist=[-1 for _ in range(G.n)]

    # Init distance and path
    dist=[-1 for _ in range(G.n)]
    prev=[-1 for _ in range(G.n)]
    state=True
    iteration=0
    relaxedEdge = [-1,-1]

    
    # Edge list
    while state:
        state=False
        relaxedEdge=[] #Reset 

        for u in G.V:
            for v in G.adj[u]:
                if (relax (u, v, G, dist)):
                    prev[v]=u       #To tracce path for infinite arbitrage 
                    state=True      
                    relaxedEdge.append([u,v]) # Edges affected by infinite arbitrage, is reset every while iter.

        # Check -ve cycle
        if (iteration == G.n and state):
            print("Negative cycle detected:\t", prev, relaxedEdge)
            return prev, relaxedEdge, True
            
        iteration=iteration+1

    return [], [], False 

# /*************************************************************
# *   Author          : H M Fazle Rabbi
# *   Date Modified   : 20191008_1429
# *   Description     : Parse back from end to cycle. Expects
# *   only 1 -ve cycle in graph.
# *   Copyright © 2000, MV Technology Ltd. All rights reserved.
# *************************************************************/
def extractInfiniteArbitragePoint(node, relax_edge):
    visited = [False for _ in range(len(node))]
    v =relax_edge[-1][0]
    while(True):
        if visited[v]==True:
            return v
        visited[v]=True
        v=node[v]

        # Reached source
        if v==-1:
            return -1
    return -1



if __name__ == '__main__':
        # Read inputs
    fname="Graph_ShortestPath.txt"
    n, m, adj, weight, G, rG = LoadWeightedGraphFromFile(fname)
    
    
    # Shortest path
    # shortest_path=dijkstra(s=0, t=3, G=G)
    node, relax_edge, present =negative_cycle(G=G)
    print("Node's source: ",node)
    print("Relaxed edge: ", relax_edge)
    print("Negative cycle preset: ", present)
    print("Cycle Node point: ", extractInfiniteArbitragePoint(node, relax_edge))