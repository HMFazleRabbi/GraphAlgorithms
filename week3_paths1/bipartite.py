#Uses python3

import sys
import queue
from GraphAlgoLibrary import *


# In the mathematical field of graph theory, a bipartite graph is a graph whose 
# vertices can be divided into two disjoint and independent sets U and V such that 
# every edge connects a vertex in U to one in V. Vertex sets U and V are usually 
# called the parts of the graph. Equivalently, a bipartite graph is a graph that 
# does not contain any odd-length cycles.
def bipartite(adj, s):

    # Init Nodes
    # Note: Possible to init all nodes because this is a UNDIRECTED graph hence
    # no difference between source and sink
    dist=[-1 for _ in range(len(adj))]

    # Init Queue
    q = queue.Queue()
    q.put(s)
    dist[s]=0

    # Assign distance 
    while not q.empty():
        # Deque - Processed
        u = q.get()

        # Enqeque - discover
        for v in adj[u]:
            if dist[v]==-1:
                q.put(v)
                dist[v]=dist[u]+1
    
            # Bipartite Visualization:
            # Circular Ring Analogy-
            # In circular ring graph, the nodes at same distance cant 
            # connect between them. Alternate between ring of team and fan
            # as circle propagates.
            # The ring graph can be flatnned into a bipartite graph 
            # https://study.com/cimages/multimages/16/bipartite4.jpg by assigning
            # each ring to one group and the following ring to the next and following
            # following to this group and so on the pattern repeats.
            # Tree Analogy:
            # The leaves at each level are only connect to leaves at nexxt level and 
            # not between them.
            if dist[v]==dist[u]:
                return 0


    return 1

if __name__ == '__main__':
    # Read inputs
    # fname="Graph.txt"   # Graph that is bipartite
    fname="Graph-Bipartite.txt" # Graph that is not  bipartite. Observe (8 5) and (8 2) edges
    n, m, adj, _, _ = LoadGraphFromFile(fname)

    # Create Undirected edges
    undirectedAdj = ConvertToUndirectedAdjList(adj)
    # print(adj,undirectedAdj)

    # Start bipartite check from random node
    s=0
    print("Bipartite: %s"%( "True" if bipartite(undirectedAdj, s) else "False"))
    
