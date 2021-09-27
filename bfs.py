from graphs import Graph, Vertex
from basic import Queue

def bfs(G, S):
    # Mark S as explored, all other vertices are unexplored
    start = G.getVertex(S)
    start.setExplored()
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
                Q.enqueue(neighbor)