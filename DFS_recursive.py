class Graph:
    #Constructor
    def __init__(self, edges, n):
        
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, v, discovered):

    discovered[v] = True # Set source node as discovered
    print(v, end=' ') #Print current node

    #do this for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)

if __name__ == "__main__":

     # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13

    graph = Graph(edges, n)

    discovered = [False] * n

    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)