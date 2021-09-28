from graph import Graph, Vertex
from basic import Queue

def bfs(G, s):
    # Mark S as explored, all other vertices are unexplored
    start = G.getVertex(s)
    start.setExplored()
    start.setDistance(0)
    # create a queue and initialize it with S
    Q = Queue()
    Q.enqueue(start)
    while not Q.isEmpty():
        # remove the vertex from the front of Q and call it V
        V = Q.dequeue()
        # for each edge (V,W) in V's adjacency, if W is unexplored, mark it as explored and add it to the queue
        for neighbor in V.getConnections():
            if not neighbor.isExplored():
                neighbor.setExplored()
                neighbor.setDistance(V.getDistance() + 1)
                Q.enqueue(neighbor)