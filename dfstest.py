from dfs import dfs
from graph import Graph

G = Graph()
V = ['a', 'b', 'c', 'd', 'e', 'f']
for vertex in V:
    G.addVertex(vertex)
G.addEdge('a', 'b')
G.addEdge('b', 'c')
G.addEdge('c', 'a')
G.addEdge('b', 'd')
G.addEdge('d', 'e')
G.addEdge('e', 'f')
G.addEdge('f', 'e')

dfs(G, 'a')

G.showConnections()
G.showDistances()
