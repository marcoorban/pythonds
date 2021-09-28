from dfs import dfs
from graph import Graph

G = Graph()
V = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
for vertex in V:
    G.addVertex(vertex)
print(G.getVertices())
G.addEdge('a', 'b')
G.addEdge('a', 'c')
G.addEdge('a', 'd')
G.addEdge('b', 'e')
G.addEdge('b', 'f')
G.addEdge('b', 'g')
G.addEdge('h', 'i')
G.addEdge('d', 'j')
G.addEdge('e', 'k')
G.addEdge('f', 'm')
G.addEdge('k', 'l')
G.addEdge('l', 'n')
G.addEdge('o', 'p')
G.addEdge('o', 'q')

dfs(G, 'a')

l = G.getVertex('l')
p = G.getVertex('p')
print(p.getDistance())
print(l.getDistance())
