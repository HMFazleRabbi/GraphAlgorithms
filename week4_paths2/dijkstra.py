#Uses python3

import sys
import queue, heapq
from  GraphAlgoLibrary import *


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
 
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
 
    def pop(self):
        return heapq.heappop(self._queue)[-1]

def dijkstra(s, t, G):

	# Init distance and path
	dist=[-1 for _ in range(G.n)]
	prev=[-1 for _ in range(G.n)]
	path=[]

	# Init Queue
	q=PriorityQueue()
	q.push(s, 0)
	dist[s]=0


	# Assign distance 
	while q._queue:
	    # Deque - Processed
	    u = q.pop()

	    # Enqeque - discover
	    for v in G.adj[u]:
	        if (relax (u, v, G, dist)):
	        	prev[v]=u
	        	q.push(v, dist[v])


	#Target reachable
	if (dist[t]==-1):
		return [], [], -1

	# Trace path
	dst=t
	length=0
	path.append(dst)
	pathlength=[]
	for i in range(G.m):
		length=length+G.EdgeWeight(prev[dst],dst)
		pathlength.append(G.EdgeWeight(prev[dst],dst))
		dst=prev[dst]
		path.append(dst)
		if (dst==s):
			break

	
	return path[::-1], pathlength[::-1], length



# Assuming no negative cycle and no -ve wqeights
def native(s, t, G):
	dist=[-1 for _ in range(len(adj))]

    # Init distance and path
	dist=[-1 for _ in range(G.n)]
	prev=[-1 for _ in range(G.n)]
	path=[]
	state=True

	
	# Edhe list
	while state:
		state=False
		for u in G.V:
			for v in G.adj[u]:
				if (relax (u, v, G, dist)):
					prev[v]=u
					state=True

	#Target reachable
	if (dist[t]==-1):
		return [], [], -1

	# Trace path
	dst=t
	length=0
	path.append(dst)
	pathlength=[]
	for i in range(G.m):
		length=length+G.EdgeWeight(prev[dst],dst)
		pathlength.append(G.EdgeWeight(prev[dst],dst))
		dst=prev[dst]
		path.append(dst)
		if (dst==s):
			break



	return path[::-1], pathlength[::-1], length

if __name__ == '__main__':
	    # Read inputs
    fname="Graph.txt"
    n, m, adj, weight, G, rG = LoadWeightedGraphFromFile(fname)
    
    
	# Shortest path
    # shortest_path=dijkstra(s=0, t=3, G=G)
    shortest_path=native(s=0, t=4, G=G)
    print(shortest_path)

