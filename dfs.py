
def dfs(G, s):
    # Recursive version of depth-first search
    start = G.getVertex(s)
    start.setDistance(0)
    dfs_recur(G, start)

def dfs_recur(G, s):
    s.setExplored()
    for neighbor in s.getConnections():
        if not neighbor.isExplored():
            neighbor.setDistance(s.getDistance() + 1)
            dfs_recur(G, neighbor)
