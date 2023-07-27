from collections import deque

# A class to represent a graph
class Graph:

    def __init__(self, edges, n):

        # A list of lists to represent adjacency list
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# Perform BFS recursively on the graph
def BFS(graph, q, discovered):

    if not q:
        return
    
    #dequeue front node and print
    v = q.popleft()
    print(v, end=' ')

    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
    
    BFS(graph, q, discovered)

if __name__ == "__main__":

    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]

    n = 15

    graph = Graph(edges, n)

    discovered = [False] * n

    q = deque()

    for i in range(n):
        if not discovered[i]:
            discovered[i] = True

            q.append(i)

            BFS(graph, q, discovered)

# O(V + E) 