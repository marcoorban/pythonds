from basic import myStack
from graph import Graph

def dfs(G, s):
    # Recursive version of depth-first search
    start = G.getVertex(s)
    start.setDistance(0)
    recursion(G, start)

def recursion(G, s):
    for neighbor in s.getConnections():
        if not neighbor.isExplored():
            neighbor.setDistance(s.getDistance() + 1)
            recursion(G, neighbor)


