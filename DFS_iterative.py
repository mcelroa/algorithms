from collections import deque

class Graph:
    #Constructor
    def __init__(self, edges, n):
        
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, v, discovered):

    stack = deque()

    #push source node into stack
    stack.append(v)

    # loop until stack empty
    while stack:

        # pop vertex from stack
        v = stack.pop()

        # if already discovered, ignore
        if discovered[v]:
            continue
            
        #if not discovered
        discovered[v] = True
        print(v, end=' ')

        #do for every edge (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)

if __name__ == "__main__":
        # List of graph edges as per the above diagram
        edges = [
            # Notice that node 0 is unconnected
            (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
            (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
            # (6, 9) introduces a cycle
        ]
    
        # total number of nodes in the graph (labelled from 0 to 12)
        n = 13
    
        # build a graph from the given edges
        graph = Graph(edges, n)
    
        # to keep track of whether a vertex is discovered or not
        discovered = [False] * n
    
        # Do iterative DFS traversal from all undiscovered nodes to
        # cover all connected components of a graph
        for i in range(n):
            if not discovered[i]:
                DFS(graph, i, discovered)