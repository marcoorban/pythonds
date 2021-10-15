import sys
import os

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.explored = False
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self, color):
        self.color = color
        
    def setDistance(self, d):
        self.dist = d
        
    def setPred(self, p):
        self.pred = p
        
    def setDiscovery(self, dtime):
        self.disc = dtime
        
    def setFinish(self, ftime):
        self.fin = ftime
        
    def setExplored(self):
        self.explored = True
        
    def getFinish(self):
        return self.fin
    
    def getDiscovery(self):
        return self.disc
    
    def getPred(self):
        return self.disc
    
    def getDistance(self):
        return self.dist
    
    def isExplored(self):
        return self.explored

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def showConnections(self):
        connections = []
        for vertex in self.connectedTo.keys():
            connections.append(self.id + "->" + vertex.id)
        print(connections)

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def showConnections(self):
        for key in self.vertList.keys():
            vertex = self.getVertex(key)
            vertex.showConnections()

    def showDistances(self):
        for key in self.vertList.keys():
            vertex = self.getVertex(key)
            print(vertex.id + ":" + str(vertex.getDistance()))

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())