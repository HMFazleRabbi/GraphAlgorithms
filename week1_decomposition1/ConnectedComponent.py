# Uses python3

import sys
import time
import datetime


def Explore(v, adj):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            Explore(u, adj)


def number_of_components(adj):
    result = 0
    # write your code here
    for v in range(len(adj)):
        if not visited[v]:
            Explore(v, adj)
            result = result + 1
    return result

# ////////////////////////////////////
# MAIN
# ////////////////////////////////////
if __name__ == '__main__':
    # Example:   4 4 1 2 3 2 4 3 1 4 1 4

    print("Time: %s\n Please input list (Example 4 2 1 2 3 2 1 4 ):" %
          (datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))

    input = sys.stdin.read()
    statTimer = time.time()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]

    # Visited components
    visited = []
    visited = [False for _ in range(n)]
    x, y = x - 1, y - 1
    print("Nodes: %d Edges: %d\n\tSearching: (%d, %d)" % (n, m, x, y))
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
    print("Runtime: %d s" % (time.time() - statTimer))
