from collections import defaultdict

class TopologicalSort:
    def __init__(self,vertices2):
        self.graph = defaultdict(list)
        self.vertices = vertices2 
        
        
    def addEdge(self,u,ver):# adds edges to the graph
        self.graph[u].append(ver)
        
        
    def topoSort_Util(self,ver,visited,stack):
 
        visited[ver] = True
        for i in self.graph[ver]:
            if visited[i] == False:
                self.topoSort(i,visited,stack)
        stack.insert(0,ver)
        
        
    def topoSort(self):
        visited = [False] * self.vertices
        stack = []
        for i in range(self.vertices):
            if visited[i] == False:
                self.topoSort_Util(i,visited,stack)
  
