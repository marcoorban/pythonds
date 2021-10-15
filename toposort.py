class TopoSort():

    def __init__(self, G):
        self.graph = G
        self.curLabel = G.getVertices()
        self.ordering = {}

    def toposort(self):
        for v in self.graph.getVertices():
            vertex = self.graph.getVertex(v)
            if not vertex.isExplored():
                self.dfs_topo(vertex)

    def dfs_topo(self, s):
        s.setExplored()
        for neighbor in s.getConnections():
            if not neighbor.isExplored():
                self.dfs_topo(neighbor)
        self.ordering[s] = self.curLabel
        self.curLabel -= 1

    def get_ordering(self, vertex):
        if vertex in self.ordering.keys():
            return self.ordering[vertex]

